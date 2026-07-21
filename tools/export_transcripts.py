#!/usr/bin/env python3
"""OKF raw-transcript exporter. Runs on the VPS host. Never prints secrets."""
import csv, io, json, os, re, subprocess, sys, urllib.request, urllib.parse

OUT = "/tmp/okf_export"
RAW = os.path.join(OUT, "raw")
os.makedirs(RAW, exist_ok=True)
csv.field_size_limit(10 * 1024 * 1024)

PG = ["docker", "exec", "dynachat-postgres", "psql", "-U", "dynachat", "-d", "dynachat"]


def copy_csv(sql):
    cmd = PG + ["-c", f"COPY ({sql}) TO STDOUT WITH CSV"]
    p = subprocess.run(cmd, capture_output=True)
    if p.returncode != 0:
        sys.stderr.write(p.stderr.decode("utf-8", "replace"))
        raise SystemExit("psql COPY failed")
    return p.stdout.decode("utf-8", "replace")


KEY_NAMES = ("YOUTUBE_API_KEY", "YT_API_KEY", "GOOGLE_API_KEY", "YOUTUBE_DATA_API_KEY")


def _scan_env_files():
    import glob
    roots = [
        "/opt/dynachat/app/deploy", "/opt/dynachat/app", "/opt/dynachat",
        "/home/archon", "/home/archon/dynachat",
    ]
    seen = set()
    for root in roots:
        for pat in (".env", ".env.*", "*.env", "*.env.*"):
            for path in glob.glob(os.path.join(root, pat)):
                if path in seen or not os.path.isfile(path):
                    continue
                seen.add(path)
                try:
                    with open(path, encoding="utf-8", errors="replace") as f:
                        for line in f:
                            line = line.strip()
                            if line.startswith("#") or "=" not in line:
                                continue
                            k, _, v = line.partition("=")
                            k = k.strip().replace("export ", "").strip()
                            if k in KEY_NAMES:
                                v = v.strip().strip('"').strip("'")
                                if v:
                                    return v
                except Exception:
                    pass
    return ""


def get_api_key():
    for name in KEY_NAMES:
        for container in ("dynachat-app-green", "dynachat-app-blue"):
            try:
                p = subprocess.run(
                    ["docker", "exec", container, "sh", "-c", f'printf "%s" "${name}"'],
                    capture_output=True, timeout=15)
                v = p.stdout.decode().strip()
                if v:
                    return v
            except Exception:
                pass
    return _scan_env_files()


def hms(sec):
    sec = int(round(float(sec)))
    if sec < 0:
        sec = 0
    return f"{sec // 3600}:{(sec % 3600) // 60:02d}:{sec % 60:02d}"


def slugify(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9\s-]", "", t)
    t = re.sub(r"[\s_]+", "-", t)
    t = re.sub(r"-+", "-", t).strip("-")
    return t or "video"


def yt_id(url):
    m = re.search(r"[?&]v=([A-Za-z0-9_-]{11})", url or "")
    if m:
        return m.group(1)
    m = re.search(r"youtu\.be/([A-Za-z0-9_-]{11})", url or "")
    return m.group(1) if m else ""


def paragraphs_from_chunks(chunks):
    """chunks: list of (chunk_index, start_seconds, content). Returns list of (start_seconds, text)."""
    paras = []
    cur_words = []
    cur_start = None
    for ci, ss, content in chunks:
        words = content.split()
        if not words:
            continue
        if cur_start is None:
            cur_start = ss
        cur_words.extend(words)
        if len(cur_words) >= 50:
            paras.append((cur_start, " ".join(cur_words)))
            cur_words = []
            cur_start = None
    if cur_words:
        paras.append((cur_start if cur_start is not None else 0.0, " ".join(cur_words)))
    return paras


def paragraphs_from_text(text):
    words = text.split()
    paras = []
    for i in range(0, len(words), 55):
        paras.append(" ".join(words[i:i + 55]))
    return paras


