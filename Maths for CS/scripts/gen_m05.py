#!/usr/bin/env python3
"""Generate complete Module 05 Sets, Logic & Proof topic bundles."""
from __future__ import annotations

from pathlib import Path

BASE = Path("/home/Marau/Marau/University/Maths for CS")
MOD = BASE / "05 Sets, Logic & Proof"
WE = BASE / "90 Worked Examples"
PQ = BASE / "91 Practice Questions"
MT = BASE / "92 Mastery Tests"
AN = BASE / "93 Answers and Mark Schemes"
GL = BASE / "00 Glossary/Terms"

PASS_MARKS = 22  # 22/25 = 88%, meets 85% threshold


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def glossary(term: str, definition: str, topic: str, builds_on: str, cs_use: str) -> str:
    return f"""# {term}

{definition}

First introduced in: [[{topic}]]
Builds on: [[{builds_on}]]
Used in CS: {cs_use}

## Related Notes
Search backlinks in Obsidian to see every topic that uses [[{term}]].
"""


def gen_topic_note(t: dict) -> str:
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
        f"For fully worked solutions, use [[{name} - Worked Examples]].",
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
        f"Assessment links: [[{name} - Worked Examples]], [[{name} - Practice Questions]], [[{name} - Mastery Test]], [[{name} - Answers]]",
    ]
    return "\n".join(lines) + "\n"


def gen_worked(t: dict) -> str:
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
        lines += [f"## Example {i} - {ex['title']}", "", f"Question: {ex['q']}", ""]
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


def gen_practice(t: dict) -> str:
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
    lines.append(
        f"Pass target: 85%. You should get at least {target} out of {total} correct before taking [[{name} - Mastery Test]]."
    )
    return "\n".join(lines) + "\n"


def gen_mastery(t: dict) -> str:
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
        "- Section D (Apply and Prove): 5 marks",
        "- Section E (CS Transfer): 5 marks",
        "",
        f"Pass: Section A full marks required; overall {PASS_MARKS}/25 minimum (85%).",
    ]
    return "\n".join(lines) + "\n"


# Import topic definitions
from m05_data import TOPICS  # noqa: E402


def gen_cumulative() -> str:
    return """# 05 Sets, Logic & Proof - Cumulative Test

Use this after completing every topic in [[05 MOC - Sets Logic and Proof]].

> [!danger] Test conditions
> Closed book. Paper only. Allow 90 minutes. Pass target: 85% (43/50 marks).

---

## Section A - Set Theory (15 marks)

### 5.1 Set Theory Basics (5 marks)
1. **(1 mark)** Define [[set]] and [[element]] in your own words.
2. **(1 mark)** Write the set of vowels in `{a, e, i, o, u, x}` using roster notation.
3. **(1 mark)** Is `3 ∈ {1, 2, 4}`? Explain.
4. **(2 marks)** Explain the difference between `∅` and `{∅}`.

### 5.2 Subsets, Unions and Intersections (5 marks)
1. **(1 mark)** Is `{2, 4} ⊆ {1, 2, 3, 4}`? Justify.
2. **(2 marks)** Compute `{1, 2, 3} ∪ {3, 4, 5}` and `{1, 2, 3} ∩ {3, 4, 5}`.
3. **(2 marks)** Find `{a, b, c, d} \\ {b, d}`.

### 5.3 Venn Diagrams and Cardinality (5 marks)
1. **(2 marks)** Draw a Venn diagram for sets A and B where |A| = 5, |B| = 4, and |A ∩ B| = 2. Find |A ∪ B|.
2. **(2 marks)** State the inclusion-exclusion formula for two sets.
3. **(1 mark)** What does it mean for two sets to be disjoint?

---

## Section B - Logic and Boolean Algebra (15 marks)

### 5.4 Infinity and Countability (5 marks)
1. **(2 marks)** Explain why the integers are countable even though they are infinite.
2. **(1 mark)** Give one reason countability matters in computer science.
3. **(2 marks)** Is the set of all finite binary strings countable? Explain briefly.

### 5.5 Propositional Logic (5 marks)
1. **(2 marks)** Translate `logged_in AND (admin OR moderator)` into symbols.
2. **(1 mark)** When is `p ∨ q` false?
3. **(2 marks)** Give one example of a proposition and one sentence that is not a proposition.

### 5.6 Truth Tables (5 marks)
1. **(2 marks)** Build a truth table for `p → q`.
2. **(2 marks)** What is a tautology? Give an example.
3. **(1 mark)** How many rows does a truth table with 3 variables need?

---

## Section C - Proof Methods (20 marks)

### 5.7 Implication and Equivalence (5 marks)
1. **(2 marks)** Write the contrapositive of "If n is even, then n² is even."
2. **(2 marks)** Explain why the converse can be false when the original implication is true.
3. **(1 mark)** When are two statements logically equivalent?

### 5.8 Boolean Algebra and De Morgan Laws (5 marks)
1. **(2 marks)** Simplify `¬(A ∧ B)` using De Morgan.
2. **(2 marks)** Simplify `(A ∨ B) ∧ (A ∨ ¬B)`.
3. **(1 mark)** Name one identity law for AND.

### 5.9 Direct Proof and Counterexample (4 marks)
1. **(2 marks)** Prove: the sum of two even integers is even.
2. **(2 marks)** Disprove "every prime is odd" with a counterexample.

### 5.10 Proof by Contradiction and Contrapositive (3 marks)
1. **(2 marks)** Outline a proof by contradiction that √2 is irrational.
2. **(1 mark)** State when contrapositive proof is preferred over direct proof.

### 5.11 Proof by Induction (3 marks)
1. **(2 marks)** State the two steps of mathematical induction.
2. **(1 mark)** Verify the base case for 1 + 2 + ... + n = n(n+1)/2 when n = 1.

---

## Section D - Reflection (not marked; required)

- Which three topics felt strongest?
- Which three topics need review?
- Which topic connects most clearly to computer science?
- Which prerequisite from earlier modules should you revisit?

---

## Marking checklist

| Section | Marks available | Your score |
|---------|-----------------|------------|
| A | 15 | |
| B | 15 | |
| C | 20 | |
| **Total** | **50** | |

**Pass:** 43/50 or higher (85%).

**Decision:**
- [ ] Pass - continue to [[06 MOC - Discrete Mathematics]].
- [ ] Review - retake weak topics and write correction notes.
- [ ] Restart - rebuild set and logic foundations from [[5.1 Set Theory Basics]].
"""


