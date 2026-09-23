#!/usr/bin/env python3
"""Generate complete Module 11 Advanced Topics bundles."""
from pathlib import Path

BASE = Path("/home/Marau/Marau/University/Maths for CS")
MOD = BASE / "11 Advanced & Masters-Level Topics"
WE = BASE / "90 Worked Examples"
PQ = BASE / "91 Practice Questions"
MT = BASE / "92 Mastery Tests"
AN = BASE / "93 Answers and Mark Schemes"
GL = BASE / "00 Glossary/Terms"

PASS = "85%"
PASS_MARKS = 22


def gen_topic_note(t):
    name = t["id"] + " " + t["title"]
    lines = [
        f"# {name}",
        "",
        f"Tags: {t['tags']}",
        "",
        "## You need these breadcrumbs",
        "",
    ]
    for bc in t["breadcrumbs"]:
        lines.append(f"- [[{bc}]]")
    lines += [
        "",
        "Return to any breadcrumb you cannot explain without looking. Module 11 assumes proof notation, asymptotic reasoning, and prior CS maths — not arithmetic drills.",
        "",
        "## Position in the Course",
        f"Prerequisites: {', '.join('[[' + p + ']]' for p in t['prereq'])}",
        "",
        f"Used later in: {', '.join('[[' + u + ']]' for u in t['used_later'])}",
        "",
        "Mastery threshold: 85% overall, and 100% on the New Words section.",
        "",
        "> [!tip] How to study this note",
        "> Read one concept, cover it, then explain it aloud in your own words. After each example, copy the problem onto paper and solve it again without looking.",
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
        "- define every term in [[#New Words]]",
    ]
    for pg in t["pass_gate"]:
        lines.append(f"- {pg}")
    lines += [
        "- answer at least 9 out of 10 mini-quiz questions correctly",
        f"- complete [[{name} - Mastery Test]]",
        "",
        "## Related Notes",
        f"Backward links: {', '.join('[[' + p + ']]' for p in t['prereq'])}",
        "",
        f"Forward links: {', '.join('[[' + u + ']]' for u in t['used_later'])}",
        "",
        f"Assessment links: [[{name} - Worked Examples]], [[{name} - Practice Questions]], [[{name} - Mastery Test]], [{name} - Answers]]",
    ]
    return "\n".join(lines) + "\n"


def gen_worked(t):
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
        lines += [f"## Example {i} - {ex['title']}", f"Question: {ex['q']}", ""]
        for j, s in enumerate(ex["steps"], 1):
            lines.append(f"### Step {j}")
            if isinstance(s, list):
                lines.extend(s)
            else:
                lines.append(s)
            lines.append("")
        lines.append(f"Answer: **{ex['answer']}**")
        lines.append("")
        if ex.get("note"):
            lines += [f"> [!important] {ex['note']}", ""]
    return "\n".join(lines) + "\n"


def gen_practice(t):
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
    idx = 1
    for s, qs in zip(sec, t["practice_sections"]):
        lines.append(f"## {s}")
        for q in qs:
            lines.append(f"{idx}. {q}")
            idx += 1
        lines.append("")
    total = sum(len(x) for x in t["practice_sections"])
    target = int(total * 0.85)
    lines.append(f"Pass target: 85%. You should get at least {target} out of {total} correct before taking [[{name} - Mastery Test]].")
    return "\n".join(lines) + "\n"


