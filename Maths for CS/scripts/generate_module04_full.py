#!/usr/bin/env python3
"""Generate ALL Module 04 Geometry & Trigonometry content files."""

from __future__ import annotations

from pathlib import Path

BASE = Path("/home/Marau/Marau/University/Maths for CS")
MOD = BASE / "04 Geometry & Trigonometry"
WE = BASE / "90 Worked Examples"
PQ = BASE / "91 Practice Questions"
MT = BASE / "92 Mastery Tests"
AN = BASE / "93 Answers and Mark Schemes"
GL = BASE / "00 Glossary/Terms"

PASS = "85%"
PASS_MARKS = 22
THRESHOLD = "85%"


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
        f"Mastery threshold: {THRESHOLD} overall, and 100% on the New Words section.",
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
        body = c["body"]
        if isinstance(body, str):
            lines.append(body)
        else:
            lines.extend(body)
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
    if t.get("formulas"):
        lines += ["## Formula Reference", ""]
        lines.extend(t["formulas"])
        lines.append("")
    if t.get("prereq_bridge"):
        lines += ["## Prerequisites in Practice", ""]
        lines.extend(t["prereq_bridge"])
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
    if t.get("cs_extended"):
        lines += ["", "### Extended CS Applications", ""]
        lines.extend(t["cs_extended"])
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
        "## Study Sequence",
        "1. Read New Words aloud and write each definition from memory.",
        "2. Work through every Chunked Example on paper without skipping steps.",
        "3. Complete Section A of the practice sheet (vocabulary only).",
        "4. Attempt the mini-quiz closed-book.",
        "5. Take the mastery test; score Section A at 100% before moving on.",
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
        for s in ex["steps"]:
            lines.append(f"### Step")
            lines.append(s)
            lines.append("")
        lines.append(f"Answer: **{ex['answer']}**")
        lines.append("")
        if ex.get("note"):
            lines += [f"> [!important] {ex['note']}", ""]
    lines += [
        "## Self-Check",
        "You understand these examples when you can explain each solution without notes and connect at least one example to a computer science use case.",
    ]
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
    lines.append(
        f"Pass target: {THRESHOLD}. You should get at least {target} out of {total} correct before taking [[{name} - Mastery Test]]."
    )
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
        f"Pass mark: {THRESHOLD}. You must score full marks on Section A before moving on.",
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

## First introduced in
[[{topic}]]

## Builds on
{builds_on}

## Used in CS
{cs_use}
"""


def gen_cumulative(topics: list[dict]) -> str:
    blocks = []
    for t in topics:
        blocks.append(f"### {t['id']} - {t['title']} ({t['cum_marks']} marks)")
        for i, q in enumerate(t["cum_questions"], 1):
            blocks.append(f"{i}. {q}")
        blocks.append("")
    body = "\n".join(blocks)
    return f"""# 04 Geometry & Trigonometry - Cumulative Test

Use this after completing every topic in [[04 MOC - Geometry and Trigonometry]].

> [!danger] Test conditions
> Closed book. Paper only. Allow 90 minutes. Pass target: 85% (43/50 marks).

## Instructions
Show all working. Include units where measurements appear. For CS transfer questions, name the geometry idea and the programming context.

## Section A - Foundations (10 marks)

{chr(10).join(blocks[:20])}

## Section B - Trigonometry and Circles (15 marks)

{chr(10).join(blocks[20:50]) if len(blocks) > 20 else body}

## Section C - Vectors and Graphics (15 marks)

{chr(10).join(blocks[50:]) if len(blocks) > 50 else ''}

## Mixed Challenge (10 marks)

26. A right triangle has legs 5 cm and 12 cm. Find the hypotenuse and explain how this becomes a distance check in collision code. (2 marks)
27. Convert 135° to radians. (1 mark)
28. Vector **a** = (3, 4). Find |**a**|. (2 marks)
29. **u** · **v** = 0. What does this tell you about the angle between them? (1 mark)
30. Name model space and screen space in one sentence each. (2 marks)
31. A unit circle point has x-coordinate 0.6. Without a calculator, is the y-coordinate positive or negative in Quadrant I? (1 mark)
32. Arc length on a circle of radius 8 cm with central angle π/4 radians. (1 mark)

## Reflection
- Which three topics felt strongest?
- Which three topics need review?
- Which topic connects most clearly to computer science?
- Which prerequisite from [[3.1 Coordinates and Axes]] or [[3.10 Piecewise and Step Functions]] did you use most?

## Marking
Total: 50 marks. Pass: 43/50 (85%).

Decision:
- [ ] Pass - continue to [[5.1 Set Theory Basics]].
- [ ] Review - retake weak topics and write correction notes.
- [ ] Restart - rebuild geometry foundations from [[4.1 Lines Angles and Triangles]].
"""


def gen_unlock(topics: list[dict]) -> str:
    items = [f"- [[{t['id']} {t['title']}]] - {t['cs_one_liner']}" for t in topics]
    return f"""# 04 Geometry & Trigonometry - What This Unlocks in CS

