#!/usr/bin/env python3
"""Normalize note image links onto the ../assets/ convention and verify they resolve.

This site stores every attachment flat in static/assets/. The render hooks in
layouts/_default/_markup/ rewrite a destination of `../assets/NAME` to `/assets/NAME`,
so `../assets/` is the one prefix that is guaranteed to work from any note depth.
Logseq already exports that way; Obsidian, Typora and Notion do not.

The script rewrites the other spellings onto `../assets/`, leaves already-correct
Logseq links untouched, and reports anything it cannot resolve.

Dry run by default:

    scripts/fix-image-links.py              # report what would change
    scripts/fix-image-links.py --apply      # write the changes
    scripts/fix-image-links.py --orphans    # also list unreferenced assets
    scripts/fix-image-links.py --collect --apply   # move stray attachments into static/assets
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"
ASSETS = REPO / "static" / "assets"

# Destination is the canonical prefix the render hooks understand.
CANON = "../assets/"

# Prefixes other editors emit for the same flat attachment folder.
ALIAS_PREFIXES = (
    "../assets/",
    "./assets/",
    "assets/",
    "/assets/",
    "attachment/",
    "attachments/",
    "./attachment/",
    "./attachments/",
    "../attachment/",
    "../attachments/",
)

ASSET_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".avif",
    ".pdf", ".mp4", ".webm", ".mov", ".mp3", ".m4a", ".wav",
}

# Extensions a browser will never render inside an <img> tag.
NON_IMAGE_SUFFIXES = {".pdf", ".mp4", ".webm", ".mov", ".mp3", ".m4a", ".wav"}

EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//)", re.IGNORECASE)
WINDOWS_ABS = re.compile(r"^[A-Za-z]:[\\/]")
# Logseq suffixes an epoch-ms stamp and a counter: name_1772347152956_0.png
LOGSEQ_STAMP = re.compile(r"^(?P<stem>.+?)_\d{10,}_\d+$")


# --------------------------------------------------------------------------- #
# asset index
# --------------------------------------------------------------------------- #

class AssetIndex:
    """Resolve a referenced filename to a real file in static/assets."""

    def __init__(self, assets_dir: Path):
        self.dir = assets_dir
        self.names: list[str] = sorted(
            p.name for p in assets_dir.iterdir() if p.is_file()
        ) if assets_dir.is_dir() else []
        self._exact = {n: n for n in self.names}
        self._lower: dict[str, str] = {}
        self._loose: dict[str, str] = {}
        self._stamped: dict[str, list[str]] = {}
        for n in self.names:
            self._lower.setdefault(n.lower(), n)
            self._loose.setdefault(self._loose_key(n), n)
            stem, ext = os.path.splitext(n)
            m = LOGSEQ_STAMP.match(stem)
            if m:
                key = self._loose_key(m.group("stem") + ext)
                self._stamped.setdefault(key, []).append(n)

    @staticmethod
    def _loose_key(name: str) -> str:
        """Collapse the separators editors silently swap when renaming."""
        return re.sub(r"[\s_\-]+", "", name.lower())

    def resolve(self, filename: str) -> tuple[str | None, str]:
        """Return (real filename, how it was matched)."""
        if filename in self._exact:
            return filename, "exact"
        lower = self._lower.get(filename.lower())
        if lower:
            return lower, "case"
        loose = self._loose.get(self._loose_key(filename))
        if loose:
            return loose, "loose"
        # A bare `image.png` may be the un-stamped name of a Logseq export,
        # but only trust it when exactly one asset could be meant.
        candidates = self._stamped.get(self._loose_key(filename), [])
        if len(candidates) == 1:
            return candidates[0], "timestamped"
        return None, "missing"


# --------------------------------------------------------------------------- #
# markdown scanning
# --------------------------------------------------------------------------- #

@dataclass
class Link:
    """One inline link or image, with the offsets needed to rewrite it."""
    is_image: bool
    label: str
    dest: str
    start: int          # offset of `!` or `[`
    end: int            # offset just past the closing `)`
    dest_start: int
    dest_end: int
    bracketed: bool     # destination was written as <...>
    tail: str           # anything after the destination, e.g. a " title"


def _match_bracket(text: str, i: int, open_ch: str, close_ch: str) -> int:
    """Index just past the bracket opened at `i`, or -1 if unbalanced."""
    depth = 0
    while i < len(text):
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch == open_ch:
            depth += 1
        elif ch == close_ch:
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return -1


def _scan_destination(text: str, i: int) -> tuple[int, int, bool] | None:
    """Parse a CommonMark link destination starting at `i` (just past `(`)."""
    while i < len(text) and text[i] in " \t\n":
        i += 1
    if i < len(text) and text[i] == "<":
        end = text.find(">", i)
        if end == -1:
            return None
        return i + 1, end, True
    start = i
    depth = 0
    while i < len(text):
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch in " \t\n":
            break
        if ch == "(":
            depth += 1
        elif ch == ")":
            if depth == 0:
                break
            depth -= 1
        i += 1
    return (start, i, False) if i > start else None


def find_links(text: str) -> list[Link]:
    """Find inline images and links. Balanced parens in a destination are kept."""
    out: list[Link] = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch != "[":
            i += 1
            continue
        is_image = i > 0 and text[i - 1] == "!"
        label_end = _match_bracket(text, i, "[", "]")
        if label_end == -1 or label_end >= len(text) or text[label_end] != "(":
            i += 1
            continue
        parsed = _scan_destination(text, label_end + 1)
        if parsed is None:
            i += 1
            continue
        dest_start, dest_end, bracketed = parsed
        close = _match_bracket(text, label_end, "(", ")")
        if close == -1:
            i += 1
            continue
        out.append(Link(
            is_image=is_image,
            label=text[i + 1:label_end - 1],
            dest=text[dest_start:dest_end],
            start=i - 1 if is_image else i,
            end=close,
            dest_start=dest_start,
            dest_end=dest_end,
            bracketed=bracketed,
            tail=text[dest_end + (1 if bracketed else 0):close - 1],
        ))
        i = close
    return out


WIKI_EMBED = re.compile(r"!\[\[([^\[\]|]+?)(?:\|([^\[\]]*))?\]\]")


# --------------------------------------------------------------------------- #
# rewriting
# --------------------------------------------------------------------------- #

def wanted_filename(dest: str) -> str | None:
    """The attachment this destination is reaching for, or None if it isn't one."""
    if not dest or EXTERNAL.match(dest) and not WINDOWS_ABS.match(dest):
        return None
    if dest.startswith("#"):
        return None

    decoded = urllib.parse.unquote(dest)
    if WINDOWS_ABS.match(decoded):
        return decoded.replace("\\", "/").rsplit("/", 1)[-1]

    normal = decoded.replace("\\", "/")
    for prefix in ALIAS_PREFIXES:
        if normal.lower().startswith(prefix.lower()):
            # Flat store: everything past the prefix collapses to a basename.
            return normal[len(prefix):].rsplit("/", 1)[-1] or None
    if "/" not in normal and os.path.splitext(normal)[1].lower() in ASSET_SUFFIXES:
        return normal
    return None


