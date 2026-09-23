#!/usr/bin/env python3
"""Topic content specifications for Module 07 Linear Algebra."""


def topic_shell(
    num, title, tags, prereqs, used_later, plain, everyday, terms, concepts, why, mistakes, cs_section,
    checkpoint, mini_quiz, pass_gate, backward, forward,
):
    nw = "\n".join(f"- [[{t}]] - {d}" for t, d in terms)
    return f"""# {num} {title}

Tags: {tags}

## Position in the Course
Prerequisites: {", ".join(f"[[{p}]]" for p in prereqs)}

Used later in: {", ".join(f"[[{u}]]" for u in used_later)}

Mastery threshold: 85% overall, and 100% on the New Words section.

> [!tip] How to study this note
> Read one concept, cover it, then explain it aloud in your own words. After each example, copy the problem onto paper and solve it again without looking. Matrices reward slow, labelled steps.

## Plain-English Idea
{plain}

> [!example] Everyday idea
{everyday}

## New Words
{nw}

You pass this topic only when you can define all five terms without looking.

{concepts}

## Why This Works
{why}

## Worked Examples
For fully worked solutions, use [[{num} {title} - Worked Examples]].

## Common Mistakes
{mistakes}

## Where This Shows Up in CS
{cs_section}

## Checkpoint Questions
{checkpoint}

## Mini-Quiz
{mini_quiz}

## Pass Gate
{pass_gate}

## Related Notes
Backward links: {", ".join(f"[[{b}]]" for b in backward)}

Forward links: {", ".join(f"[[{f}]]" for f in forward)}

Assessment links: [[{num} {title} - Worked Examples]], [[{num} {title} - Practice Questions]], [[{num} {title} - Mastery Test]], [[{num} {title} - Answers]]
"""


def assessment_header(title: str, theory: str, extra: str = "") -> str:
    return f"""# {title}

Theory note: [[{theory}]]
{extra}
"""

# Each entry: dict with keys matching emit_bundle parameters


