---
name: channel-to-kb
description: "Build an OKF (Open Knowledge Format) knowledge base from any YouTube channel. Uses Google's OKF standard so any AI can read the output with zero setup. Free, no API key. Uses pytubefix + youtube_transcript_api. Invoke with /channel-to-kb @ChannelHandle"
argument-hint: <@ChannelHandle or channel-URL>
---

# Build an OKF Knowledge Base from a YouTube Channel (Free)

Turn any YouTube channel into a synthesized, cross-linked knowledge base in [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog). OKF is Google's open standard for LLM-readable knowledge bases: plain markdown + YAML frontmatter, navigated by index and relative links, no database or embeddings required. Any AI can read the output with zero setup.

Uses pytubefix for channel enumeration and youtube_transcript_api for in-memory transcript fetching. Free, no API key required.

**Trade-offs:** fastest to set up (zero config), but transcript fetching can be blocked on cloud IPs. Run from a local machine for best results.

## Before you start

Read the OKF contract this bundle obeys:
1. Read `SCHEMA.md` in this repo (the maintainer contract: page types, frontmatter schemas, linking rules)
2. Skim the [OKF SPEC](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) for the hard rules (every page needs `type` in frontmatter, `index.md` is reserved, cross-links are relative markdown paths)

## Step 1: Fetch transcripts

```bash
uv run .claude/skills/channel-to-kb/scripts/fetch_transcripts.py $ARGUMENTS --output-dir ./raw
```

This enumerates all videos and fetches English transcripts. Output: `raw/<slug>.md` files (each with `type: raw-transcript` frontmatter, OKF-conformant) + `raw/manifest.json`.

Flags:
- `--limit N` to cap the number of videos (start here for testing)
- `--delay 2.0` to increase the pause between requests if you hit rate limits

Wait for the script to complete before proceeding.

## Step 2: Build the OKF knowledge base

Read `.claude/references/pipeline-guide.md` for the full process. It produces an OKF-conformant bundle with the structure defined in `SCHEMA.md`. The stages:

1. **Extract** - read each raw transcript, extract concepts/entities/quotes as JSON to `scripts/extractions/`
2. **Canonicalize** - merge all extractions into a frozen taxonomy (`scripts/manifest.json` + `scripts/taxonomy.json`)
3. **Write** - write OKF concept/entity/source pages from the manifest (each with proper `type`, `title`, `description` frontmatter per SCHEMA.md)
4. **Index** - build `index.md` files for each directory (OKF's navigation layer)
5. **Validate** - run `python lint.py` to enforce OKF conformance, link integrity, and index coverage

Process in batches per the guide. For channels under ~30 videos, this fits in one session. For larger channels, save your extraction JSONs and resume across sessions.

## Step 3: Validate OKF conformance

```bash
python lint.py
```

This enforces the OKF contract: every `.md` has `type` frontmatter (E1), every relative link resolves (E2), every page appears in its directory's `index.md` (E3), sources/raw parity (E4). Fix all errors. The knowledge base is ready when lint passes clean.
