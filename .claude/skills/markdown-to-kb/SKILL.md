---
name: markdown-to-kb
description: "Build an OKF (Open Knowledge Format) knowledge base from any folder of markdown files (course notes, docs, blog posts, exports, wikis). Same pipeline as the YouTube skills, but the source is markdown instead of transcripts. Free, no API key. Invoke with /markdown-to-kb <path-to-markdown-folder>"
argument-hint: <path-to-markdown-folder>
---

# Build an OKF Knowledge Base from a Folder of Markdown Files

Turn any folder of markdown files into a synthesized, cross-linked knowledge base in [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog). OKF is Google's open standard for LLM-readable knowledge bases: plain markdown + YAML frontmatter, navigated by index and relative links, no database or embeddings required. Any AI can read the output with zero setup.

Unlike the `channel-to-kb-*` skills (which turn YouTube transcripts into an OKF bundle), this skill accepts **any folder of markdown files** as the source: course exports, documentation, blog archives, wiki dumps, note vaults, meeting notes, RFCs, ADRs — anything already in `.md`. It normalizes each file into an immutable `raw/<slug>.md` with OKF frontmatter, then runs the same extract → canonicalize → write → index → validate pipeline.

**Trade-offs:** you skip the whole "fetch transcripts" step, but you own the input quality. Garbage-in-garbage-out applies — if your markdown lacks structure or has no natural topical grouping, the extraction pass will still work but the resulting taxonomy will be shallow.

## When to use this skill

Use `markdown-to-kb` when your source material is already text and you want it treated as first-class OKF sources. Good example inputs:

- A folder of exported course modules (e.g. Dynamous AI Mastery lessons in markdown)
- A dumped Substack / blog archive
- A folder of RFCs, ADRs, or design docs
- Exported wiki pages (any wiki, any format, as long as they are `.md`)
- Meeting notes, retros, or postmortems

If your source is a YouTube channel, use `channel-to-kb`, `channel-to-kb-ytdlp`, or `channel-to-kb-supadata` instead. If your source is markdown, use this skill.

## Before you start

Read the OKF contract this bundle obeys:
1. Read `SCHEMA.md` in this repo (the maintainer contract: page types, frontmatter schemas, linking rules)
2. Skim the [OKF SPEC](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) for the hard rules (every page needs `type` in frontmatter, `index.md` is reserved, cross-links are relative markdown paths)

The key difference from the YouTube skills: source pages carry `type: source` with a `source_type: markdown` field (instead of `youtube_id` / `url` / `duration`). The provenance model is otherwise identical — every synthesized concept/entity cites the raw markdown file(s) it came from.

## Step 1: Ingest markdown files

```bash
uv run .claude/skills/markdown-to-kb/scripts/ingest_markdown.py $ARGUMENTS --output-dir ./raw
```

This walks the source folder, normalizes each `.md` file (slugifies the filename, preserves the original path in frontmatter as `origin`), and writes:

- `raw/<slug>.md` — the immutable copy with `type: raw-source` frontmatter (OKF-conformant)
- `raw/manifest.json` — one entry per ingested file: `{slug, title, origin, ingested_at, sha256, source_type}`

Flags:
- `--limit N` cap the number of files (useful for a first pass on a large folder)
- `--include "**/*.md"` glob pattern (default: `**/*.md`)
- `--exclude "**/README.md"` glob pattern to skip boilerplate
- `--source-name "Dynamous AI Mastery"` optional human label carried into frontmatter and later used in citations
- `--source-url "https://dynamous.ai/"` optional canonical URL for the collection, used in `## Sources` sections

Wait for the script to complete before proceeding.

## Step 2: Build the OKF knowledge base

Read `.claude/references/pipeline-guide.md` for the full extract → canonicalize → write → index process. It applies identically whether the raw files are YouTube transcripts or markdown docs; the only differences are:

1. **Extract** — read each raw markdown file (from `raw/*.md`) instead of a transcript, extract concepts/entities/quotes as JSON to `scripts/extractions/`. When the source has headings, prefer them as chunk boundaries; fall back to ~800-word windows only when the file is flat.
2. **Canonicalize** — merge all extractions into a frozen taxonomy (`scripts/manifest.json` + `scripts/taxonomy.json`)
3. **Write** — write OKF concept/entity/source pages from the manifest. Source pages use the `type: source` schema with `source_type: markdown` and `origin: <original relative path>` in place of the YouTube fields; the `raw:` pointer works the same way.
4. **Index** — build `index.md` files for each directory (OKF's navigation layer)
5. **Validate** — run `python lint.py` to enforce OKF conformance, link integrity, and index coverage

Process in batches per the guide. For folders under ~30 files, this fits in one session. For larger folders, save your extraction JSONs and resume across sessions.

## Step 3: Validate OKF conformance

```bash
python lint.py
```

This enforces the OKF contract: every `.md` has `type` frontmatter (E1), every relative link resolves (E2), every page appears in its directory's `index.md` (E3), sources/raw parity (E4). Fix all errors. The knowledge base is ready when lint passes clean.

## Example: ingest a Dynamous AI Mastery course export

```bash
# You have ~10 markdown files exported from a Dynamous course lesson
uv run .claude/skills/markdown-to-kb/scripts/ingest_markdown.py ~/dynamous-export \
  --output-dir ./raw \
  --source-name "Dynamous AI Mastery" \
  --source-url "https://dynamous.ai/"
```

Then follow the pipeline guide. You will end up with concept pages like `concepts/ai-second-brain.md` and `concepts/pydantic-ai-agents.md`, entity pages like `entities/tools/pydantic-ai.md`, and one `sources/<slug>.md` per lesson — all cross-linked, all citing the raw markdown they came from, all lint-clean.
