#!/usr/bin/env python3
"""Generate Module 04 topics 4.3-4.10, glossary, and module files."""
from pathlib import Path

BASE = Path("/home/Marau/Marau/University/Maths for CS")
GEO, WE, PQ, MT, ANS, GLOSS = (
    BASE / "04 Geometry & Trigonometry",
    BASE / "90 Worked Examples",
    BASE / "91 Practice Questions",
    BASE / "92 Mastery Tests",
    BASE / "93 Answers and Mark Schemes",
    BASE / "00 Glossary/Terms",
)
BC = "[[1.3 Addition and Subtraction]], [[1.4 Multiplication and Division]], [[2.2 Simplifying Expressions]], [[2.5 Solving Linear Equations]], [[3.1 Coordinates and Axes]], [[3.2 Function Notation and Mapping]]"
written, failures = [], []

def w(p, c):
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(c, encoding="utf-8")
        written.append(str(p))
    except Exception as e:
        failures.append(f"{p}: {e}")

def g(term, defn, topic, prior, cs):
    w(GLOSS / f"{term}.md", f"# {term}\n{defn}\nFirst introduced in: [[{topic}]]\nBuilds on: [[{prior}]]\nUsed in CS: {cs}\n## Related Notes\nSearch backlinks in Obsidian to see every topic that uses [[{term}]].\n")

def steps_block(steps):
    out = []
    for i, (label, code) in enumerate(steps, 1):
        out.append(f"Step {i}: {label}.\n\n```text\n{code}\n```")
    return "\n\n".join(out)

def concept(n, title, body, ct, callout, q, steps, ans):
    return f"""## Concept {n} - {title}
{body}

> [!{ct}] {ct.capitalize()}
> {callout}

### Chunked Example
Question: {q}

{steps_block(steps)}

Answer: **{ans}**.
"""

def topic_note(t):
    cs = "\n".join(f"- {m}" for m in t["mistakes"])
    ck = "\n".join(f"{i}. {q}" for i, q in enumerate(t["ck"], 1))
    mq = "\n".join(f"{i}. {q}" for i, q in enumerate(t["mq"], 1))
    nw = "\n".join(f"- [[{a}]] - {b}" for a, b in t["nw"])
    conc = "\n".join(concept(i+1, *c) for i, c in enumerate(t["conc"]))
    pg = "\n".join(f"- {x}" for x in t["pg"])
    return f"""# {t['id']}

Tags: {t['tags']}

## Position in the Course
Prerequisites: {t['pre']}

Used later in: {t['fwd']}

Earlier modules: {BC}

Mastery threshold: 85% overall, and 100% on the New Words section.

> [!tip] How to study this note
> {t['tip']}

## Plain-English Idea
{t['plain']}

> [!example] Everyday idea
> {t['everyday']}

## New Words
{nw}

You pass this topic only when you can define all five terms without looking.

{conc}
## Why This Works
{t['why']}

## Worked Examples
For fully worked solutions, use [[{t['id']} - Worked Examples]].

### Example 1 - Quick Check
Question: {t['qq']}

Solution:

```text
{t['qa']}
```

Answer: **{t['qans']}**.

## Common Mistakes
{cs}

> [!failure] Mistake pattern
> {t['fail']}

## Where This Shows Up in CS
{t['cs']}

## Checkpoint Questions
{ck}

## Mini-Quiz
{mq}

## Pass Gate
You may move to {t['next']} only when you can:

{pg}

- answer at least 9 out of 10 mini-quiz questions correctly
- complete [[{t['id']} - Mastery Test]] with at least 22/25 and full marks on definitions

## Related Notes
Backward links: {t['pre']}, {BC}

Forward links: {t['fwd']}

Assessment links: [[{t['id']} - Worked Examples]], [[{t['id']} - Practice Questions]], [[{t['id']} - Mastery Test]], [[{t['id']} - Answers]]
"""

