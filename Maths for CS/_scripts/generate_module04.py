#!/usr/bin/env python3
"""Generate Module 04 Geometry & Trigonometry content (topics 4.2–4.10)."""
from pathlib import Path

BASE = Path("/home/Marau/Marau/University/Maths for CS")
GEO = BASE / "04 Geometry & Trigonometry"
WE = BASE / "90 Worked Examples"
PQ = BASE / "91 Practice Questions"
MT = BASE / "92 Mastery Tests"
ANS = BASE / "93 Answers and Mark Schemes"
GLOSS = BASE / "00 Glossary/Terms"

BREADCRUMBS = (
    "[[1.3 Addition and Subtraction]], [[1.4 Multiplication and Division]], "
    "[[2.2 Simplifying Expressions]], [[2.5 Solving Linear Equations]], "
    "[[3.1 Coordinates and Axes]], [[3.2 Function Notation and Mapping]]"
)

written = []
failures = []


def write(path: Path, content: str):
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        written.append(str(path))
    except Exception as e:
        failures.append(f"{path}: {e}")


def gloss(term, definition, topic, builds_on, cs_use):
    write(GLOSS / f"{term}.md", f"""# {term}
{definition}
First introduced in: [[{topic}]]
Builds on: [[{builds_on}]]
Used in CS: {cs_use}
## Related Notes
Search backlinks in Obsidian to see every topic that uses [[{term}]].
""")


def concept_block(num, title, body, callout_type, callout_text, example_q, steps, answer):
    steps_text = "\n\n".join(
        f"Step {i+1}: {s.split(': ', 1)[0] if ': ' in s else s.split('. ', 1)[0]}.\n\n```text\n{s.split(': ', 1)[1] if ': ' in s else s}\n```"
        if not s.strip().startswith("```")
        else f"Step {i+1}.\n\n{s}"
        for i, s in enumerate(steps)
    )
    # simpler step formatting
    step_lines = []
    for i, s in enumerate(steps, 1):
        step_lines.append(f"Step {i}: {s[0]}\n\n```text\n{s[1]}\n```")
    steps_fmt = "\n\n".join(step_lines)
    return f"""## Concept {num} - {title}
{body}

> [!{callout_type}] {callout_type.capitalize()}
> {callout_text}

### Chunked Example
Question: {example_q}

{steps_fmt}

Answer: **{answer}**.
"""


def make_topic(t):
    """Generate main topic note."""
    concepts = ""
    for i, c in enumerate(t["concepts"], 1):
        concepts += concept_block(i, c["title"], c["body"], c["callout_type"], c["callout"], c["q"], c["steps"], c["a"]) + "\n"

    mistakes = "\n".join(f"- Mistake: {m[0]}\n- Fix: {m[1]}" for m in t["mistakes"])
    checkpoints = "\n".join(f"{i}. {q}" for i, q in enumerate(t["checkpoints"], 1))
    mini = "\n".join(f"{i}. {q}" for i, q in enumerate(t["mini_quiz"], 1))
    new_words = "\n".join(f"- [[{w[0]}]] - {w[1]}" for w in t["terms"])

    return f"""# {t['title']}

Tags: #maths/geometry #maths/trigonometry #cs/graphics #cs/algorithms

## Position in the Course
Prerequisites: {t['prereq']}

Used later in: {t['forward']}

Earlier modules: {BREADCRUMBS}

Mastery threshold: 85% overall, and 100% on the New Words section.

> [!tip] How to study this note
> {t['study_tip']}

## Plain-English Idea
{t['plain']}

> [!example] Everyday idea
> {t['everyday']}

## New Words
{new_words}

You pass this topic only when you can define all five terms without looking.

{concepts}
## Why This Works
{t['why']}

This builds on measurement and algebra from {BREADCRUMBS}. Each formula counts units consistently: lengths add for [[perimeter]], lengths multiply for [[area]] and [[volume]], and the exponent on the unit tells you the dimension.

## Worked Examples
For fully worked solutions, use [[{t['title']} - Worked Examples]].

### Example 1 - Quick Check
Question: {t['quick_q']}

Solution:

```text
{t['quick_a']}
```

Answer: **{t['quick_ans']}**.

## Common Mistakes
{mistakes}

> [!failure] Mistake pattern
> {t['failure_pattern']}

## Where This Shows Up in CS
{t['cs_section']}

## Checkpoint Questions
{checkpoints}

## Mini-Quiz
{mini}

## Pass Gate
You may move to {t['next']} only when you can:

{t['pass_gate']}

- answer at least 9 out of 10 mini-quiz questions correctly
- complete [[{t['title']} - Mastery Test]] with at least 22/25 and full marks on definitions

## Related Notes
Backward links: {t['prereq']}, {BREADCRUMBS}

Forward links: {t['forward']}

Assessment links: [[{t['title']} - Worked Examples]], [[{t['title']} - Practice Questions]], [[{t['title']} - Mastery Test]], [[{t['title']} - Answers]]
"""


