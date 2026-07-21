#!/usr/bin/env python
"""
build_indexes.py - regenerate every directory index.md from the taxonomy + frontmatter.

Deterministic and idempotent. Reads each page's `title` + `description` and writes
grouped, progressive-disclosure listings (SCHEMA §7). The thematic groupings are NOT
hardcoded here: they live in `scripts/taxonomy.json` (produced by the ingestion/merge
pass), so scaling the bundle never requires editing this script. Anything present on
disk but absent from the taxonomy lands under "Other", so nothing is silently dropped.

Run from anywhere:

    python scripts/build_indexes.py

taxonomy.json shape:
{
  "concept_themes":   [["Theme name", ["slug", ...]], ...],
  "tool_themes":      [["Theme name", ["slug", ...]], ...],
  "source_clusters":  [["Cluster name", ["slug", ...]], ...]
}
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAXONOMY = json.loads((ROOT / "scripts" / "taxonomy.json").read_text(encoding="utf-8"))

FM_TITLE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)
FM_DESC = re.compile(r"^description:\s*(.+?)\s*$", re.MULTILINE)
FM_DUR = re.compile(r"^duration:\s*(.+?)\s*$", re.MULTILINE)


def meta(p: Path) -> tuple[str, str, str]:
    text = p.read_text(encoding="utf-8")
    fm = text[3 : text.find("\n---", 3)] if text.startswith("---") else ""
    t = FM_TITLE.search(fm)
    d = FM_DESC.search(fm)
    dur = FM_DUR.search(fm)
    title = (t.group(1) if t else p.stem).strip().strip('"').strip("'")
    desc = (d.group(1) if d else "").strip().strip('"').strip("'")
    # Brackets in a display title break markdown link syntax [a [b]](url); soften them.
    title = title.replace("[", "(").replace("]", ")")
    return title, desc, (dur.group(1).strip().strip('"') if dur else "")


def bullet(rel: str, title: str, desc: str) -> str:
    return f"- [{title}]({rel})" + (f" - {desc}" if desc else "")


def grouped_index(directory: Path, themes, header: str, intro: str) -> None:
    present = {p.stem: p for p in directory.glob("*.md") if p.name != "index.md"}
    listed: set[str] = set()
    lines = [f"# {header}", "", intro, ""]
    for name, ids in themes:
        rows = []
        for i in ids:
            if i in present:
                t, d, _ = meta(present[i])
                rows.append(bullet(f"{i}.md", t, d))
                listed.add(i)
        if rows:
            lines.append(f"## {name}")
            lines += rows + [""]
    leftover = sorted(set(present) - listed)
    if leftover:
        lines.append("## Other")
        for i in leftover:
            t, d, _ = meta(present[i])
            lines.append(bullet(f"{i}.md", t, d))
        lines.append("")
    (directory / "index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"  wrote {(directory / 'index.md').relative_to(ROOT)} ({len(present)} pages)")


def flat_index(directory: Path, header: str, intro: str) -> None:
    pages = sorted(p for p in directory.glob("*.md") if p.name != "index.md")
    lines = [f"# {header}", "", intro, ""]
    for p in pages:
        t, d, _ = meta(p)
        lines.append(bullet(f"{p.name}", t, d))
    (directory / "index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"  wrote {(directory / 'index.md').relative_to(ROOT)} ({len(pages)} pages)")


def sources_index() -> None:
    directory = ROOT / "sources"
    present = {p.stem: p for p in directory.glob("*.md") if p.name != "index.md"}
    lines = ["# Sources", "",
             "One synthesized summary per video, with provenance to the immutable "
             "[raw transcript](../raw/index.md). Grouped by theme.", ""]
    listed: set[str] = set()
    for name, slugs in TAXONOMY.get("source_clusters", []):
        rows = []
        for s in slugs:
            if s in present:
                t, d, _ = meta(present[s])
                rows.append(bullet(f"{s}.md", t, d))
                listed.add(s)
        if rows:
            lines.append(f"## {name}")
            lines += rows + [""]
    leftover = sorted(set(present) - listed)
    if leftover:
        lines.append("## Other")
        for s in leftover:
            t, d, _ = meta(present[s])
            lines.append(bullet(f"{s}.md", t, d))
        lines.append("")
    (directory / "index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"  wrote sources/index.md ({len(present)} pages)")


def raw_index() -> None:
    directory = ROOT / "raw"
    pages = sorted((p for p in directory.glob("*.md") if p.name != "index.md"),
                   key=lambda p: p.stem)
    lines = ["# Raw Transcripts", "",
             "Immutable, timestamped transcripts (the source of truth); never hand-edit. "
             "Synthesized summaries live in [sources/](../sources/index.md).", ""]
    for p in pages:
        t, _, dur = meta(p)
        lines.append(f"- [{t}]({p.name})" + (f" - {dur}" if dur else ""))
    (directory / "index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"  wrote raw/index.md ({len(pages)} transcripts)")


def entities_root() -> None:
    lines = [
        "# Entities", "",
        "Nameable things that exist across the videos, split by kind.", "",
        "## Groups", "",
        "- [Tools & products](tools/index.md) - coding agents, SDKs, RAG/data tools, integrations.",
        "- [People](people/index.md) - creators and voices referenced in the videos.",
        "- [Organizations](organizations/index.md) - the companies and research labs behind the tools.",
        "",
    ]
    (ROOT / "entities" / "index.md").write_text("\n".join(lines), encoding="utf-8")
    print("  wrote entities/index.md")


def main() -> int:
    print("Building indexes from scripts/taxonomy.json ...")
    grouped_index(ROOT / "concepts", TAXONOMY.get("concept_themes", []), "Concepts",
                  "Ideas, techniques, patterns, and mental models mined from the videos. "
                  "Grouped by theme.")
    entities_root()
    grouped_index(ROOT / "entities" / "tools", TAXONOMY.get("tool_themes", []),
                  "Tools & Products",
                  "Tools, products, and frameworks referenced across the videos.")
    flat_index(ROOT / "entities" / "people", "People",
               "Creators and voices referenced in the videos.")
    flat_index(ROOT / "entities" / "organizations", "Organizations",
               "The companies and research labs behind the tools and ideas.")
    sources_index()
    raw_index()
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