def worked(t):
    ex = ""
    for i, e in enumerate(t["we"], 1):
        st = "\n\n".join(f"### Step {j+1} - {s[0]}\n```text\n{s[1]}\n```" for j, s in enumerate(e[2]))
        ex += f"## Example {i} - {e[0]}\nQuestion: {e[1]}\n\n{st}\n\nAnswer: **{e[3]}**.\n\n"
    return f"# {t['id']} - Worked Examples\n\nTheory note: [[{t['id']}]]\n\nUse these examples before attempting [[{t['id']} - Practice Questions]].\n\n> [!tip] Worked example routine\n> {t['wetip']}\n\n{ex}"

def practice(t):
    n, out = 1, f"# {t['id']} - Practice Questions\n\nTheory note: [[{t['id']}]]\n\nAnswers: [[{t['id']} - Answers]]\n\n> [!tip] Paper-first rule\n> {t['pqtip']}\n\n"
    for sec, qs in t["pq"]:
        out += f"## {sec}\n"
        for q in qs:
            out += f"{n}. {q}\n"; n += 1
        out += "\n"
    return out + f"## Next Step\nMark using [[{t['id']} - Answers]], then attempt [[{t['id']} - Mastery Test]].\n"

def mastery(t):
    return f"# {t['id']} - Mastery Test\n\nTheory note: [[{t['id']}]]\n\nAnswers: [[{t['id']} - Answers]]\n\nPass mark: 85% (22/25). You must score full marks on Section A before moving on.\n\n> [!danger] Test condition\n> Do this without notes. Use paper.\n\n{t['mt']}\n\n## Marking\nTotal: 25 marks. Pass: Section A 5/5 required; overall 22/25.\n\nDecision:\n- [ ] Pass - move to {t['next']}.\n- [ ] Review - [[94 Review Sheets]].\n- [ ] Restart - reread [[{t['id']}]] and redo worked examples.\n"

def answers(t):
    return f"# {t['id']} - Answers\n\nTheory note: [[{t['id']}]]\n\nMastery test: [[{t['id']} - Mastery Test]]\n\nPractice set: [[{t['id']} - Practice Questions]]\n\n{t['ans']}\n"

# ── TOPIC DEFINITIONS ───────────────────────────────────────────────────────

