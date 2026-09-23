# 03 Functions & Graphs - Printable Summary

Understand inputs, outputs, mappings, graph shapes, logs, exponentials, transformations, and piecewise behaviour.

## What You Must Be Able To Do

### Foundations (3.1–3.3)
- [ ] [[3.1 Coordinates and Axes]] — Locate points precisely using horizontal and vertical positions; read quadrants and intercepts.
- [ ] [[3.2 Function Notation and Mapping]] — Treat a rule as a machine that turns inputs into outputs; use `f(x)` notation.
- [ ] [[3.3 Linear Functions and Gradient]] — Model constant-rate change with `y = mx + c`; compute gradient from two points.

### Curves and growth (3.4–3.7)
- [ ] [[3.4 Quadratic Functions]] — Sketch parabolas; find roots, vertex, and axis of symmetry.
- [ ] [[3.5 Polynomials]] — Evaluate, factorise, and interpret degree and end behaviour.
- [ ] [[3.6 Exponential Functions]] — Model repeated multiplication; recognise growth and decay curves.
- [ ] [[3.7 Logarithms]] — Reverse exponentials; evaluate `log_a(b)`; apply log laws.

### Structure and behaviour (3.8–3.10)
- [ ] [[3.8 Inverse and Composite Functions]] — Chain functions inside-out; find and check linear inverses; test one-to-one.
- [ ] [[3.9 Transformations of Graphs]] — Translate, reflect, and stretch graphs using function notation.
- [ ] [[3.10 Piecewise and Step Functions]] — Evaluate piecewise rules; use floor `⌊x⌋` and ceiling `⌈x⌉`.

## Key Rules Cheat Sheet

### Linear functions
```text
y = mx + c
m = (y₂ - y₁) / (x₂ - x₁)     gradient
c = y-intercept (value when x = 0)
```

### Quadratic (vertex form)
```text
y = a(x - h)² + k
vertex: (h, k)
a > 0 → opens up;  a < 0 → opens down
```

### Exponentials and logarithms
```text
y = a·bˣ          exponential growth/decay
log_a(aˣ) = x     log undoes exponential
log(xy) = log x + log y
log(xⁿ) = n·log x
```

### Composition and inverses
```text
(f ∘ g)(x) = f(g(x))     inside function first
f⁻¹ undoes f:  f(f⁻¹(x)) = x
Linear inverse: undo operations in reverse order
```

### Graph transformations (from y = f(x))
```text
f(x) + k          translate up k (k < 0 → down)
f(x - h)          translate right h (h < 0 → left)
-f(x)             reflect in x-axis
f(-x)             reflect in y-axis
a·f(x)            vertical stretch (|a| > 1) or compression (0 < |a| < 1)
f(bx)             horizontal compression (|b| > 1) or stretch (0 < |b| < 1)
a·f(b(x - h)) + k combined transformation
```

### Piecewise, floor, ceiling
```text
Choose the rule whose interval contains the input
⌊x⌋ = greatest integer ≤ x    (floor — round down)
⌈x⌉ = smallest integer ≥ x     (ceiling — round up)
Step function: constant on each interval, jumps at boundaries
```

## CS Quick Reference

| Topic | CS object | Example |
|-------|-----------|---------|
| 3.1 | pixel / game position | `(x, y) = (640, 480)` |
| 3.2 | function / API handler | `def f(x): return 2*x + 1` |
| 3.3 | linear interpolation | `lerp(a, b, t) = a + t(b - a)` |
| 3.4 | trajectory / easing | parabolic arc under gravity |
| 3.6 | memory doubling | `2^n` bytes for n address bits |
| 3.7 | binary search depth | `O(log₂ n)` comparisons |
| 3.8 | encode/decode pipeline | `decode(encode(msg)) = msg` |
| 3.9 | sprite transform / normalise | `(x - min) / (max - min)` |
| 3.10 | pricing tier / pagination | `ceil(total / page_size)` |

## Folder Pass Gate
Before leaving this folder, you must:

- Pass every topic mastery test (85% overall, 100% on definitions).
- Retake any failed topic after writing a correction note in [[94 Review Sheets]].
- Explain at least three CS connections from [[03 Functions & Graphs - What This Unlocks in CS]].
- Complete [[03 Functions & Graphs - Cumulative Test]] with at least 85%.

## Key CS Unlocks
See [[03 Functions & Graphs - What This Unlocks in CS]].

## Forward Link
Next folder: [[04 MOC - Geometry]] — start with [[4.1 Lines Angles and Triangles]].
