# 02 Algebra - What This Unlocks in CS

Turn arithmetic into general rules using symbols, expressions, equations, and rearrangement.

Algebra is the language programs use to describe quantities that change. Every variable in code, every formula in a graphics shader, and every constraint in a type checker has an algebraic shape. This folder builds the fluency to read, simplify, solve, and rearrange those rules without guessing.

## CS Connections

### Foundations (2.1–2.4)
- [[2.1 Variables Expressions and Equations]] — Variables are the language of programs, formulas, and algorithms. A Python assignment `total = price * qty` is an equation in code form.
- [[2.2 Simplifying Expressions]] — Simplification makes code, formulas, and proofs easier to reason about. Reducing `2n + 3n` to `5n` mirrors removing redundant computation.
- [[2.3 Expanding Brackets]] — Compilers and symbolic tools expand expressions during optimisation. Expanding `(x+1)(x+2)` is the same structural step as multiplying out nested terms in a cost formula.
- [[2.4 Factorising]] — Factorising helps simplify algorithms and understand polynomial behaviour. Recognising `n^2 - 1 = (n-1)(n+1)` reveals when a loop condition can be split.

### Equations and constraints (2.5–2.8)
- [[2.5 Solving Linear Equations]] — Solving constraints appears in layout engines, type inference, and systems modelling. Finding `x` in `2x + 5 = 17` is the same task as solving for an unknown width under a fixed total.
- [[2.6 Rearranging Formulae]] — Rearranging formulas is needed when deriving performance, graphics, and ML equations. Making `t` the subject of `v = d/t` gives `t = d/v` for a timing benchmark.
- [[2.7 Inequalities]] — Program branches and validation rules are often inequalities. `if age >= 18` and `if memory < limit` are inequality guards in production code.
- [[2.8 Simultaneous Equations]] — Systems of equations appear in graphics, optimisation, and linear algebra. Two lines intersecting on screen, or two budget constraints that must both hold, are 2×2 systems.

### Powers, roots, and rational forms (2.9–2.11)
- [[2.9 Indices and Powers]] — Powers appear in exponential growth, binary sizes, and algorithm analysis. `n` bits represent `2^n` patterns; nested doubling loops grow like powers of 2.
- [[2.10 Surds and Roots]] — Exact roots occur in geometry, normalisation, and distance calculations. Distance `√(Δx² + Δy²)` should stay exact until the last display step to limit floating-point drift.
- [[2.11 Algebraic Fractions]] — Rational expressions appear in probability, calculus, and algorithmic formulas. Hit rate `h/(h+m)` is an algebraic fraction whose restriction `h+m ≠ 0` becomes a guard clause.

## How the Folder Fits Together

```text
Variables → Simplify/Expand/Factorise → Solve one equation
    → Rearrange formulas → Inequalities → Systems (2 equations)
        → Powers → Exact roots → Fractions with algebra
```

Each topic preserves meaning while changing form — the same principle compilers, proof assistants, and CAS tools use when transforming expressions.

## Practical Unlocks After This Folder

After passing Module 02, you should be able to:

1. Read a formula in code and identify the unknown you need to isolate.
2. Simplify before evaluating — fewer operations, fewer bugs.
3. Model two constraints at once and detect when they contradict.
4. Interpret `2^n` as bit capacity, memory scaling, or exponential work.
5. Keep surds exact in geometry problems before rounding for display.
6. Write rational metrics with correct domain restrictions (no divide-by-zero).

## Next Step
After passing this folder, continue to [[03 MOC - Graphs and Geometry]] (starting with [[3.1 Coordinates and Axes]]) and keep revisiting weak links through [[Progress Tracker]].
