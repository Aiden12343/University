#!/usr/bin/env python3
"""Generate complete Module 10 CS Applications topic bundles."""
from pathlib import Path

BASE = Path("/home/Marau/Marau/University/Maths for CS")
MOD = BASE / "10 CS Applications"
WE = BASE / "90 Worked Examples"
PQ = BASE / "91 Practice Questions"
MT = BASE / "92 Mastery Tests"
AN = BASE / "93 Answers and Mark Schemes"
GL = BASE / "00 Glossary/Terms"
PASS_MARKS = 22


def gen_topic_note(t):
    name = f"{t['id']} {t['title']}"
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
        "> Read one concept, cover it, then explain it aloud in your own words. After each case study, trace the maths back to an earlier module note before moving on.",
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
            if s.startswith("```") or (j > 1 and c["steps"][j - 2].startswith("```") and not s.startswith("Step")):
                lines.append(s)
            else:
                lines.append(f"Step {j}: {s}")
        lines.append("")
        lines.append(f"Answer: {c['answer']}")
        lines.append("")
    lines += [
        "## Why This Works",
        t["why"],
        "",
        f"For fully worked solutions, use [[{name} - Worked Examples]].",
        "",
        "## Common Mistakes",
    ]
    for m in t["mistakes"]:
        lines.append(f"- {m}")
    lines += ["", "> [!failure] Mistake pattern", f"> {t['failure']}", "", "## Where This Shows Up in CS", t["cs_intro"], ""]
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
        f"Assessment links: [[{name} - Worked Examples]], [[{name} - Practice Questions]], [[{name} - Mastery Test]], [[{name} - Answers]]",
    ]
    return "\n".join(lines) + "\n"


def gen_worked(t):
    name = f"{t['id']} {t['title']}"
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
    lines += [
        "## Self-Check",
        "You understand these examples when you can explain:",
        "",
    ]
    for sc in t["self_check"]:
        lines.append(f"- {sc}")
    return "\n".join(lines) + "\n"


def gen_practice(t):
    name = f"{t['id']} {t['title']}"
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


