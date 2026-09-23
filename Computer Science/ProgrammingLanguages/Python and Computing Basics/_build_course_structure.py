#!/usr/bin/env python3
"""Build the Obsidian-friendly course tree from the two source originals.

The source Markdown and PDF are deliberately left in place.  Every Markdown
teaching section is copied verbatim (apart from promoting its section heading
to the note title); the generated navigation, practice, glossary, review, and
reference notes only organise those copies.
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "original.md"
PDF_TEXT = ROOT / "_cs_algorithms_handbook_extracted.txt"

MODULES = {
    1: "Computer Hardware",
    2: "Systems, Translation & Operating Systems",
    3: "Programs, Algorithms & the Shell",
    4: "Python Workshop & Environment",
    5: "Python Syntax & Semantics",
    6: "Control Flow & Iteration",
    7: "Built-in Data Structures",
    8: "Functions, Scope & Abstraction",
    9: "Objects, Classes & the Data Model",
    10: "Modules, Packages & Distribution",
    11: "Data, Files & the Standard Library",
    12: "Software Engineering Discipline",
    13: "Algorithms & Computational Thinking",
    14: "Concurrency & Performance",
    15: "Inside CPython",
    16: "Data Science & Numerical Computing",
    17: "Machine Learning",
    18: "Web Development",
    19: "Cybersecurity",
    20: "Systems & DevOps",
}

META_HEADINGS = ("Common misconceptions", "Exercises", "Cumulative glossary", "References and further study")
INVALID_FILENAME = re.compile(r'[<>:"/\\|?*]')


def clean_filename(value: str) -> str:
    """Make a portable filename while retaining the visible source title."""
    return INVALID_FILENAME.sub(" -", value).rstrip(" .")


def write_note(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def note_title(chunk: str) -> str:
    return chunk.splitlines()[0].removeprefix("## ").strip()


def as_note(chunk: str) -> str:
    """Only the structural heading changes; the supplied source body is exact."""
    lines = chunk.splitlines()
    lines[0] = "# " + lines[0].removeprefix("## ")
    return "\n".join(lines)


def split_chapters(source: str) -> tuple[str, dict[int, list[str]]]:
    starts = list(re.finditer(r"^# Chapter (\d+) — .+$", source, re.MULTILINE))
    preface = source[: starts[0].start()]
    chapters: dict[int, list[str]] = {}
    for index, match in enumerate(starts):
        number = int(match.group(1))
        end = starts[index + 1].start() if index + 1 < len(starts) else len(source)
        body = source[match.end() : end]
        headings = list(re.finditer(r"^## .+$", body, re.MULTILINE))
        chunks = [body[heading.start() : (headings[position + 1].start() if position + 1 < len(headings) else len(body))].strip()
                  for position, heading in enumerate(headings)]
        chapters[number] = chunks
    return preface, chapters


def is_meta(title: str, kind: str) -> bool:
    lowered = title.lower()
    if kind == "practice":
        return "exercises" in lowered
    if kind == "review":
        return "common misconceptions" in lowered
    if kind == "glossary":
        return "cumulative glossary" in lowered
    if kind == "sources":
        return "references and further study" in lowered
    return any(marker.lower() in lowered for marker in META_HEADINGS)


def build_moc(number: int, module: str, topics: list[tuple[str, str]], extras: list[tuple[str, str]]) -> str:
    lines = [
        f"# {number:02d} MOC - {module}",
        "",
        f"This folder contains the complete source material for Chapter {number}, split into navigable topic notes.",
        "",
        "## Topics",
    ]
    lines.extend(f"- [ ] [[{filename}|{title}]]" for filename, title in topics)
    if extras:
        lines.extend(["", "## Chapter resources"])
        lines.extend(f"- [[{filename}|{label}]]" for filename, label in extras)
    return "\n".join(lines)


def algorithm_title(page: str, page_number: int) -> str:
    for line in page.splitlines():
        candidate = line.strip().replace("\x0c", "")
        if re.match(r"^[a-z_][a-z0-9_]*(?:\([^)]*\))? (?:FUNCTION|CLASS|HELPER)$", candidate):
            return candidate.split("(")[0].split(" ")[0]
    for line in page.splitlines():
        candidate = line.strip().replace("\x0c", "")
        if candidate and not candidate.startswith("CS Algorithms Toolkit") and not re.fullmatch(r"\d+", candidate):
            return candidate[:70]
    return f"Handbook page {page_number}"


def algorithm_category(line: str) -> str | None:
    value = line.strip().replace("\x0c", "")
    match = re.fullmatch(r"(\d+)\s+([A-Z][A-Z &-]+)", value)
    if not match:
        return None
    return f"{int(match.group(1)):02d} {match.group(2).title()}"


def build_algorithm_handbook() -> tuple[list[str], int] | None:
    """Organise PDF extraction by its printed section/page boundaries.

    A page is deliberately retained as a unit: it prevents a code listing or
    worked example from being silently cut in half during PDF-to-text import.
    """
    if not PDF_TEXT.exists():
        print("Algorithm handbook extraction not found; retaining the existing handbook notes unchanged.")
        return None

    text = PDF_TEXT.read_text(encoding="utf-8")
    pages = text.split("\f")
    handbook_root = ROOT / "90 Algorithms Handbook"
    groups: defaultdict[str, list[tuple[str, str]]] = defaultdict(list)
    current = "00 Handbook Guides"
    self_test_pages: list[str] = []
    for page_number, page in enumerate(pages, start=1):
        if not page.strip():
            continue
        category = next((algorithm_category(line) for line in page.splitlines() if algorithm_category(line)), None)
        if category:
            current = category
        if "Appendix: self-tests" in page or "Self-tests" in page:
            current = "11 Self Tests"
            self_test_pages.append(page)
        title = algorithm_title(page, page_number)
        filename = clean_filename(f"{page_number:02d} {title}")
        relative = f"{current}/{filename}"
        write_note(handbook_root / f"{relative}.md", "# " + title + "\n\n" + page.strip())
        groups[current].append((relative, title))

    moc_lines = [
        "# 90 MOC - Algorithms Handbook",
        "",
        "Page-preserving topic notes extracted from [[cs_algorithms_handbook.pdf]]. The original PDF remains the canonical layout source.",
    ]
    for group, entries in sorted(groups.items()):
        moc_lines.extend(["", f"## {group}"])
        moc_lines.extend(f"- [[{relative}|{title}]]" for relative, title in entries)
    write_note(handbook_root / "90 MOC - Algorithms Handbook.md", "\n".join(moc_lines))
    if self_test_pages:
        write_note(
            ROOT / "91 Practice Questions" / "90 Algorithms Handbook - Self Tests.md",
            "# Algorithms Handbook - Self Tests\n\n" + "\n\n".join(self_test_pages),
        )
    return sorted(groups), sum(len(entries) for entries in groups.values())


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    preface, chapters = split_chapters(source)
    if sorted(chapters) != list(range(1, 23)):
        raise ValueError("Expected the source document to contain Chapters 1–22.")

    # The introductory title, editorial standard, and original table of contents
    # are source content too, so preserve them as a standalone note.
    write_note(ROOT / "00 Start Here" / "Original Scope and Table of Contents.md", preface.strip())

    glossary_entries: list[tuple[str, str]] = []
    source_entries: list[tuple[str, str]] = []
    practice_entries: list[tuple[str, str]] = []
    review_entries: list[tuple[str, str]] = []
    module_entries: list[tuple[int, str, str]] = []
    topic_count = 0

    for number, module in MODULES.items():
        folder = ROOT / f"{number:02d} {module}"
        chunks = chapters[number]
        topics: list[tuple[str, str]] = []
        extras: list[tuple[str, str]] = []
        for chunk in chunks:
            title = note_title(chunk)
            filename = clean_filename(title)
            if is_meta(title, "practice"):
                practice_name = f"{number:02d} {module} - Practice Questions"
                write_note(ROOT / "91 Practice Questions" / f"{practice_name}.md", as_note(chunk))
                practice_entries.append((practice_name, f"{number:02d} {module}"))
                extras.append((practice_name, "Practice Questions"))
            elif is_meta(title, "review"):
                review_name = f"{number:02d} {module} - Review Sheet"
                write_note(ROOT / "94 Review Sheets" / f"{review_name}.md", as_note(chunk))
                review_entries.append((review_name, f"{number:02d} {module}"))
                extras.append((review_name, "Common Misconceptions Review"))
            elif is_meta(title, "glossary"):
                glossary_name = f"{number:02d} {module} - Glossary"
                write_note(ROOT / "00 Glossary" / f"{glossary_name}.md", as_note(chunk))
                glossary_entries.append((glossary_name, f"{number:02d} {module}"))
                extras.append((glossary_name, "Chapter Glossary"))
            elif is_meta(title, "sources"):
                source_name = f"{number:02d} {module} - References"
                write_note(ROOT / "96 Sources and Further Reading" / f"{source_name}.md", as_note(chunk))
                source_entries.append((source_name, f"{number:02d} {module}"))
                extras.append((source_name, "References and Further Study"))
            else:
                write_note(folder / f"{filename}.md", as_note(chunk))
                topics.append((filename, title))
                topic_count += 1
        moc_name = f"{number:02d} MOC - {module}"
        write_note(folder / f"{moc_name}.md", build_moc(number, module, topics, extras))
        module_entries.append((number, module, moc_name))

    # Chapter 21 is the already-curated A–Z glossary. Its sections remain
    # individual notes so the exact source definitions are easy to navigate.
    az_entries: list[tuple[str, str]] = []
    for chunk in chapters[21]:
        title = note_title(chunk)
        filename = clean_filename(title)
        write_note(ROOT / "00 Glossary" / f"{filename}.md", as_note(chunk))
        az_entries.append((filename, title))

    # Chapter 22 is organised as source-literacy and bibliographic notes.
    for chunk in chapters[22]:
        title = note_title(chunk)
        filename = clean_filename(title)
        write_note(ROOT / "96 Sources and Further Reading" / f"{filename}.md", as_note(chunk))
        source_entries.append((filename, title))

    write_note(
        ROOT / "00 Glossary" / "00 Glossary MOC.md",
        "# Glossary MOC\n\n## Chapter glossaries\n"
        + "\n".join(f"- [[{name}|{label}]]" for name, label in glossary_entries)
        + "\n\n## Cumulative A–Z glossary from the source\n"
        + "\n".join(f"- [[{name}|{label}]]" for name, label in az_entries),
    )
    write_note(
        ROOT / "91 Practice Questions" / "91 Practice Questions MOC.md",
        "# Practice Questions MOC\n\nThe original chapter exercises are retained without rewriting or answer-key changes.\n\n"
        + "\n".join(f"- [[{name}|{label}]]" for name, label in practice_entries)
        + "\n- [[90 Algorithms Handbook - Self Tests|Algorithms Handbook Self Tests]]",
    )
    write_note(
        ROOT / "94 Review Sheets" / "94 Review Sheets MOC.md",
        "# Review Sheets MOC\n\n"
        + "\n".join(f"- [[{name}|{label}]]" for name, label in review_entries),
    )
    write_note(
        ROOT / "96 Sources and Further Reading" / "96 Sources MOC.md",
        "# Sources and Further Reading MOC\n\n"
        + "\n".join(f"- [[{name}|{label}]]" for name, label in source_entries),
    )
    handbook_result = build_algorithm_handbook()
    if handbook_result is None:
        groups: list[str] = []
        handbook_page_count = 0
        handbook_coverage = (
            "The algorithm-handbook source extraction is not present in this folder, so the existing handbook notes were retained unchanged."
        )
    else:
        groups, handbook_page_count = handbook_result
        handbook_coverage = (
            f"The handbook was extracted into {handbook_page_count} page-preserving notes across {len(groups)} groups."
        )

    home_lines = [
        "# Computing & Python - Home",
        "",
        "Start with [[Original Scope and Table of Contents]], then follow the mandatory modules in numeric order. Modules 16–20 are optional specialist branches after the mandatory trunk.",
        "",
        "## Core navigation",
        "- [[00 Glossary MOC|Glossary]]",
        "- [[91 Practice Questions MOC|Practice Questions]]",
        "- [[94 Review Sheets MOC|Review Sheets]]",
        "- [[96 Sources MOC|Sources and Further Reading]]",
        "- [[90 MOC - Algorithms Handbook|Algorithms Handbook]]",
        "",
        "## Mandatory trunk",
    ]
    home_lines.extend(f"- [[{moc}|{number:02d} {module}]]" for number, module, moc in module_entries[:15])
    home_lines.extend(["", "## Optional branches"])
    home_lines.extend(f"- [[{moc}|{number:02d} {module}]]" for number, module, moc in module_entries[15:])
    write_note(ROOT / "Home.md", "\n".join(home_lines))
    write_note(
        ROOT / "00 Start Here" / "Source Coverage.md",
        "# Source Coverage\n\n"
        "The final curriculum source is preserved unchanged:\n"
        "- [[original.md]]\n"
        f"The Markdown source was split into {topic_count} teaching notes, {len(practice_entries)} chapter practice notes, "
        f"{len(glossary_entries) + len(az_entries)} glossary notes, and {len(source_entries)} source notes. "
        f"{handbook_coverage}\n\n"
        "Generated by [[_build_course_structure.py]]. Re-run it after deliberately replacing a source original.",
    )
    print(f"Generated {topic_count} teaching notes and {handbook_page_count} handbook notes.")


if __name__ == "__main__":
    main()