TOPICS = [
# 4.3 Circle Geometry
{
"id": "4.3 Circle Geometry", "tags": "#maths/geometry #maths/circles #cs/graphics #cs/algorithms",
"pre": "[[4.2 Perimeter Area and Volume]]", "fwd": "[[4.4 Pythagoras Theorem]]", "next": "[[4.4 Pythagoras Theorem]]",
"tip": "Mark the centre, draw a radius, then decide whether the question needs distance around (circumference), distance across (diameter), or part of the edge (arc).",
"plain": "A **circle** is the set of points the same distance from a centre. The **radius** is that fixed distance; the **diameter** is twice the radius across the centre. **Circumference** is the perimeter of a circle. **Pi (π)** is the special ratio circumference ÷ diameter ≈ 3.14159. An **arc** is a curved part of the circumference.",
"everyday": "A bicycle wheel's rim length is circumference. A pizza's width is diameter. A slice's crust edge is an arc.",
"nw": [("radius","the distance from the centre of a circle to any point on the circle."),
       ("diameter","the distance across a circle through its centre; twice the radius."),
       ("circumference","the distance around the outside edge of a circle."),
       ("pi","the constant ratio of a circle's circumference to its diameter, approximately 3.14159."),
       ("arc","a portion of the circumference of a circle between two points.")],
"conc": [
("Radius and Diameter", "The [[radius]] `r` reaches from centre to edge. The [[diameter]] `d` passes through the centre:\n\n```text\nd = 2r\nr = d/2\n```\n\nDoubling from [[1.4 Multiplication and Division]] links radius and diameter.", "important", "Every diameter is made of two radii in a straight line.", "A circle has radius 7 cm. Find the diameter.", [("Double the radius","d = 2 × 7 = 14")], "14 cm"),
("Circumference Formula", "The [[circumference]] `C` is perimeter of a circle:\n\n```text\nC = 2πr = πd\n```\n\n[[pi]] is the same for every circle — circumference divided by diameter always gives π.", "example", "For r = 5: C = 2π(5) ≈ 31.4 (using π ≈ 3.14).", "Find the circumference of a circle with radius 10 cm. Use π ≈ 3.14.", [("Use C = 2πr","C = 2 × 3.14 × 10 = 62.8")], "62.8 cm"),
("Pi as a Ratio", "[[pi]] ≈ 3.14159 is irrational — it never terminates or repeats. It connects [[circumference]] and [[diameter]]:\n\n```text\nπ = C/d\n```\n\nArea of a circle (preview): `A = πr²`.", "tip", "Memorise π ≈ 3.14 for estimates; use calculator π for accuracy.", "A circle has diameter 20 cm. Find circumference (π ≈ 3.14).", [("C = πd","C = 3.14 × 20 = 62.8")], "62.8 cm"),
("Area of a Circle", "Area uses [[unit squared]] from [[4.2 Perimeter Area and Volume]]:\n\n```text\nA = πr²\n```\n\nSquare the radius first, then multiply by π.", "warning", "A = πr² is not 2πr — do not confuse area with circumference.", "Find the area of a circle with radius 6 cm (π ≈ 3.14).", [("Square radius","r² = 36"),("Multiply by π","A = 3.14 × 36 = 113.04")], "113.04 cm²"),
("Arc Length", "An [[arc]] is a fraction of the full [[circumference]]. If the arc is `f` of a full turn:\n\n```text\narc length = f × 2πr\n```\n\nHalf a circle: f = ½, arc = πr.", "example", "A semicircle arc is half the full circumference.", "Find the arc length for a quarter circle of radius 8 cm (π ≈ 3.14).", [("Full circumference","C = 2 × 3.14 × 8 = 50.24"),("Quarter arc","50.24 / 4 = 12.56")], "12.56 cm"),
("Circles in Coordinates", "A circle centred at origin with [[radius]] r has equation (from [[3.1 Coordinates and Axes]]):\n\n```text\nx² + y² = r²\n```\n\nPoints on the circle satisfy this — foundation for [[4.6 Unit Circle]].", "important", "The unit circle is r = 1: x² + y² = 1.", "Does (3, 4) lie on a circle centred at origin with r = 5?", [("Check x²+y²","3² + 4² = 9 + 16 = 25"),("Compare r²","r² = 25 — yes, on the circle")], "Yes"),
("Sectors and Segments Preview", "A **sector** is a pizza-slice region bounded by two radii and an arc. Its area is a fraction of πr². This prepares for radians in [[4.7 Radians and Degrees]].", "tip", "Sector area = (angle/360) × πr² in degrees.", "A semicircle has radius 4 cm. Find area (π ≈ 3.14).", [("Half full circle","A = ½ × π × 4²"),("Calculate","A = 0.5 × 3.14 × 16 = 25.12")], "25.12 cm²"),
],
"why": "Every circle has the same shape ratio: circumference is always π times diameter. Area πr² follows because a circle fills π radius-squared units of space. These formulas extend perimeter and area from [[4.2 Perimeter Area and Volume]] to curved boundaries.",
"qq": "Find circumference of r = 5 cm (π ≈ 3.14).", "qa": "C = 2πr = 2 × 3.14 × 5 = 31.4", "qans": "31.4 cm",
"mistakes": [("Using πr instead of 2πr for circumference.","Use C = 2πr or C = πd."),
             ("Using 2πr for area.","Area is πr², not 2πr."),
             ("Confusing radius and diameter.","Check whether the given length reaches the centre."),
             ("Forgetting to square r in area.","A = π × r × r, not π × r."),
             ("Using degrees in arc without converting fraction.","Arc = (fraction of full turn) × 2πr.")],
"fail": "If circumference and area formulas are swapped, check whether the question asks for distance around or flat coverage.",
"cs": "Circles model wheels, rounded UI corners, and collision radii. `Math.hypot(x,y)` checks distance from origin — a circle test. Game AI uses **aggro radius**: enemies react when player distance ≤ r.\n\n```python\nimport math\ndef on_circle(x, y, r):\n    return math.hypot(x, y) <= r\n```\nSignal processing uses circular rotation; clock faces and loading spinners trace arcs.",
"ck": ["Define radius and diameter.","Write two circumference formulas.","What is π?","Write the circle area formula.","What is an arc?","Convert r = 9 cm to diameter.","C for d = 14 cm (π≈3.14)?","Does (5,12) lie on r=13 circle?","Name a CS use of radius.","How does arc length relate to circumference?"],
"mq": ["Define [[radius]].","Define [[diameter]].","Define [[circumference]].","Define [[pi]].","Define [[arc]].","C for r=8 cm (π≈3.14).","A for r=5 cm (π≈3.14).","d for r=11 cm.","Arc = half circle, r=6 (π≈3.14).","One CS example using circles."],
"pg": ["- define all five New Words","- convert between radius and diameter","- find circumference and area","- compute simple arc lengths","- test points on x²+y²=r²"],
"wetip": "Label r or d first. Pick C = 2πr or A = πr² before substituting.",
"we": [("Radius to Diameter","r = 9 cm. Find d.",[("Double","d = 18")],"d = 18 cm"),
       ("Circumference","r = 12 cm, π≈3.14.",[("Formula","C = 2πr = 2×3.14×12"),("Result","C = 75.36 cm")],"75.36 cm"),
       ("Circle Area","r = 10 cm, π≈3.14.",[("Square","r² = 100"),("Area","A = 314 cm²")],"314 cm²"),
       ("CS Aggro Radius","Player at (3,4), enemy radius 6.",[("Distance","hypot(3,4)=5"),("Compare","5 ≤ 6 — in range")],"Player is in aggro range"),
       ("Spot Mistake","Learner uses A=2πr for r=4.",[("Error","That is circumference formula"),("Fix","A = π×16 ≈ 50.27 cm²")],"A ≈ 50.27 cm²")],
"pqtip": "Draw the circle. Mark centre, radius, and what is asked.",
"pq": [("Section A - Vocabulary",["Define [[radius]].","Define [[diameter]].","Define [[circumference]].","Define [[pi]].","Define [[arc]].","Why is π the same for every circle?"]),
       ("Section B - Core Skills",["r=7: find d and C (π≈3.14).","d=30: find r and C (π≈3.14).","r=9: find A (π≈3.14).","C=62.8, find r (π≈3.14).","Semicircle r=5: arc length (π≈3.14).","Quarter circle r=12: arc (π≈3.14).","A=78.5, find r (π≈3.14).","Does (8,15) lie on r=17 circle?","Annulus: outer r=10, inner r=6 — find ring area.","Wheel diameter 70 cm — distance after 10 revolutions?"]),
       ("Section C - Mistake-Spotting",["Learner: A=2πr for r=3.","Learner: C=πr² for r=5.","Learner uses diameter as radius in A=πr².","Learner says π=22/7 exactly.","Learner forgets to halve for semicircle arc."]),
       ("Section D - Mixed Practice",["r=15: C and A.","d=18: r and C.","Sector 90°, r=8: arc and area.","Two circles r=3 and r=5 — compare areas.","x²+y²=49 — radius?","Circle through (0,5) centred origin — equation?","Pipe outer d=10, inner d=6 — cross-section area.","C=100 — find d.","A=154, find r (π≈3.14).","Hexagon inscribed in r=10 circle — compare perimeters conceptually."]),
       ("Section E - CS Transfer",["Explain aggro radius in games.","Why does `hypot(x,y)<=r` test a disk?","Loading spinner: 270° arc of r=40 px — arc length?","Rounded rectangle corner uses quarter circle r=8 — arc length?","Signal phase wraps every 360° — link to circumference."])],
"mt": """## Section A - Definitions (5 marks)
1. Define [[radius]]. (1) 2. Define [[diameter]]. (1) 3. Define [[circumference]]. (1) 4. Define [[pi]]. (1) 5. Define [[arc]]. (1)
## Section B - Core Skills (10 marks)
6. r=6: find d. (1) 7. r=6: find C (π≈3.14). (1) 8. r=6: find A (π≈3.14). (2) 9. d=20: find C (π≈3.14). (2) 10. Semicircle r=10: arc (π≈3.14). (2) 11. (6,8) on r=10 circle? (2)
## Section C - Error Checking (5 marks)
12. Fix: A=2πr for r=5. (1) 13. Fix: C=πr for r=5. (1) 14. r=4: A=? (1) 15. Quarter arc r=8 (π≈3.14). (1) 16. Why is d=2r? (1)
## Section D - Reasoning (2 marks)
17. Why is π constant for all circles? (1) 18. Circumference vs area — different units? (1)
## Section E - CS (3 marks)
19. `hypot(5,12)<=13` — true? (1) 20. Aggro radius 8, player distance 7.5 — triggered? (1) 21. One CS use of arc length. (1)""",
"ans": """## Practice & Mastery Solutions (selected)
**Key answers:** d=2r; C=2πr; A=πr²; arc = fraction×2πr.
7. d=14, C≈43.96 | 8. r=15, C≈94.2 | 9. A≈254.34 | 10. r=10 | 11. arc≈15.7 | 12. arc≈18.84
**Mastery:** 6.d=12 | 7.C≈37.68 | 8.A≈113.04 | 9.C≈62.8 | 10.arc≈31.4 | 11.Yes (100=100)
12.A=π×25≈78.5 | 13.C=2π×5≈31.4 | 14.A≈50.24 | 15.arc≈12.56 | 19.True | 20.Yes
**Pass: 22/25, A=5/5.**""",
"gloss": [("radius","The distance from the centre of a circle to any point on the circle.","4.3 Circle Geometry","4.2 Perimeter Area and Volume","Aggro and blast-radius checks in games use radius distance tests."),
          ("diameter","The distance across a circle through its centre; equal to twice the radius.","4.3 Circle Geometry","radius","Screen size and wheel dimensions are often quoted as diameter."),
          ("circumference","The distance around the outside edge of a circle.","4.3 Circle Geometry","perimeter","Animation loops and wheel rotation distance track circumference."),
          ("pi","The constant ratio circumference÷diameter, approximately 3.14159.","4.3 Circle Geometry","1.4 Multiplication and Division","Trigonometric functions in libraries use π in radian conversion."),
          ("arc","A portion of the circumference between two points on a circle.","4.3 Circle Geometry","circumference","UI progress arcs and circular path animation follow arc length.")],
},
]

# Add remaining topics 4.4-4.10 via exec of external data file
exec(open(BASE / "_scripts/m04_topics_data.py").read())

def generate_all():
    for t in TOPICS:
        tid = t["id"]
        w(GEO / f"{tid}.md", topic_note(t))
        w(WE / f"{tid} - Worked Examples.md", worked(t))
        w(PQ / f"{tid} - Practice Questions.md", practice(t))
        w(MT / f"{tid} - Mastery Test.md", mastery(t))
        w(ANS / f"{tid} - Answers.md", answers(t))
        for term, defn, topic, prior, cs in t["gloss"]:
            g(term, defn, topic, prior, cs)

if __name__ == "__main__":
    generate_all()
    print(f"Written: {len(written)}")
    if failures: print("Failures:", failures)