Measure shape, angle, distance, and motion — the maths behind graphics, robotics, physics engines, and spatial algorithms.

This module turns coordinate arithmetic from [[3.1 Coordinates and Axes]] into the geometry language programs use to place objects, rotate cameras, detect collisions, and project 3D scenes onto screens. Every later topic in linear algebra, graphics pipelines, and game physics assumes you can reason with triangles, trig ratios, vectors, and transforms.

## CS Connections
{chr(10).join(items)}

## Concrete Unlocks

### Rendering and layout
Triangle meshes, circle arcs for UI rounded corners, and axis-aligned bounding boxes all depend on perimeter, area, and angle facts from the first half of this module.

### Distance and collision
Pythagoras and the distance formula underpin circle–circle tests, nearest-neighbour queries, and pathfinding heuristics. Vectors extend this to 3D ray casting and surface normals.

### Rotation and animation
SOHCAHTOA, the unit circle, and radians feed directly into rotation matrices and quaternion interpolation in [[4.10 Geometry for Computer Graphics]].

### Similarity and ML features
The dot product measures alignment between feature vectors, cosine similarity ranks documents, and orthogonal vectors define independent signal components in PCA-style pipelines.

## Study Path
1. Master lines and triangles before area — you need angle facts to justify shape formulas.
2. Master Pythagoras before trig ratios — right triangles define sine, cosine, and tangent.
3. Master the unit circle before radians — radian measure is arc length on the unit circle.
4. Master vectors before dot product — projection is built from components and magnitude.
5. Finish with graphics transforms — they combine everything in one matrix pipeline.

## Prerequisites Worth Revisiting
- [[3.1 Coordinates and Axes]] — every distance and vector starts with ordered pairs.
- [[3.10 Piecewise and Step Functions]] — piecewise domains appear in angle rules and quadrant signs.
- [[2.5 Solving Linear Equations]] — solving for unknown angles uses the same algebra.

## Next Step
After passing this folder, continue to [[5.1 Set Theory Basics]] and keep revisiting weak links through [[Progress Tracker]].
"""


def gen_summary(topics: list[dict]) -> str:
    items = [f"- [ ] [[{t['id']} {t['title']}]] - {t['plain_short']}" for t in topics]
    return f"""# 04 Geometry & Trigonometry - Printable Summary

Measure shape, angle, distance, and motion for graphics, robotics, and spatial algorithms.

## What You Must Be Able To Do
{chr(10).join(items)}

## Key Formulas Quick Reference

```text
Triangle angle sum:     A + B + C = 180°
Rectangle area:         A = l × w
Circle circumference:   C = 2πr = πd
Circle area:            A = πr²
Pythagoras:             a² + b² = c²   (c = hypotenuse)
Distance formula:       d = √((x₂−x₁)² + (y₂−y₁)²)
SOHCAHTOA:              sin = O/H,  cos = A/H,  tan = O/A
Unit circle:            (cos θ, sin θ) on x² + y² = 1
Degree ↔ radian:        radians = degrees × π/180
Arc length:             s = rθ   (θ in radians)
Vector magnitude:       |v| = √(x² + y²)
Dot product:            u·v = u₁v₁ + u₂v₂ = |u||v|cos θ
```

## Quadrant Signs (Unit Circle)

```text
Quadrant I:   cos +,  sin +
Quadrant II:  cos −,  sin +
Quadrant III: cos −,  sin −
Quadrant IV:  cos +,  sin −
```

## Graphics Transform Pipeline

```text
model space → world space → view space → clip space → screen space
Typical 2D/3D ops: translation (shift), rotation (turn), scaling (stretch)
```

## Folder Pass Gate
Before leaving this folder, you must:

- Pass every topic mastery test ({THRESHOLD} overall, 100% on definitions).
- Retake any failed topic after writing a correction note.
- Explain how this folder connects to computer science.
- Complete the cumulative test for this folder (43/50).

## Key CS Unlocks
See [[04 Geometry & Trigonometry - What This Unlocks in CS]].
"""


def main() -> None:
    from module_04_topics import TOPICS  # noqa: WPS433

    files: list[str] = []
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
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
            files.append(str(p))
        for term, defn in t["terms"]:
            gp = GL / f"{term}.md"
            gp.write_text(
                gen_glossary(
                    term,
                    defn,
                    name,
                    t["glossary_builds"].get(term, t["prereq"][0] if t["prereq"] else "3.1 Coordinates and Axes"),
                    t["glossary_cs"][term],
                ),
                encoding="utf-8",
            )
            files.append(str(gp))
    for p, content in [
        (MOD / "04 Geometry & Trigonometry - Cumulative Test.md", gen_cumulative(TOPICS)),
        (MOD / "04 Geometry & Trigonometry - What This Unlocks in CS.md", gen_unlock(TOPICS)),
        (MOD / "04 Geometry & Trigonometry - Printable Summary.md", gen_summary(TOPICS)),
    ]:
        p.write_text(content, encoding="utf-8")
        files.append(str(p))
    print(f"Generated {len(files)} files")
    for f in sorted(files):
        print(f)


if __name__ == "__main__":
    main()
