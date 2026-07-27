# Pipeline Guide: Raw Transcripts to OKF Knowledge Base

This is the step-by-step process for turning a directory of raw transcripts (`raw/*.md`) into a complete [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog) knowledge base. The output is a Karpathy-style LLM wiki conforming to the [OKF SPEC](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md): plain markdown + YAML frontmatter, navigated by index and relative links, readable by any AI with zero setup.

The architecture: **extract wide, canonicalize once, write wide**. Two parallel passes with one serial barrier in the middle.

## Prerequisites

Before starting, confirm:
- `raw/*.md` files exist with correct OKF frontmatter (`type: raw-transcript`, `immutable: true`)
- `raw/manifest.json` exists listing all videos
- You have read `SCHEMA.md` (the OKF contract every page obeys: page types, frontmatter schemas, linking conventions)
- You understand the OKF hard rules: every page has a `type` in YAML frontmatter, `index.md` is reserved for directory listings, cross-links are relative markdown paths (never `[[wikilinks]]`)

## Phase 1: Extract (per video, parallelizable)

For each `raw/<slug>.md`, read the full transcript and extract the concepts and entities it teaches. Write one JSON file per video to `scripts/extractions/<slug>.json`.

**Process each transcript in batches of ~10.** For each video:

1. Read the raw transcript
2. Identify the concepts (ideas, techniques, patterns, mental models) and entities (tools, people, organizations) the video substantively teaches
3. For each concept/entity, capture 1-3 verbatim timestamped quotes (copy exact words from the transcript)
4. Write the extraction as JSON

**Extraction JSON format:**
```json
{
  "slug": "<video-slug>",
  "thesis": "one-sentence thesis of the video",
  "summary": "2-3 paragraph synthesized summary",
  "tags": ["3-7 lowercase topic tags"],
  "key_moments": [{"ts": "H:MM:SS", "note": "what happens"}],
  "concepts": [
    {
      "slug": "kebab-case-id",
      "name": "Display Name",
      "one_liner": "one-sentence definition",
      "tags": ["topic-tags"],
      "quotes": [{"ts": "H:MM:SS", "text": "verbatim quote, <=240 chars"}],
      "related": ["other-concept-slugs"]
    }
  ],
  "entities": [
    {
      "slug": "kebab-case-id",
      "name": "Display Name",
      "subtype": "tool|person|organization",
      "one_liner": "what it is",
      "resource": "canonical URL if known",
      "quotes": [{"ts": "H:MM:SS", "text": "verbatim quote"}]
    }
  ]
}
```

**Rules:**
- Use STABLE, GENERAL slugs: `the-piv-loop` not `plan-implement-validate-loop`
- Only extract what the video ACTUALLY teaches substantively (typically 5-20 concepts, 3-15 entities)
- Quotes must be VERBATIM from the transcript at real timestamps
- Skip sponsor reads, one-off tool mentions, and noise

## Phase 2: Canonicalize (once, serial, the barrier)

This is the critical step. Load all extraction JSONs and merge them into a single frozen taxonomy.

1. **Aggregate:** Group concept candidates by normalized slug across all extractions. For each group, collect: slug, name variants, video count, all one-liners, union of tags, all quotes with their source video.

2. **Deduplicate:** Merge near-identical candidates into single canonical pages. Examples of merges:
   - `piv-loop` + `the-piv-loop` + `plan-implement-validate` -> `the-piv-loop`
   - `claude-code` + `claude-code-cli` -> `claude-code`

3. **Apply the page-creation threshold:** A concept gets its own page if it appears in >= 2 videos OR is the subject of one clearly substantial deep-dive. Below that bar, it is a mention on a parent page, not its own file.

4. **Assign themes:** Group each concept into a theme (e.g., "AI coding landscape", "Memory systems", "RAG & retrieval"). These drive the index structure.

5. **Do the same for entities:** Deduplicate, assign subtype (tool/person/organization) by majority vote, keep canonical URLs.

6. **Freeze the manifest:** Write `scripts/manifest.json` with every canonical page, its description, related slugs, and per-video quotes. Also write `scripts/taxonomy.json` with theme groupings.

**The manifest is the contract.** After this step, no structural decisions remain. Writers execute against the manifest without inventing new pages or merging anything.

## Phase 3: Write OKF pages (per page, parallelizable)

With the manifest frozen, write every page as an OKF concept document. Every page MUST have YAML frontmatter with a non-empty `type` field (the only strictly required OKF field). Process in batches of ~7 pages. Follow the page schemas defined in `SCHEMA.md`.

