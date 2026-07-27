# /// script
# dependencies = ["yt-dlp"]
# ///
"""Fetch all transcripts from a YouTube channel using yt-dlp.

Free, no API key required. Handles both channel enumeration and subtitle download.

Usage:
    uv run fetch_transcripts.py @ChannelHandle
    uv run fetch_transcripts.py https://www.youtube.com/@ChannelHandle
    uv run fetch_transcripts.py @ChannelHandle --limit 10 --output-dir ./raw
"""
import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import yt_dlp


def slugify(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug)
    return slug.strip("-")


def format_ts(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h}:{m:02d}:{s:02d}"


def format_duration(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def normalize_channel_url(channel: str) -> str:
    if channel.startswith("http"):
        return channel
    handle = channel if channel.startswith("@") else f"@{channel}"
    return f"https://www.youtube.com/{handle}/videos"


def parse_json3(data: dict) -> list[dict]:
    segments = []
    for event in data.get("events", []):
        segs = event.get("segs")
        if not segs:
            continue
        text = "".join(s.get("utf8", "") for s in segs).strip()
        if not text or text == "\n":
            continue
        start_ms = event.get("tStartMs", 0)
        duration_ms = event.get("dDurationMs", 0)
        segments.append({
            "start": start_ms / 1000.0,
            "duration": duration_ms / 1000.0,
            "text": text,
        })
    return segments


def group_into_paragraphs(segments, target_words=50):
    paragraphs = []
    buf, start, wc = [], None, 0
    for seg in segments:
        if start is None:
            start = seg["start"]
        buf.append(seg["text"])
        wc += len(seg["text"].split())
        if wc >= target_words:
            paragraphs.append({"start": start, "text": " ".join(buf).strip()})
            buf, start, wc = [], None, 0
    if buf:
        paragraphs.append({"start": start, "text": " ".join(buf).strip()})
    return paragraphs


def main():
    ap = argparse.ArgumentParser(description="Fetch YouTube channel transcripts (yt-dlp)")
    ap.add_argument("channel", help="YouTube channel URL or @handle")
    ap.add_argument("--output-dir", default="./raw", help="Where to write raw/*.md files (default: ./raw)")
    ap.add_argument("--limit", type=int, default=None, help="Max videos to fetch (default: all)")
    ap.add_argument("--delay", type=float, default=2.0, help="Seconds between subtitle requests (default: 2.0)")
    args = ap.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    tmp_subs = out / ".subs_tmp"
    tmp_subs.mkdir(exist_ok=True)

    url = normalize_channel_url(args.channel)

    # Step 1: enumerate videos
    print(f"Enumerating videos from {url} ...")
    enum_opts = {"extract_flat": True, "quiet": True}
    if args.limit:
        enum_opts["playlistend"] = args.limit

    with yt_dlp.YoutubeDL(enum_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    entries = [e for e in (info or {}).get("entries", []) if e]
    print(f"Found {len(entries)} videos\n")

    if not entries:
        print("No videos found. Check the channel URL.", file=sys.stderr)
        sys.exit(1)

    # Step 2: fetch subtitles + metadata per video
    manifest_videos = []
    used_slugs: set[str] = set()
    skipped = []

    for i, entry in enumerate(entries):
        vid_id = entry["id"]
        title = entry.get("title", vid_id)
        upload_date = entry.get("upload_date", "")

        slug = slugify(title)
        if not slug:
            slug = vid_id
        if slug in used_slugs:
            n = 2
            while f"{slug}-{n}" in used_slugs:
                n += 1
            slug = f"{slug}-{n}"
        used_slugs.add(slug)

        print(f"[{i + 1}/{len(entries)}] {title}")

        sub_opts = {
            "skip_download": True,
            "writeautomaticsub": True,
            "writesubtitles": True,
            "subtitleslangs": ["en"],
            "subtitlesformat": "json3",
            "outtmpl": str(tmp_subs / f"{vid_id}.%(ext)s"),
            "quiet": True,
            "no_warnings": True,
            "ignoreerrors": True,
        }

        try:
            with yt_dlp.YoutubeDL(sub_opts) as ydl:
                meta = ydl.extract_info(f"https://www.youtube.com/watch?v={vid_id}", download=True)

            # Find the json3 subtitle file
            sub_file = None
            for candidate in tmp_subs.glob(f"{vid_id}*.json3"):
                sub_file = candidate
                break

            if not sub_file or not sub_file.exists():
                skipped.append({"id": vid_id, "title": title, "reason": "no subtitles available"})
                print(f"  -> SKIPPED (no subtitles)")
                time.sleep(args.delay)
                continue

            sub_data = json.loads(sub_file.read_text(encoding="utf-8"))
            segments = parse_json3(sub_data)
            paragraphs = group_into_paragraphs(segments)

            # Clean up subtitle file
            sub_file.unlink(missing_ok=True)

            # Get duration and publish date from metadata
            duration_sec = (meta or {}).get("duration", 0)
            duration = format_duration(duration_sec) if duration_sec else ""

            published = ""
            if upload_date and len(upload_date) == 8:
                published = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
            elif meta and meta.get("upload_date"):
                ud = meta["upload_date"]
                published = f"{ud[:4]}-{ud[4:6]}-{ud[6:8]}"

            safe_title = title.replace('"', '\\"')
            md = f"""---
type: raw-transcript
title: "{safe_title}"
youtube_id: {vid_id}
url: https://www.youtube.com/watch?v={vid_id}
slug: {slug}
published: "{published}"
duration: "{duration}"
fetched_at: {datetime.now(timezone.utc).strftime("%Y-%m-%d")}
immutable: true
---

## Transcript

"""
            for p in paragraphs:
                md += f"**[{format_ts(p['start'])}]** {p['text']}\n\n"

            (out / f"{slug}.md").write_text(md, encoding="utf-8")

            manifest_videos.append({
                "slug": slug,
                "title": title,
                "youtube_id": vid_id,
                "url": f"https://www.youtube.com/watch?v={vid_id}",
                "published": published,
                "duration": duration,
                "segments": len(segments),
                "paragraphs": len(paragraphs),
            })
            print(f"  -> {slug}.md ({len(paragraphs)} paragraphs)")

        except Exception as e:
            skipped.append({"id": vid_id, "title": title, "reason": str(e)})
            print(f"  -> ERROR: {e}")

        time.sleep(args.delay)

    # Clean up temp dir
    for f in tmp_subs.iterdir():
        f.unlink(missing_ok=True)
    tmp_subs.rmdir()

    manifest = {
        "channel": url,
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "total_videos": len(entries),
        "transcripts_fetched": len(manifest_videos),
        "skipped": len(skipped),
        "videos": manifest_videos,
        "skipped_videos": skipped,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nDone: {len(manifest_videos)} transcripts -> {out}/")
    if skipped:
        print(f"Skipped {len(skipped)} videos (no subtitles available)")


if __name__ == "__main__":
    main()
