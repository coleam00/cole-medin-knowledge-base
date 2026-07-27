# /// script
# dependencies = ["pytubefix", "youtube-transcript-api"]
# ///
"""Fetch all transcripts from a YouTube channel.

Uses pytubefix (channel enumeration) + youtube_transcript_api (in-memory transcripts).
Free, no API key required.

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

from pytubefix import Channel
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
)


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


def normalize_channel_url(channel: str) -> str:
    if channel.startswith("http"):
        return channel
    handle = channel if channel.startswith("@") else f"@{channel}"
    return f"https://www.youtube.com/{handle}"


def main():
    ap = argparse.ArgumentParser(description="Fetch YouTube channel transcripts (free)")
    ap.add_argument("channel", help="YouTube channel URL or @handle")
    ap.add_argument("--output-dir", default="./raw", help="Where to write raw/*.md files (default: ./raw)")
    ap.add_argument("--limit", type=int, default=None, help="Max videos to fetch (default: all)")
    ap.add_argument("--delay", type=float, default=1.5, help="Seconds between transcript requests (default: 1.5)")
    args = ap.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    url = normalize_channel_url(args.channel)
    print(f"Enumerating videos from {url} ...")

    c = Channel(url)
    all_urls = list(c.video_urls)
    if args.limit:
        all_urls = all_urls[: args.limit]

    video_entries = []
    for u in all_urls:
        vid_id = str(u).split("v=")[1].split("&")[0]
        video_entries.append({"id": vid_id, "url": str(u)})

    print(f"Found {len(video_entries)} videos\n")

    if not video_entries:
        print("No videos found. Check the channel URL.", file=sys.stderr)
        sys.exit(1)

    api = YouTubeTranscriptApi()
    manifest_videos = []
    used_slugs: set[str] = set()
    skipped = []

    for i, entry in enumerate(video_entries):
        vid_id = entry["id"]
        print(f"[{i + 1}/{len(video_entries)}] {vid_id}")

        try:
            transcript = api.fetch(vid_id, languages=["en"])
            segments = transcript.to_raw_data()
            paragraphs = group_into_paragraphs(segments)

            # Derive title from the first ~10 words of transcript if we don't have it
            # pytubefix video_urls doesn't include titles; we use the transcript API response
            title = vid_id
            try:
                from pytubefix import YouTube
                yt = YouTube(f"https://www.youtube.com/watch?v={vid_id}")
                title = yt.title or vid_id
            except Exception:
                if paragraphs:
                    title = " ".join(paragraphs[0]["text"].split()[:10]) + "..."

            slug = slugify(title)
            if not slug:
                slug = vid_id
            if slug in used_slugs:
                n = 2
                while f"{slug}-{n}" in used_slugs:
                    n += 1
                slug = f"{slug}-{n}"
            used_slugs.add(slug)

            if segments:
                last = segments[-1]
                total_sec = last["start"] + last.get("duration", 0)
                duration = format_duration(total_sec)
            else:
                duration = ""

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
                "url": f"https://www.youtube.com/watch?v={vid_id}",
                "duration": duration,
                "segments": len(segments),
                "paragraphs": len(paragraphs),
            })
            print(f"  {title}")
            print(f"  -> {slug}.md ({len(paragraphs)} paragraphs)")

        except (TranscriptsDisabled, NoTranscriptFound) as e:
            skipped.append({"id": vid_id, "title": "", "reason": type(e).__name__})
            print(f"  -> SKIPPED ({type(e).__name__})")
        except Exception as e:
            skipped.append({"id": vid_id, "title": "", "reason": str(e)})
            print(f"  -> ERROR: {e}")

        time.sleep(args.delay)

    manifest = {
        "channel": url,
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "total_videos": len(video_entries),
        "transcripts_fetched": len(manifest_videos),
        "skipped": len(skipped),
        "videos": manifest_videos,
        "skipped_videos": skipped,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nDone: {len(manifest_videos)} transcripts -> {out}/")
    if skipped:
        print(f"Skipped {len(skipped)} videos (no captions available)")


if __name__ == "__main__":
    main()