def main():
    print("Loading videos...")
    videos = []
    vr = csv.reader(io.StringIO(copy_csv(
        "SELECT id, title, url, transcript FROM videos WHERE source_type='youtube' ORDER BY id")))
    for row in vr:
        vid, title, url, transcript = row
        videos.append({"id": vid, "title": title, "url": url, "transcript": transcript})
    print(f"  {len(videos)} youtube videos")

    print("Loading chunks...")
    chunks_by_video = {}
    cr = csv.reader(io.StringIO(copy_csv(
        "SELECT video_id, chunk_index, start_seconds, end_seconds, content FROM chunks "
        "WHERE source_type='youtube' ORDER BY video_id, chunk_index")))
    n_chunks = 0
    for row in cr:
        vid, ci, ss, es, content = row
        chunks_by_video.setdefault(vid, []).append(
            (int(ci), float(ss), float(es), content))
        n_chunks += 1
    print(f"  {n_chunks} chunks across {len(chunks_by_video)} videos")

    # Fetch publish dates
    ids = [yt_id(v["url"]) for v in videos]
    ids = [i for i in ids if i]
    uniq = list(dict.fromkeys(ids))
    pub = {}
    cache_path = os.path.join(OUT, "dates.json")
    if os.path.exists(cache_path):
        try:
            with open(cache_path) as f:
                pub = {k: v for k, v in json.load(f).items() if v}
            print(f"Loaded {len(pub)} cached dates")
        except Exception:
            pub = {}
    key = get_api_key()
    if key:
        print(f"Fetching publish dates from YouTube Data API (key len {len(key)})...")
        for i in range(0, len(uniq), 50):
            batch = uniq[i:i + 50]
            qs = urllib.parse.urlencode(
                {"part": "snippet", "id": ",".join(batch), "key": key})
            u = f"https://www.googleapis.com/youtube/v3/videos?{qs}"
            try:
                with urllib.request.urlopen(u, timeout=30) as r:
                    data = json.load(r)
                for item in data.get("items", []):
                    pa = item.get("snippet", {}).get("publishedAt", "")
                    pub[item["id"]] = pa[:10] if pa else ""
            except Exception as e:
                sys.stderr.write(f"  API batch {i} error: {e}\n")

    # Scrape watch-page microformat for any id still missing a date (keyless)
    todo = [i for i in uniq if not pub.get(i)]
    if todo:
        print(f"Scraping publish dates from watch pages for {len(todo)} ids (keyless)...")
        pats = [
            re.compile(r'<meta\s+itemprop="datePublished"\s+content="(\d{4}-\d{2}-\d{2})'),
            re.compile(r'<meta\s+itemprop="uploadDate"\s+content="(\d{4}-\d{2}-\d{2})'),
            re.compile(r'"publishDate":"(\d{4}-\d{2}-\d{2})'),
            re.compile(r'"uploadDate":"(\d{4}-\d{2}-\d{2})'),
            re.compile(r'"datePublished":"(\d{4}-\d{2}-\d{2})'),
        ]
        headers = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        for n, vid_id in enumerate(todo, 1):
            date = ""
            for attempt in range(3):
                try:
                    req = urllib.request.Request(
                        f"https://www.youtube.com/watch?v={vid_id}", headers=headers)
                    with urllib.request.urlopen(req, timeout=20) as r:
                        html = r.read().decode("utf-8", "replace")
                    for pat in pats:
                        m = pat.search(html)
                        if m:
                            date = m.group(1)
                            break
                    if date:
                        break
                except Exception:
                    pass
            if date:
                pub[vid_id] = date
            if n % 25 == 0:
                print(f"  scraped {n}/{len(todo)}...")
    print(f"  got dates for {len([1 for i in uniq if pub.get(i)])} / {len(uniq)} ids")
    with open(cache_path, "w") as f:
        json.dump({i: pub.get(i, "") for i in uniq}, f)

    # Build files
    used_slugs = {}
    manifest = []
    n_ts = 0
    n_fallback = 0
    n_nodate = 0
    for v in videos:
        title = v["title"]
        url = v["url"]
        vid = v["id"]
        ytid = yt_id(url)
        base = slugify(title)
        if base in used_slugs:
            used_slugs[base] += 1
            slug = f"{base}-{used_slugs[base]}"
        else:
            used_slugs[base] = 1
            slug = base

        chunks = chunks_by_video.get(vid)
        has_ts = bool(chunks)
        duration = ""
        body_lines = []
        if has_ts:
            trip = [(ci, ss, content) for (ci, ss, es, content) in chunks]
            max_end = max(es for (_, _, es, _) in chunks)
            duration = hms(max_end)
            for start, text in paragraphs_from_chunks(trip):
                body_lines.append(f"**[{hms(start)}]** {text}")
            n_ts += 1
        else:
            for text in paragraphs_from_text(v["transcript"]):
                body_lines.append(text)
            n_fallback += 1

        published = pub.get(ytid, "")
        if not published:
            n_nodate += 1

        esc_title = title.replace('"', '\\"')
        fm = [
            "---",
            "type: raw-transcript",
            f'title: "{esc_title}"',
            f"youtube_id: {ytid}",
            f"url: {url}",
            f"slug: {slug}",
            f"published: {published}",
            f'duration: "{duration}"',
            "fetched_at: 2026-07-21",
            "immutable: true",
            "---",
            "",
            "## Transcript",
            "",
        ]
        content = "\n".join(fm) + "\n" + "\n\n".join(body_lines) + "\n"
        with open(os.path.join(RAW, f"{slug}.md"), "w", encoding="utf-8") as f:
            f.write(content)

        manifest.append({
            "slug": slug, "youtube_id": ytid, "url": url, "title": title,
            "published": published, "duration": duration,
        })

    # sort manifest by published desc (blank dates last), then title
    manifest.sort(key=lambda m: (m["published"] or "0000-00-00", m["title"]), reverse=True)
    for rank, m in enumerate(manifest, 1):
        m["recency_rank"] = rank
    with open(os.path.join(RAW, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    dated = [m["published"] for m in manifest if m["published"]]
    print("=== SUMMARY ===")
    print(f"videos_written: {len(videos)}")
    print(f"with_timestamps: {n_ts}")
    print(f"fallback_no_timestamps: {n_fallback}")
    print(f"missing_publish_date: {n_nodate}")
    if dated:
        print(f"min_published: {min(dated)}")
        print(f"max_published: {max(dated)}")
    print(f"files_in_raw: {len(os.listdir(RAW))}")


if __name__ == "__main__":
    main()
