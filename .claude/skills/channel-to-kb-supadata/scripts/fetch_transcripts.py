# /// script
# dependencies = ["supadata"]
# ///
"""Fetch all transcripts from a YouTube channel using Supadata.

Managed API. Requires a SUPADATA_API_KEY (free tier: 100 credits).

Usage:
    SUPADATA_API_KEY=your_key uv run fetch_transcripts.py @ChannelHandle
    uv run fetch_transcripts.py @ChannelHandle --api-key your_key
    uv run fetch_transcripts.py @ChannelHandle --limit 10 --output-dir ./raw
"""
import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from supadata import Supadata


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


def group_into_paragraphs(segments, target_words=50):
    paragraphs = []
    buf, start, wc = [], None, 0
    for seg in segments:
        start_sec = seg.offset / 1000.0 if hasattr(seg, "offset") else seg.get("offset", 0) / 1000.0
        text = seg.text if hasattr(seg, "text") else seg.get("text", "")
        if start is None:
            start = start_sec
        buf.append(text)
        wc += len(text.split())
        if wc >= target_words:
            paragraphs.append({"start": start, "text": " ".join(buf).strip()})
            buf, start, wc = [], None, 0
    if buf:
        paragraphs.append({"start": start, "text": " ".join(buf).strip()})
    return paragraphs


def normalize_handle(channel: str) -> str:
    if channel.startswith("http"):
        m = re.search(r"@([\w.-]+)", channel)
        if m:
            return f"@{m.group(1)}"
        m = re.search(r"/channel/(UC[\w-]+)", channel)
        if m:
            return m.group(1)
    if not channel.startswith("@"):
        return f"@{channel}"
    return channel


def main():
    ap = argparse.ArgumentParser(description="Fetch YouTube channel transcripts (Supadata)")
    ap.add_argument("channel", help="YouTube channel URL or @handle")
    ap.add_argument("--output-dir", default="./raw", help="Where to write raw/*.md files (default: ./raw)")
    ap.add_argument("--limit", type=int, default=None, help="Max videos to fetch (default: all)")
    ap.add_argument("--api-key", default=None, help="Supadata API key (or set SUPADATA_API_KEY env var)")
    ap.add_argument("--delay", type=float, default=0.5, help="Seconds between requests (default: 0.5)")
    args = ap.parse_args()

    api_key = args.api_key or os.environ.get("SUPADATA_API_KEY")
    if not api_key:
        print("Error: set SUPADATA_API_KEY or pass --api-key", file=sys.stderr)
        sys.exit(1)

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    sd = Supadata(api_key=api_key)
    handle = normalize_handle(args.channel)
    limit = args.limit or 5000

    print(f"Enumerating videos for {handle} ...")
    channel_resp = sd.youtube.channel.videos(id=handle, type="video", limit=limit)
    video_ids = channel_resp.videoIds if hasattr(channel_resp, "videoIds") else channel_resp.get("videoIds", [])
    print(f"Found {len(video_ids)} videos\n")

    if not video_ids:
        print("No videos found. Check the channel handle.", file=sys.stderr)
        sys.exit(1)

    manifest_videos = []
    used_slugs: set[str] = set()
    skipped = []

    for i, vid_id in enumerate(video_ids):
        vid_url = f"https://www.youtube.com/watch?v={vid_id}"
        print(f"[{i + 1}/{len(video_ids)}] {vid_id}")

        try:
            transcript = sd.transcript(url=vid_url, text=False, lang="en", mode="native")
            content = transcript.content if hasattr(transcript, "content") else transcript.get("content", [])

            if not content:
                skipped.append({"id": vid_id, "title": "", "reason": "empty transcript"})
                print(f"  -> SKIPPED (empty)")
                time.sleep(args.delay)
                continue

            # Get title from transcript metadata if available
            title = ""
            if hasattr(transcript, "title"):
                title = transcript.title or ""
            if not title:
                title = vid_id

            paragraphs = group_into_paragraphs(content)

            # Calculate duration from last segment
            if content:
                last = content[-1]
                last_offset = last.offset if hasattr(last, "offset") else last.get("offset", 0)
                last_dur = last.duration if hasattr(last, "duration") else last.get("duration", 0)
                total_ms = last_offset + last_dur
                duration = format_duration(total_ms / 1000.0)
            else:
                duration = ""

            slug = slugify(title)
            if not slug:
                slug = vid_id
            if slug in used_slugs:
                n = 2
                while f"{slug}-{n}" in used_slugs:
                    n += 1
                slug = f"{slug}-{n}"
            used_slugs.add(slug)

            safe_title = title.replace('"', '\\"')
            md = f"""---
type: raw-transcript
title: "{safe_title}"
youtube_id: {vid_id}
url: https://www.youtube.com/watch?v={vid_id}
slug: {slug}
published: ""
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
                "url": vid_url,
                "duration": duration,
                "paragraphs": len(paragraphs),
            })
            print(f"  -> {slug}.md ({len(paragraphs)} paragraphs)")

        except Exception as e:
            skipped.append({"id": vid_id, "title": "", "reason": str(e)})
            print(f"  -> ERROR: {e}")

        time.sleep(args.delay)

    manifest = {
        "channel": handle,
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "total_videos": len(video_ids),
        "transcripts_fetched": len(manifest_videos),
        "skipped": len(skipped),
        "videos": manifest_videos,
        "skipped_videos": skipped,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nDone: {len(manifest_videos)} transcripts -> {out}/")
    if skipped:
        print(f"Skipped {len(skipped)} videos (no transcripts available)")


if __name__ == "__main__":
    main()