### 3a. Source pages (`sources/<slug>.md`)

One per video. Each is a 2-3 paragraph synthesized summary (NOT a transcript dump), plus structured sections.

```yaml
---
type: source
title: "Full Video Title"
description: "One-sentence thesis."
youtube_id: abc123
url: https://www.youtube.com/watch?v=abc123
slug: video-slug
published: "2026-05-14"
duration: "14:52"
raw: "../raw/video-slug.md"
tags: [topic1, topic2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Body: summary, `## Concepts covered` (links to concept pages), `## Entities` (links to entity pages), `## Key moments` (timestamped), `## Transcript` (link to raw).

### 3b. Concept pages (`concepts/<slug>.md`)

Each synthesizes EVERY video that discusses the concept, cited under `## Sources`.

```yaml
---
type: concept
title: "The PIV Loop"
description: "One-sentence definition."
tags: [workflow, planning]
videos: [video-slug-1, video-slug-2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Body: open by DEFINING the concept with a verbatim timestamped quote. Then typed-edge sections (`## Prerequisites`, `## Builds on`, `## Contrasts with`, `## Implemented by`, `## Tools`, `## Related`). End with mandatory `## Sources`:
```markdown
## Sources

- [Video Title](../sources/video-slug.md) - "[H:MM:SS] verbatim quote from the video"
- [Another Video](../sources/another-slug.md) - "[H:MM:SS] another quote"
```

Target: 250-600 words of synthesis. Link liberally.

### 3c. Entity pages (`entities/{tools,people,organizations}/<slug>.md`)

```yaml
---
type: entity
subtype: tool
title: "Claude Code"
description: "One-sentence description."
resource: "https://canonical-url.com"
tags: [coding-agent]
videos: [video-slug-1, video-slug-2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Body: what it is and how it is used in the channel's context. Typed edges: `## Realizes`, `## Contrasts with`, `## Works with`, `## Related`. Mandatory `## Sources`.

### OKF linking rules (critical)

Per the OKF SPEC, cross-links are ordinary relative markdown links. The kind of relationship is carried by the section heading the link sits under (OKF links are untyped; we recover semantics from headings).

- ALL links are **relative markdown paths**: `[Name](../concepts/slug.md)`, `[Name](../entities/tools/slug.md)`
- **Never** use `[[wikilinks]]` (OKF requires standard markdown links)
- Bidirectional: if A links to B, B links back to A
- Type every edge with the heading it lives under (`## Prerequisites`, `## Builds on`, `## Contrasts with`, `## Implemented by`, `## Related`, `## Sources`)

## Phase 4: Build OKF Indexes

Every directory needs an `index.md` (a reserved filename in OKF, used for directory listings). Entries format:
```markdown
- [Display Name](relative-path.md) - one-line description
```

Group under `## Theme` headings using the taxonomy from Phase 2. If a `scripts/build_indexes.py` script exists, run it:
```bash
python scripts/build_indexes.py
```

Otherwise, build them by hand: `concepts/index.md`, `entities/index.md` (with sub-indexes for `tools/`, `people/`, `organizations/`), `sources/index.md`, `raw/index.md`.

The **root `index.md`** declares `okf_version: "0.1"` in its frontmatter (per OKF SPEC) and links to all sub-indexes plus theme groupings. This is the most important file in the bundle - it is what any consuming AI reads first to navigate the knowledge base. Invest in it.

## Phase 5: Validate OKF Conformance

Run `python lint.py` and fix every error. This enforces the OKF SPEC and the bundle's own SCHEMA.md contract:
- E1: every `.md` has YAML frontmatter with non-empty `type` (OKF's one hard rule)
- E2: every relative markdown link resolves to a real file (OKF uses relative links, never wikilinks)
- E3: every concept/entity/source page appears in its directory's `index.md` (OKF navigation completeness)
- E4: `sources/` and `raw/` have matching slugs (provenance integrity)
- W1: orphan pages with no inbound links (link density is a quality signal)

Iterate until lint passes clean.

## Batching guidance for large channels

For channels with 50+ videos, process in stages across sessions:
- **Extract:** 10-15 videos per batch
- **Canonicalize:** do this ONCE after all extractions are complete
- **Write:** 7-10 pages per batch
- Save your `scripts/extractions/`, `scripts/manifest.json`, and `scripts/taxonomy.json` between sessions
