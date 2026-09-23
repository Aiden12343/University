#!/usr/bin/env python3
"""Generate complete Module 04 Geometry & Trigonometry topic bundles."""

from pathlib import Path

BASE = Path("/home/Marau/Marau/University/Maths for CS")

TOPICS = [
    {
        "id": "4.1",
        "name": "Lines Angles and Triangles",
        "tags": "#maths/geometry #maths/trigonometry #cs/graphics",
        "prereq": "[[3.10 Piecewise and Step Functions]]",
        "next": "[[4.2 Perimeter Area and Volume]]",
        "forward": "[[4.2 Perimeter Area and Volume]], [[4.4 Pythagoras Theorem]], [[4.10 Geometry for Computer Graphics]]",
        "plain": "Geometry starts with naming shapes and measuring how much one line turns relative to another.",
        "everyday": "When a door is half open, the door and the frame form an angle. When two train tracks never meet, they are parallel.",
        "words": [
            ("line", "a straight path that extends forever in both directions with no thickness."),
            ("angle", "the amount of turn between two rays or line segments that meet at a point."),
            ("parallel", "lines in the same plane that never meet, no matter how far they are extended."),
            ("triangle", "a flat shape with exactly three straight sides and three interior angles."),
            ("angle sum", "the fact that the three interior angles of any triangle add to 180°."),
        ],
        "glossary_builds": [
            ("line", "[[3.1 Coordinates and Axes]]"),
            ("angle", "[[line]]"),
            ("parallel", "[[line]], [[angle]]"),
            ("triangle", "[[line]], [[angle]]"),
            ("angle sum", "[[triangle]], [[angle]]"),
        ],
        "glossary_cs": [
            ("line", "Ray casting and edge detection treat scene geometry as collections of line segments."),
            ("angle", "Camera field of view, joint rotations, and steering angles all measure turn."),
            ("parallel", "Parallel projection in graphics keeps parallel lines parallel on screen."),
            ("triangle", "GPUs render almost everything as triangles because three points always define a flat face."),
            ("angle sum", "Mesh deformation checks use angle sums to detect folded or broken surfaces."),
        ],
        "cs_objects": "triangle meshes, edge lists, normal vectors, collision polygons",
        "cs_connection": "Every 3D model in a game engine is stored as vertices connected by edges and filled with triangles.",
        "concepts": [
            {
                "title": "Concept 1 - Points, Lines, and Segments",
                "body": """A **point** marks a location. It has no size.

A [[line]] extends forever in both directions. In diagrams we draw a segment with arrowheads to suggest infinity.

A **line segment** is the part of a line between two endpoints. Programs usually store segments because they have finite start and end coordinates.

```text
Point:     *
Segment:   A--------B
Line:      <----A--------B---->
```

In [[3.1 Coordinates and Axes]], you learned to name locations with `(x, y)`. A segment from `(0, 0)` to `(4, 0)` lies along the x-axis.

> [!important] Lines vs segments in CS
> Collision detection uses **segments** (walls, edges). Infinite lines appear in clipping and projection maths.""",
                "example_q": "Name the object: the path from pixel (10, 20) to pixel (50, 20).",
                "example_steps": [
                    "Step 1: It has two endpoints, so it is not an infinite line.",
                    "Step 2: It is a straight path between two points.",
                    "Step 3: This is a **line segment** from `(10, 20)` to `(50, 20)`.",
                ],
                "example_a": "A **line segment** (often called an edge in graphics).",
                "callout": "tip",
                "callout_text": "When reading geometry in code, ask: is this infinite or bounded?",
            },
            {
                "title": "Concept 2 - Measuring Angles",
                "body": """An [[angle]] is formed when two rays or segments meet at a **vertex**.

We measure angles in **degrees** (°). A full turn is 360°. A half turn is 180°. A quarter turn is 90°.

```text
        ray
       /
      /  θ  ← angle at vertex
     /
----●----
     ray
```

Common names:

```text
acute:   less than 90°
right:   exactly 90°
obtuse:  between 90° and 180°
straight: exactly 180°
```

> [!warning] Always name the vertex
> In ∠ABC, the middle letter B is the vertex. The angle is at B, not at A or C.""",
                "example_q": "Classify an angle of 120°.",
                "example_steps": [
                    "Step 1: 120° is greater than 90°.",
                    "Step 2: 120° is less than 180°.",
                    "Step 3: The angle is **obtuse**.",
                ],
                "example_a": "**Obtuse angle** (120°).",
                "callout": "example",
                "callout_text": "A laptop lid opened to about 110° forms an obtuse angle between screen and keyboard.",
            },
            {
                "title": "Concept 3 - Parallel Lines and Transversals",
                "body": """Two [[parallel]] lines never meet. The symbol is ∥.

When a third line (a **transversal**) crosses parallel lines, special angle pairs appear:

```text
        t (transversal)
        |
   ----●----  line 1
        |
   ----●----  line 2 (parallel to line 1)
```

- **Corresponding angles** are equal.
- **Alternate interior angles** are equal.
- **Co-interior angles** add to 180°.

These facts come from [[angle]] relationships and are used heavily in proofs and in CAD layout.

> [!tip] Spotting parallel lines
> Look for the arrow marks on diagrams — they mark parallel pairs.""",
                "example_q": "Lines L1 and L2 are parallel. A transversal makes a 65° angle with L1. What is the corresponding angle on L2?",
                "example_steps": [
                    "Step 1: Corresponding angles on parallel lines are equal.",
                    "Step 2: The matching angle on L2 is also 65°.",
                ],
                "example_a": "**65°** (corresponding angles are equal).",
                "callout": "important",
                "callout_text": "Parallel line angle rules only work when the lines are genuinely parallel.",
            },
            {
                "title": "Concept 4 - Types of Triangles",
                "body": """A [[triangle]] has three sides and three angles.

By sides:

```text
equilateral:  all three sides equal
isosceles:    two sides equal
scalene:      no sides equal
```

By angles:

```text
acute:        all angles < 90°
right:        one angle = 90°
obtuse:       one angle > 90°
```

The **right triangle** (one 90° angle) is essential for [[4.4 Pythagoras Theorem]] and [[4.5 Trig Ratios SOHCAHTOA]].

> [!example] GPU fact
> Graphics hardware prefers triangles because three non-collinear points always lie in one flat plane.""",
                "example_q": "A triangle has sides 5 cm, 5 cm, and 8 cm. What type by sides? Can it be equilateral?",
                "example_steps": [
                    "Step 1: Two sides are equal (5 and 5).",
                    "Step 2: The third side differs (8).",
                    "Step 3: It is **isosceles**, not equilateral.",
                ],
                "example_a": "**Isosceles** triangle.",
                "callout": "warning",
                "callout_text": "Do not assume a triangle is right-angled unless you know one angle is exactly 90°.",
            },
            {
                "title": "Concept 5 - Angle Sum in a Triangle",
                "body": """The [[angle sum]] property: interior angles of any triangle add to **180°**.

```text
     A
    / \\
   /   \\
  /  θ1 \\
 /       \\
B---------C
θ2    θ3

θ1 + θ2 + θ3 = 180°
```

If you know two angles, subtract their sum from 180° to find the third.

This connects to [[angle]] measurement and prepares you for polygon angle sums later.

> [!important] Interior vs exterior
> The angle **inside** the triangle is the interior angle. An exterior angle equals the sum of the two remote interior angles.""",
                "example_q": "Two angles of a triangle are 50° and 70°. Find the third angle.",
                "example_steps": [
                    "Step 1: Use the [[angle sum]] rule: all three add to 180°.",
                    "Step 2: Third angle = 180° − 50° − 70° = 60°.",
                ],
                "example_a": "**60°**",
                "callout": "failure",
                "callout_text": "A common error is adding only two angles and stopping. Always check the three angles sum to 180°.",
            },
            {
                "title": "Concept 6 - Angles Around a Point and on a Straight Line",
                "body": """Angles on a **straight line** add to 180°.

Angles **around a point** add to 360°.

```text
straight line:   α + β = 180°

full turn:       α + β + γ + δ = 360°
```

These two rules combine with [[angle sum]] in triangles to solve many geometry puzzles.

When a [[line]] is cut by another line, supplementary angles (next to each other on a straight line) always sum to 180°.

> [!tip] Check your work
> After finding an unknown angle, verify adjacent angles on a straight line sum to 180°.""",
                "example_q": "Two angles on a straight line are (2x)° and (3x)°. Find x.",
                "example_steps": [
                    "Step 1: Angles on a straight line sum to 180°.",
                    "Step 2: 2x + 3x = 180 → 5x = 180.",
                    "Step 3: x = 36.",
                ],
                "example_a": "**x = 36** (the angles are 72° and 108°).",
                "callout": "example",
                "callout_text": "A hinge that opens 120° leaves 60° between the door and the frame extension — supplementary angles.",
            },
        ],
        "mistakes": [
            ("Confusing lines with segments", "A segment has endpoints; a line does not. In code, edges are segments."),
            ("Misidentifying the vertex", "In ∠ABC, the angle is at B. Always locate the middle letter."),
            ("Using parallel-line rules on non-parallel lines", "Check for parallel marks or given information first."),
            ("Assuming a triangle is right-angled from a drawing", "Measure or use given data; drawings can be misleading."),
            ("Forgetting angle sum is 180°", "After finding two angles, subtract from 180° for the third."),
            ("Mixing interior and exterior angles", "Exterior angle at a vertex equals 180° minus the interior angle at that vertex."),
        ],
        "checkpoint": [
            "What is the difference between a line and a line segment?",
            "Define [[angle]] in your own words.",
            "What does [[parallel]] mean?",
            "State the [[angle sum]] rule for triangles.",
            "An isosceles triangle has two angles of 65°. Find the third angle.",
            "Classify an angle of 90°.",
            "Two parallel lines are cut by a transversal. Corresponding angles are 48°. What is the matching angle on the second line?",
            "Why are triangles preferred over quadrilaterals for 3D mesh faces?",
            "Angles on a straight line sum to how many degrees?",
            "Name one CS object that uses line segments.",
        ],
        "miniquiz": [
            "Define [[line]] in one sentence.",
            "Define [[parallel]] in one sentence.",
            "Find the missing angle in a triangle with angles 35° and 85°.",
            "Classify a triangle with sides 3, 4, 5 cm by side lengths.",
            "Two angles on a straight line are 110° and x°. Find x.",
            "Is 95° acute, right, or obtuse?",
            "Sketch two [[parallel]] lines cut by a transversal. Mark one pair of corresponding angles.",
            "Explain why three vertices always define a flat face.",
            "A triangle has all angles equal. What is each angle?",
            "Give one CS example where [[angle]] measurement matters.",
        ],
        "we_examples": [
            ("Classify Angles", "Classify each angle: 45°, 90°, 135°, 180°.", [
                "45°: greater than 0°, less than 90° → **acute**.",
                "90°: exactly a quarter turn → **right**.",
                "135°: between 90° and 180° → **obtuse**.",
                "180°: straight line → **straight angle**.",
            ], "45° acute; 90° right; 135° obtuse; 180° straight."),
            ("Find Missing Triangle Angle", "Two angles of a triangle are 48° and 62°. Find the third.", [
                "Step 1: Use [[angle sum]]: interior angles add to 180°.",
                "Step 2: Third = 180° − 48° − 62° = 70°.",
                "Step 3: Check: 48 + 62 + 70 = 180 ✓",
            ], "**70°**"),
            ("Parallel Lines and Transversal", "Parallel lines are cut by a transversal. One angle is 112°. Find the co-interior angle on the same side.", [
                "Step 1: Co-interior angles on parallel lines sum to 180°.",
                "Step 2: Other angle = 180° − 112° = 68°.",
            ], "**68°**"),
            ("Spot the Mistake", "A learner says a triangle with angles 60°, 60°, 70° is valid. Explain the error.", [
                "Step 1: Add the angles: 60 + 60 + 70 = 190°.",
                "Step 2: Triangle [[angle sum]] must be 180°, not 190°.",
                "Step 3: The third angle must be 60°, not 70°, for an equilateral triangle — or the given triple is impossible.",
            ], "Invalid: angles sum to 190°, not 180°. Reduce one angle by 10°."),
            ("Identify Triangle Type", "Sides are 7, 7, 10 cm. Classify by sides and find angles if the equal angles are opposite equal sides.", [
                "Step 1: Two equal sides → **isosceles**.",
                "Step 2: Equal angles are opposite equal sides.",
                "Step 3: Let base angles be x: 2x + apex = 180° (need apex angle or use symmetry).",
            ], "**Isosceles** triangle."),
            ("CS Application - Mesh Edge", "A triangle mesh edge runs from `(0,0)` to `(100,0)`. Another edge from `(100,0)` to `(100,100)`. What angle do they form at `(100,0)`?", [
                "Step 1: First edge is horizontal (right). Second goes up (vertical).",
                "Step 2: Horizontal and vertical meet at 90°.",
                "Step 3: This is a **right angle** — common in axis-aligned UI layouts.",
            ], "**90°** (right angle) at the corner vertex."),
        ],
        "practice_a": [
            "Define [[line]].",
            "Define [[angle]].",
            "Define [[parallel]].",
            "Define [[triangle]].",
            "Define [[angle sum]].",
            "In one sentence, explain why order matters when naming ∠ABC.",
        ],
        "practice_b": [
            "Classify 30°.",
            "Classify 100°.",
            "Find the third angle in a triangle with angles 40° and 75°.",
            "Find the third angle in a triangle with angles 55° and 55°.",
            "Two angles on a straight line are 65° and x°. Find x.",
            "Angles around a point are 80°, 95°, 110°, and x°. Find x.",
            "A triangle has sides 6, 6, 6 cm. Classify by sides.",
            "A triangle has sides 5, 12, 13 cm. Is it scalene?",
            "Parallel lines cut by a transversal: corresponding angle is 73°. Find the matching angle.",
            "Co-interior angles are 118° and x°. Find x (parallel lines).",
        ],
        "practice_c": [
            "A learner says all triangles have a 90° angle. Correct them.",
            "A learner adds triangle angles and gets 190°. What went wrong?",
            "A learner calls a line segment an infinite line. Explain the difference.",
            "A learner uses alternate angle equality without parallel lines. Why is that invalid?",
        ],
        "practice_d": [
            "An isosceles triangle has apex angle 40°. Find each base angle.",
            "A triangle has angles in ratio 1:2:3. Find all three angles.",
            "Exterior angle of a triangle is 120°. One remote interior angle is 50°. Find the other.",
            "Can a triangle have two obtuse angles? Explain.",
            "Two parallel lines, transversal makes 55° with first line. Find alternate interior angle on second line.",
            "Sketch a scalene right triangle and label the right angle.",
        ],
        "practice_e": [
            "A UI panel corner is axis-aligned. What angle do adjacent edges form?",
            "Explain why game meshes use triangles, not arbitrary quadrilaterals.",
            "A robot arm joint rotates 45° from horizontal. What type of angle is 45°?",
            "Two edges meet at 180°. What does that tell you about the path?",
            "Write one sentence linking [[parallel]] lines to parallel projection in graphics.",
        ],
        "mastery_a": [
            "Define [[line]].",
            "Define [[angle]].",
            "Define [[parallel]].",
            "Define [[triangle]].",
            "Define [[angle sum]].",
            "Give a labelled example using at least three new words.",
        ],
        "mastery_b": [
            "Find the third angle in a triangle with angles 52° and 61°.",
            "Classify an angle of 135°.",
            "Two angles on a straight line are (4x)° and (2x)°. Find x.",
            "Parallel lines, corresponding angle 84°. Find matching angle.",
            "Isosceles triangle, base angles 70° each. Find apex angle.",
            "Explain why the [[angle sum]] rule works for every triangle.",
        ],
        "mastery_c": [
            "A learner says 40° + 50° + 100° = 180° forms a valid triangle. Correct them.",
            "A learner marks alternate angles equal without parallel lines. Explain the error.",
            "Describe two common mistakes when working with triangles.",
        ],
        "mastery_e": [
            "A mesh face has three vertices. Why must the face be planar?",
            "A game object rotates 90° about the y-axis. What angle type is 90°?",
            "Explain why edge lists store segments, not infinite lines.",
            "Write one sentence connecting geometry to CS.",
            "Create one correction note for any question you missed, or write \"none missed\".",
        ],
    },
]

# We'll extend with more topics - for now write a function framework and add all 10 topics
# Due to script size, topics 4.2-4.10 will be added in the same structure

def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path

print(f"Script loaded with {len(TOPICS)} topics (partial)")