def make_worked(t):
    exs = ""
    for i, e in enumerate(t["worked"], 1):
        steps = "\n\n".join(f"### Step {j+1} - {s[0]}\n```text\n{s[1]}\n```" for j, s in enumerate(e["steps"]))
        exs += f"""## Example {i} - {e['title']}
Question: {e['q']}

{steps}

Answer: **{e['a']}**.

"""
    return f"""# {t['title']} - Worked Examples

Theory note: [[{t['title']}]]

Use these examples before attempting [[{t['title']} - Practice Questions]].

> [!tip] Worked example routine
> {t['worked_tip']}

{exs}"""


def make_practice(t):
    sections = ""
    for sec, qs in t["practice"].items():
        sections += f"## {sec}\n" + "\n".join(f"{i}. {q}" for i, q in qs, 1) + "\n\n"
    # fix enumerate
    out = f"""# {t['title']} - Practice Questions

Theory note: [[{t['title']}]]

Answers: [[{t['title']} - Answers]]

> [!tip] Paper-first rule
> {t['practice_tip']}

"""
    n = 1
    for sec, qs in t["practice"].items():
        out += f"## {sec}\n"
        for q in qs:
            out += f"{n}. {q}\n"
            n += 1
        out += "\n"
    out += f"""## Self-Check Before Marking
- Did you show units where needed?
- Did you label diagrams and vectors clearly?
- Did you check answers with a second method or reasonable estimate?

## Next Step
Mark using [[{t['title']} - Answers]], then attempt [[{t['title']} - Mastery Test]].
"""
    return out


def make_mastery(t):
    return f"""# {t['title']} - Mastery Test

Theory note: [[{t['title']}]]

Answers: [[{t['title']} - Answers]]

Pass mark: 85% (22/25). You must score full marks on Section A before moving on.

> [!danger] Test condition
> Do this without looking at the topic note, worked examples, or answers. Use paper. Mark it afterwards.

## Allowed Working
You may use blank paper, a pencil, and a basic calculator for arithmetic only.

You may not use notes, examples, search, or the answer sheet.

Show one step per line. Include units on measurement answers.

{t['mastery_body']}

## Marking
Total: 25 marks.

Pass:

- Section A: 5 out of 5 required.
- Overall: at least 22 out of 25.

Decision:

- [ ] Pass - move to {t['next']}.
- [ ] Review - create a correction note in [[94 Review Sheets]] and retake tomorrow.
- [ ] Restart - reread [[{t['title']}]] and redo [[{t['title']} - Worked Examples]].

## Retake Focus
If Section A is not perfect, rewrite the five glossary cards first.

If Section B is weak, redo Examples 1-3 from [[{t['title']} - Worked Examples]].

If Section E is weak, reread the CS section in [[{t['title']}]].
"""


def make_answers(t):
    return f"""# {t['title']} - Answers

Theory note: [[{t['title']}]]

Mastery test: [[{t['title']} - Mastery Test]]

Practice set: [[{t['title']} - Practice Questions]]

{t['answers_body']}
"""


# ── TOPIC DATA ──────────────────────────────────────────────────────────────

TOPICS = []

