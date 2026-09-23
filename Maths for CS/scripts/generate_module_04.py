#!/usr/bin/env python3
"""Generate complete Module 04 Geometry and Trigonometry bundle."""
from pathlib import Path

BASE = Path("/home/Marau/Marau/University/Maths for CS")
MOD = BASE / "04 Geometry & Trigonometry"
WE = BASE / "90 Worked Examples"
PQ = BASE / "91 Practice Questions"
MT = BASE / "92 Mastery Tests"
ANS = BASE / "93 Answers and Mark Schemes"
GLOSS = BASE / "00 Glossary/Terms"

def w(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path

# --- TOPIC 4.1 ---
TOPIC_41 = r'''# 4.1 Lines Angles and Triangles

Tags: #maths/geometry #maths/angles #cs/graphics #cs/games

## Position in the Course
Prerequisites: [[3.10 Piecewise and Step Functions]], [[3.1 Coordinates and Axes]]

Used later in: [[4.2 Perimeter Area and Volume]], [[4.4 Pythagoras Theorem]], [[4.10 Geometry for Computer Graphics]]

Mastery threshold: 85% overall, and 100% on the New Words section.

> [!tip] How to study this note
> Draw every shape before calculating. Label vertices, mark equal angles with the same symbol, and mark parallel lines with matching arrows.

## Plain-English Idea
Geometry starts with naming shapes and measuring how much they turn. A **line** is a straight path with no thickness; an **angle** measures rotation between two rays; **parallel** lines never meet; a **triangle** has three sides and three angles whose **angle sum** is always 180°.

> [!example] Everyday idea
> A door hinge opens through an angle. Two railway tracks run parallel. A roof truss forms triangles because triangles resist bending — the same reason game meshes use triangle faces.

## New Words
- [[line]] - a straight path that extends forever in both directions.
- [[angle]] - the amount of turn between two rays meeting at a vertex.
- [[parallel]] - lines in the same plane that never intersect.
- [[triangle]] - a polygon with exactly three sides and three angles.
- [[angle sum]] - the total of all interior angles in a shape.

You pass this topic only when you can define all five terms without looking.

## Concept 1 - Points, Lines, and Rays
A **point** marks a location. A **line** extends forever in both directions. A **ray** starts at one point and goes forever in one direction. A **line segment** has two endpoints.

This builds on [[3.1 Coordinates and Axes]], where every point has coordinates `(x, y)`.

> [!important] Line vs segment
> In proofs, "line" often means infinite extension. In measurement problems, you usually mean a segment with a definite length.

### Chunked Example
Question: Point A is at `(0, 0)` and point B is at `(4, 0)`. Describe the line through A and B.

Step 1: Both points share `y = 0`.

Step 2: The line is horizontal on the x-axis.

Step 3: As a set of points:

```text
{(x, 0) : x is any real number}
```

Answer: The **horizontal line y = 0** (the x-axis).

## Concept 2 - Naming and Measuring Angles
An [[angle]] is formed when two rays share a vertex. We measure angles in **degrees** (°).

Types:
- **Acute**: less than 90°
- **Right**: exactly 90°
- **Obtuse**: between 90° and 180°
- **Straight**: exactly 180°

> [!warning] Always identify the vertex first
> In ∠ABC, the middle letter B is the vertex. The angle is at B, not at A or C.

### Chunked Example
Question: Two rays meet at O. One ray points east, the other points north-east (45° from east). What is the angle?

Step 1: East to north-east is a quarter-turn of 45°.

Step 2: Check: acute, less than 90°.

Answer: **45°**.

## Concept 3 - Parallel Lines and Transversals
[[parallel]] lines stay the same distance apart and never cross. When a third line (a **transversal**) crosses parallel lines, matching angle pairs appear:

- **Corresponding angles** are equal
- **Alternate angles** are equal
- **Co-interior angles** add to 180°

These facts come from [[2.4 Angles on a Line and at a Point]] logic extended to parallel structure.

> [!tip] Z and F patterns
> Alternate angles form a Z shape. Corresponding angles form an F shape. Use the letter shapes to spot equal angles quickly.

### Chunked Example
Question: Lines l and m are parallel. A transversal makes a 65° angle with l. Find the corresponding angle on m.

Step 1: Corresponding angles are equal when lines are parallel.

Step 2: Copy the angle to the matching position on m.

Answer: **65°**.

## Concept 4 - Triangle Facts
A [[triangle]] has three sides and three interior angles. The [[angle sum]] of any triangle is:

```text
180°
```

Triangle types by sides:
- **Equilateral**: three equal sides
- **Isosceles**: two equal sides
- **Scalene**: no equal sides

Triangle types by angles:
- **Acute**: all angles < 90°
- **Right**: one angle = 90°
- **Obtuse**: one angle > 90°

> [!example] CS connection
> Game engines store meshes as lists of triangle vertices. Each triangle face has exactly three corner points — the same structure you label on paper.

### Chunked Example
Question: A triangle has angles 55° and 70°. Find the third angle.

Step 1: Use angle sum.

```text
55 + 70 + x = 180
```

Step 2: Add known angles.

```text
125 + x = 180
```

Step 3: Solve.

```text
x = 55
```

Answer: **55°**. The triangle is isosceles (55°, 55°, 70° — wait, 55+70+55=180, so angles are 55°, 70°, 55°).

## Concept 5 - Exterior Angles
An **exterior angle** of a triangle equals the sum of the two opposite interior angles:

```text
exterior angle = sum of remote interior angles
```

This follows from the [[angle sum]] rule and straight-line angles (180°).

> [!important] One exterior angle per vertex extension
> Extend one side; the exterior angle sits outside the triangle at that vertex.

### Chunked Example
Question: Interior angles at A and B are 40° and 75°. Find the exterior angle at C.

Step 1: Find interior angle at C.

```text
C = 180 - 40 - 75 = 65°
```

Step 2: Exterior angle at C is supplementary.

```text
exterior = 180 - 65 = 115°
```

Step 3: Check with remote interior rule.

```text
40 + 75 = 115 ✓
```

Answer: **115°**.

## Concept 6 - Angles in Coordinates and Game Space
[[3.1 Coordinates and Axes]] gives every vertex a position. In a 2D game, a character at `(3, 4)` facing east has direction angle 0°; facing north is 90° counter-clockwise from east.

When two edges meet, the angle between their direction vectors matters for collision normals and lighting — preview for [[4.8 Vectors Basics]].

> [!example] CS connection
> A tile map uses grid coordinates. Diagonal movement between `(0,0)` and `(1,1)` turns 45° from pure horizontal movement.

### Chunked Example
Question: A sprite moves from `(0, 0)` to `(3, 0)` then turns to `(3, 3)`. What angle did it turn?

Step 1: First leg is along +x (0°).

Step 2: Second leg goes from `(3,0)` to `(3,3)` — straight up (+y).

Step 3: Turn from +x to +y is 90° counter-clockwise.

Answer: **90°** turn.

## Why This Works
Angle facts are consistent because they preserve the flat geometry of a plane. [[3.1 Coordinates and Axes]] lets you place shapes precisely; [[2.4 Angles on a Line and at a Point]] (if studied) explains why angles on a straight line sum to 180°.

The triangle angle sum (180°) comes from drawing a line parallel to one side through the opposite vertex — parallel-line angle facts make the three angles at that point add to a straight line.

In symbols, for triangle ABC:

```text
∠A + ∠B + ∠C = 180°
```

## Worked Examples
For fully worked solutions, use [[4.1 Lines Angles and Triangles - Worked Examples]].

### Example 1 - Quick Angle Sum
Question: Find the missing angle in a triangle with 90° and 38°.

```text
180 - 90 - 38 = 52°
```

Answer: **52°**.

## Common Mistakes
- Mistake: Using the wrong vertex when naming ∠ABC.
- Fix: Middle letter is always the vertex.
- Mistake: Assuming any three lengths form a triangle.
- Fix: Longest side must be less than the sum of the other two (preview of [[4.4 Pythagoras Theorem]]).
- Mistake: Mixing up alternate and corresponding angles.
- Fix: Draw the Z or F pattern and label matching pairs.
- Mistake: Forgetting co-interior angles sum to 180°, not equal.
- Fix: Co-interior = same-side interior = supplementary.
- Mistake: Measuring from the wrong ray when finding turn angle.
- Fix: State the starting direction and rotation sense (clockwise/counter-clockwise).

> [!failure] Mistake pattern
> If your triangle angles do not sum to 180°, one angle was misread or a parallel-line fact was applied incorrectly.

## Where This Shows Up in CS
- **Game coordinates**: every mesh vertex is a point; every edge is a segment.
- **Collision detection**: triangle faces define solid surfaces in 3D engines.
- **UI layout**: parallel lines create consistent margins; right angles align panels.
- **Pathfinding grids**: turns at intersections are angle changes between movement directions.
- **SVG/Canvas**: `line`, `polygon`, and `path` elements rely on the same vocabulary.

## Checkpoint Questions
1. What is the difference between a line and a line segment?
2. Define [[angle]] in your own words.
3. What does [[parallel]] mean?
4. What is the [[angle sum]] of any triangle?
5. Name the three types of triangle by side length.
6. If corresponding angles are equal, what must be true about the lines?
7. An exterior angle of a triangle is 120°. One remote interior angle is 50°. Find the other.
8. Point `(2, 5)` — which axis is the horizontal coordinate?
9. Why do game meshes use triangles instead of four-sided faces alone?
10. Which later topic uses right triangles for distance?

## Mini-Quiz
1. Define [[line]].
2. Define [[angle]].
3. Define [[parallel]].
4. Define [[triangle]].
5. Define [[angle sum]].
6. Find the missing angle: 47°, 63°, ?
7. Lines are parallel. Corresponding angle = 112°. Find the matching angle on the second line.
8. Classify a triangle with angles 90°, 45°, 45°.
9. Exterior angle = 95°. Remote interior angles are 40° and ?
10. A turn from east to north is how many degrees counter-clockwise?

## Pass Gate
You may move to [[4.2 Perimeter Area and Volume]] only when you can:

- define every term in [[#New Words]]
- name angles and identify the vertex correctly
- use parallel-line angle facts (corresponding, alternate, co-interior)
- find missing triangle angles using angle sum and exterior-angle rules
- connect points and lines to coordinate grids from [[3.1 Coordinates and Axes]]
- answer at least 8 out of 10 mini-quiz questions correctly
- complete [[4.1 Lines Angles and Triangles - Mastery Test]]

## Related Notes
Backward links: [[3.1 Coordinates and Axes]], [[3.10 Piecewise and Step Functions]], [[2.4 Angles on a Line and at a Point]]

Forward links: [[4.2 Perimeter Area and Volume]], [[4.4 Pythagoras Theorem]], [[4.10 Geometry for Computer Graphics]]

Assessment links: [[4.1 Lines Angles and Triangles - Worked Examples]], [[4.1 Lines Angles and Triangles - Practice Questions]], [[4.1 Lines Angles and Triangles - Mastery Test]], [[4.1 Lines Angles and Triangles - Answers]]
'''

WE_41 = r'''# 4.1 Lines Angles and Triangles - Worked Examples

Theory note: [[4.1 Lines Angles and Triangles]]

Use these examples before attempting [[4.1 Lines Angles and Triangles - Practice Questions]].

> [!tip] Worked example routine
> Draw the diagram first. Mark parallel lines, label every angle, then apply the correct rule.

## Example 1 - Missing Triangle Angle
Question: A triangle has angles 48° and 71°. Find the third angle.

### Step 1 - State angle sum rule
```text
48 + 71 + x = 180
```

### Step 2 - Add known angles
```text
119 + x = 180
```

### Step 3 - Solve
```text
x = 61
```

Answer: **61°**.

## Example 2 - Parallel Lines and Corresponding Angles
Question: Lines AB and CD are parallel. A transversal makes a 73° angle with AB. Find the corresponding angle on CD.

### Step 1 - Identify angle type
Corresponding angles are equal when lines are parallel.

### Step 2 - Apply rule
```text
corresponding angle = 73°
```

Answer: **73°**.

## Example 3 - Alternate Angles
Question: Parallel lines with alternate angles labelled x and 118°. Find x.

### Step 1 - Alternate angles are equal
```text
x = 118
```

Answer: **118°**.

## Example 4 - Exterior Angle
Question: Remote interior angles are 52° and 61°. Find the exterior angle.

### Step 1 - Apply exterior angle theorem
```text
exterior = 52 + 61 = 113
```

Answer: **113°**.

## Example 5 - Spot the Mistake
Question: A learner says a triangle can have angles 80°, 60°, and 50°. What is wrong?

### Step 1 - Sum the angles
```text
80 + 60 + 50 = 190
```

### Step 2 - Compare to angle sum
```text
190 ≠ 180
```

### Step 3 - Correct approach
Third angle should be `180 - 80 - 60 = 40°`.

Answer: Angles must sum to **180°**, not 190°. Correct third angle: **40°**.

## Example 6 - CS Transfer: Tile Map Turn
Question: A character walks right from `(0,0)` to `(4,0)`, then up to `(4,3)`. What angle does the path turn at `(4,0)`?

### Step 1 - First segment direction
Right = 0° from +x axis.

### Step 2 - Second segment direction
Up = 90° from +x axis.

### Step 3 - Turn angle
```text
90 - 0 = 90° counter-clockwise
```

Answer: **90°** turn — a right angle.

Practice next: [[4.1 Lines Angles and Triangles - Practice Questions]]
'''

PQ_41 = r'''# 4.1 Lines Angles and Triangles - Practice Questions

Theory note: [[4.1 Lines Angles and Triangles]]

Answers: [[4.1 Lines Angles and Triangles - Answers]]

> [!tip] Paper-first rule
> Draw every diagram. Mark parallel lines with arrows and equal angles with matching arcs before calculating.

## How to Use This Practice
For angle questions, write:

```text
known angles:
rule used:
calculation:
answer:
```

## Section A - Vocabulary
1. Define [[line]].
2. Define [[angle]].
3. Define [[parallel]].
4. Define [[triangle]].
5. Define [[angle sum]].
6. What is the difference between a ray and a line segment?

## Section B - Core Skills
7. Find the missing angle: 35°, 82°, ?
8. Find the missing angle: 90°, 27°, ?
9. A triangle has angles x, x, and 40°. Find x.
10. An isosceles triangle has a vertex angle of 36°. Find each base angle.
11. Parallel lines: corresponding angle = 105°. Find the matching angle.
12. Parallel lines: alternate angle = 67°. Find the other alternate.
13. Co-interior angles: one is 118°. Find the other.
14. Exterior angle = 130°. One remote interior = 55°. Find the other remote interior.
15. Classify by sides: 5 cm, 5 cm, 8 cm.
16. Classify by angles: 30°, 60°, 90°.
17. How many degrees in a straight angle?
18. Two angles on a straight line are (3x)° and (2x + 40)°. Find x.

## Section C - Mistake-Spotting
For each question, write the mistake, correction, and reason.

19. A learner says a triangle can have angles 70°, 60°, 55°.
20. A learner treats co-interior angles as equal instead of summing to 180°.
21. A learner names ∠CAB when the vertex is B.
22. A learner says parallel lines meet at infinity so the rule does not apply.

## Section D - Mixed Practice
23. A triangle has angles in ratio 2 : 3 : 4. Find all three angles.
24. Parallel lines cut by transversal: one angle is 124°. Find all four co-interior pairs' partners.
25. An exterior angle is twice one remote interior of 35°. Find the other remote interior.
26. Points A(0,0), B(4,0), C(4,3) form a triangle. What type by angle at B?
27. From east to south-west, how many degrees clockwise is the turn?
28. Three angles of a quadrilateral are 85°, 95°, 110°. Find the fourth (use angle sum of quadrilateral = 360°).

## Section E - CS Transfer
29. Why do 3D meshes prefer triangle faces over arbitrary polygons?
30. A sprite at `(10, 20)` moves to `(10, 50)`. What direction angle (from +x, counter-clockwise)?
31. Two UI panels share a border — what angle do their edges make if aligned flush?
32. In a tile map, moving diagonally one step changes both x and y by 1. What turn from pure horizontal?

## Stretch
33. Parallel lines: one angle is (2x + 10)° and its co-interior partner is (3x - 5)°. Find x and both angles.

## Self-Check Before Marking
- Did every triangle angle sum check to 180°?
- Did you identify the vertex before naming an angle?
- Did parallel-line facts apply only when lines are marked parallel?

## Marking Routine
Mark in a different colour. Retake failed sections before [[4.1 Lines Angles and Triangles - Mastery Test]].
'''

MT_41 = r'''# 4.1 Lines Angles and Triangles - Mastery Test

Theory note: [[4.1 Lines Angles and Triangles]]

Answers: [[4.1 Lines Angles and Triangles - Answers]]

Pass mark: 85% (22 out of 25). You must score full marks on Section A before moving on.

> [!danger] Test condition
> Do this without notes. Draw diagrams where needed.

## Section A - Definitions (5 marks)
1. Define [[line]]. (1)
2. Define [[angle]]. (1)
3. Define [[parallel]]. (1)
4. Define [[triangle]]. (1)
5. Define [[angle sum]]. (1)

## Section B - Core Skills (10 marks)
6. Missing angle: 56°, 74°, ? (1)
7. Isosceles triangle: base angles 65° each. Vertex angle? (1)
8. Corresponding angle = 88° on parallel lines. Matching angle? (1)
9. Alternate angles: 71° and ? (1)
10. Co-interior: 112° and ? (1)
11. Exterior angle with remote interiors 48° and 59°? (1)
12. Classify triangle: 60°, 60°, 60°. (1)
13. Straight line angles: 4x and (5x + 18)°. Find x. (1)
14. Angles in ratio 1:2:3 in a triangle. Smallest angle? (1)
15. Quadrilateral angles 90°, 90°, 100°, ? (1)

## Section C - Mixed / Error Checking (5 marks)
16. Correct: "A triangle has angles 90°, 45°, 50°." (1)
17. Name the vertex in ∠PQR. (1)
18. Why do co-interior angles sum to 180° not equal? (1)
19. Points (0,0), (5,0), (5,5): angle at (5,0)? (1)
20. Exterior angle 140°, one remote interior 85°. Other? (1)

## Section D - Reasoning (2 marks)
21. Explain why triangle angle sum is 180° using parallel lines. (1)
22. Why are triangles used as mesh faces in graphics? (1)

## Section E - Computer Science Transfer (3 marks)
23. A path goes from (0,0) to (6,0) then to (6,4). Turn angle at (6,0)? (1)
24. What CS object corresponds to a line segment between two vertices? (1)
25. Name one place parallel-line reasoning appears in UI or layout. (1)

## Marking
Total: 25 marks. Pass: Section A 5/5 required; overall ≥ 22/25.

Decision:
- [ ] Pass - move to [[4.2 Perimeter Area and Volume]].
- [ ] Review - correction note in [[94 Review Sheets]], retake tomorrow.
- [ ] Restart - reread [[4.1 Lines Angles and Triangles]] and redo worked examples.
'''

ANS_41 = r'''# 4.1 Lines Angles and Triangles - Answers

Theory note: [[4.1 Lines Angles and Triangles]]

Practice: [[4.1 Lines Angles and Triangles - Practice Questions]]

Mastery test: [[4.1 Lines Angles and Triangles - Mastery Test]]

## Practice Questions - Answers

### Section A
1. A straight path extending forever in both directions. (1)
2. The amount of turn between two rays at a vertex. (1)
3. Lines in the same plane that never meet. (1)
4. A three-sided polygon. (1)
5. The total of interior angles in a shape; 180° for any triangle. (1)
6. A ray has one endpoint; a segment has two endpoints and finite length. (1)

### Section B
7. `180 - 35 - 82 = **47°**`
8. `180 - 90 - 27 = **63°**`
9. `2x + 40 = 180`, `x = **70°**`
10. Base angles = `(180 - 36)/2 = **72°**` each
11. **105°**
12. **67°**
13. `180 - 118 = **62°**`
14. `130 - 55 = **75°**`
15. Isosceles (1)
16. Right triangle (1)
17. **180°**
18. `5x + 40 = 180`, `x = **28**`

### Section C
19. Sum is 185° ≠ 180°. Correct third angle: **50°**.
20. Co-interior supplementary: if one is a, other is `180 - a`.
21. Vertex is middle letter; ∠CAB has vertex A, not B.
22. Parallel lines in Euclidean geometry never meet; rules apply exactly.

### Section D
23. `9k = 180`, angles **40°, 60°, 80°**
24. Supplement of 124° is **56°** for co-interior partners
25. Other remote = `2(35) - 35 = **35°**` (exterior = 70°)
26. Right angle at B (1)
27. **135°** clockwise from east to south-west
28. `360 - 290 = **70°**`

### Section E
29. Triangles are always planar and rigid; GPUs rasterise triangles efficiently.
30. **90°** (straight up from +x)
31. **180°** or **0°** — collinear flush edges
32. **45°** from horizontal to diagonal

### Stretch
33. `2x + 10 + 3x - 5 = 180`, `x = 35`, angles **80°** and **100°**

## Mastery Test - Mark Scheme

Section A: 1 mark each for clear own-words definitions.

Section B: 6. **50°** 7. **50°** 8. **88°** 9. **71°** 10. **68°** 11. **107°** 12. Equilateral 13. `9x+18=180`, x=18 14. **30°** 15. **80°**

Section C: 16. Third angle should be **45°** 17. **Q** 18. Same-side interior between parallels are supplementary 19. **90°** 20. **55°**

Section D: 21. Draw line parallel to base through opposite vertex; angles on straight line sum to 180° 22. Always planar, hardware-optimised, rigid structure

Section E: 23. **90°** 24. Edge / mesh edge / line segment between vertices 25. Parallel margins, flexbox rows, grid tracks
'''

GLOSS_41 = {
    "line": ("A straight path that extends forever in both directions with no thickness.", "[[4.1 Lines Angles and Triangles]]", "[[3.1 Coordinates and Axes]]", "SVG line elements and edge lists in mesh geometry use line segments between vertices."),
    "angle": ("The amount of turn, measured in degrees, between two rays sharing a vertex.", "[[4.1 Lines Angles and Triangles]]", "[[line]]", "Sprite rotation and camera yaw are angle values applied each frame."),
    "parallel": ("Lines in the same plane that stay the same distance apart and never intersect.", "[[4.1 Lines Angles and Triangles]]", "[[line]]", "Parallel CSS flex rows and railway-track metaphors in layout engines never converge."),
    "triangle": ("A polygon with exactly three sides, three vertices, and three interior angles.", "[[4.1 Lines Angles and Triangles]]", "[[angle sum]]", "GPUs rasterise 3D models as lists of triangle faces with three corner indices."),
    "angle sum": ("The total of all interior angles in a polygon; 180° for every triangle.", "[[4.1 Lines Angles and Triangles]]", "[[triangle]]", "Validating mesh data checks that planar triangle corners lie in a consistent flat orientation."),
}

# Write 4.1 files
w(MOD / "4.1 Lines Angles and Triangles.md", TOPIC_41)
w(WE / "4.1 Lines Angles and Triangles - Worked Examples.md", WE_41)
w(PQ / "4.1 Lines Angles and Triangles - Practice Questions.md", PQ_41)
w(MT / "4.1 Lines Angles and Triangles - Mastery Test.md", MT_41)
w(ANS / "4.1 Lines Angles and Triangles - Answers.md", ANS_41)
for term, (defn, intro, builds, cs) in GLOSS_41.items():
    w(GLOSS / f"{term}.md", f"# {term}\n{defn}\nFirst introduced in: {intro}\nBuilds on: {builds}\nUsed in CS: {cs}\n## Related Notes\nSearch backlinks in Obsidian to see every topic that uses [[{term}]].\n")

print("4.1 done")
