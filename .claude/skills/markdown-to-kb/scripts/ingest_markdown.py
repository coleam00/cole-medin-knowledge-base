#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
ingest_markdown.py — normalize a folder of markdown files into OKF `raw/` entries.

Mirrors the shape of `.claude/skills/channel-to-kb/scripts/fetch_transcripts.py`
but the input is a local folder of `.md` files instead of a YouTube channel.

Each input file becomes:
  raw/<slug>.md         # immutable copy with OKF frontmatter (type: raw-source)
  raw/manifest.json     # append/refresh entry: {slug, title, origin, ...}

Usage:
    uv run ingest_markdown.py <source-folder> --output-dir ./raw
    uv run ingest_markdown.py ~/dynamous-export --output-dir ./raw \\
        --source-name "Dynamous AI Mastery" \\
        --source-url  "https://dynamous.ai/"

The script is deterministic and idempotent: re-running over the same folder
updates the manifest in place and rewrites raw files only when their sha256
changes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s\-_]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "untitled"


def sha256_of(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def strip_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_text_without_fences, body). Empty frontmatter if absent."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return m.group(1), text[m.end():]


def infer_title(body: str, fallback: str) -> str:
    m = H1_RE.search(body)
    if m:
        return m.group(1).strip()
    return fallback.replace("-", " ").strip().title()


def build_frontmatter(
    *,
    slug: str,
    title: str,
    origin: str,
    ingested_at: str,
    sha: str,
    source_name: str | None,
    source_url: str | None,
) -> str:
    lines = [
        "---",
        "type: raw-source",
        "immutable: true",
        f'title: "{title.replace(chr(34), chr(39))}"',
        f"slug: {slug}",
        f'origin: "{origin}"',
        "source_type: markdown",
    ]
    if source_name:
        lines.append(f'source_name: "{source_name}"')
    if source_url:
        lines.append(f"source_url: {source_url}")
    lines += [
        f"ingested_at: {ingested_at}",
        f"sha256: {sha}",
        "---",
        "",
    ]
    return "\n".join(lines)


def collect(source: Path, includes: list[str], excludes: list[str]) -> list[Path]:
    seen: dict[Path, None] = {}
    for pattern in includes:
        for p in source.glob(pattern):
            if p.is_file() and p.suffix.lower() == ".md":
                seen[p.resolve()] = None
    for pattern in excludes:
        for p in source.glob(pattern):
            seen.pop(p.resolve(), None)
    return sorted(seen)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("source", help="folder of markdown files to ingest")
    ap.add_argument("--output-dir", default="./raw", help="target directory (default: ./raw)")
    ap.add_argument("--include", action="append", default=None,
                    help="glob(s) to include (default: **/*.md)")
    ap.add_argument("--exclude", action="append", default=None,
                    help="glob(s) to exclude (repeatable)")
    ap.add_argument("--limit", type=int, default=0, help="max files to ingest (0 = all)")
    ap.add_argument("--source-name", default=None,
                    help='human label for the collection, e.g. "Dynamous AI Mastery"')
    ap.add_argument("--source-url", default=None,
                    help="canonical URL for the collection")
    args = ap.parse_args()

    source = Path(args.source).expanduser().resolve()
    if not source.is_dir():
        print(f"error: source is not a directory: {source}", file=sys.stderr)
        return 2

    out = Path(args.output_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)

    includes = args.include or ["**/*.md"]
    excludes = args.exclude or []
    files = collect(source, includes, excludes)
    if args.limit:
        files = files[: args.limit]

    if not files:
        print(f"error: no markdown files matched under {source}", file=sys.stderr)
        return 2

    manifest_path = out / "manifest.json"
    manifest: dict[str, dict] = {}
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            manifest = {}

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    used_slugs: set[str] = set(manifest.keys())
    written = 0
    unchanged = 0

    for src_path in files:
        rel = src_path.relative_to(source).as_posix()
        raw_text = src_path.read_text(encoding="utf-8", errors="replace")
        _, body = strip_frontmatter(raw_text)

        base_slug = slugify(src_path.stem)
        slug = base_slug
        i = 2
        # deterministic disambiguation by relative path if two files collide
        if slug in used_slugs and manifest.get(slug, {}).get("origin") != rel:
            parent_hint = slugify(src_path.parent.name) if src_path.parent != source else ""
            candidate = f"{parent_hint}-{base_slug}" if parent_hint else f"{base_slug}-{i}"
            while candidate in used_slugs and manifest.get(candidate, {}).get("origin") != rel:
                i += 1
                candidate = f"{base_slug}-{i}"
            slug = candidate
        used_slugs.add(slug)

        title = infer_title(body, base_slug)
        sha = sha256_of(body)
        target = out / f"{slug}.md"

        prior = manifest.get(slug)
        if prior and prior.get("sha256") == sha and target.exists():
            unchanged += 1
            continue

        frontmatter = build_frontmatter(
            slug=slug,
            title=title,
            origin=rel,
            ingested_at=now,
            sha=sha,
            source_name=args.source_name,
            source_url=args.source_url,
        )
        target.write_text(frontmatter + body.lstrip("\n"), encoding="utf-8")
        manifest[slug] = {
            "slug": slug,
            "title": title,
            "origin": rel,
            "source_type": "markdown",
            "source_name": args.source_name,
            "source_url": args.source_url,
            "ingested_at": now,
            "sha256": sha,
        }
        written += 1

    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"ingested {len(files)} file(s) from {source}: "
        f"{written} written/updated, {unchanged} unchanged. "
        f"manifest: {manifest_path.relative_to(Path.cwd()) if manifest_path.is_relative_to(Path.cwd()) else manifest_path}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
