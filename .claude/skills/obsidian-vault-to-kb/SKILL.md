---
name: obsidian-vault-to-kb
description: "Build an OKF (Open Knowledge Format) knowledge base from an Obsidian vault. Same pipeline as the YouTube skills, but the source is an Obsidian vault: wikilinks are resolved and rewritten to OKF-compliant relative markdown links, aliases and tags are preserved into OKF frontmatter, and vault config is skipped. Free, no API key. Invoke with /obsidian-vault-to-kb <path-to-vault>"
argument-hint: <path-to-obsidian-vault>
---

# Build an OKF Knowledge Base from an Obsidian Vault

Turn an Obsidian vault into a synthesized, cross-linked knowledge base in [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog). OKF is Google's open standard for LLM-readable knowledge bases: plain markdown + YAML frontmatter, navigated by index and relative links, no database or embeddings required.

Obsidian vaults are *almost* OKF-shaped — plain markdown with YAML frontmatter — with two important departures that this skill fixes on the way in:

1. Obsidian uses `[[wikilinks]]` (global-name lookups), but OKF **forbids** wikilinks and requires ordinary relative markdown links (see `SCHEMA.md` §2.4 and OKF SPEC §5). This skill resolves every `[[Target]]` and `[[Target|Alias]]` against the vault's file namespace and rewrites it to `[Alias](../relative/path/to/target.md)`.
2. Obsidian metadata (`aliases`, `tags`, cssclass, publish flags, etc.) lives in frontmatter but not in the OKF schema. This skill preserves `aliases` and `tags`, drops Obsidian-only fields, and adds the OKF-required `type: raw-source` plus `source_type: obsidian`.

Everything downstream of `raw/` (extract → canonicalize → write → index → validate) is unchanged. This skill is a thin adapter that turns "my Obsidian vault" into "an OKF-clean folder of raw markdown sources" the existing pipeline already knows how to process.

**Trade-offs:** you keep the human-authored structure of your vault (aliases, tags, backlinks) while satisfying OKF's link-format rule. Unresolved wikilinks (targets missing from the vault) are preserved as plain text and logged so you can decide whether to stub them.

## When to use this skill

Use `obsidian-vault-to-kb` when your source is an Obsidian vault or an Obsidian-flavored markdown folder that uses `[[wikilinks]]`. Good example inputs:

- Your personal Obsidian vault (notes, daily notes, MOCs)
- An exported vault a colleague sent you
- A folder of markdown notes that use `[[...]]` even if you never opened Obsidian on it

If your source is plain markdown without wikilinks, use `markdown-to-kb` instead. If it's a YouTube channel, use one of the `channel-to-kb-*` skills.

## Before you start

Read the OKF contract this bundle obeys:
1. Read `SCHEMA.md` in this repo (especially §2.4: cross-links are relative markdown paths, never wikilinks)
2. Skim the [OKF SPEC](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)

## Step 1: Ingest the vault

```bash
uv run .claude/skills/obsidian-vault-to-kb/scripts/ingest_obsidian.py $ARGUMENTS --output-dir ./raw
```

This walks the vault, resolves wikilinks, and writes:

- `raw/<slug>.md` — the immutable copy with OKF frontmatter (`type: raw-source`, `source_type: obsidian`), body rewritten so every `[[Target]]` becomes `[Target](relative/path.md)`
- `raw/manifest.json` — one entry per note, including preserved `aliases` and `tags`
- `raw/_obsidian_ingest_report.json` — one-time report listing unresolved wikilinks, ambiguous names (same basename in multiple folders), and skipped files

Flags:
- `--limit N` cap the number of notes ingested (useful for a first pass on large vaults)
- `--include-attachments` also copy referenced images/PDFs under `raw/_attachments/` (default: skipped, only referenced by path)
- `--vault-name "My Vault"` optional human label carried into frontmatter; defaults to the folder name
- `--drop-tag daily` skip notes carrying a given tag (repeatable); useful for excluding daily notes or drafts

By default the skill excludes `.obsidian/`, `.trash/`, `.git/`, and any file matching `*.excalidraw.md`.

Wait for the script to complete and review `_obsidian_ingest_report.json` before proceeding.

## Step 2: Build the OKF knowledge base

Read `.claude/references/pipeline-guide.md` for the full extract → canonicalize → write → index process. It applies identically whether the raw files are YouTube transcripts, plain markdown, or Obsidian notes; the only differences for Obsidian sources are:

- **Extract** — the raw file already contains OKF-compliant relative links (this skill rewrote them at ingest time), so extraction can follow links to find related notes if useful. Chunk by headings when present.
- **Frontmatter carry-through** — when the note has `aliases`, prefer them as candidate `title`s during canonicalization; when the note has `tags`, seed them into the canonical concept/entity page's `tags`.
- **Source page shape** — `sources/<slug>.md` uses `type: source` with `source_type: obsidian`, `origin: <vault-relative-path>`, and (if set) `vault_name`.

Process in batches per the guide.

## Step 3: Validate OKF conformance

```bash
python lint.py
```

Fix everything it reports. In particular, an Obsidian vault often has orphan or hub notes (MOCs) that will surface as `W1 orphan` warnings until the concept/entity write stage links them; that's expected during the pipeline, not a bug in the ingest.

## Wikilink resolution rules (what this skill actually does)

Obsidian resolves `[[Target]]` by matching `Target` against every filename in the vault (case-insensitive, no path). This skill does the same, with these deterministic rules:

- `[[Target]]` → `[Target](relative/path/to/target.md)` if exactly one `target.md` (case-insensitive) exists in the vault.
- `[[Target|Alias]]` → `[Alias](relative/path/to/target.md)` — the alias becomes the link text.
- `[[Target#Heading]]` → `[Target](relative/path/to/target.md#heading)` — the heading anchor is slugified per common markdown-lint rules.
- `[[folder/Target]]` → resolved by exact path within the vault first, then falls back to basename lookup.
- `![[Image.png]]` → `![Image](_attachments/image.png)` when `--include-attachments` is set; otherwise `![Image](Image.png)` is preserved as-is and the target is listed in the ingest report.
- **Ambiguous** (two files with the same basename in different folders): the wikilink is left as plain text `Target` and listed under `ambiguous` in the report. Fix by renaming one of the notes or by using the full-path form `[[folder/Target]]` in the source vault.
- **Unresolved** (target does not exist): the wikilink is stripped to plain text `Target` and listed under `unresolved` in the report.

## Example: ingest a personal vault

```bash
uv run .claude/skills/obsidian-vault-to-kb/scripts/ingest_obsidian.py \
  ~/vaults/agentic-notes \
  --output-dir ./raw \
  --vault-name "Agentic Notes" \
  --drop-tag draft \
  --drop-tag daily
```

Then follow the pipeline guide. The resulting bundle looks and lints exactly like the YouTube-sourced one, and Obsidian users can still open `raw/` in Obsidian if they want — the rewritten relative links stay valid inside Obsidian too (Obsidian falls back to relative-link resolution when a target isn't a wikilink).