def encode_dest(filename: str) -> str:
    """Write `../assets/NAME` so Goldmark parses it back as one destination."""
    dest = CANON + filename
    if any(c in dest for c in " \t") or not _parens_balanced(dest):
        return f"<{dest}>"
    return dest


def _parens_balanced(s: str) -> bool:
    depth = 0
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


@dataclass
class FileReport:
    path: Path
    fixed: list[str] = field(default_factory=list)
    demoted: list[str] = field(default_factory=list)
    broken: list[str] = field(default_factory=list)
    text: str = ""
    changed: bool = False


def process(path: Path, index: AssetIndex, fix_embeds: bool, demote: bool) -> FileReport:
    original = path.read_text(encoding="utf-8")
    rel = path.relative_to(REPO)
    report = FileReport(path=path)
    text = original

    if fix_embeds:
        def sub_embed(m: re.Match[str]) -> str:
            target, alias = m.group(1).strip(), (m.group(2) or "").strip()
            real, how = index.resolve(urllib.parse.unquote(target))
            if real is None:
                # Probably a note embed, not an attachment. Leave it alone.
                return m.group(0)
            report.fixed.append(f"![[{target}]] -> {CANON}{real}" + ("" if how == "exact" else f"  ({how} match)"))
            return f"![{alias}]({encode_dest(real)})"
        text = WIKI_EMBED.sub(sub_embed, text)

    # Rewrite right-to-left so earlier offsets stay valid.
    for link in reversed(find_links(text)):
        filename = wanted_filename(link.dest)
        if filename is None:
            continue
        real, how = index.resolve(filename)
        if real is None:
            report.broken.append(f"line {text.count(chr(10), 0, link.start) + 1}: {link.dest}")
            continue

        new_dest = encode_dest(real)
        current = f"<{link.dest}>" if link.bracketed else link.dest
        # An <img> pointing at a PDF or video never renders; make it a link.
        needs_demote = (
            demote
            and link.is_image
            and os.path.splitext(real)[1].lower() in NON_IMAGE_SUFFIXES
        )

        if new_dest == current and not needs_demote:
            continue

        if needs_demote:
            label = link.label or os.path.splitext(real)[0]
            replacement = f"[{label}]({new_dest}{link.tail})"
            report.demoted.append(f"{link.dest} -> link (not an image)")
        else:
            prefix = "!" if link.is_image else ""
            replacement = f"{prefix}[{link.label}]({new_dest}{link.tail})"
            note = "" if how == "exact" else f"  ({how} match)"
            report.fixed.append(f"{link.dest} -> {CANON}{real}{note}")

        text = text[:link.start] + replacement + text[link.end:]

    report.text = text
    report.changed = text != original
    return report