def gen_unlock() -> str:
    items = []
    for t in TOPICS:
        name = f"{t['id']} {t['title']}"
        items.append(f"- [[{name}]] - {t['cs_one_liner']}")
    return f"""# 05 Sets, Logic & Proof - What This Unlocks in CS

Build the language of rigorous CS reasoning: sets, logic, Boolean rules, and proof.

This module is the first where maths directly models how programs think. Every later topic in algorithms, security, databases, and type systems assumes you can reason with sets, evaluate Boolean conditions, and follow a proof.

## CS Connections
{chr(10).join(items)}

## Concrete Unlocks

### Data and queries
Set operations underpin SQL `UNION`, `INTERSECT`, and filter composition. Cardinality and inclusion-exclusion prevent double-counting in analytics pipelines.

### Control flow
Every `if`, `while`, and permission check is propositional logic. Truth tables and De Morgan laws explain why refactoring conditions preserves behaviour.

### Specifications
Implication (`requires`, `ensures`, preconditions) is the language of contracts, API docs, and formal verification tools.

### Correctness
Direct proof, counterexample, contradiction, contrapositive, and induction are the proof tools used in algorithm analysis, compiler correctness, and security impossibility results.

## Study Path
1. Master sets before logic — collections appear everywhere in CS data models.
2. Master truth tables before Boolean algebra — tables justify every simplification rule.
3. Master implication before proof — proofs are chains of justified implications.
4. Do not skip induction — it is the standard tool for loops and recursion.

## Next Step
After passing this folder, continue to [[06 MOC - Discrete Mathematics]] and keep revisiting weak links through [[Progress Tracker]].
"""


def gen_summary() -> str:
    items = []
    for t in TOPICS:
        name = f"{t['id']} {t['title']}"
        items.append(f"- [ ] [[{name}]] - {t['plain_short']}")
    return f"""# 05 Sets, Logic & Proof - Printable Summary

Build the language of rigorous CS reasoning: sets, logic, Boolean rules, and proof.

## What You Must Be Able To Do
{chr(10).join(items)}

## Key Symbols Quick Reference

```text
∈  element of          ⊆  subset           ∪  union
∉  not element of      ⊂  proper subset    ∩  intersection
∅  empty set           A\\B  difference     |A|  cardinality
∧  AND                 ∨  OR               ¬  NOT
→  implies             ↔  iff              ≡  equivalent
∀  for all             ∃  there exists     ∄  there does not exist
```

## Proof Methods at a Glance

| Method | When to use | CS example |
|--------|-------------|------------|
| Direct | Show P → Q by assuming P | Prove loop invariant from init |
| Counterexample | Disprove ∀x P(x) | Find input that breaks claim |
| Contrapositive | Prove ¬Q → ¬P instead of P → Q | Security: no log ⇒ no breach |
| Contradiction | Assume opposite, derive ⊥ | √2 irrational, halting impossibility |
| Induction | Claims over n ∈ ℕ | List length, recursive function |

## Folder Pass Gate
Before leaving this folder, you must:

- Pass every topic mastery test (85% overall, 100% on definitions).
- Retake any failed topic after writing a correction note.
- Explain how this folder connects to computer science.
- Complete the cumulative test for this folder (43/50).

## Key CS Unlocks
See [[05 Sets, Logic & Proof - What This Unlocks in CS]].
"""


def main() -> None:
    files: list[str] = []
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
            write(p, content)
            files.append(str(p))
        for term, defn in t["terms"]:
            gp = GL / f"{term}.md"
            builds = t["glossary_builds"].get(term, t["prereq"][0] if t["prereq"] else "1.1 Counting and Number Sense")
            write(gp, glossary(term, defn, name, builds, t["glossary_cs"][term]))
            files.append(str(gp))

    for p, content in [
        (MOD / "05 Sets, Logic & Proof - Cumulative Test.md", gen_cumulative()),
        (MOD / "05 Sets, Logic & Proof - What This Unlocks in CS.md", gen_unlock()),
        (MOD / "05 Sets, Logic & Proof - Printable Summary.md", gen_summary()),
    ]:
        write(p, content)
        files.append(str(p))

    print(f"Generated {len(files)} files")
    for f in sorted(files):
        print(f)


if __name__ == "__main__":
    main()
