#!/usr/bin/env python3
"""Generate complete Module 07 Linear Algebra topic bundles."""
from __future__ import annotations

import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from module07_topics import TOPICS  # noqa: E402

BASE = Path("/home/Marau/Marau/University/Maths for CS")
MOD = BASE / "07 Linear Algebra"
WE = BASE / "90 Worked Examples"
PQ = BASE / "91 Practice Questions"
MT = BASE / "92 Mastery Tests"
AN = BASE / "93 Answers and Mark Schemes"
GL = BASE / "00 Glossary/Terms"

PASS = "85%"
PASS_MARKS = 22


def gen_topic_note(t: dict) -> str:
    name = t["id"] + " " + t["title"]
    lines = [
        f"# {name}",
        "",
        f"Tags: {t['tags']}",
        "",
        "## Position in the Course",
        f"Prerequisites: {', '.join('[[' + p + ']]' for p in t['prereq'])}",
        "",
        f"Used later in: {', '.join('[[' + u + ']]' for u in t['used_later'])}",
        "",
        "Mastery threshold: 85% overall, and 100% on the New Words section.",
        "",
        "> [!tip] How to study this note",
        "> Read one concept, cover it, then explain it aloud in your own words. After each example, copy the problem onto paper and solve it again without looking. Matrices reward slow, labelled steps.",
        "",
        "## Plain-English Idea",
        t["plain"],
        "",
    ]
    if t.get("everyday"):
        lines += ["> [!example] Everyday idea", f"> {t['everyday']}", ""]
    lines += ["## New Words"]
    for term, defn in t["terms"]:
        lines.append(f"- [[{term}]] - {defn}")
    lines += ["", "You pass this topic only when you can define all five terms without looking.", ""]
    for i, c in enumerate(t["concepts"], 1):
        lines.append(f"## Concept {i} - {c['title']}")
        lines.append("")
        lines.extend(c["body"])
        lines.append("")
        lines.append(f"> [!{c['callout']}] {c['callout_title']}")
        for cl in c["callout_body"]:
            lines.append(f"> {cl}")
        lines.append("")
        lines.append("### Chunked Example")
        lines.append(f"Question: {c['q']}")
        lines.append("")
        for j, s in enumerate(c["steps"], 1):
            lines.append(f"Step {j}: {s}")
        lines.append("")
        lines.append(f"Answer: {c['answer']}")
        lines.append("")
    lines += [
        "## Why This Works",
        t["why"],
        "",
        "For fully worked solutions, use [[" + name + " - Worked Examples]].",
        "",
        "## Common Mistakes",
    ]
    for m in t["mistakes"]:
        lines.append(f"- {m}")
    lines += [
        "",
        "> [!failure] Mistake pattern",
        f"> {t['failure']}",
        "",
        "## Where This Shows Up in CS",
        t["cs_intro"],
        "",
    ]
    lines.extend(t["cs_body"])
    lines += ["", "## Checkpoint Questions"]
    for i, q in enumerate(t["checkpoint"], 1):
        lines.append(f"{i}. {q}")
    lines += ["", "## Mini-Quiz"]
    for i, q in enumerate(t["mini_quiz"], 1):
        lines.append(f"{i}. {q}")
    lines += [
        "",
        "## Pass Gate",
        f"You may move to [[{t['next']}]] only when you can:",
        "",
        "- define every term in [[#New Words]] without looking",
    ]
    for pg in t["pass_gate"]:
        lines.append(f"- {pg}")
    lines += [
        "- answer at least 9 out of 10 mini-quiz questions correctly",
        f"- complete [[{name} - Mastery Test]] with at least {PASS_MARKS}/25 marks",
        "",
        "## Related Notes",
        f"Backward links: {', '.join('[[' + p + ']]' for p in t['prereq'])}",
        "",
        f"Forward links: {', '.join('[[' + u + ']]' for u in t['used_later'])}",
        "",
        f"Assessment links: [[{name} - Worked Examples]], [[{name} - Practice Questions]], [[{name} - Mastery Test]], [[{name} - Answers]]",
    ]
    return "\n".join(lines) + "\n"


