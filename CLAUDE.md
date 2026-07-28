# Cole Medin AI Knowledge Base

This is an [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog) knowledge base synthesized from Cole Medin's entire long-form YouTube catalog on agentic coding, AI engineering, RAG, memory systems, and more.

## How to use it

1. Read `index.md` first - it groups every concept by theme and links to all sub-indexes.
2. Read `SCHEMA.md` for the page types and frontmatter contract.
3. Follow relative links into `concepts/`, `entities/`, and `sources/` to answer questions.
4. Every concept and entity page ends with a `## Sources` section citing the exact video(s) and timestamps the information came from. Always cite these when answering.

## Structure

- **`concepts/`** - ideas, techniques, patterns, mental models (one page per idea, synthesizing every video that covers it)
- **`entities/`** - tools, people, organizations (subfolders: `tools/`, `people/`, `organizations/`)
- **`sources/`** - one summary page per video with key moments and linked concepts
- **`raw/`** - immutable timestamped transcripts (the source of truth)
- **`index.md`** - the entry point and navigation map

## Rules

- Navigate by index, not by loading everything. Open only the pages a question needs.
- Cross-links are relative markdown paths (never wikilinks) per OKF convention.
- If something is not covered in the knowledge base, say so instead of guessing.
- When answering, cite the concept/entity pages used and the source video(s) they came from.
