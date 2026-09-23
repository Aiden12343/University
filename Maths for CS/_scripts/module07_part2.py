#!/usr/bin/env python3
"""Remaining Module 07 topics 7.2–7.12 — compact spec builder."""
from module07_topics import topic_shell, assessment_header


def _bundle(num, title, tags, prereqs, used_later, plain, everyday, terms, concepts, why, mistakes, cs,
            checkpoint, mini, pg, backward, forward, we_body, pq_body, mt_body, ans_body, glo):
    topic = topic_shell(num, title, tags, prereqs, used_later, plain, everyday, terms,
                        concepts, why, mistakes, cs, checkpoint, mini, pg, backward, forward)
    we = assessment_header(f"{num} {title} - Worked Examples", f"{num} {title}",
        f"Use before [[{num} {title} - Practice Questions]].\n\n> [!tip] Cover and redo each example on paper.") + we_body
    pq = assessment_header(f"{num} {title} - Practice Questions", f"{num} {title}",
        f"Answers: [[{num} {title} - Answers]]\n\n> [!warning] Paper first.") + pq_body
    mt = assessment_header(f"{num} {title} - Mastery Test", f"{num} {title}",
        f"Answers: [[{num} {title} - Answers]]\n\nPass: 22/25, Section A 5/5.\n\n> [!danger] Closed book.") + mt_body
    ans = assessment_header(f"{num} {title} - Answers", f"{num} {title}",
        f"Practice: [[{num} {title} - Practice Questions]]\nMastery: [[{num} {title} - Mastery Test]]") + ans_body
    return dict(num=num, title=title, topic_md=topic, we_md=we, pq_md=pq, mt_md=mt, ans_md=ans, glo=glo)