def gen_worked(t: dict) -> str:
    name = t["id"] + " " + t["title"]
    lines = [
        f"# {name} - Worked Examples",
        "",
        f"Theory note: [[{name}]]",
        "",
        f"Use these examples before attempting [[{name} - Practice Questions]].",
        "",
        "> [!tip] How to use worked examples",
        "> Read the worked solution once. Then cover it and solve the same question again on paper. If you cannot repeat it, you are not ready for the practice sheet yet.",
        "",
    ]
    for i, ex in enumerate(t["worked"], 1):
        lines += [f"## Example {i} - {ex['title']}", "", f"Question: {ex['q']}", ""]
        for j, s in enumerate(ex["steps"], 1):
            lines.append(f"### Step {j}")
            lines.append(s)
            lines.append("")
        lines.append(f"Answer: **{ex['answer']}**")
        lines.append("")
        if ex.get("note"):
            lines += [f"> [!important] {ex['note']}", ""]
    return "\n".join(lines) + "\n"


def gen_practice(t: dict) -> str:
    name = t["id"] + " " + t["title"]
    lines = [
        f"# {name} - Practice Questions",
        "",
        f"Theory note: [[{name}]]",
        "",
        f"Answers: [[{name} - Answers]]",
        "",
        "> [!warning] Practice rule",
        "> Try every question on paper before checking the answers. If you only read the answers, you are training recognition, not recall.",
        "",
    ]
    sec = ["A. Vocabulary", "B. Core Skills", "C. Spot the Mistake", "D. Mixed Practice", "E. Computer Science Transfer"]
    n = 1
    for s, qs in zip(sec, t["practice_sections"]):
        lines.append(f"## {s}")
        for q in qs:
            lines.append(f"{n}. {q}")
            n += 1
        lines.append("")
    total = sum(len(x) for x in t["practice_sections"])
    target = int(total * 0.85)
    lines.append(f"Pass target: 85%. You should get at least {target} out of {total} correct before taking [[{name} - Mastery Test]].")
    return "\n".join(lines) + "\n"


def gen_mastery(t: dict) -> str:
    name = t["id"] + " " + t["title"]
    lines = [
        f"# {name} - Mastery Test",
        "",
        f"Theory note: [[{name}]]",
        "",
        f"Answers: [[{name} - Answers]]",
        "",
        f"Pass mark: 85%. You must score full marks on Section A before moving on.",
        "",
        "> [!danger] Test condition",
        "> Do this without looking at the topic note, worked examples, or answers. Use paper. Mark it afterwards.",
        "",
        "## Section A - Definitions",
        "Each answer must be in your own words.",
        "",
    ]
    n = 1
    for term, _ in t["terms"]:
        lines.append(f"{n}. What is [[{term}]]? (1 mark)")
        n += 1
    lines += ["", "## Section B - Core Skills"]
    for q in t["mastery_b"]:
        lines.append(f"{n}. {q}")
        n += 1
    lines += ["", "## Section C - Spot the Mistake"]
    for q in t["mastery_c"]:
        lines.append(f"{n}. {q}")
        n += 1
    lines += ["", "## Section D - Apply and Prove"]
    for q in t["mastery_d"]:
        lines.append(f"{n}. {q}")
        n += 1
    lines += ["", "## Section E - Computer Science Transfer"]
    for q in t["mastery_e"]:
        lines.append(f"{n}. {q}")
        n += 1
    lines += [
        "",
        "## Marking",
        "Total: 25 marks.",
        "",
        "Pass:",
        "",
        f"- Section A: {len(t['terms'])} out of {len(t['terms'])} required.",
        f"- Overall: at least {PASS_MARKS} out of 25.",
        "",
        "Decision:",
        "",
        f"- [ ] Pass - move to [[{t['next']}]].",
        "- [ ] Review - create a correction note in [[94 Review Sheets]] and retake tomorrow.",
        f"- [ ] Restart - reread [[{name}]] and redo the worked examples.",
    ]
    return "\n".join(lines) + "\n"