def gen_mastery(t):
    name = f"{t['id']} {t['title']}"
    lines = [
        f"# {name} - Mastery Test",
        "",
        f"Theory note: [[{name}]]",
        "",
        f"Answers: [[{name} - Answers]]",
        "",
        "Pass mark: 85%. You must score full marks on Section A before moving on.",
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
        lines.append(f"{n}. What is [[{term}]]?")
        n += 1
    lines += ["", "## Section B - Core Skills"]
    for q in t["mastery_b"]:
        lines.append(f"{n}. {q}")
        n += 1
    lines += ["", "## Section C - Spot the Mistake"]
    for q in t["mastery_c"]:
        lines.append(f"{n}. {q}")
        n += 1
    lines += ["", "## Section D - Apply and Analyse"]
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


def gen_answers(t):
    name = f"{t['id']} {t['title']}"
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
        "- Section D (Apply and Analyse): 5 marks",
        "- Section E (CS Transfer): 5 marks",
        "",
        "Pass: Section A full marks required; overall 22/25 minimum (85%).",
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


def concept(title, body, callout, callout_title, callout_body, q, steps, answer):
    return {
        "title": title,
        "body": body if isinstance(body, list) else [body],
        "callout": callout,
        "callout_title": callout_title,
        "callout_body": callout_body if isinstance(callout_body, list) else [callout_body],
        "q": q,
        "steps": steps,
        "answer": answer,
    }


# ---------------------------------------------------------------------------
# TOPIC DATA — import from companion file
# ---------------------------------------------------------------------------
from module_10_topics import TOPICS  # noqa: E402


def gen_cumulative():
    sections = []
    marks_per = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    for t, m in zip(TOPICS, marks_per):
        name = f"{t['id']} {t['title']}"
        sections.append(f"### {t['id']} - {t['title']} ({m} marks)")
        for i, q in enumerate(t["cum_questions"], 1):
            sections.append(f"{i}. {q}")
        sections.append("")
    body = "\n".join(sections)
    return f"""# 10 CS Applications - Cumulative Test

Use this after completing every topic in [[10 MOC - CS Applications]].

> [!danger] Test conditions
> Closed book. Paper only. Allow 120 minutes. Pass target: 85% (21/25 marks on selected questions below; full paper 50 marks at 43/50).

## Instructions
Answer every section. Show working for calculations. Definitions must be in your own words.

## Mixed Application Questions (50 marks total)

{body}

## Reflection
- Which three topics felt strongest?
- Which three topics need review?
- Which topic connects most clearly to computer science?
- Which prerequisite from Modules 05–09 should you revisit?

## Marking
Total: 50 marks (approximately 4–5 marks per topic cluster). Pass: 43/50 (85%).

Decision:
- [ ] Pass - continue to [[11 MOC - Advanced CS Maths]].
- [ ] Review - retake weak topics and write correction notes.
- [ ] Restart - rebuild CS application foundations from [[10.1 Big O Theta and Omega]].
"""


def gen_unlock():
    items = []
    for t in TOPICS:
        name = f"{t['id']} {t['title']}"
        items.append(f"- [[{name}]] - {t['cs_one_liner']}")
    blocks = """
## Concrete Unlocks

### Algorithms and performance
[[10.1 Big O Theta and Omega]] and [[10.2 Algorithm Complexity Case Studies]] turn loop counts from [[5.11 Proof by Induction]] into predictions you can defend in code review. You compare sorting, searching, and graph methods before shipping.

### Representation and numerics
[[10.3 Binary Hexadecimal and Number Bases]] and [[10.4 Floating Point and Rounding Error]] explain why `0.1 + 0.2 != 0.3` in JavaScript and why memory dumps use hex. Links back to [[1.2 Place Value and Number Lines]] and [[2.9 Indices and Powers]].

### Security and integrity
[[10.5 Hashing and Checksums]], [[10.6 Cryptography RSA and Diffie Hellman]], and [[10.7 Error Correction QR and Reed Solomon]] connect [[5.10 Proof by Contradiction and Contrapositive]] hardness assumptions to HTTPS, git commit IDs, and QR codes that still scan when scratched.

### Machine learning
[[10.8 Machine Learning Vectors and Matrices]] and [[10.9 Neural Network Maths]] make PyTorch/TensorFlow operations readable: dot products from [[4.8 Vectors Basics]], matrix multiply from [[4.9 Matrices Basics]], gradients from [[9.9 Gradient Descent and Optimisation]].

### Systems and theory
[[10.10 Graphs in Networks and AI Search]] applies [[6.4 Graph Theory Basics]] to routing and A*. [[10.11 Type Theory and Program Logic Intro]] connects [[5.5 Propositional Logic]] to Rust, Haskell, and proof assistants. [[10.12 Research Paper Maths Reading]] prepares you for arXiv and conference papers.

## Study Path
1. Master Big-O before case studies — notation is the shared language.
2. Master bases before floating point — IEEE 754 is binary science.
3. Master hashing before RSA — modular arithmetic appears in both.
4. Master vectors before neural nets — every layer is matrix algebra.
5. Finish with paper reading — it integrates all prior modules.
"""
    return f"""# 10 CS Applications - What This Unlocks in CS

Tie mathematical tools directly to algorithms, systems, security, data, ML, and graphics.

This module is where theory from Modules 05–09 becomes inspectable in real systems. Every topic here should send you back to at least one earlier note when you get stuck.

## CS Connections
{chr(10).join(items)}
{blocks}

## Next Step
After passing this folder, continue to [[11 MOC - Advanced CS Maths]] and keep revisiting weak links through [[Progress Tracker]].
"""


def gen_summary():
    items = []
    for t in TOPICS:
        name = f"{t['id']} {t['title']}"
        items.append(f"- [ ] [[{name}]] - {t['plain_short']}")
    return f"""# 10 CS Applications - Printable Summary

Tie mathematical tools directly to algorithms, systems, security, data, ML, and graphics.

## What You Must Be Able To Do
{chr(10).join(items)}

## Module 10 Quick Reference

```text
Big-O       O(g) upper bound on growth
Binary      base-2, bit = 0 or 1, byte = 8 bits
Float       sign × mantissa × 2^exponent (IEEE 754)
Hash        data → fixed-size fingerprint (one-way)
RSA         encrypt with public e,n; decrypt with private d
ML vector   features · weights + bias → prediction
Neural net  layer: W·x + b, then activation σ
Graph       nodes + edges; BFS/DFS/Dijkstra/A*
Type        program expression ↔ mathematical object
Paper       definition → lemma → theorem → proof
```

## Prerequisite Map (Modules 05–09)
- Sets & logic: [[5.1 Set Theory Basics]], [[5.5 Propositional Logic]], [[5.11 Proof by Induction]]
- Discrete: [[6.4 Graph Theory Basics]], [[6.7 Modular Arithmetic]]
- Linear algebra: [[4.8 Vectors Basics]], [[4.9 Matrices Basics]]
- Probability: [[8.1 Probability Basics]]
- Calculus: [[9.1 Limits and Continuity]], [[9.9 Gradient Descent and Optimisation]]

## Folder Pass Gate
Before leaving this folder, you must:

- Pass every topic mastery test (85% overall, 100% on definitions).
- Retake any failed topic after writing a correction note.
- Explain how this folder connects to computer science.
- Complete [[10 CS Applications - Cumulative Test]] (43/50).

## Key CS Unlocks
See [[10 CS Applications - What This Unlocks in CS]].
"""


def main():
    files = []
    for t in TOPICS:
        name = f"{t['id']} {t['title']}"
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
        topic_name = name
        for term, defn in t["terms"]:
            gp = GL / f"{term}.md"
            builds = t["glossary_builds"].get(term, t["prereq"][0] if t["prereq"] else "9.10 Convex Optimisation Basics")
            gp.write_text(
                gen_glossary(term, defn, topic_name, builds, t["glossary_cs"][term]),
                encoding="utf-8",
            )
            files.append(str(gp))
    for p, content in [
        (MOD / "10 CS Applications - Cumulative Test.md", gen_cumulative()),
        (MOD / "10 CS Applications - What This Unlocks in CS.md", gen_unlock()),
        (MOD / "10 CS Applications - Printable Summary.md", gen_summary()),
    ]:
        p.write_text(content, encoding="utf-8")
        files.append(str(p))
    print(f"Generated {len(files)} files")
    for f in sorted(files):
        print(f)


if __name__ == "__main__":
    main()