def gen_mastery(t):
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
        "## Section A - Definitions (5 marks)",
        "Each answer must be in your own words. All five required to pass.",
        "",
    ]
    n = 1
    for term, _ in t["terms"]:
        lines.append(f"{n}. What is [[{term}]]? (1 mark)")
        n += 1
    lines += ["", "## Section B - Core Skills (8 marks)"]
    for q in t["mastery_b"]:
        lines.append(f"{n}. {q}")
        n += 1
    lines += ["", "## Section C - Spot the Mistake (4 marks)"]
    for q in t["mastery_c"]:
        lines.append(f"{n}. {q}")
        n += 1
    lines += ["", "## Section D - Apply and Prove (5 marks)"]
    for q in t["mastery_d"]:
        lines.append(f"{n}. {q}")
        n += 1
    lines += ["", "## Section E - Computer Science Transfer (3 marks)"]
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
        f"- Overall: at least {PASS_MARKS} out of 25 ({PASS}).",
        "",
        "Decision:",
        "",
        f"- [ ] Pass - move to [[{t['next']}]].",
        "- [ ] Review - create a correction note in [[94 Review Sheets]] and retake tomorrow.",
        f"- [ ] Restart - reread [[{name}]] and redo the worked examples.",
    ]
    return "\n".join(lines) + "\n"


def gen_answers(t):
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
        "- Section B (Core Skills): 8 marks",
        "- Section C (Spot the Mistake): 4 marks",
        "- Section D (Apply and Prove): 5 marks",
        "- Section E (CS Transfer): 3 marks",
        "",
        f"Pass: Section A full marks required; overall {PASS_MARKS}/25 minimum ({PASS}).",
    ]
    return "\n".join(lines) + "\n"


def gen_glossary(term, defn, topic, builds_on, cs_use):
    return f"""# {term}

{defn}

First introduced in: [[{topic}]]
Builds on: [[{builds_on}]]
Used in CS: {cs_use}

## Related Notes
Search backlinks in Obsidian to see every topic that uses [[{term}]].
"""


def gen_cumulative(topics):
    sections = []
    marks_per = 2
    total = 0
    for t in topics:
        name = t["id"] + " " + t["title"]
        sections.append(f"### {t['id']} - {t['title']} ({marks_per} marks)")
        for i, q in enumerate(t["cum_questions"], 1):
            sections.append(f"{i}. {q} (1 mark)")
        sections.append("")
        total += marks_per + len(t["cum_questions"])
    body = "\n".join(sections)
    return f"""# 11 Advanced & Masters-Level Topics - Cumulative Test

Use this after completing every topic in [[11 MOC - Advanced Topics]].

> [!danger] Test conditions
> Closed book. Paper only. Allow 120 minutes. Pass target: 85%.

## Instructions
Answer every section from memory. Show reasoning for proof and calculation questions. Definitions must be precise.

{body}

## Reflection
- Which three topics felt strongest?
- Which three topics need review?
- Which topic connects most clearly to computer science?
- Which prerequisite from earlier modules should you revisit?

## Marking
Total: 54 marks. Pass: 46/54 (85%).

Decision:
- [ ] Pass - you have completed Module 11 at mastery level.
- [ ] Review - retake weak topics and write correction notes in [[94 Review Sheets]].
- [ ] Restart - rebuild foundations from [[10.1 Big O Theta and Omega]] and [[5.11 Proof by Induction]].
"""


def gen_unlock(topics):
    items = [f"- [[{t['id']} {t['title']}]] - {t['cs_one_liner']}" for t in topics]
    return f"""# 11 Advanced & Masters-Level Topics - What This Unlocks in CS

Prepare for master's-level AI, algorithms, security, theory, and research-heavy CS.

This module bridges undergraduate CS maths to research papers, advanced systems, and specialist security. Each topic assumes you can read notation, follow proofs, and connect abstract definitions to concrete implementations.

## CS Connections
{chr(10).join(items)}

## Concrete Unlocks

### Algorithms and complexity
Reductions and hierarchy results explain why some problems resist fast exact algorithms — motivating randomisation, approximation, and heuristics in production systems.

### Machine learning
Statistical learning theory, optimisation, multivariable calculus, and representation learning are the mathematical backbone of training and deploying neural networks responsibly.

### Security and cryptography
Finite fields, elliptic curves, and lattice problems underpin modern TLS, signatures, and post-quantum migration paths.

### Programming language theory
Lambda calculus, semantics, and category theory clarify how compilers, type systems, and functional abstractions relate.

### Research readiness
Information theory and mathematical writing prepare you to read papers, state claims precisely, and communicate proofs in dissertations and technical reports.

## Study Path
1. Complete complexity → randomisation → approximation before graph and learning topics.
2. Treat optimisation, calculus, and linear algebra as one ML stack — revisit together when training models.
3. Do cryptography topics (11.13–11.16) in order; each layer uses the previous algebraic structure.
4. Finish with information theory and research writing — they synthesise the whole module.

## Next Step
After passing this folder, use [[Progress Tracker]] to revisit weak links and read primary sources via [[10.12 Research Paper Maths Reading]].
"""