# 4.2
TOPICS.append({
    "title": "4.2 Perimeter Area and Volume",
    "prereq": "[[4.1 Lines Angles and Triangles]]",
    "forward": "[[4.3 Circle Geometry]]",
    "next": "[[4.3 Circle Geometry]]",
    "study_tip": "Draw the shape, label every edge, then decide whether the question asks for edge length (perimeter), flat coverage (area), or space filled (volume).",
    "plain": "**Perimeter** is the total distance around a shape's boundary. **Area** measures how much flat surface a shape covers. **Volume** measures how much three-dimensional space an object occupies. Units matter: perimeter uses ordinary length units, area uses **unit squared**, and volume uses **unit cubed**.",
    "everyday": "Painting a wall needs area in square metres. Fencing a garden needs perimeter in metres. Filling a box with sand needs volume in cubic centimetres.",
    "terms": [
        ("perimeter", "the total distance around the outside edge of a flat shape."),
        ("area", "the amount of flat surface inside a shape's boundary, measured in square units."),
        ("volume", "the amount of three-dimensional space an object occupies, measured in cubic units."),
        ("unit squared", "a square unit such as cm² or m² used to measure area."),
        ("unit cubed", "a cubic unit such as cm³ or m³ used to measure volume."),
    ],
    "concepts": [
        {"title": "Perimeter Is the Sum of Edge Lengths", "body": "The [[perimeter]] of a polygon is found by adding every side length. For a rectangle with length `L` and width `W`:\n\n```text\nP = 2L + 2W\n```\n\nThis uses repeated addition from [[1.3 Addition and Subtraction]] and doubling from [[1.4 Multiplication and Division]].", "callout_type": "important", "callout": "Perimeter always uses length units (cm, m), never squared or cubed units.", "q": "A rectangle is 8 cm long and 5 cm wide. Find its perimeter.", "steps": [("Add the four sides", "P = 8 + 5 + 8 + 5"), ("Or use the formula", "P = 2(8) + 2(5) = 16 + 10 = 26")], "a": "26 cm"},
        {"title": "Area of Rectangles and Triangles", "body": "[[area]] counts how many unit squares fit inside a shape.\n\nRectangle:\n\n```text\nA = length × width\n```\n\nTriangle (half a rectangle):\n\n```text\nA = ½ × base × height\n```\n\nThe height must be perpendicular to the base, linking to right angles in [[4.1 Lines Angles and Triangles]].", "callout_type": "warning", "callout": "Do not confuse slanted side length with perpendicular height.", "q": "Find the area of a triangle with base 10 cm and height 6 cm.", "steps": [("Write the formula", "A = ½ × b × h"), ("Substitute", "A = ½ × 10 × 6 = 30")], "a": "30 cm²"},
        {"title": "Reading and Writing Unit Squared", "body": "A [[unit squared]] such as `cm²` means a square 1 cm on each side. If a rectangle is 4 cm by 3 cm, its area is:\n\n```text\n4 × 3 = 12 square centimetres = 12 cm²\n```\n\nThe small 2 is not an ordinary exponent on the number — it belongs to the unit.", "callout_type": "example", "callout": "12 cm² means twelve squares each 1 cm wide and 1 cm tall.", "q": "A tile is 20 cm by 20 cm. How many cm² does one tile cover?", "steps": [("Multiply length by width", "20 × 20 = 400")], "a": "400 cm²"},
        {"title": "Volume of a Cuboid", "body": "[[volume]] for a cuboid (box shape) is:\n\n```text\nV = length × width × height\n```\n\nEach layer of unit cubes stacks to fill the box. Multiplication from [[1.4 Multiplication and Division]] counts layers × rows × columns of unit cubes.", "callout_type": "important", "callout": "Volume answers must include a cubed unit such as cm³ or m³.", "q": "A box is 4 cm × 3 cm × 2 cm. Find its volume.", "steps": [("Multiply the three edges", "V = 4 × 3 × 2 = 24")], "a": "24 cm³"},
        {"title": "Unit Cubed and Capacity", "body": "A [[unit cubed]] such as `m³` is a cube 1 m on each edge. In computing, memory and storage are often quoted in bytes, but 3D simulations still track physical volume for physics engines and voxel grids.", "callout_type": "tip", "callout": "1 litre = 1000 cm³. Useful when checking whether a container fits.", "q": "How many 1 cm³ cubes fit in a 5 cm × 2 cm × 2 cm box?", "steps": [("Find volume", "V = 5 × 2 × 2 = 20"), ("Each cube is 1 cm³", "20 cubes fit")], "a": "20 cubes"},
        {"title": "Composite Shapes", "body": "Split awkward shapes into rectangles or triangles, find each area, then add or subtract. This is the same divide-and-conquer idea used in recursive algorithms.", "callout_type": "example", "callout": "An L-shaped room is two rectangles glued together — find each area, then add.", "q": "An L-shape is a 6×4 rectangle with a 2×2 corner removed. Find the area.", "steps": [("Full rectangle", "6 × 4 = 24"), ("Removed corner", "2 × 2 = 4"), ("Subtract", "24 - 4 = 20")], "a": "20 cm²"},
    ],
    "why": "Perimeter adds lengths because you walk each edge once. Area multiplies two perpendicular lengths because you tile a surface with rows and columns of unit squares. Volume multiplies three edge lengths because you stack layers of unit cubes.",
    "quick_q": "Find the area of a 7 m × 4 m rectangle.",
    "quick_a": "A = 7 × 4 = 28",
    "quick_ans": "28 m²",
    "mistakes": [
        ("Using cm instead of cm² for area.", "Write square units for every area answer."),
        ("Using cm² instead of cm³ for volume.", "Volume always needs a cubed unit."),
        ("Adding side lengths when the question asks for area.", "Re-read: perimeter = add edges; area = multiply base and height."),
        ("Using slanted side as height in a triangle.", "Height must meet the base at a right angle."),
        ("Forgetting to double both length and width for perimeter.", "Use P = 2L + 2W or add all four sides explicitly."),
    ],
    "failure_pattern": "If units look wrong (cm for area, or cm² for volume), the measurement type was confused.",
    "cs_section": "Game engines store **axis-aligned bounding boxes** as width, height, depth — volume and surface area drive culling and physics. Texture memory is width × height × bytes-per-pixel (a 2D area calculation). Voxel worlds count occupied cells, a discrete volume measure.\n\n```python\n# Collision box volume check (simplified)\ndef aabb_volume(w, h, d):\n    return w * h * d\n\ndef texture_bytes(w, h, bpp=4):\n    return w * h * bpp  # area × bytes per pixel\n```",
    "checkpoints": ["What is perimeter?", "What unit type does area use?", "Write the volume formula for a cuboid.", "Why is triangle area half of base × height?", "How do you find the area of an L-shape?", "What is 1 cm² in words?", "Convert: a 10 cm cube has what volume?", "What prerequisite topic gives right angles for height?", "Name one CS object that uses area.", "Name one CS object that uses volume."],
    "mini_quiz": ["Define [[perimeter]].", "Define [[area]].", "Define [[volume]].", "Define [[unit squared]].", "Define [[unit cubed]].", "Find the perimeter of a 9 cm × 4 cm rectangle.", "Find the area of a triangle with base 8 and height 5.", "Find the volume of a 3×4×5 cuboid.", "A square has side 6 cm. Find perimeter and area.", "Explain one CS use of area or volume."],
    "pass_gate": "- define every term in [[#New Words]]\n- compute perimeter, area, and volume for rectangles, triangles, and cuboids\n- use correct squared and cubed units\n- split a composite shape into simpler parts\n- connect measurements to collision boxes or texture sizing",
    "worked_tip": "Label the shape, write the formula, substitute, then check units.",
    "worked": [
        {"title": "Rectangle Perimeter and Area", "q": "A screen panel is 24 cm wide and 13 cm tall. Find perimeter and area.", "steps": [("Perimeter", "P = 2(24) + 2(13) = 48 + 26 = 74"), ("Area", "A = 24 × 13 = 312")], "a": "P = 74 cm, A = 312 cm²"},
        {"title": "Triangle Area", "q": "Find the area of a triangle with base 14 m and height 9 m.", "steps": [("Formula", "A = ½ × 14 × 9"), ("Calculate", "A = 7 × 9 = 63")], "a": "63 m²"},
        {"title": "Cuboid Volume", "q": "A crate is 1.2 m × 0.8 m × 0.5 m. Find its volume.", "steps": [("Multiply edges", "V = 1.2 × 0.8 × 0.5"), ("Calculate", "V = 0.48")], "a": "0.48 m³"},
        {"title": "CS Transfer — Texture Memory", "q": "A 1920×1080 RGBA texture uses 4 bytes per pixel. How many bytes?", "steps": [("Area in pixels", "1920 × 1080 = 2,073,600"), ("Bytes per pixel", "2,073,600 × 4 = 8,294,400")], "a": "8,294,400 bytes (~7.9 MiB)"},
        {"title": "Spot the Mistake", "q": "A learner says a 5 cm × 5 cm square has area 20 cm. Find and fix the error.", "steps": [("Identify", "Used perimeter (5+5+5+5=20) instead of area"), ("Correct", "A = 5 × 5 = 25 cm²")], "a": "Area is 25 cm², not 20 cm"},
    ],
    "practice_tip": "Sketch each shape. Write P, A, or V at the top so you answer the right measurement.",
    "practice": {
        "Section A - Vocabulary": ["Define [[perimeter]].", "Define [[area]].", "Define [[volume]].", "Define [[unit squared]].", "Define [[unit cubed]].", "Why must area units be squared?"],
        "Section B - Core Skills": ["Find the perimeter of a 12 cm × 7 cm rectangle.", "Find the area of a 12 cm × 7 cm rectangle.", "A square has perimeter 36 cm. Find its side length and area.", "Triangle: base 16 cm, height 9 cm. Find area.", "Cuboid: 6 cm × 4 cm × 3 cm. Find volume.", "L-shape: 10×6 rectangle minus 4×3 corner. Find area.", "A room is 5 m × 4 m. How many 1 m² tiles cover the floor?", "A box holds 120 cm³. Can a 5×4×6 cm object fit?", "Find perimeter of an equilateral triangle with side 8 cm.", "A pool is 25 m × 10 m × 2 m deep. Find volume in m³."],
        "Section C - Mistake-Spotting": ["A learner writes area = 15 cm for a 5×3 rectangle. Correct it.", "A learner uses m² for the volume of a box. Correct the unit.", "A learner uses the slanted side 13 cm as height when base is 12 cm. Why is this wrong?", "A learner adds 2L + W for perimeter. Fix the formula.", "A learner says 1 m² = 100 cm². Correct the conversion idea."],
        "Section D - Mixed Practice": ["Square side 11 cm: perimeter and area.", "Rectangle 2.5 m × 1.2 m: area in m².", "Cuboid volume 180 cm³ with base 10×6. Find height.", "Composite: two 4×3 rectangles joined on a long side. Total area?", "How many 50 cm² stickers cover a 200 cm² panel?", "Perimeter of regular hexagon side 5 cm.", "Triangle area 48 cm², base 12 cm. Find height.", "Open-top box 8×5×4 cm: find base area and volume.", "Compare areas: 7×7 square vs 6×8 rectangle.", "A voxel chunk is 16×16×16 cells. How many cells?"],
        "Section E - CS Transfer": ["A sprite is 64×64 pixels, 4 bytes/pixel. Find memory in bytes.", "An AABB has width 2, height 3, depth 4 game units. Find volume.", "Why do texture atlases care about total pixel area?", "A tile map is 100×80 tiles of 32×32 px. Find total pixel area.", "A physics engine approximates a car as a 4×2×1.5 m box. Volume?", "Explain perimeter vs area for a UI border vs button fill."],
    },
    "mastery_body": """## Section A - Definitions (5 marks)
Each answer must be in your own words.

1. Define [[perimeter]]. (1)
2. Define [[area]]. (1)
3. Define [[volume]]. (1)
4. Define [[unit squared]]. (1)
5. Define [[unit cubed]]. (1)

## Section B - Core Skills (10 marks)
6. Perimeter of 15 cm × 8 cm rectangle. (1)
7. Area of 15 cm × 8 cm rectangle. (1)
8. Area of triangle: base 20 cm, height 7 cm. (2)
9. Volume of 5×4×3 cm cuboid. (2)
10. Square perimeter 40 cm — find side and area. (2)
11. L-shape: 8×5 rectangle, 3×2 corner removed — area. (2)

## Section C - Mixed / Error Checking (5 marks)
12. Correct: "A 6×6 square has area 24 cm." (1)
13. Correct: "Volume of a box is 50 cm²." (1)
14. A tile is 30 cm × 30 cm. Area in cm². (1)
15. How many 1 cm³ cubes in a 4×3×2 box? (1)
16. Explain why triangle height must be perpendicular to base. (1)

## Section D - Reasoning (2 marks)
17. Why does area use squared units? (1)
18. Why does volume use cubed units? (1)

## Section E - Computer Science Transfer (3 marks)
19. 128×128 RGBA texture, 4 bytes/pixel — total bytes? (1)
20. AABB w=3, h=2, d=5 — volume? (1)
21. One sentence: why game collision uses box dimensions. (1)
""",
    "answers_body": """## Practice Questions — Solutions

**Section A**
1. Total distance around a shape's boundary.
2. Flat surface covered, in square units.
3. Three-dimensional space occupied, in cubic units.
4. A square unit such as cm² measuring area.
5. A cubic unit such as cm³ measuring volume.
6. Area counts squares in two dimensions, so units are multiplied twice.

**Section B**
7. P = 2(12)+2(7) = **38 cm**
8. A = 12×7 = **84 cm²**
9. Side = 36/4 = **9 cm**; A = **81 cm²**
10. A = ½×16×9 = **72 cm²**
11. V = 6×4×3 = **72 cm³**
12. 10×6 − 4×3 = 60−12 = **48 cm²**
13. 5×4 = **20 tiles**
14. Object volume = 120 cm³ = box volume — **fits exactly**
15. P = 3×8 = **24 cm**
16. V = 25×10×2 = **500 m³**

**Section C**
19. Area = 5×3 = **15 cm²**, not 15 cm.
20. Use **m³** for volume.
21. Height must be **perpendicular** to base.
22. P = **2L + 2W**
23. 1 m² = **10,000 cm²** (100×100)

**Sections D & E** — full working in mark schemes: composite areas by split/add; pixel memory = width×height×bytes; voxel count = product of dimensions.

---

## Mastery Test — Mark Scheme

**A (5)** — definitions as above; all required for pass.

**B**
6. **38 cm** (1)
7. **120 cm²** (1)
8. **70 cm²** (2)
9. **60 cm³** (2)
10. Side **10 cm**, area **100 cm²** (2)
11. 40−6 = **34 cm²** (2)

**C**
12. Area = 6×6 = **36 cm²** (1)
13. **50 cm³** (1)
14. **900 cm²** (1)
15. **24** cubes (1)
16. Only perpendicular height gives true vertical distance to base (1)

**D**
17. Area spans two dimensions → unit×unit (1)
18. Volume spans three dimensions → unit³ (1)

**E**
19. 128×128×4 = **65,536 bytes** (1)
20. 3×2×5 = **30** cubic units (1)
21. Volume/dimensions define overlap tests for physics/culling (1)

**Total: 25 marks. Pass: 22/25 with 5/5 on Section A.**
""",
    "glossary": [
        ("perimeter", "The total distance around the outside edge of a flat shape.", "4.1 Lines Angles and Triangles", "Collision boundary length and fence-style path planning in simulations."),
        ("area", "The amount of flat surface inside a shape, measured in square units.", "4.1 Lines Angles and Triangles", "Texture pixel counts and UI layout regions are area calculations."),
        ("volume", "The amount of three-dimensional space an object occupies.", "4.2 Perimeter Area and Volume", "Axis-aligned bounding boxes in physics engines use width×height×depth."),
        ("unit squared", "A square unit such as cm² used to measure area.", "1.4 Multiplication and Division", "Screen resolution width×height counts pixels in square units."),
        ("unit cubed", "A cubic unit such as cm³ used to measure volume.", "4.2 Perimeter Area and Volume", "Voxel grids count occupied cells as discrete cubic units."),
    ],
})

print("Script part 1 loaded — run full generator after all topics appended")
