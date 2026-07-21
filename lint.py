#!/usr/bin/env python
"""
lint.py — deterministic health check for this OKF knowledge-base bundle.

No dependencies (stdlib only). Run from the bundle root:

    python lint.py            # full report; exit 1 if any ERROR
    python lint.py --quiet    # only print errors/warnings

Checks (see SCHEMA.md §9):
  E1  every non-reserved .md has YAML frontmatter with a non-empty `type`
  E2  every relative markdown link resolves to a file/dir in the bundle
  E3  every concept/entity/source page is listed in its directory index.md
  E4  sources/<slug>.md <-> raw/<slug>.md parity (both directions)
  W1  orphan pages: concept/entity pages with no inbound link from a non-index page
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESERVED = {"index.md", "log.md"}
# Repository tooling that is intentionally not an OKF concept doc.
META_EXEMPT_FROM_TYPE: set[str] = set()  # every .md carries a type; nothing exempt

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
TYPE_RE = re.compile(r"^type:\s*(.+?)\s*$", re.MULTILINE)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")


def strip_code(text: str) -> str:
    """Remove fenced blocks and inline code so example links in docs aren't linted."""
    return INLINE_CODE_RE.sub("", FENCE_RE.sub("", text))

errors: list[str] = []
warnings: list[str] = []


def md_files() -> list[Path]:
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]


def frontmatter(text: str) -> str | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else None


def get_type(text: str) -> str | None:
    fm = frontmatter(text)
    if fm is None:
        return None
    m = TYPE_RE.search(fm)
    return m.group(1).strip().strip('"').strip("'") if m else None


def check_types(files: list[Path]) -> None:
    for p in files:
        if p.name in RESERVED:
            continue
        t = get_type(p.read_text(encoding="utf-8"))
        if not t:
            errors.append(f"E1 missing/empty `type` frontmatter: {p.relative_to(ROOT)}")


def check_links(files: list[Path]) -> dict[Path, set[Path]]:
    """Return inbound-link map (target -> set of source pages) as a side effect."""
    inbound: dict[Path, set[Path]] = {}
    for p in files:
        text = strip_code(p.read_text(encoding="utf-8"))
        for raw in LINK_RE.findall(text):
            link = raw.split()[0]  # drop optional "title"
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = link.split("#", 1)[0]
            if not target:
                continue
            dest = (p.parent / target).resolve()
            if not dest.exists():
                errors.append(
                    f"E2 broken link `{link}` in {p.relative_to(ROOT)}"
                )
                continue
            if dest.suffix == ".md":
                inbound.setdefault(dest, set()).add(p)
    return inbound


def dir_index_targets(index: Path) -> set[Path]:
    if not index.exists():
        return set()
    targets: set[Path] = set()
    for raw in LINK_RE.findall(index.read_text(encoding="utf-8")):
        link = raw.split()[0].split("#", 1)[0]
        # Match full URL schemes, not the substring "http" — a slug like
        # `http-request-extensibility.md` is a local file, not an external URL.
        if link.startswith(("http://", "https://", "mailto:")) or not link:
            continue
        targets.add((index.parent / link).resolve())
    return targets


def check_index_coverage() -> None:
    # concepts, entities (recursive), sources: each page must appear in an index.
    groups = {
        "concepts": list((ROOT / "concepts").glob("*.md")),
        "entities": list((ROOT / "entities").rglob("*.md")),
        "sources": list((ROOT / "sources").glob("*.md")),
    }
    # Collect every target linked from every index.md in the bundle.
    all_index_targets: set[Path] = set()
    for idx in ROOT.rglob("index.md"):
        all_index_targets |= dir_index_targets(idx)
    for group, files in groups.items():
        for p in files:
            if p.name in RESERVED:
                continue
            if p.resolve() not in all_index_targets:
                errors.append(
                    f"E3 not listed in any index.md: {p.relative_to(ROOT)}"
                )


def check_source_raw_parity() -> None:
    src = {p.stem for p in (ROOT / "sources").glob("*.md") if p.name not in RESERVED}
    raw = {p.stem for p in (ROOT / "raw").glob("*.md") if p.name not in RESERVED}
    for slug in sorted(src - raw):
        errors.append(f"E4 sources/{slug}.md has no matching raw/{slug}.md")
    for slug in sorted(raw - src):
        warnings.append(f"E4 raw/{slug}.md has no matching sources/{slug}.md (not yet ingested)")


def check_orphans(inbound: dict[Path, set[Path]]) -> None:
    pages = list((ROOT / "concepts").glob("*.md")) + list((ROOT / "entities").rglob("*.md"))
    for p in pages:
        if p.name in RESERVED:
            continue
        srcs = {s for s in inbound.get(p.resolve(), set()) if s.name != "index.md"}
        if not srcs:
            warnings.append(f"W1 orphan (no inbound link from a content page): {p.relative_to(ROOT)}")


def main() -> int:
    quiet = "--quiet" in sys.argv
    files = md_files()
    check_types(files)
    inbound = check_links(files)
    check_index_coverage()
    check_source_raw_parity()
    check_orphans(inbound)

    if not quiet:
        print(f"Scanned {len(files)} markdown files under {ROOT.name}/")
    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  ERROR {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
