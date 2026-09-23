#!/usr/bin/env python3
"""Generate complete Module 08 Probability and Statistics topic bundles."""
from __future__ import annotations

from pathlib import Path

BASE = Path("/home/Marau/Marau/University/Maths for CS")
MOD = BASE / "08 Probability & Statistics"
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
Builds on: [[{builds_on}]]
Used in CS: {cs_use}

## Related Notes
Search backlinks in Obsidian to see every topic that uses [[{term}]].
"""


def gen_cumulative() -> str:
    blocks = []
    for t in TOPICS:
        name = t["id"] + " " + t["title"]
        blocks.append(f"### {t['id']} - {t['title']} ({t['cum_marks']} marks)")
        for i, q in enumerate(t["cum_questions"], 1):
            blocks.append(f"{i}. {q}")
        blocks.append("")
    body = "\n".join(blocks)
    return f"""# 08 Probability & Statistics - Cumulative Test

Use this after completing every topic in [[08 MOC - Probability and Statistics]].

> [!danger] Test conditions
> Closed book. Paper only. Allow 120 minutes. Pass target: 85% (43/50 marks).

## Instructions
Answer every question on paper first. Show fractions before decimals where exact values matter. For Bayes and conditional probability questions, label prior, likelihood, and posterior.

## Section A - Probability Foundations (15 marks)

{chr(10).join(blocks[:15])}

## Section B - Random Variables and Distributions (15 marks)

{chr(10).join(blocks[15:30]) if len(blocks) > 15 else ''}

## Section C - Data, Inference, and Information (20 marks)

{chr(10).join(blocks[30:]) if len(blocks) > 30 else ''}

## Reflection
- Which three topics felt strongest?
- Which three topics need review?
- Which topic connects most clearly to computer science?
- Which prerequisite from [[1.6 Fractions]] or [[1.7 Decimals and Percentages]] did you use most?

## Marking
Total: 50 marks. Pass: 43/50 (85%).

Decision:
- [ ] Pass - continue to [[09 MOC - Calculus]].
- [ ] Review - retake weak topics and write correction notes.
- [ ] Restart - rebuild probability foundations from [[8.1 Probability Basics]].
"""


def gen_unlock() -> str:
    items = [f"- [[{t['id']} {t['title']}]] - {t['cs_one_liner']}" for t in TOPICS]
    return f"""# 08 Probability & Statistics - What This Unlocks in CS

Reason under uncertainty, summarise data, test claims, and prepare for machine learning.

This module turns counting and fractions into tools for prediction, measurement, and decision-making under uncertainty. Every later topic in ML, security, networking, and systems monitoring assumes you can read probabilities, update beliefs, and summarise data honestly.

## CS Connections
{chr(10).join(items)}

## Concrete Unlocks

### Reliability and risk
Probability and conditional probability underpin fault tolerance, spam filtering, fraud detection, and diagnostic systems. You cannot write a meaningful risk score without a sample space and an event.

### Performance and cost
Expected value and discrete distributions model average runtime, queue lengths, retry counts, and packet arrivals. These are the maths behind capacity planning.

### Data science pipeline
Descriptive statistics, correlation, regression, and hypothesis testing are the first tools in experiment analysis, A/B testing, and dashboard design.

### Probabilistic AI
Bayes theorem, Bayesian inference, and information theory connect directly to Naive Bayes classifiers, posterior sampling, cross-entropy loss, and compression codecs.

## Study Path
1. Master fractions-as-probability in [[8.1 Probability Basics]] before touching Bayes.
2. Master conditional probability in [[8.2 Conditional Probability]] before [[8.3 Bayes Theorem]] — Bayes is conditional probability written backwards.
3. Master expected value before distributions — distributions are shorthand for weighted averages.
4. Do not skip hypothesis testing — it is how engineers decide whether a benchmark improvement is real.

## Prerequisites Worth Revisiting
- [[1.6 Fractions]] — probability is a fraction of equally likely outcomes.
- [[1.7 Decimals and Percentages]] — probabilities convert cleanly to percentages for communication.
- [[7.12 Numerical Stability in Linear Algebra]] — regression and covariance rely on stable numeric computation.

## Next Step
After passing this folder, continue to [[09 MOC - Calculus]] and keep revisiting weak links through [[Progress Tracker]].
"""


def gen_summary() -> str:
    items = [f"- [ ] [[{t['id']} {t['title']}]] - {t['plain_short']}" for t in TOPICS]
    return f"""# 08 Probability & Statistics - Printable Summary

Reason under uncertainty, summarise data, test claims, and prepare for ML.

## What You Must Be Able To Do
{chr(10).join(items)}

## Key Symbols Quick Reference

```text
P(A)           probability of event A
P(A|B)         probability of A given B
P(A ∩ B)       A and B both happen
P(A ∪ B)       A or B (or both) happen
P(A')          complement of A
E(X)           expected value of random variable X
Var(X)         variance of X
σ              standard deviation
H(X)           entropy
I(X;Y)         mutual information
```

## Probability as Fraction (from [[1.6 Fractions]])

```text
P(event) = favourable outcomes / total equally likely outcomes
3/4 = 0.75 = 75%
```

## Bayes at a Glance

```text
P(H|E) = P(E|H) × P(H) / P(E)

prior     = P(H)        belief before evidence
likelihood = P(E|H)     how likely evidence is if H true
evidence  = P(E)        normalising total
posterior = P(H|E)      updated belief after evidence
```

## Folder Pass Gate
Before leaving this folder, you must:

- Pass every topic mastery test (85% overall, 100% on definitions).
- Retake any failed topic after writing a correction note.
- Explain how this folder connects to computer science.
- Complete the cumulative test for this folder (43/50).

## Key CS Unlocks
See [[08 Probability & Statistics - What This Unlocks in CS]].
"""


# ---------------------------------------------------------------------------
# Topic data — imported from companion module
# ---------------------------------------------------------------------------
from module_08_topics import TOPICS  # noqa: E402


def main() -> None:
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
            p.write_text(content, encoding="utf-8")
            files.append(str(p))
        for term, defn in t["terms"]:
            gp = GL / f"{term}.md"
            gp.write_text(
                gen_glossary(
                    term,
                    defn,
                    name,
                    t["glossary_builds"].get(term, t["prereq"][0] if t["prereq"] else "1.1 Counting and Number Sense"),
                    t["glossary_cs"][term],
                ),
                encoding="utf-8",
            )
            files.append(str(gp))
    for p, content in [
        (MOD / "08 Probability & Statistics - Cumulative Test.md", gen_cumulative()),
        (MOD / "08 Probability & Statistics - What This Unlocks in CS.md", gen_unlock()),
        (MOD / "08 Probability & Statistics - Printable Summary.md", gen_summary()),
    ]:
        p.write_text(content, encoding="utf-8")
        files.append(str(p))
    print(f"Generated {len(files)} files")
    for f in sorted(files):
        print(f)


if __name__ == "__main__":
    main()
