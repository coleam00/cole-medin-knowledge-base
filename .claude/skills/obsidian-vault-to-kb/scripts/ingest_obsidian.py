#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
ingest_obsidian.py — ingest an Obsidian vault into OKF `raw/` entries.

Mirrors the shape of `.claude/skills/channel-to-kb/scripts/fetch_transcripts.py`
and `.claude/skills/markdown-to-kb/scripts/ingest_markdown.py`, but understands
Obsidian's wikilink flavor and rewrites every `[[Target]]` into an OKF-legal
relative markdown link (SCHEMA.md §2.4 forbids wikilinks).

For each vault note it writes:
  raw/<slug>.md                       # OKF frontmatter, body with wikilinks rewritten
  raw/manifest.json                   # {slug, title, origin, aliases, tags, ...}
  raw/_obsidian_ingest_report.json    # {unresolved, ambiguous, skipped, attachments}

Usage:
    uv run ingest_obsidian.py <vault-path> --output-dir ./raw
    uv run ingest_obsidian.py ~/vaults/agentic-notes --output-dir ./raw \\
        --vault-name "Agentic Notes" --drop-tag daily

Stdlib-only. Deterministic. Idempotent (sha256-gated rewrites).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


# --- regexes ---------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)

# [[Target]], [[Target|Alias]], [[folder/Target#Heading|Alias]]
# Not preceded by '!' (that is an embed, handled separately).
WIKILINK_RE = re.compile(r"(?<!\!)\[\[([^\[\]\n]+?)\]\]")
# ![[Image.png]] or ![[Note#Heading]] — embeds
EMBED_RE = re.compile(r"\!\[\[([^\[\]\n]+?)\]\]")

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".pdf"}

# very simple YAML list/scalar parsers (Obsidian frontmatter is usually simple)
LIST_INLINE_RE = re.compile(r"^\[(.*)\]$")


# --- helpers ---------------------------------------------------------------


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s\-_]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "untitled"


def slugify_heading(text: str) -> str:
    # markdown-lint-ish: lowercase, spaces->hyphens, drop punctuation
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s\-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


