#!/usr/bin/env python3
"""Lightweight status check for the markdown wiki."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
INDEX = WIKI / "index.md"


def markdown_pages():
    return sorted(p for p in WIKI.rglob("*.md") if p.is_file())


def wikilinks(text):
    return re.findall(r"\[\[([^\]]+)\]\]", text)


def main():
    pages = markdown_pages()
    index_text = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    known = {p.relative_to(WIKI).with_suffix("").as_posix() for p in pages}
    known.update({p.stem for p in pages})

    broken = []
    for page in pages:
        text = page.read_text(encoding="utf-8")
        for link in wikilinks(text):
            target = link.split("|", 1)[0].strip().lstrip("/")
            target = target[:-3] if target.endswith(".md") else target
            if target not in known and target.replace("../", "") not in known:
                broken.append((page.relative_to(ROOT), link))

    unindexed = [
        p.relative_to(WIKI).as_posix()
        for p in pages
        if p.name not in {"index.md"} and p.stem not in index_text and p.relative_to(WIKI).with_suffix("").as_posix() not in index_text
    ]

    print(f"wiki_pages: {len(pages)}")
    print(f"broken_wikilinks: {len(broken)}")
    for page, link in broken:
        print(f"  - {page}: [[{link}]]")
    print(f"unindexed_pages: {len(unindexed)}")
    for page in unindexed:
        print(f"  - {page}")


if __name__ == "__main__":
    main()