def gen_answers(t: dict) -> str:
    name = t["id"] + " " + t["title"]
    lines = [
        f"# {name} - Answers",
        "",
        f"Theory note: [[{name}]]",
        "",
        f"Practice questions: [[{name} - Practice Questions]]",
        "",
        f"Mastery test: [[{name} - Mastery Test]]",
        "",
        "> [!note] Marking guidance",
        "> Some explanation answers can be worded differently. Mark them correct if the meaning is precise and the learner could use the idea without help.",
        "",
        "## Practice Answers",
        "",
    ]
    sec_names = ["A. Vocabulary", "B. Core Skills", "C. Spot the Mistake", "D. Mixed Practice", "E. Computer Science Transfer"]
    idx = 1
    for sn, ans in zip(sec_names, t["practice_answers"]):
        lines.append(f"### {sn}")
        for a in ans:
            lines.append(f"{idx}. {a}")
            idx += 1
        lines.append("")
    lines += ["## Mastery Test Answers", ""]
    for i, a in enumerate(t["mastery_answers"], 1):
        lines.append(f"{i}. {a}")
    lines += [
        "",
        "## Mark Scheme",
        f"- Section A (Definitions): {len(t['terms'])} marks (1 each)",
        "- Section B (Core Skills): 6 marks",
        "- Section C (Spot the Mistake): 4 marks",
        "- Section D (Apply and Prove): 5 marks",
        "- Section E (CS Transfer): 5 marks",
        "",
        f"Pass: Section A full marks required; overall {PASS_MARKS}/25 minimum ({PASS}).",
    ]
    return "\n".join(lines) + "\n"


def gen_glossary(term: str, defn: str, topic: str, builds_on: str, cs_use: str) -> str:
    return f"""# {term}

{defn}

First introduced in: [[{topic}]]
Builds on: {builds_on}
Used in CS: {cs_use}

## Related Notes
Search backlinks in Obsidian to see every topic that uses [[{term}]].
"""


def main() -> None:
    files: list[str] = []
    line_counts: dict[str, int] = {}
    for t in TOPICS:
        name = t["id"] + " " + t["title"]
        topic_content = gen_topic_note(t)
        topic_path = MOD / f"{name}.md"
        line_counts[str(topic_path)] = len(topic_content.splitlines())
        paths = [
            (topic_path, topic_content),
            (WE / f"{name} - Worked Examples.md", gen_worked(t)),
            (PQ / f"{name} - Practice Questions.md", gen_practice(t)),
            (MT / f"{name} - Mastery Test.md", gen_mastery(t)),
            (AN / f"{name} - Answers.md", gen_answers(t)),
        ]
        for p, content in paths:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
            files.append(str(p))
        for term, defn in t["terms"]:
            gp = GL / f"{term}.md"
            builds = t["glossary_builds"].get(term, t["prereq"][0] if t["prereq"] else "4.8 Vectors Basics")
            if not builds.startswith("[["):
                builds = f"[[{builds}]]"
            gp.write_text(
                gen_glossary(term, defn, name, builds, t["glossary_cs"][term]),
                encoding="utf-8",
            )
            files.append(str(gp))
    print(f"Generated {len(files)} files\n")
    for f in sorted(files):
        rel = Path(f).relative_to(BASE)
        lc = line_counts.get(f, "")
        extra = f" ({lc} lines)" if lc else ""
        print(f"  {rel}{extra}")
    short = [f for f, n in line_counts.items() if n < 350]
    if short:
        print(f"\nWarning: {len(short)} topic notes under 350 lines")


if __name__ == "__main__":
    main()