def gen_summary(topics):
    items = [f"- [ ] [[{t['id']} {t['title']}]] - {t['plain_short']}" for t in topics]
    return f"""# 11 Advanced & Masters-Level Topics - Printable Summary

Prepare for master's-level AI, algorithms, security, theory, and research-heavy CS.

## What You Must Be Able To Do
{chr(10).join(items)}

## Module 11 at a Glance

| Block | Topics | CS focus |
|-------|--------|----------|
| Algorithms | 11.1–11.4 | Complexity, randomisation, approximation, graphs |
| Learning | 11.5–11.10 | Theory, PGMs, optimisation, calculus, numerics |
| PLT & algebra | 11.11–11.13 | Categories, lambda, finite fields |
| Security | 11.14–11.16 | ECC, lattices, quantum intro |
| Synthesis | 11.17–11.18 | Information theory, research writing |

## Folder Pass Gate
Before leaving this folder, you must:

- Pass every topic mastery test (85% overall, 100% on definitions).
- Retake any failed topic after writing a correction note.
- Explain how each block connects to computer science.
- Complete [[11 Advanced & Masters-Level Topics - Cumulative Test]] at 85%.

## Key CS Unlocks
See [[11 Advanced & Masters-Level Topics - What This Unlocks in CS]].
"""


from module_11_topics import TOPICS  # noqa: E402


def main():
    files = []
    for t in TOPICS:
        name = t["id"] + " " + t["title"]
        paths = [
            (MOD / f"{name}.md", gen_topic_note(t)),
            (WE / f"{name} - Worked Examples.md", gen_worked(t)),
            (PQ / f"{name} - Practice Questions.md", gen_practice(t)),
            (MT / f"{name} - Mastery Test.md", gen_mastery(t)),
            (AN / f"{name} - Answers.md", gen_answers(t)),
        ]
        for p, content in paths:
            p.write_text(content, encoding="utf-8")
            files.append(str(p))
        for term, defn in t["terms"]:
            gp = GL / f"{term}.md"
            gp.write_text(
                gen_glossary(
                    term,
                    defn,
                    name,
                    t["glossary_builds"].get(term, t["breadcrumbs"][-1]),
                    t["glossary_cs"][term],
                ),
                encoding="utf-8",
            )
            files.append(str(gp))
    for p, content in [
        (MOD / "11 Advanced & Masters-Level Topics - Cumulative Test.md", gen_cumulative(TOPICS)),
        (MOD / "11 Advanced & Masters-Level Topics - What This Unlocks in CS.md", gen_unlock(TOPICS)),
        (MOD / "11 Advanced & Masters-Level Topics - Printable Summary.md", gen_summary(TOPICS)),
    ]:
        p.write_text(content, encoding="utf-8")
        files.append(str(p))
    print(f"Generated {len(files)} files")
    for f in sorted(files):
        print(f)
    # Verify line counts for topic notes
    short = []
    for t in TOPICS:
        name = t["id"] + " " + t["title"]
        path = MOD / f"{name}.md"
        n = len(path.read_text(encoding="utf-8").splitlines())
        if n < 350:
            short.append(f"{name}: {n} lines")
    if short:
        print("WARNING - topic notes under 350 lines:")
        for s in short:
            print(s)
    else:
        print("All topic notes >= 350 lines.")


if __name__ == "__main__":
    main()