# --------------------------------------------------------------------------- #
# stray attachment collection
# --------------------------------------------------------------------------- #

def collect_strays(index: AssetIndex, apply: bool) -> list[str]:
    """Move attachments Obsidian dropped inside content/ into static/assets."""
    moved: list[str] = []
    for path in sorted(CONTENT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in ASSET_SUFFIXES:
            continue
        target = ASSETS / path.name
        if target.exists():
            if target.read_bytes() == path.read_bytes():
                moved.append(f"{path.relative_to(REPO)} (duplicate of existing asset)")
                if apply:
                    path.unlink()
                continue
            stem, ext = os.path.splitext(path.name)
            n = 1
            while target.exists():
                target = ASSETS / f"{stem}-{n}{ext}"
                n += 1
        moved.append(f"{path.relative_to(REPO)} -> static/assets/{target.name}")
        if apply:
            shutil.move(str(path), str(target))
    return moved


# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    ap.add_argument("--collect", action="store_true", help="move stray attachments from content/ into static/assets/")
    ap.add_argument("--orphans", action="store_true", help="list assets no note references")
    ap.add_argument("--no-embeds", action="store_true", help="leave Obsidian ![[wikilink]] embeds alone")
    ap.add_argument("--no-demote", action="store_true", help="leave ![](x.pdf) as an image instead of a link")
    ap.add_argument("--strict", action="store_true", help="exit non-zero if any link is unresolved")
    ap.add_argument("paths", nargs="*", type=Path, help="limit to these files or directories")
    args = ap.parse_args()

    if not ASSETS.is_dir():
        print(f"error: {ASSETS} does not exist", file=sys.stderr)
        return 2

    index = AssetIndex(ASSETS)

    if args.collect:
        strays = collect_strays(index, args.apply)
        if strays:
            print(f"{'moved' if args.apply else 'would move'} {len(strays)} stray attachment(s):")
            for s in strays:
                print(f"  {s}")
            print()
            index = AssetIndex(ASSETS)
        else:
            print("no stray attachments under content/\n")

    roots = args.paths or [CONTENT]
    files: list[Path] = []
    for root in roots:
        root = root if root.is_absolute() else (Path.cwd() / root)
        files.extend([root] if root.is_file() else sorted(root.rglob("*.md")))

    reports = [
        process(f, index, fix_embeds=not args.no_embeds, demote=not args.no_demote)
        for f in files
    ]

    n_fixed = n_demoted = n_broken = 0
    for r in reports:
        if not (r.fixed or r.demoted or r.broken):
            continue
        print(r.path.relative_to(REPO))
        for line in r.fixed:
            print(f"  fix     {line}")
        for line in r.demoted:
            print(f"  demote  {line}")
        for line in r.broken:
            print(f"  BROKEN  {line}")
        print()
        n_fixed += len(r.fixed)
        n_demoted += len(r.demoted)
        n_broken += len(r.broken)
        if r.changed and args.apply:
            r.path.write_text(r.text, encoding="utf-8")

    if args.orphans:
        referenced: set[str] = set()
        for f in files:
            text = f.read_text(encoding="utf-8")
            for link in find_links(text):
                name = wanted_filename(link.dest)
                if name:
                    real, _ = index.resolve(name)
                    if real:
                        referenced.add(real)
            for m in WIKI_EMBED.finditer(text):
                real, _ = index.resolve(urllib.parse.unquote(m.group(1).strip()))
                if real:
                    referenced.add(real)
        orphans = [n for n in index.names if n not in referenced]
        print(f"unreferenced assets: {len(orphans)} of {len(index.names)}")
        for n in orphans:
            print(f"  {n}")
        print()

    verb = "rewrote" if args.apply else "would rewrite"
    changed_files = sum(1 for r in reports if r.changed)
    print(
        f"{len(files)} note(s) scanned | {verb} {n_fixed} link(s) "
        f"and {n_demoted} non-image embed(s) across {changed_files} file(s) | "
        f"{n_broken} unresolved"
    )
    if not args.apply and changed_files:
        print("dry run - re-run with --apply to write these changes")

    return 1 if args.strict and n_broken else 0


if __name__ == "__main__":
    sys.exit(main())