def t71():
    num, title = "7.1", "Matrix Notation and Shape"
    concepts = r'''
## Concept 1 — A Matrix Is a Rectangular Table of Numbers
A [[matrix]] is a rectangular arrangement of numbers in [[row]]s and [[column]]s.

```text
A = | 1  2  3 |
    | 4  5  6 |
```

This matrix has **2 rows** and **3 columns**. Each number is an [[entry]].

> [!important] Read by row, then column
> Entry in row 2, column 1 is **4**. We write this as `a_21` or `A[1,0]` in zero-based code.

### Chunked Example
Question: How many rows and columns does this matrix have?

```text
| 7  0 |
| 3  9 |
| 1  2 |
```

Step 1: Count horizontal lines of numbers — there are **3 rows**.

Step 2: Count vertical columns — there are **2 columns**.

Answer: **3 × 2** matrix (3 rows, 2 columns).

## Concept 2 — Rows and Columns
A [[row]] runs **horizontally**. A [[column]] runs **vertically**.

```text
Row 1 of A:  [1, 2, 3]
Column 2 of A: | 2 |
               | 5 |
```

In [[4.8 Vectors Basics]], you met column vectors like `(3, 4)`. A column vector is a matrix with **one column**. A row vector has **one row**.

> [!example] Bridge from vectors
> The vector `(2, 5, 1)` as a column matrix:

```text
| 2 |
| 5 |
| 1 |
```

This is a **3 × 1** matrix — three rows, one column.

### Chunked Example
Question: Write the second row of

```text
B = | 0  4  1 |
    | 6  2  7 |
```

Step 1: Row 2 is the second horizontal line.

Step 2: Read left to right: `6, 2, 7`.

Answer: **Row 2 = [6, 2, 7]**.

## Concept 3 — Entries and Indexing
An [[entry]] is one number inside the matrix. Position matters.

Notation `a_ij` means row `i`, column `j` (starting at 1 in maths notes; code often starts at 0).

```text
| 1  2 |
| 3  4 |

a_11 = 1    a_12 = 2
a_21 = 3    a_22 = 4
```

> [!warning] Row first, column second
> `(row, column)` — not `(column, row)`. This matches spreadsheet and array conventions in many languages.

### Chunked Example
Question: Find `c_23` in

```text
C = | 5  1  8 |
    | 0  3  2 |
    | 9  4  6 |
```

Step 1: Row 2 is `| 0  3  2 |`.

Step 2: Column 3 of that row is **2**.

Answer: **c_23 = 2**.

## Concept 4 — Dimension m × n
The [[dimension]] of a matrix is written **rows × columns**, read "m by n".

```text
2 × 3  →  2 rows, 3 columns
1 × 4  →  row vector (one row, four columns)
4 × 1  →  column vector (four rows, one column)
3 × 3  →  square matrix (same number of rows and columns)
```

This order matches [[1.4 Multiplication and Times Tables]]: first number counts rows, second counts columns — like "3 rows of 4" giving a 3×4 grid.

> [!tip] Quick check
> A spreadsheet with 100 data rows and 5 columns stores a **100 × 5** matrix.

### Chunked Example
Question: State the dimension of

```text
| 1  0  0  0 |
```

Step 1: Count rows — **1**.

Step 2: Count columns — **4**.

Answer: **1 × 4** (a row vector).

## Concept 5 — Square and Special Shapes
A matrix is **square** when rows = columns.

```text
| 1  2 |
| 3  4 |   →  2 × 2 square

| 1  0  0 |
| 0  1  0 |
| 0  0  1 | →  3 × 3 identity shape (studied in [[7.4 Identity and Inverse Matrices]])
```

A **column matrix** (n × 1) stores the components of a vector from [[4.8 Vectors Basics]]. A **row matrix** (1 × n) is the same data written horizontally.

> [!important] Shape before operation
> You cannot add or combine matrices until you know their dimensions. Shape is the first thing to check — like checking units in [[1.12 Ratio Proportion and Units]].

### Chunked Example
Question: Is this matrix square?

```text
| 2  0  1 |
| 5  3  4 |
```

Step 1: Rows = 2, columns = 3.

Step 2: 2 ≠ 3, so it is not square.

Answer: **No** — it is **2 × 3**, not square.

## Concept 6 — Matrices as Data Tables
In computer science, a matrix often stores **data**, not just geometry.

```text
         Feature1  Feature2  Feature3
User A      1.2      0.0      3.1
User B      0.5      2.7      1.0
```

Each **row** can be one user. Each **column** can be one feature. This is exactly how many machine-learning datasets are stored before [[10.8 Machine Learning Vectors and Matrices]].

An image greyscale grid is also a matrix: each [[entry]] is a pixel brightness.

### Chunked Example
Question: A 640×480 greyscale image is stored as a matrix. What are the dimensions?

Step 1: Convention: rows × columns = height × width (or rows = height).

Step 2: 480 rows and 640 columns (or 640×480 depending on convention — always state which).

Answer: Typically **480 × 640** if rows are vertical pixel lines; check your library docs.
'''
    why = r'''Matrices extend [[4.8 Vectors Basics]] from single lists to **tables of numbers**. The row×column convention from [[1.4 Multiplication and Times Tables]] ("3 rows of 4") tells you how many entries fit in a grid and prevents off-by-one errors when indexing.

If you know the dimension, you know:
- how many entries in total (rows × columns, again from [[1.4 Multiplication and Times Tables]])
- whether the matrix can represent a vector (one row or one column)
- whether later operations like addition ([[7.2 Matrix Addition and Scalar Multiplication]]) are even defined'''
    mistakes = r'''- Swapping row and column counts (calling a 2×3 matrix "3×2").
- Using `(column, row)` order when the convention is `(row, column)`.
- Treating a single number as a matrix without stating it is 1×1.
- Forgetting that a column vector from [[4.8 Vectors Basics]] is an n×1 matrix, not 1×n.
- Assuming every matrix is square — most data tables are rectangular.

> [!failure] Mistake pattern
> If your index goes out of range, check whether you counted rows and columns from 0 or 1, and whether your language uses `[row][col]` order.'''
    cs = r'''Matrices appear as:

- **NumPy arrays** — `A.shape` returns `(rows, cols)`
- **Image buffers** — height × width grids of pixel values
- **Spreadsheets** — rows of records, columns of fields
- **Transformation stacks** — 4×4 matrices in graphics (later in [[7.8 Linear Transformations]])
- **Weight matrices** — in neural networks ([[10.9 Neural Network Maths]])

```python
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.shape)   # (2, 3) — 2 rows, 3 columns
print(A[1, 2])   # 6 — row index 1, column index 2
```'''
    checkpoint = r'''1. What is a matrix?
2. What is the difference between a row and a column?
3. What does "2 × 3" mean for a matrix?
4. Find the entry in row 2, column 1 of `[[1,2],[3,4]]` (using 1-based indexing).
5. How is a column vector from [[4.8 Vectors Basics]] written as a matrix?
6. Is a 5×1 matrix a row vector or column vector?
7. How many entries in a 4×7 matrix?
8. Why must you state row count before column count?'''
    mini = r'''1. Define [[matrix]] in your own words.
2. Define [[row]] in your own words.
3. Define [[column]] in your own words.
4. Define [[entry]] in your own words.
5. Define [[dimension]] in your own words.
6. State the dimensions of a 3-row, 2-column matrix.
7. Write `(4, 1, 7)` as a column matrix.
8. Extract row 1 from `[[0,5],[3,2]]`.
9. Is `[[1,0,0],[0,1,0]]` square? What size?
10. Name one CS object stored as a matrix.'''
    pg = f'''You may move to [[7.2 Matrix Addition and Scalar Multiplication]] only when you can:

- define every term in [[#New Words]]
- state rows × columns for any small matrix
- read and write entries using row/column indices
- connect column vectors from [[4.8 Vectors Basics]] to n×1 matrices
- answer at least 9 out of 10 mini-quiz questions correctly
- complete [[{num} {title} - Mastery Test]]'''
    topic = topic_shell(
        num, title,
        "#maths/linear-algebra #maths/matrices #cs/data-structures",
        ["6.12 Computability and Decidability", "4.8 Vectors Basics"],
        ["7.2 Matrix Addition and Scalar Multiplication", "10.8 Machine Learning Vectors and Matrices"],
        "A **matrix** is a rectangular grid of numbers arranged in **rows** (horizontal) and **columns** (vertical). Every number in the grid is an **entry**. The **dimension** tells you how many rows and columns there are, written rows×columns — for example, 2×3 means 2 rows and 3 columns.",
        "A spreadsheet with students as rows and test scores as columns is a matrix. Each cell is an entry. Saying the sheet is '30 by 5' means 30 rows and 5 columns — the same language as matrix dimension.",
        [
            ("matrix", "a rectangular array of numbers arranged in rows and columns."),
            ("row", "a horizontal line of entries across a matrix."),
            ("column", "a vertical line of entries down a matrix."),
            ("entry", "a single number at a specific row and column position in a matrix."),
            ("dimension", "the size of a matrix, written as rows × columns."),
        ],
        concepts, why, mistakes, cs, checkpoint, mini, pg,
        ["6.12 Computability and Decidability", "4.8 Vectors Basics", "1.4 Multiplication and Times Tables"],
        ["7.2 Matrix Addition and Scalar Multiplication", "7.3 Matrix Multiplication"],
    )
    we = assessment_header(f"{num} {title} - Worked Examples", f"{num} {title}") + r'''
Use these examples before attempting [[7.1 Matrix Notation and Shape - Practice Questions]].

> [!tip] How to use worked examples
> Read once, cover, then redo on paper. Label rows, columns, and every entry.

## Example 1 — State Dimensions
Question: Give the dimensions of

```text
M = | 1  0  2 |
    | 4  5  6 |
    | 7  8  9 |
```

### Step 1 — Count rows
There are 3 horizontal lines → **3 rows**.

### Step 2 — Count columns
Each row has 3 numbers → **3 columns**.

Answer: **3 × 3** (square matrix).

## Example 2 — Read an Entry
Question: Find `m_12` in matrix M above.

### Step 1 — Go to row 1
Row 1: `[1, 0, 2]`

### Step 2 — Take column 2
Column 2 entry: **0**

Answer: **m_12 = 0**

## Example 3 — Column Vector as Matrix
Question: Write the vector `(3, -1, 4)` from [[4.8 Vectors Basics]] as a column matrix.

### Step 1 — One component per row
```text
|  3 |
| -1 |
|  4 |
```

### Step 2 — State dimension
3 rows, 1 column.

Answer: **3 × 1** column matrix.

## Example 4 — Spot the Mistake
Question: A learner says a 4×2 matrix has 8 rows. Correct them.

### Step 1 — Parse dimension notation
4×2 means **4 rows**, **2 columns**.

### Step 2 — Identify error
The learner swapped or misread "rows" as total entries.

Answer: It has **4 rows** and **2 columns**, **8 entries** in total (4×2 from [[1.4 Multiplication and Times Tables]]).

## Example 5 — CS: NumPy Shape
Question: `A = np.array([[10, 20], [30, 40], [50, 60]])`. What is `A.shape`? What is `A[2, 0]`?

### Step 1 — Shape is (rows, cols)
3 rows, 2 columns → `(3, 2)`.

### Step 2 — Index [2, 0]
Row index 2 (third row), column 0 → **50**.

Answer: **shape (3, 2)**, **A[2, 0] = 50**.

## Example 6 — Total Entries
Question: How many entries in a 100×50 matrix?

### Step 1 — Multiply rows × columns
100 × 50 = 5000 (from [[1.4 Multiplication and Times Tables]]).

Answer: **5000 entries**.
'''
    pq = assessment_header(f"{num} {title} - Practice Questions", f"{num} {title}",
        "Answers: [[7.1 Matrix Notation and Shape - Answers]]\n\n> [!warning] Practice rule\n> Try every question on paper before checking answers.") + r'''
## A. Vocabulary
1. Define [[matrix]].
2. Define [[row]].
3. Define [[column]].
4. Define [[entry]].
5. Define [[dimension]].
6. How does a column vector from [[4.8 Vectors Basics]] relate to matrix shape?

## B. Core Skill — Dimensions and Entries
7. State dimensions: `[[1,2,3],[4,5,6]]`
8. State dimensions: `[[7],[8],[9]]`
9. State dimensions: `[[0,1]]`
10. Find entry (row 2, col 3) in `[[1,2,3],[4,5,6],[7,8,9]]` (1-based).
11. Write row 2 of `[[2,0],[5,1],[3,3]]`.
12. Write column 1 of `[[2,0],[5,1],[3,3]]`.
13. Is `[[1,0],[0,1]]` square? What size?
14. How many entries in a 6×4 matrix?

## C. Spot the Mistake
15. A learner calls `[[1,2],[3,4],[5,6]]` a 2×3 matrix. Fix the description.
16. A learner says `a_31` in a 2×2 matrix is valid. Explain the error.
17. A learner writes vector `(1,2)` as a 1×2 column matrix. Correct the shape.

## D. Mixed
18. Write `(5, 0, -2)` as a column matrix and state its dimension.
19. Which has more entries: 3×8 or 8×3?
20. List rows and columns for a spreadsheet with 200 users and 12 features (rows = users).

## E. Computer Science Transfer
21. If `A.shape == (4, 7)` in NumPy, how many rows and columns?
22. An RGB image is sometimes stored as height×width×3. How many rows if height=1080 and you flatten one channel to a matrix?
23. Explain why `[row][col]` indexing matches mathematical `a_ij` with 0-based adjustment.
24. Why does declaring matrix dimensions prevent buffer overruns?
25. Write one sentence linking matrices to [[10.8 Machine Learning Vectors and Matrices]].

Pass target: 85%. Definitions must be perfect.
'''
    mt = assessment_header(f"{num} {title} - Mastery Test", f"{num} {title}",
        "Answers: [[7.1 Matrix Notation and Shape - Answers]]\n\nPass mark: 85% (22/25). Section A: 100% required.\n\n> [!danger] Test condition\n> No notes. Paper only.") + r'''
## Section A — Definitions
1. What is a [[matrix]]?
2. What is a [[row]]?
3. What is a [[column]]?
4. What is an [[entry]]?
5. What is [[dimension]] (for a matrix)?

## Section B — Read and Write
6. Dimensions of `[[1,2],[3,4],[5,6]]`?
7. Entry (2,1) in `[[1,2,3],[4,5,6]]` (1-based)?
8. Write `(2,7,1)` as a column matrix.
9. Row 3 of `[[0,1],[2,3],[4,5]]`?
10. Entries in a 5×5 matrix?

## Section C — Spot the Mistake
11. Explain why calling a 3×1 matrix a "row vector" is wrong.
12. Fix: "A 2×4 matrix has 4 rows."
13. A learner indexes `[col][row]`. Why is this dangerous?

## Section D — Mixed
14. Is `[[1,2,3],[4,5,6]]` square?
15. How many columns in a 12×1 matrix?
16. Total entries in 20×30?
17. Column 2 of `[[8,1,0],[2,3,9]]`?

## Section E — CS Transfer
18. `B.shape = (100, 5)` — interpret.
19. Link column vectors to [[4.8 Vectors Basics]].
20. One CS use of matrices.
21. Why rows×cols matches [[1.4 Multiplication and Times Tables]]?
22. Difference between 7×1 and 1×7?
23. Why check shape before [[7.2 Matrix Addition and Scalar Multiplication]]?
24. Pixel grid 800 wide, 600 tall — one common matrix size statement.
25. One sentence: why this topic belongs in a CS maths course.

## Marking
Total: 25 marks. Pass: 22/25 and 5/5 on Section A.

Decision:
- [ ] Pass — move to [[7.2 Matrix Addition and Scalar Multiplication]].
- [ ] Review — [[94 Review Sheets]], retake tomorrow.
- [ ] Restart — reread [[7.1 Matrix Notation and Shape]], redo worked examples.
'''
    ans = assessment_header(f"{num} {title} - Answers", f"{num} {title}",
        "Practice: [[7.1 Matrix Notation and Shape - Practice Questions]]\nMastery: [[7.1 Matrix Notation and Shape - Mastery Test]]") + r'''
## Practice Answers
### A
1. Rectangular array of numbers in rows and columns.
2. Horizontal line of entries.
3. Vertical line of entries.
4. One number at a specific position.
5. Size rows×columns.
6. Column vector is n×1 (n rows, 1 column).

### B
7. 2×3  8. 3×1  9. 1×2  10. **4**  11. [5,1]  12. [2,5,3]ᵀ or column (2,5,3)
13. Yes, 2×2  14. **24**

### C
15. It is **3×2** (3 rows, 2 columns).
16. Row 3 does not exist in 2×2.
17. Column vector should be **2×1**: transpose (1,2) vertically.

### D
18. [[5],[0],[-2]] — 3×1  19. Same count: **24** each  20. 200 rows, 12 columns

### E
21. 4 rows, 7 columns  22. **1080 rows** (one channel as height×width)
23. i=j-1 for 1-based a_ij  24. Bounds match allocated memory

## Mastery Answers
1–5. Same as practice A.
6. 3×2  7. 4  8. [[2],[7],[1]]  9. [4,5]  10. 25
11. 3×1 has 3 rows, 1 col → column vector  12. **2 rows, 4 columns**
13. Swaps axes → wrong entry/wrong bounds  14. No  15. **1**  16. 600
17. [1,3]ᵀ or column (1,3,9)  18. 100×5 data table  19. n×1 stores components
20. Images, ML datasets, transforms  21. Grid counting  22. 7×1 column vs 1×7 row
23. Addition needs matching shape  24. **600×800** or 800×600 — state convention

## Mark Scheme
A: 5 (all required) | B–E: 20 total. Pass 22/25.
'''
    glo = {
        "matrix": ("A rectangular array of numbers arranged in rows and columns.", "[[4.8 Vectors Basics]]", "NumPy arrays and image buffers store multi-dimensional data as matrices."),
        "row": ("A horizontal line of entries across a matrix.", "[[7.1 Matrix Notation and Shape]]", "Each row of a CSV file imported into pandas becomes one matrix row."),
        "column": ("A vertical line of entries down a matrix.", "[[7.1 Matrix Notation and Shape]]", "Feature columns in scikit-learn's design matrix hold one attribute per column."),
        "entry": ("A single number at a specific row and column position in a matrix.", "[[7.1 Matrix Notation and Shape]]", "Accessing `A[i,j]` reads one matrix entry for computation."),
        "dimension": ("The size of a matrix, written as rows × columns.", "[[1.4 Multiplication and Times Tables]]", "Checking `.shape` before operations prevents dimension mismatch bugs in tensor code."),
    }
    return dict(num=num, title=title, topic_md=topic, we_md=we, pq_md=pq, mt_md=mt, ans_md=ans, glo=glo)


ALL_TOPICS = [t71()]
