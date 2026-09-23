# 03 Functions & Graphs - What This Unlocks in CS

Understand inputs, outputs, mappings, graph shapes, logs, exponentials, transformations, and piecewise behaviour.

Functions are the backbone of programming: every API endpoint, every data transform, and every graphics pipeline is a rule that maps inputs to outputs. This folder builds the fluency to read function notation, interpret graph shapes, chain operations, and model real systems where the rule changes with the input range.

## CS Connections

### Foundations (3.1–3.3)
- [[3.1 Coordinates and Axes]] — Coordinates describe pixels, graph nodes, game-world positions, and data points in scatter plots. Every `(x, y)` pair in a chart library or collision system uses the same grid structure you plot on paper.
- [[3.2 Function Notation and Mapping]] — Functions are a shared idea in maths, programming, APIs, and data pipelines. A Python `def transform(x): return x * 2` is the same input→output contract as `f(x) = 2x`; type signatures in languages like Haskell make this explicit.
- [[3.3 Linear Functions and Gradient]] — Linear models describe cost-per-unit pricing, constant-speed motion, linear interpolation between keyframes, and simple ML baselines. Gradient (rate of change) is the slope of a loss curve near its current point.

### Curves and growth (3.4–3.7)
- [[3.4 Quadratic Functions]] — Quadratics appear in optimisation parabolas, physics trajectories, camera easing curves, and least-squares error surfaces. Finding the vertex tells you the best or worst value in a bowl-shaped cost function.
- [[3.5 Polynomials]] — Polynomials underpin interpolation (Bezier and spline curves), error-correcting codes, and Taylor approximations in numerical libraries. Degree determines how many turns a curve can make.
- [[3.6 Exponential Functions]] — Population models, compound interest, memory doubling, recursion-tree blow-up, and ML training curves all grow (or decay) exponentially. Recognising exponential shape prevents underestimating resource needs.
- [[3.7 Logarithms]] — Big-O analysis (`O(log n)` for binary search), tree depth, entropy in information theory, and decibel scales all use logarithms to compress large ranges into readable numbers.

### Structure and behaviour (3.8–3.10)
- [[3.8 Inverse and Composite Functions]] — Encoding/decoding, encrypt/decrypt, serialise/parse, and middleware pipelines are composition and inverse chains. `decode(encode(data)) = data` is the identity check that proves a round trip works.
- [[3.9 Transformations of Graphs]] — Graphics engines apply translation (move), scale (stretch), and reflection (flip) to every drawable object. Data normalisation — `(x - min) / (max - min)` — uses the same translation and compression rules to map features into a standard range for machine learning.
- [[3.10 Piecewise and Step Functions]] — Pricing tiers, tax brackets, if/else chains, and guard clauses are piecewise rules in code. `Math.floor` and `Math.ceil` implement step-function rounding used in array binning, pagination, and memory-page allocation.

## How the Folder Fits Together

```text
Coordinates → Function notation → Linear/quadratic/polynomial shapes
    → Exponential growth ↔ Logarithmic scale
        → Compose and invert functions
            → Transform graphs (move, flip, stretch)
                → Piecewise rules and step functions (different rule per interval)
```

Each topic adds a way to describe how outputs depend on inputs — the same question every program, shader, and algorithm answers.

## Practical Unlocks After This Folder

After passing Module 03, you should be able to:

1. Read `f(g(x))` and trace execution order in a code pipeline.
2. Recognise exponential growth in logs and resource planning before it becomes a crisis.
3. Use `O(log n)` confidently because you understand what logarithms measure.
4. Normalise data or sprite coordinates using translation and scale.
5. Translate a pricing tier or validation rule into a correct if/else chain without gaps or overlaps.
6. Choose floor vs ceiling when converting continuous values to discrete counts (pages, buckets, indices).

## Next Step
After passing this folder, continue to [[04 MOC - Geometry]] (starting with [[4.1 Lines Angles and Triangles]]) and keep revisiting weak links through [[Progress Tracker]].