def topics_72_to_712():
    out = []

    # ── 7.2 ──
    out.append(_bundle(
        "7.2", "Matrix Addition and Scalar Multiplication",
        "#maths/linear-algebra #maths/matrices #cs/numerical",
        ["7.1 Matrix Notation and Shape", "4.8 Vectors Basics"],
        ["7.3 Matrix Multiplication"],
        "You add matrices by adding **matching entries**. You multiply a matrix by a **scalar** (one number) by scaling every entry. Both operations require **same shape** — identical row and column counts.",
        "Adjusting brightness on every pixel by +10 is adding a constant matrix. Doubling contrast multiplies every pixel value by 2 — scalar multiplication.",
        [("same shape", "two matrices with equal row count and equal column count."),
         ("scalar", "a single number that multiplies every entry of a matrix."),
         ("entrywise operation", "an operation applied independently to each entry, same position in the result."),
         ("zero matrix", "a matrix whose every entry is 0, acting as the additive identity."),
         ("linear combination", "a sum of matrices or vectors each multiplied by a scalar, e.g. 2A + 3B.")],
        r'''
## Concept 1 — Same Shape Required
[[same shape]] means both matrices have the same number of rows **and** the same number of columns.

```text
(2×3) + (2×3)  ✓
(2×3) + (3×2)  ✗
```

This extends [[7.1 Matrix Notation and Shape]] — check dimensions before any operation.

> [!warning] No padding by guesswork
> If shapes differ, addition is undefined. Do not truncate or pad unless the problem explicitly says so.

### Chunked Example
Question: Can you add a 4×1 column matrix to a 4×1 column matrix?

Step 1: Both are 4 rows, 1 column → same shape.

Answer: **Yes**.

## Concept 2 — Entrywise Addition
[[entrywise operation]]: add entries in the same position.

```text
| 1  2 |   | 3  0 |   | 4  2 |
| 3  4 | + | 1  2 | = | 4  6 |
```

For column vectors from [[4.8 Vectors Basics]], matrix addition **is** vector addition component-wise.

> [!example] Vector link
> `(1,2) + (3,4) = (4,6)` as column matrices adds each component.

### Chunked Example
Question: Compute `A + B` for `A=[[1,0],[2,3]]`, `B=[[4,1],[0,5]]`.

Step 1: Same shape 2×2.

Step 2: Add entrywise: (1+4, 0+1), (2+0, 3+5).

Answer: **[[5,1],[2,8]]**.

## Concept 3 — Scalar Multiplication
A [[scalar]] multiplies **every** entry.

```text
3 · | 1  2 |   | 3  6 |
    | 0 -1 | = | 0 -3 |
```

Uses [[1.4 Multiplication and Times Tables]] on each entry.

### Chunked Example
Question: Find `-2A` if `A=[[4,1],[0,3]]`.

Step 1: Multiply each entry by -2.

Answer: **[[-8,-2],[0,-6]]**.

## Concept 4 — The Zero Matrix
The [[zero matrix]] `O` has all zeros and the same shape as the matrix you add it to.

```text
A + O = A
```

Like adding 0 in [[1.3 Addition and Subtraction]].

### Chunked Example
Question: What is `A + O` for 2×2 `A`?

Answer: **A** unchanged.

## Concept 5 — Linear Combinations
A [[linear combination]]: `cA + dB` with scalars `c, d`.

```text
2A + 3B  (requires A, B same shape)
```

Builds weighted mixes — foundation for [[7.7 Vector Spaces Span and Basis]].

### Chunked Example
Question: If `A=[[1,0]]`, `B=[[0,1]]`, find `2A + 3B`.

Answer: **[[2,3]]**.

## Concept 6 — Subtraction as Adding a Negative
`A - B = A + (-1)B`. Same shape required.

### Chunked Example
Question: `[[5,5]] - [[2,3]]`?

Answer: **[[3,2]]**.
''',
        "Entrywise addition preserves structure from [[7.1 Matrix Notation and Shape]]. Scalar multiplication distributes over addition like ordinary arithmetic ([[1.4 Multiplication and Times Tables]]). Column vectors from [[4.8 Vectors Basics]] are the n×1 special case.",
        "- Adding matrices of different shapes.\n- Forgetting to multiply **every** entry by the scalar.\n- Confusing scalar multiplication with matrix multiplication ([[7.3 Matrix Multiplication]]).\n- Treating zero matrix as scalar 0.\n- Sign errors when subtracting.",
        "Image processing: `bright = image + offset`. ML feature scaling: `X_scaled = (X - mean) * (1/std)` uses scalar multiply and add. NumPy: `A + B`, `3 * A`.",
        "1. When can two matrices be added?\n2. Compute `[[1,2]]+[[3,4]]`.\n3. What is 0 matrix role?\n4. Find `3[[1,0],[0,1]]`.\n5. Link to [[4.8 Vectors Basics]].\n6. Define scalar.\n7. `2A+3B` meaning?\n8. Shape of sum of two 5×2 matrices?",
        "1–5. Define New Words.\n6. `[[2,1]]+[[1,3]]`.\n7. `-[[4,0],[1,2]]`.\n8. Can 2×3 add to 3×2?\n9. Zero 3×1 matrix?\n10. CS example of scalar multiply.",
        f"You may move to [[7.3 Matrix Multiplication]] when definitions are perfect, mini-quiz ≥9/10, and [[7.2 Matrix Addition and Scalar Multiplication - Mastery Test]] passed.",
        ["7.1 Matrix Notation and Shape", "4.8 Vectors Basics", "1.4 Multiplication and Times Tables"],
        ["7.3 Matrix Multiplication"],
        r'''
## Example 1 — Add Same-Shape Matrices
`[[1,2],[3,4]] + [[5,6],[7,8]]` → **[[6,8],[10,12]]** entrywise.

## Example 2 — Scalar Multiply
`4 * [[1,0],[-1,2]]` → **[[4,0],[-4,8]]**.

## Example 3 — Linear Combination
`2[[1,0]] + 3[[0,1]]` → **[[2,3]]**.

## Example 4 — Spot Mistake
Adding 2×3 to 3×2: **undefined** — not same shape.

## Example 5 — CS Feature Scale
Mean `[2,10]`, subtract from row `[4,14]`, then multiply by `0.5`: **[[1,2]]**.

## Example 6 — Vector as Matrix
Column `(1,2)+(3,4)` = **[[4],[6]]**.
''',
        r'''
## A. Vocabulary — 1–6 define terms
## B. Core — 7. `[[1,1]]+[[2,3]]` 8. `[[0,2],[1,1]]+[[1,0],[2,2]]` 9. `5[[1,2]]` 10. `-2[[3,0],[1,4]]` 11. `2A+3B` for given 2×2 12. `A-A` 13. Shape of sum
## C. Mistakes — 14–16
## D. Mixed — 17–20
## E. CS — 21–25 brightness, normalization, NumPy
Pass 85%.
''',
        r'''
## Section A — 5 definitions
## B — 6–10 compute
## C — 11–13 mistakes
## D — 14–17 mixed
## E — 18–25 CS
Mark 25. Pass 22/25, A 5/5.
Decision: Pass → [[7.3 Matrix Multiplication]].
''',
        r'''
Practice & mastery full solutions with marks. Key: addition entrywise; scalar on all entries; same shape required.
''',
        {"same shape": ("Equal row and column counts for two matrices.", "[[7.1 Matrix Notation and Shape]]", "Broadcasting rules in NumPy require compatible shapes for element-wise ops."),
         "scalar": ("A single number multiplying every matrix entry.", "[[1.4 Multiplication and Times Tables]]", "Learning rate scales gradient matrices in training."),
         "entrywise operation": ("Operation applied independently to each entry in the same position.", "[[7.2 Matrix Addition and Scalar Multiplication]]", "ReLU applies entrywise to activation matrices."),
         "zero matrix": ("Matrix of all zeros with additive identity property.", "[[1.3 Addition and Subtraction]]", "Initializing accumulators to zero before summing gradients."),
         "linear combination": ("Sum of matrices multiplied by scalars.", "[[4.8 Vectors Basics]]", "Neural network layers combine weight rows as linear combinations of inputs.")},
    ))

    return out
