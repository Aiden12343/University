# 03 Functions & Graphs - Cumulative Test

Use this after completing every topic in [[03 MOC - Functions and Graphs]].

Pass target: **85%** (at least 26 out of 30 marks).

> [!danger] Test conditions
> No notes. Paper only. Show one step per line. For piecewise questions, state the matching interval. For transformations, name the move before writing the formula.

---

## Section A — Vocabulary and concepts (6 marks)

1. **(1 mark)** Define *function* and give one example from programming.
2. **(1 mark)** What is the gradient of a line, and what does it measure?
3. **(1 mark)** State the relationship between exponentials and logarithms in one sentence.
4. **(1 mark)** Define *composition* of functions.
5. **(1 mark)** Define *translation* of a graph.
6. **(1 mark)** Define *piecewise rule*.

---

## Section B — Core graph and function skills (12 marks)

7. **(2 marks)** The points `(1, 3)` and `(4, 9)` lie on a straight line. Find the gradient and the equation in the form `y = mx + c`.

8. **(2 marks)** For `f(x) = x² - 4`, find the roots and the coordinates of the vertex.

9. **(2 marks)** Simplify: `log₂(8) + log₂(4)`. Evaluate `2³`.

10. **(2 marks)** If `f(x) = 2x + 1` and `g(x) = x - 3`, find `f(g(5))` and `g(f(5))`.

11. **(2 marks)** Find the inverse of `f(x) = 3x - 6`.

12. **(2 marks)** Describe the transformations from `y = x²` to `y = -(x + 2)² + 5`.

---

## Section C — Piecewise, floor, and mixed (6 marks)

13. **(2 marks)** For:

    ```text
    h(x) = {  x + 1,   if x < 0
           {  x²,      if 0 ≤ x ≤ 2
           {  6,       if x > 2
    ```

    find `h(-1)`, `h(1)`, and `h(3)`.

14. **(2 marks)** Evaluate `⌊-4.3⌋`, `⌈-4.3⌉`, and `⌈5001 / 4096⌉`.

15. **(2 marks)** A step function has `f(x) = 2` on `[0, 4)` and `f(x) = 5` on `[4, 8)`. Find `f(3.9)` and `f(4)`. Is the dot at `(4, 2)` open or closed?

---

## Section D — Computer science transfer (6 marks)

16. **(2 marks)** A data pipeline is `store(normalise(parse(raw)))`. State the execution order and explain what composition means here.

17. **(2 marks)** Exam scores range from 50 to 150. Write a formula mapping score `s` to the interval [0, 1]. Name the transformations used.

18. **(2 marks)** An API charges 3 credits per call for the first 200 calls, then 2 credits per call beyond 200.
    - Write `cost(n)` as a piecewise function.
    - Find `cost(350)`.

---

## Section E — Reflection (not marked; required)

- Which three topics felt strongest?
- Which three topics need review?
- Which topic connects most clearly to computer science?
- Which prerequisite from [[02 MOC - Algebra]] should you revisit if any question above failed?

---

## Marking checklist

| Section | Marks available | Your score |
|---------|-------------------|------------|
| A | 6 | |
| B | 12 | |
| C | 6 | |
| D | 6 | |
| **Total** | **30** | |

**Pass:** 26/30 or higher.

Decision:
- [ ] Pass — proceed to [[04 MOC - Geometry]].
- [ ] Review — list failed question numbers, write correction notes, retake weak topics.
- [ ] Restart — reread [[03 MOC - Functions and Graphs]] from the weakest prerequisite forward.

---

## Model solutions (for self-marking after attempt)

<details>
<summary>Click only after finishing the test</summary>

**A**
1. A rule mapping each input to exactly one output; e.g. `def square(n): return n * n`.
2. Gradient = change in y ÷ change in x; it measures the steepness or rate of change of a line.
3. Logarithms undo exponentials: if `b^x = y`, then `log_b(y) = x`.
4. Applying one function to the result of another: `(f ∘ g)(x) = f(g(x))`.
5. A shift of a graph horizontally or vertically without changing its shape.
6. A function defined by different formulas on different input intervals.

**B**
7. `m = (9 - 3)/(4 - 1) = 2`. Using point (1, 3): `3 = 2(1) + c` → `c = 1`. Equation: **`y = 2x + 1`**.
8. Roots: `x² - 4 = 0` → **`x = ±2`**. Vertex: **`(0, -4)`**.
9. `log₂(8) + log₂(4) = 3 + 2 = **5**`. `2³ = **8**`.
10. `g(5) = 2`, `f(g(5)) = f(2) = **5**`. `f(5) = 11`, `g(f(5)) = g(11) = **8**`.
11. `y = 3x - 6` → `x = (y + 6)/3`. **`f⁻¹(x) = (x + 6)/3`**.
12. **Left 2**, **reflection in x-axis**, **up 5**.

**C**
13. `h(-1) = **0**`, `h(1) = **1**`, `h(3) = **6**`.
14. `⌊-4.3⌋ = **-5**`, `⌈-4.3⌉ = **-4**`, `⌈5001/4096⌉ = **2**`.
15. `f(3.9) = **2**`, `f(4) = **5**`. Dot at (4, 2) is **open** (interval `[0, 4)` excludes 4).

**D**
16. Order: **`parse(raw)`**, then **`normalise(...)`**, then **`store(...)`**. Composition means each stage feeds its output as the next stage's input.
17. **`(s - 50) / 100`**. Translation (subtract 50), then vertical compression (divide by 100).
18. `cost(n) = { 3n, if n ≤ 200; 600 + 2(n - 200), if n > 200 }`. `cost(350) = 600 + 2(150) = **900** credits`.

</details>

Answers with full working: see individual topic answer sheets in [[93 Answers and Mark Schemes/93 Answers and Mark Schemes MOC]].