def sha256_of(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def split_frontmatter(text: str) -> tuple[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return m.group(1), text[m.end():]


def parse_simple_yaml(fm: str) -> dict:
    """Parse a subset of YAML sufficient for Obsidian frontmatter."""
    out: dict = {}
    key = None
    for raw in fm.splitlines():
        line = raw.rstrip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- ") and key is not None:
            out.setdefault(key, []).append(line[2:].strip().strip('"').strip("'"))
            continue
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        k = k.strip()
        v = v.strip()
        key = k
        if not v:
            out[k] = []  # anticipate block-list children
            continue
        m = LIST_INLINE_RE.match(v)
        if m:
            items = [i.strip().strip('"').strip("'") for i in m.group(1).split(",") if i.strip()]
            out[k] = items
        else:
            out[k] = v.strip('"').strip("'")
        key = None
    return out


def infer_title(fm: dict, body: str, fallback: str) -> str:
    for candidate in ("title",):
        v = fm.get(candidate)
        if isinstance(v, str) and v.strip():
            return v.strip()
    m = H1_RE.search(body)
    if m:
        return m.group(1).strip()
    return fallback.replace("-", " ").strip().title()


def collect_notes(vault: Path, excludes: list[str]) -> list[Path]:
    skip_dirs = {".obsidian", ".trash", ".git"}
    notes: list[Path] = []
    for p in vault.rglob("*.md"):
        if any(part in skip_dirs for part in p.relative_to(vault).parts):
            continue
        if p.name.endswith(".excalidraw.md"):
            continue
        if any(p.match(pat) for pat in excludes):
            continue
        notes.append(p)
    return sorted(notes)


def collect_attachments(vault: Path) -> dict[str, Path]:
    """Basename -> path (first hit wins deterministically by sorted order)."""
    attachments: dict[str, Path] = {}
    for p in sorted(vault.rglob("*")):
        if not p.is_file():
            continue
        if p.suffix.lower() in IMAGE_EXTS:
            attachments.setdefault(p.name.lower(), p)
    return attachments


def norm_name(s: str) -> str:
    """Normalize a name for wikilink lookup: lowercase, spaces<->hyphens<->underscores collapse."""
    s = s.lower().strip()
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s


def build_name_index(notes: list[Path], vault: Path) -> tuple[dict[str, list[Path]], dict[str, Path]]:
    """
    Return (basename_index, path_index). Names normalized so that
    'The PIV Loop', 'the-piv-loop', and 'the_piv_loop' all collide.
    """
    basename: dict[str, list[Path]] = {}
    by_path: dict[str, Path] = {}
    for p in notes:
        stem = norm_name(p.stem)
        basename.setdefault(stem, []).append(p)
        rel_parts = [norm_name(part) for part in p.relative_to(vault).with_suffix("").parts]
        by_path["/".join(rel_parts)] = p
    return basename, by_path


# --- wikilink rewriting ----------------------------------------------------


def rewrite_wikilinks(
    body: str,
    *,
    source: Path,
    vault: Path,
    basename_index: dict[str, list[Path]],
    path_index: dict[str, Path],
    output_dir: Path,
    slug_of: dict[Path, str],
    unresolved: list[str],
    ambiguous: list[str],
    attachments_index: dict[str, Path],
    include_attachments: bool,
    copied_attachments: dict[str, str],
) -> str:
    """
    Rewrite `[[...]]` and `![[...]]` in `body`.
    Links are rewritten to point at sibling files inside `output_dir` (raw/),
    because that is where the ingested copies will live.
    """

    def resolve_note(target: str) -> Path | None:
        target = target.strip()
        if not target:
            return None
        raw = target.removesuffix(".md")
        if "/" in raw:
            key_path = "/".join(norm_name(part) for part in raw.split("/"))
            if key_path in path_index:
                return path_index[key_path]
        stem = norm_name(raw.split("/")[-1])
        hits = basename_index.get(stem, [])
        if len(hits) == 1:
            return hits[0]
        if len(hits) > 1:
            ambiguous.append(target)
            return None
        unresolved.append(target)
        return None

    def replace_wikilink(m: re.Match) -> str:
        inner = m.group(1)
        anchor = ""
        alias = None
        if "|" in inner:
            inner, alias = inner.split("|", 1)
            alias = alias.strip()
        if "#" in inner:
            inner, heading = inner.split("#", 1)
            anchor = "#" + slugify_heading(heading)
        target = resolve_note(inner)
        text = alias if alias else inner.split("/")[-1]
        if target is None:
            return text  # leave as plain text, already logged
        # Both source and target end up as siblings in output_dir/<slug>.md.
        target_slug = slug_of.get(target)
        if not target_slug:
            return text
        return f"[{text}]({target_slug}.md{anchor})"

    def replace_embed(m: re.Match) -> str:
        inner = m.group(1).strip()
        # embed of a note vs. attachment
        stem, dot, ext = inner.rpartition(".")
        is_attachment = dot and ("." + ext.lower()) in IMAGE_EXTS
        if is_attachment:
            key = inner.lower().split("/")[-1]
            src = attachments_index.get(key)
            if not src:
                unresolved.append(inner)
                return f"![{inner}]({inner})"
            if include_attachments:
                # copy under raw/_attachments/, dedup by basename
                dest_name = copied_attachments.get(key)
                if not dest_name:
                    dest_dir = output_dir / "_attachments"
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    dest_name = src.name
                    shutil.copy2(src, dest_dir / dest_name)
                    copied_attachments[key] = dest_name
                return f"![{src.stem}](_attachments/{dest_name})"
            # not copying — just point at the original filename
            return f"![{src.stem}]({src.name})"
        # embed of a note: degrade to a normal link
        return replace_wikilink(re.match(r"\[\[(.+?)\]\]", f"[[{inner}]]"))

    body = EMBED_RE.sub(replace_embed, body)
    body = WIKILINK_RE.sub(replace_wikilink, body)
    return body


# --- frontmatter emission --------------------------------------------------


def build_frontmatter(
    *,
    slug: str,
    title: str,
    origin: str,
    ingested_at: str,
    sha: str,
    vault_name: str | None,
    aliases: list[str],
    tags: list[str],
) -> str:
    lines = [
        "---",
        "type: raw-source",
        "immutable: true",
        f'title: "{title.replace(chr(34), chr(39))}"',
        f"slug: {slug}",
        f'origin: "{origin}"',
        "source_type: obsidian",
    ]
    if vault_name:
        lines.append(f'vault_name: "{vault_name}"')
    if aliases:
        lines.append("aliases: [" + ", ".join(f'"{a}"' for a in aliases) + "]")
    if tags:
        lines.append("tags: [" + ", ".join(str(t) for t in tags) + "]")
    lines += [
        f"ingested_at: {ingested_at}",
        f"sha256: {sha}",
        "---",
        "",
    ]
    return "\n".join(lines)


# --- main ------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("vault", help="path to Obsidian vault (folder of .md notes)")
    ap.add_argument("--output-dir", default="./raw")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--exclude", action="append", default=None,
                    help="glob(s) relative to vault to exclude (repeatable)")
    ap.add_argument("--vault-name", default=None,
                    help='human label for the vault; defaults to the folder name')
    ap.add_argument("--drop-tag", action="append", default=None,
                    help="skip notes carrying this tag (repeatable)")
    ap.add_argument("--include-attachments", action="store_true",
                    help="copy referenced images/PDFs into raw/_attachments/")
    args = ap.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not vault.is_dir():
        print(f"error: vault is not a directory: {vault}", file=sys.stderr)
        return 2
    vault_name = args.vault_name or vault.name

    out = Path(args.output_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)

    excludes = args.exclude or []
    drop_tags = set(args.drop_tag or [])
    notes = collect_notes(vault, excludes)
    if not notes:
        print(f"error: no notes found in {vault}", file=sys.stderr)
        return 2

    # First pass: figure out slugs (deterministic) so wikilink rewriting knows
    # where each target lives inside `out/`.
    basename_index, path_index = build_name_index(notes, vault)
    slug_of: dict[Path, str] = {}
    used: set[str] = set()
    for p in notes:
        base = slugify(p.stem)
        slug = base
        i = 2
        while slug in used:
            slug = f"{base}-{i}"
            i += 1
        used.add(slug)
        slug_of[p] = slug

    attachments_index = collect_attachments(vault) if args.include_attachments else {}

    # Load prior manifest for idempotency
    manifest_path = out / "manifest.json"
    manifest: dict[str, dict] = {}
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            manifest = {}

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    unresolved: list[str] = []
    ambiguous: list[str] = []
    skipped: list[str] = []
    copied_attachments: dict[str, str] = {}

    to_process = notes[: args.limit] if args.limit else notes
    written = unchanged = 0

    for note in to_process:
        rel = note.relative_to(vault).as_posix()
        text = note.read_text(encoding="utf-8", errors="replace")
        fm_raw, body = split_frontmatter(text)
        fm = parse_simple_yaml(fm_raw) if fm_raw else {}

        tags_val = fm.get("tags") or []
        if isinstance(tags_val, str):
            tags_val = [tags_val]
        tags = [str(t).lstrip("#") for t in tags_val]
        if drop_tags & set(tags):
            skipped.append(rel)
            continue

        aliases_val = fm.get("aliases") or fm.get("alias") or []
        if isinstance(aliases_val, str):
            aliases_val = [aliases_val]
        aliases = [str(a) for a in aliases_val]

        title = infer_title(fm, body, note.stem)
        slug = slug_of[note]

        rewritten = rewrite_wikilinks(
            body,
            source=note,
            vault=vault,
            basename_index=basename_index,
            path_index=path_index,
            output_dir=out,
            slug_of=slug_of,
            unresolved=unresolved,
            ambiguous=ambiguous,
            attachments_index=attachments_index,
            include_attachments=args.include_attachments,
            copied_attachments=copied_attachments,
        )

        sha = sha256_of(rewritten)
        target = out / f"{slug}.md"
        prior = manifest.get(slug)
        if prior and prior.get("sha256") == sha and target.exists():
            unchanged += 1
            continue

        header = build_frontmatter(
            slug=slug, title=title, origin=rel, ingested_at=now, sha=sha,
            vault_name=vault_name, aliases=aliases, tags=tags,
        )
        target.write_text(header + rewritten.lstrip("\n"), encoding="utf-8")
        manifest[slug] = {
            "slug": slug,
            "title": title,
            "origin": rel,
            "source_type": "obsidian",
            "vault_name": vault_name,
            "aliases": aliases,
            "tags": tags,
            "ingested_at": now,
            "sha256": sha,
        }
        written += 1

    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    report = {
        "vault": str(vault),
        "vault_name": vault_name,
        "generated_at": now,
        "notes_scanned": len(notes),
        "notes_processed": len(to_process),
        "written": written,
        "unchanged": unchanged,
        "skipped_by_tag": skipped,
        "unresolved_wikilinks": sorted(set(unresolved)),
        "ambiguous_wikilinks": sorted(set(ambiguous)),
        "copied_attachments": sorted(copied_attachments.values()),
    }
    (out / "_obsidian_ingest_report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"ingested {len(to_process)} note(s) from {vault_name}: "
        f"{written} written/updated, {unchanged} unchanged, {len(skipped)} skipped-by-tag. "
        f"{len(set(unresolved))} unresolved, {len(set(ambiguous))} ambiguous wikilinks "
        f"(see raw/_obsidian_ingest_report.json)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
