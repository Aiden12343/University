# Maths for CS — Curriculum Dependency Matrix

> **Purpose:** Complete map of every module → topic → breadcrumb → prerequisite dependency.
> Every term used in any topic must trace back to 1.1 Counting and Number Sense with no leaps.

---

## How to Read This Document

Each module section contains:
1. **Overview** — module role, difficulty, threshold concept, prerequisite modules
2. **Topic Map** — table of every topic with its prerequisites, breadcrumb count, new word count, and difficulty
3. **Breadcrumb Detail** — for each topic, every concept/breadcrumb with the new terms it introduces and where those terms first appeared

**Key:**
- **Difficulty:** E (Easy), M (Medium), H (Hard), T (Threshold — the idea that stumps most students)
- **Prerequisite refs:** `Module.Topic.Breadcrumb` (e.g. `01.01.01`)
- **Chain status:** ✅ (clean chain), ⚠️ (minor gap), ❌ (broken chain — term used before defined)

---

## 00 — Glossary & Start Here

**Role:** Navigation, rules, diagnostic, and term definitions.

| File | Contents |
|------|----------|
| 00 Start Here/How To Use This Course.md | Daily study loop, printing, Obsidian links |
| 00 Start Here/Learning Rules.md | Progression rule, pass marks, failure rule |
| 00 Start Here/Progress Tracker.md | Master checklist of all 130 topics |
| 00 Start Here/Diagnostic Test - Absolute Basics.md | 12-question pre-test |
| 00 Start Here/Course Roadmap - 5 Years.md | Year 0 through Year 4-5 plans |
| 00 Glossary/Glossary MOC.md | Index to 7 category glossaries |
| 00 Glossary/Glossary - All Terms Index.md | Index to 607 individual term notes |
| 00 Glossary/Terms/*.md | 607 individual term definition files (currently placeholder text) |

**Status:** ⚠️ Glossary term files are empty placeholders ("Add your own definition after studying it").

---

## 01 — Number Foundations

**Role:** The absolute starting point. From counting objects to arithmetic fluency.
**Difficulty:** E–M (foundational, needs to be thorough)
**Threshold concept:** Place value as positional notation (1.2)
**Prerequisite modules:** None
**Feeds into:** 02 Algebra, 03 Functions, 05 Sets, 06 Discrete, 07 Linear Algebra, 10 CS Applications

### 01 Topic Map

| # | Topic | Prereq Topics | Breadcrumbs | New Words | Difficulty |
|---|-------|---------------|-------------|-----------|------------|
| 1.1 | Counting and Number Sense | None | 6 | 5 | E |
| 1.2 | Place Value and Number Lines | 1.1 | 7 | 5 | E |
| 1.3 | Addition and Subtraction | 1.2 | 10 | 5 | E |
| 1.4 | Multiplication and Times Tables | 1.3 | 8 | 5 | E |
| 1.5 | Division and Remainders | 1.4 | — | 5 | M |
| 1.6 | Fractions | 1.5 | — | 5 | M |
| 1.7 | Decimals and Percentages | 1.6 | — | 5 | M |
| 1.8 | Negative Numbers | 1.3 | — | 5 | M |
| 1.9 | Order of Operations | 1.4, 1.8 | — | 5 | M |
| 1.10 | Factors Multiples and Primes | 1.4, 1.5 | — | 5 | M |
| 1.11 | HCF and LCM | 1.10 | — | 5 | M |
| 1.12 | Ratio Proportion and Units | 1.6, 1.7 | — | 5 | M |
| 1.13 | Estimation and Error Checking | 1.9 | — | 5 | E |

### 01 Breadcrumb Detail (Topics 1.1–1.4, the critical opening chain)

#### 1.1 Counting and Number Sense

| # | Breadcrumb | New Terms | First Defined In | CS Link |
|---|-----------|-----------|-----------------|---------|
| 1 | Numbers Can Name Quantity | counting, quantity | 01.01.01 ✅ | Array size |
| 2 | One-to-One Matching | one-to-one matching | 01.01.02 ✅ | Loop counters |
| 3 | Zero Means None | zero as a number | 01.01.03 ✅ | Zero-indexing |
| 4 | Bigger, Smaller, and Equal | <, >, = | 01.01.04 ✅ | Comparison ops |
| 5 | Number Lines Show Order | number line | 01.01.05 ✅ | Memory addresses |
| 6 | Counting On | (uses prior terms) | 01.01.06 ✅ | Increment |

#### 1.2 Place Value and Number Lines

| # | Breadcrumb | New Terms | First Defined In | CS Link |
|---|-----------|-----------|-----------------|---------|
| 1 | Digits Are Symbols | digits, 0-9 | 01.02.01 ✅ | Character encoding |
| 2 | Position Gives Value | place value, ones/tens/hundreds | 01.02.02 ✅ | Memory layout |
| 3 | Expanded Form | expanded form | 01.02.03 ✅ | Bit fields |
| 4 | Comparing Large Numbers | comparing by digit length | 01.02.04 ✅ | String comparison |
| 5 | Number Lines Preserve Order | (number line from 1.1) | 01.01.05 → | Coordinate systems |
| 6 | Rounding to Landmarks | rounding, landmarks | 01.02.06 ✅ | Quantization |
| 7 | Why Computers Care About Position | binary hint | 01.02.07 ✅ | Base-2 |

#### 1.3 Addition and Subtraction

| # | Breadcrumb | New Terms | First Defined In | CS Link |
|---|-----------|-----------|-----------------|---------|
| 1 | Addition as Combining | addition, sum, total | 01.03.01 ✅ | Accumulator |
| 2 | Subtraction as Taking Away | subtraction, difference | 01.03.02 ✅ | Decrement |
| 3 | Subtraction as Difference | (uses difference) | 01.03.03 ✅ | Distance metric |
| 4 | Addition on a Number Line | (number line from 1.1) | 01.01.05 → | Offset |
| 5 | Subtraction on a Number Line | (number line from 1.1) | 01.01.05 → | Offset back |
| 6 | Column Addition Without Carrying | column alignment | 01.03.06 ✅ | Binary addition |
| 7 | Column Addition With Carrying | carry, regroup | 01.03.07 ✅ | Carry flag |
| 8 | Column Subtraction Without Borrowing | (uses column alignment) | 01.03.08 ✅ | Subtraction circuit |
| 9 | Column Subtraction With Borrowing | borrow, regroup | 01.03.09 ✅ | Borrow in ALU |
| 10 | Checking with Inverse Operations | inverse operations | 01.03.10 ✅ | Unit tests |

#### 1.4 Multiplication and Times Tables

| # | Breadcrumb | New Terms | First Defined In | CS Link |
|---|-----------|-----------|-----------------|---------|
| 1 | Multiplication as Equal Groups | multiplication, equal groups | 01.04.01 ✅ | Batch processing |
| 2 | Multiplication as Repeated Addition | (uses addition from 1.3) | 01.03.01 → | Loop unrolling |
| 3 | Multiplication as Arrays | array (grid), rows, columns | 01.04.03 ✅ | 2D array |
| 4 | Commutativity | commutative | 01.04.04 ✅ | Symmetric ops |
| 5 | Times Tables Are Stored Facts | times tables | 01.04.05 ✅ | Lookup table |
| 6 | Multiplying by 10 and 100 | scaling by place value | 01.04.06 ✅ | Bit shift |
| 7 | Scaling | scale factor | 01.04.07 ✅ | Image resize |
| 8 | Nested Loops | nested loops | 01.04.08 ✅ | O(n²) |

### 01 Dependency Chain Analysis

**Chain quality:** ✅ Excellent. Topics 1.1→1.2→1.3→1.4 build perfectly on each other.
**Gaps found:** None within the chain. Each term is defined before use.

**Recommended breadcrumb counts:**
- 1.1 Counting: 6 ✓ (fine)
- 1.2 Place Value: 7 ✓ (fine)
- 1.3 Addition/Subtraction: 10 ✓ (appropriate for foundational skill)
- 1.4 Multiplication: 8 ✓ (fine)
- 1.5–1.13: Need to verify counts but 5–7 each expected

---

## 02 — Algebra

**Role:** Turn arithmetic into general rules using symbols.
**Difficulty:** E–M
**Threshold concept:** Variable as placeholder (2.1)
**Prerequisite modules:** 01 (Number Foundations)
**Feeds into:** 03 Functions, 04 Geometry, 06 Discrete, 07 Linear Algebra

### 02 Topic Map

| # | Topic | Prereq Topics | Breadcrumbs | New Words | Difficulty |
|---|-------|---------------|-------------|-----------|------------|
| 2.1 | Variables Expressions and Equations | 1.13, 1.3 | — | 5 | E |
| 2.2 | Simplifying Expressions | 2.1 | — | 5 | E |
| 2.3 | Expanding Brackets | 2.2 | — | 5 | M |
| 2.4 | Factorising | 2.3 | — | 5 | M |
| 2.5 | Solving Linear Equations | 2.1 | — | 5 | M |
| 2.6 | Rearranging Formulae | 2.5 | — | 5 | M |
| 2.7 | Inequalities | 2.5 | — | 5 | M |
| 2.8 | Simultaneous Equations | 2.5, 3.3 | — | 5 | M |
| 2.9 | Indices and Powers | 1.4 | — | 5 | M |
| 2.10 | Surds and Roots | 2.9 | — | 5 | M |
| 2.11 | Algebraic Fractions | 2.4, 2.2 | — | 5 | H |

### 02 Dependency Chain Analysis

**Chain quality:** ✅ Good. Builds on 01. However, 2.1 lists prerequisite [[1.13 Estimation and Error Checking]] which is a later topic in Module 01 — this may be an incorrect link; the true prerequisite is 1.3 Addition and Subtraction.

**Breaks found:**
- ⚠️ 2.1 lists "Prerequisites: 1.13, 1.3" but 1.13 (Estimation) is not needed for variables. The real chain is 1.3 → 2.1.
- ⚠️ 2.8 lists prerequisite [[3.3 Linear Functions]] — this creates a cross-module dependency (02 needs 03). This creates a cycle if 03 also needs 02. Solution: 2.8 can introduce linear graphs standalone, or be taught *after* 3.3.

**Recommended breadcrumb counts:**
- 2.1 Variables: 5 breadcrumbs
- 2.5 Solving Equations: 8 breadcrumbs (critical skill)
- 2.8 Simultaneous Equations: 8 breadcrumbs (harder concept)
- All others: 5-6 breadcrumbs each

---

## 03 — Functions & Graphs

**Role:** Inputs, outputs, mappings, graph shapes, logs, exponentials.
**Difficulty:** M
**Threshold concept:** Function as a mapping rule (3.2)
**Prerequisite modules:** 01 (Number Foundations), 02 (Algebra)
**Feeds into:** 04 Geometry, 05 Sets & Logic, 06 Discrete, 07 Linear Algebra, 09 Calculus, 10 CS Applications

### 03 Topic Map

| # | Topic | Prereq Topics | Breadcrumbs | New Words | Difficulty |
|---|-------|---------------|-------------|-----------|------------|
| 3.1 | Coordinates and Axes | 1.2, 1.8 | — | 5 | E |
| 3.2 | Function Notation and Mapping | 2.1 | — | 5 | M |
| 3.3 | Linear Functions and Gradient | 3.1, 3.2 | — | 5 | M |
| 3.4 | Quadratic Functions | 3.3, 2.9 | — | 5 | M |
| 3.5 | Polynomials | 3.4, 2.9 | — | 5 | M |
| 3.6 | Exponential Functions | 3.5, 2.9 | — | 5 | M |
| 3.7 | Logarithms | 3.6 | — | 5 | H |
| 3.8 | Inverse and Composite Functions | 3.7 | — | 5 | H |
| 3.9 | Transformations of Graphs | 3.3, 3.4 | — | 5 | M |
| 3.10 | Piecewise and Step Functions | 3.2 | — | 5 | M |

### 03 Dependency Chain Analysis

**Chain quality:** ✅ Good chain. 3.1→3.2→3.3→...→3.10 flows well.

**Breaks found:**
- ⚠️ 3.7 Logarithms lists prerequisite 3.6 Exponential Functions — this is correct, but logarithms is a **threshold concept** that needs more breadcrumbs than currently exist (likely 5).

**Recommended breadcrumb counts:**
- 3.1 Coordinates: 5 breadcrumbs
- 3.2 Function Notation: 7 breadcrumbs (abstract concept needs care)
- 3.3 Linear Functions: 6 breadcrumbs
- 3.7 Logarithms: **10 breadcrumbs** (hardest topic in module — needs drip-feeding)
- 3.8 Inverse Functions: 7 breadcrumbs
- All others: 5-6 each

---

## 04 — Geometry & Trigonometry

**Role:** Shape, angle, triangle, circle, vector, and trigonometric reasoning.
**Difficulty:** M
**Threshold concept:** The unit circle linking ratios to coordinates (4.6)
**Prerequisite modules:** 01 (Number Foundations), 02 (Algebra), 03 (Functions)
**Feeds into:** 07 Linear Algebra, 10 CS Applications

### 04 Topic Map

| # | Topic | Prereq Topics | Breadcrumbs | New Words | Difficulty |
|---|-------|---------------|-------------|-----------|------------|
| 4.1 | Lines Angles and Triangles | 1.1, 1.2, 1.3 | — | 5 | E |
| 4.2 | Perimeter Area and Volume | 1.4, 1.6 | — | 5 | E |
| 4.3 | Circle Geometry | 4.1 | — | 5 | M |
| 4.4 | Pythagoras Theorem | 4.1, 2.9, 2.10 | — | 5 | M |
| 4.5 | Trig Ratios SOHCAHTOA | 4.4, 3.2 | — | 5 | H |
| 4.6 | Unit Circle | 4.5, 4.7 | — | 5 | T |
| 4.7 | Radians and Degrees | 4.1, 3.2 | — | 5 | M |
| 4.8 | Vectors Basics | 4.4, 4.5, 4.7, 3.1 | — | 5 | M |
| 4.9 | Dot Product and Projection | 4.8, 4.5 | — | 5 | H |
| 4.10 | Geometry for Computer Graphics | 4.8, 4.9 | — | 5 | M |

### 04 Dependency Chain Analysis

**Chain quality:** ⚠️ **Potential circular dependency:** 4.6 Unit Circle lists prerequisite 4.7 Radians — but 4.7 Radians is a separate topic. If 4.6 needs radians and 4.7 introduces them, this is fine (4.7 should come before 4.6 in study order, not topic number order).

**Breaks found:**
- ⚠️ 4.6 Unit Circle → needs 4.7 Radians first. Topic numbers suggest 4.7 comes after 4.6, but the actual dependency is 4.7→4.6. Study order should be: 4.5 → 4.7 → 4.6 → 4.8.
- ⚠️ 4.8 needs 3.1 (Coordinates), 4.4 (Pythagoras), 4.5 (Trig Ratios), 4.7 (Radians) — heavy cross-module dependency.

**Recommended breadcrumb counts:**
- 4.5 Trig Ratios: **10 breadcrumbs** (first encounter with sin/cos/tan — needs extensive drip-feeding)
- 4.6 Unit Circle: **12 breadcrumbs** (threshold concept — connect ratios to coordinates)
- 4.8 Vectors: 8 breadcrumbs
- 4.9 Dot Product: 7 breadcrumbs
- All others: 5-6 each

---

## 05 — Sets, Logic & Proof

**Role:** The language of rigorous CS reasoning.
**Difficulty:** M–H
**Threshold concept:** Proof by Induction (5.11); Cantor's Diagonal Argument (5.4)
**Prerequisite modules:** 01 (Number Foundations), 02 (Algebra)
**Feeds into:** 06 Discrete Mathematics, 07 Linear Algebra, 10 CS Applications, 11 Advanced

### 05 Topic Map

| # | Topic | Prereq Topics | Breadcrumbs | New Words | Difficulty |
|---|-------|---------------|-------------|-----------|------------|
| 5.1 | Set Theory Basics | 1.1, 1.2 | — | 5 | M |
| 5.2 | Subsets Unions and Intersections | 5.1 | — | 5 | M |
| 5.3 | Venn Diagrams and Cardinality | 5.2 | — | 5 | M |
| 5.4 | Infinity and Countability | 5.3 | — | 5 | T |
| 5.5 | Propositional Logic | 1.1, 5.1 | — | 5 | M |
| 5.6 | Truth Tables | 5.5 | — | 5 | M |
| 5.7 | Implication and Equivalence | 5.6 | — | 5 | M |
| 5.8 | Boolean Algebra and De Morgan Laws | 5.7 | — | 5 | M |
| 5.9 | Direct Proof and Counterexample | 5.7 | — | 5 | M |
| 5.10 | Proof by Contradiction and Contrapositive | 5.9 | — | 5 | H |
| 5.11 | Proof by Induction | 5.9, 6.1 | — | 5 | T |

### 05 Dependency Chain Analysis

**Chain quality:** ⚠️ **5.11 lists prerequisite 6.1 Sequences** — but 6.1 is in Module 06 (Discrete Maths), which comes *after* 05 in numbering. This creates a cross-module forward reference. The student hasn't studied 06 yet.

**Breaks found:**
- ❌ 5.11 Proof by Induction needs sequences (6.1) which hasn't been taught yet. Need to either: (a) move sequences to Module 05, or (b) introduce sequences informally within 5.11's own breadcrumbs, or (c) reorder so 06 comes before 05.
- ⚠️ 5.4 Infinity and Countability — introduces Cantor's diagonal argument. This is a **paradox topic** that needs extensive drip-feeding (12+ breadcrumbs recommended).
- ⚠️ 5.5 Propositional Logic lists prerequisite "1.1 Counting" — this is too thin. Need to add 2.5 (Equations) or 2.7 (Inequalities) as well.

**Recommended breadcrumb counts:**
- 5.4 Infinity & Countability: **12 breadcrumbs** (drip-feed the diagonal argument)
- 5.10 Proof by Contradiction: **8 breadcrumbs** (counterintuitive)
- 5.11 Proof by Induction: **10 breadcrumbs** (threshold concept)
- All others: 5-6 each

---

## 06 — Discrete Mathematics

**Role:** Countable structures — sequences, modular arithmetic, combinatorics, graphs, automata.
**Difficulty:** M–H
**Threshold concept:** Recurrence relations (6.6); Formal languages (6.11)
**Prerequisite modules:** 01 (Number Foundations), 02 (Algebra), 03 (Functions), 05 (Sets & Logic)
**Feeds into:** 07 Linear Algebra, 08 Probability, 10 CS Applications, 11 Advanced

### 06 Topic Map

| # | Topic | Prereq Topics | Breadcrumbs | New Words | Difficulty |
|---|-------|---------------|-------------|-----------|------------|
| 6.1 | Sequences and Series | 1.1, 1.4, 2.2 | — | 5 | M |
| 6.2 | Summation and Product Notation | 6.1 | — | 5 | M |
| 6.3 | Modular Arithmetic | 1.5, 1.4, 2.7 | — | 5 | M |
| 6.4 | Counting Rules | 5.1 | — | 5 | M |
| 6.5 | Permutations and Combinations | 6.4 | — | 5 | M |
| 6.6 | Recurrence Relations | 6.1, 6.2 | — | 5 | H |
| 6.7 | Graph Theory Basics | 5.1 | — | 5 | M |
| 6.8 | Trees and Traversal | 6.7 | — | 5 | M |
| 6.9 | Graph Algorithms BFS DFS Dijkstra | 6.8 | — | 5 | H |
| 6.10 | Relations and Functions on Sets | 5.1, 5.7 | — | 5 | M |
| 6.11 | Formal Languages and Automata | 5.5, 6.7 | — | 5 | T |
| 6.12 | Computability and Decidability | 6.11 | — | 5 | T |

### 06 Dependency Chain Analysis

**Chain quality:** ⚠️ Several issues.

**Breaks found:**
- ⚠️ 6.3 Modular Arithmetic lists prerequisite 2.7 (Inequalities) — inequalities are NOT needed for modular arithmetic. The true prerequisite is 1.5 Division and Remainders. This is a **wrong link**.
- ⚠️ 6.3 also uses 1.4 (Multiplication) — correct, but the link to 2.7 is misleading.
- ❌ 6.9 Graph Algorithms depends on 6.8 Trees — but Dijkstra's algorithm was originally in Module 11 (11.3). There's duplication/overlap between 6.9 and 11.3-11.4.
- ⚠️ 6.12 Computability and Decidability depends on 6.11 Formal Languages — chain is correct but this is very abstract and needs many breadcrumbs.

**Recommended breadcrumb counts:**
- 6.3 Modular Arithmetic: **8 breadcrumbs** (many applications, confusion about mod/remainder)
- 6.6 Recurrence Relations: **10 breadcrumbs** (threshold concept)
- 6.9 Graph Algorithms: **10 breadcrumbs** (BFS, DFS, Dijkstra each need their own breadcrumb)
- 6.11 Formal Languages: **12 breadcrumbs** (DFA, NFA, regex each step by step)
- 6.12 Computability: **8 breadcrumbs** (halting problem needs careful treatment)
- All others: 5-6 each

---

## 07 — Linear Algebra

**Role:** Vector and matrix reasoning for graphics, ML, numerical computing.
**Difficulty:** M–H
**Threshold concept:** Matrix multiplication (7.3); Eigenvalues (7.9)
**Prerequisite modules:** 01 (Number Foundations), 03 (Functions), 04 (Vectors from Geometry), 05 (Sets)
**Feeds into:** 08 Probability, 09 Calculus, 10 CS Applications, 11 Advanced

### 07 Topic Map

| # | Topic | Prereq Topics | Concepts | New Words | Difficulty |
|---|-------|---------------|----------|-----------|------------|
| 7.1 | Matrix Notation and Shape | 1.1, 1.4, 5.3 | 5 | 5 | E |
| 7.2 | Matrix Addition and Scalar Multiplication | 7.1, 1.3, 1.4 | 4 | 5 | E |
| 7.3 | Matrix Multiplication | 7.2, 7.1, 1.4 | 5 | 5 | T |
| 7.4 | Identity and Inverse Matrices | 7.3, 1.10 | 4 | 5 | M |
| 7.5 | Determinants | 7.4, 7.3 | 4 | 5 | M |
| 7.6 | Solving Linear Systems with Matrices | 7.4, 7.5, 3.2 | 5 | 5 | M |
| 7.7 | Vector Spaces Span and Basis | 5.1, 5.3, 7.1 | 5 | 5 | H |
| 7.8 | Linear Transformations | 7.3, 7.7, 4.8 | 4 | 5 | H |
| 7.9 | Eigenvalues and Eigenvectors | 7.8, 7.5, 7.3 | 4 | 5 | T |
| 7.10 | Orthogonality and Least Squares | 7.7, 7.3, 4.8 | 4 | 5 | H |
| 7.11 | Matrix Decompositions LU QR SVD | 7.6, 7.9, 7.10 | 4 | 5 | T |
| 7.12 | Numerical Stability in Linear Algebra | 7.11, 7.6 | 5 | 5 | H |

### 07 Dependency Chain Analysis

**Chain quality:** ⚠️ Several broken or incorrect prerequisite references.

**Breaks found:**
- ❌ 7.1 lists prerequisite [[5.3 Tuples and Vectors]] — but 5.3 is "Venn Diagrams and Cardinality" in the actual vault. "Tuples and Vectors" does not exist as a topic. **Term used before defined.**
- ❌ 7.6 lists prerequisite [[3.2 Solving Equations]] — but 3.2 is "Function Notation and Mapping", not "Solving Equations". Wrong reference.
- ❌ 7.7 lists prerequisite [[5.3 Tuples and Vectors]] — same as 7.1, non-existent topic.
- ❌ 7.9 forward-links to [[10.10 Dimensionality Reduction PCA]] — but 10.10 is "Graphs in Networks and AI Search" in the actual vault.
- ❌ 7.11 uses "SVD" in New Words and Concepts but SVD hasn't been defined before 7.11. It's introduced within the topic — fine for internal use, but 5 new words might not be enough for 4 decomposition types.
- ⚠️ 7.12 uses "machine epsilon" and "condition number" — these need careful definition before use.

**Recommended breadcrumb counts:**
- 7.3 Matrix Multiplication: **8 breadcrumbs** (threshold concept — shape compatibility, dot product, non-commutativity each need space)
- 7.7 Vector Spaces: **8 breadcrumbs** (abstract, needs examples)
- 7.9 Eigenvalues: **10 breadcrumbs** (threshold concept — the "why" matters more than the "how")
- 7.11 Decompositions: **8 breadcrumbs** (three separate decompositions to explain)
- All others: 5-6 each

---

## 08 — Probability & Statistics

**Role:** Reasoning under uncertainty, data summarization, hypothesis testing.
**Difficulty:** M–H
**Threshold concept:** Conditional probability (8.2); Bayes' Theorem (8.3)
**Prerequisite modules:** 01 (Number Foundations), 02 (Algebra), 05 (Sets), 06 (Combinatorics)
**Feeds into:** 10 CS Applications, 11 Advanced

### 08 Topic Map

| # | Topic | Prereq Topics | Concepts | New Words | Difficulty |
|---|-------|---------------|----------|-----------|------------|
| 8.1 | Probability Basics | 6.4, 6.5, 5.1 | 5 | 5 | M |
| 8.2 | Conditional Probability | 8.1, 5.1 | 3 | 5 | T |
| 8.3 | Bayes Theorem | 8.2, 8.1 | 3 | 5 | T |
| 8.4 | Random Variables and Expected Value | 8.1, 6.1, 6.2 | 4 | 5 | H |
| 8.5 | Discrete Distributions | 8.4, 8.1, 6.5 | 4 | 5 | M |
| 8.6 | Continuous Distributions | 8.4, 9.5, 8.5 | 4 | 5 | M |
| 8.7 | Descriptive Statistics | 8.5, 8.6, 8.4 | 4 | 5 | M |
| 8.8 | Correlation and Regression | 8.7, 7.10 | 4 | 5 | M |
| 8.9 | Hypothesis Testing | 8.6, 8.7, 8.8 | 4 | 5 | H |
| 8.10 | Bayesian Inference | 8.3, 8.6, 8.4 | 3 | 5 | H |
| 8.11 | Information Theory | 8.1, 8.4, 8.5 | 4 | 5 | H |

### 08 Dependency Chain Analysis

**Chain quality:** ⚠️ Several issues.

**Breaks found:**
- ⚠️ 8.1 lists prerequisite 5.1 (Set Theory) — correct. Also lists 6.4 (Counting Rules) and 6.5 (Permutations) — these are in Module 06, so the dependency chain is: 05 → 06 → 08, which is correct for the numbering order.
- ❌ 8.6 lists prerequisite 9.5 (Integration Basics) — this creates a **circular/forward dependency** since 09 (Calculus) comes AFTER 08 in numbering. Either 8.6 must be moved after 09, or integration must be handled intuitively without formal calculus.
- ⚠️ 8.8 lists prerequisite 7.10 (Orthogonality and Least Squares) — this is in Module 07, which is fine as a backward reference (07 comes before 08).
- ❌ 8.6 needs 9.5 Integration for continuous distributions — but the student hasn't done calculus yet. This is a **major chain break**. Options: (a) make 8.6 intuitive without integration, OR (b) reorder 09 before 08.

**Recommended breadcrumb counts:**
- 8.2 Conditional Probability: **8 breadcrumbs** (common stumbling block)
- 8.3 Bayes Theorem: **8 breadcrumbs** (intuition before formula)
- 8.4 Random Variables: **8 breadcrumbs** (abstract concept)
- 8.9 Hypothesis Testing: **8 breadcrumbs** (many moving parts)
- All others: 5-6 each

---

## 09 — Calculus

**Role:** Change, accumulation, optimization, gradients.
**Difficulty:** H
**Threshold concept:** The limit (9.1); The derivative (9.2); The integral (9.5)
**Prerequisite modules:** 01 (Number Foundations), 02 (Algebra), 03 (Functions & Graphs)
**Feeds into:** 08 Probability, 10 CS Applications, 11 Advanced

### 09 Topic Map

| # | Topic | Prereq Topics | Concepts | New Words | Difficulty |
|---|-------|---------------|----------|-----------|------------|
| 9.1 | Limits and Continuity | 2.7, 2.2, 4.6 | 5 | 5 | T |
| 9.2 | Differentiation Basics | 9.1, 2.2 | 3 | 5 | T |
| 9.3 | Differentiation Rules | 9.2, 9.1 | 4 | 5 | M |
| 9.4 | Applications of Differentiation | 9.3, 9.2 | 4 | 5 | M |
| 9.5 | Integration Basics | 9.2, 9.3 | 3 | 5 | T |
| 9.6 | Integration Techniques | 9.5, 9.3 | 2 | 5 | H |
| 9.7 | Differential Equations Intro | 9.5, 9.6, 9.3 | 2 | 5 | H |
| 9.8 | Multivariable Functions | 9.2, 9.3, 8.1 | 3 | 5 | H |
| 9.9 | Gradient Descent and Optimisation | 9.8, 9.4, 2.7 | 3 | 5 | H |
| 9.10 | Convex Optimisation Basics | 9.9, 9.8, 2.7 | 2 | 5 | H |

### 09 Dependency Chain Analysis

**Chain quality:** ❌ Significant breaks.

**Breaks found:**
- ❌ 9.1 lists prerequisite [[4.6 Trig Functions Basics]] — this topic does NOT exist. 4.6 is "Unit Circle" and 4.5 is "Trig Ratios SOHCAHTOA". Wrong reference.
- ❌ 9.8 lists prerequisite [[8.1 Probability Foundations]] — this topic does NOT exist. 8.1 is "Probability Basics". Wrong reference.
- ⚠️ 9.6 Integration Techniques has only 2 Concept sections but 5 New Words words — "Partial fractions", "Improper integral", and "Numerical integration" are listed as terms but don't have their own concept sections.
- ⚠️ 9.7 Differential Equations has only 2 Concept sections — "Separable equations" is introduced here but needs more scaffolding.
- ❌ 9.9 forward-links to [[10.12 Computer Vision Maths]] — this topic does NOT exist. 10.12 is "Research Paper Maths Reading".
- ⚠️ 9.10 Convex Optimisation has only 2 concepts (Convex Function, Convexity Check) but New Words includes "Lagrangian duality" which isn't explained in any concept.

**Recommended breadcrumb counts:**
- 9.1 Limits: **10 breadcrumbs** (threshold concept — "approaches" is hard)
- 9.2 Differentiation: **10 breadcrumbs** (first principles, notation, simple derivatives)
- 9.5 Integration: **10 breadcrumbs** (FTC is a threshold concept)
- 9.7 Differential Equations: **8 breadcrumbs** (needs more than 2 concepts)
- 9.8 Multivariable: **8 breadcrumbs**
- 9.9 Gradient Descent: **8 breadcrumbs**
- All others: 5-7 each

---

## 10 — CS Applications

**Role:** Tying mathematical tools directly to algorithms, systems, security, ML, and graphics.
**Difficulty:** H
**Threshold concept:** Big-O notation (10.1); RSA Cryptography (10.6)
**Prerequisite modules:** 01–09 (all prior modules)
**Feeds into:** 11 Advanced & Masters-Level Topics

### 10 Topic Map

| # | Topic | Prereq Topics | Concepts | New Words | Difficulty |
|---|-------|---------------|----------|-----------|------------|
| 10.1 | Big O Theta and Omega | 9.10, 6.1 | 2 | 5 | T |
| 10.2 | Algorithm Complexity Case Studies | 10.1, 6.1 | 3 | 5 | M |
| 10.3 | Binary Hexadecimal and Number Bases | 1.1, 1.2 | 3 | 5 | M |
| 10.4 | Floating Point and Rounding Error | 10.3, 1.5 | 2 | 5 | H |
| 10.5 | Hashing and Checksums | 6.2, 10.3 | 2 | 5 | M |
| 10.6 | Cryptography RSA and Diffie Hellman | 6.2, 6.12, 10.3 | 2 | 5 | T |
| 10.7 | Error Correction QR and Reed Solomon | 6.1, 10.3 | 2 | 5 | H |
| 10.8 | Machine Learning Vectors and Matrices | 7.3, 7.1, 7.2 | 2 | 5 | H |
| 10.9 | Neural Network Maths | 10.8, 9.8, 9.9 | 2 | 5 | H |
| 10.10 | Graphs in Networks and AI Search | 6.6, 10.1 | 2 | 5 | M |
| 10.11 | Type Theory and Program Logic Intro | 5.5, 5.9 | 2 | 5 | H |
| 10.12 | Research Paper Maths Reading | 10.1–10.11, 5.10, 9.10 | 2 | 5 | M |

### 10 Dependency Chain Analysis

**Chain quality:** ❌ Multiple critical breaks.

**Breaks found:**
- ❌ 10.1 lists prerequisite [[9.10 Convex Optimisation Basics]] — convex optimization is NOT a prerequisite for Big-O. Big-O only needs 3.5 (Polynomials) and 6.1 (Sequences). This is a **wildly incorrect link**.
- ❌ 10.6 lists prerequisite [[6.12 Number Theory Basics]] — this topic does NOT exist. 6.12 is "Computability and Decidability". Wrong reference.
- ❌ 10.10 lists prerequisite 6.6 (Graph Theory Basics) — correct. But then forward-links to [[6.7 Graph Theory Basics]] which doesn't match the current ordering (6.7 IS Graph Theory Basics in the actual vault).
- ❌ 10.11 lists prerequisite [[5.9 Predicate Logic]] — this topic does NOT exist. 5.9 is "Direct Proof and Counterexample". Wrong reference.
- ❌ 10.12 forward-links to [[11.1 Advanced Probability for CS]] and [[11.2 Information Theory in Depth]] — these topics do NOT exist. 11.1 is "Advanced Complexity Theory" and 11.2 is "Randomised Algorithms".
- ⚠️ 10.3 Binary is excellent (prereqs: 1.1, 1.2 — correct). This is one of the few clean chains in Module 10.

**Recommended breadcrumb counts:**
- 10.1 Big-O: **8 breadcrumbs** (formal definition is hard — "for all n > n₀" needs careful treatment)
- 10.3 Binary/Hex: **8 breadcrumbs** (base conversion needs practice)
- 10.6 Cryptography: **10 breadcrumbs** (RSA is a threshold concept — modular exponentiation, Euler's theorem, key generation all need separate breadcrumbs)
- 10.9 Neural Networks: **8 breadcrumbs**
- 10.11 Type Theory: **8 breadcrumbs**
- All others: 5-6 each

---

## 11 — Advanced & Masters-Level Topics

**Role:** Preparation for master's-level AI, algorithms, security, theory, and research.
**Difficulty:** H–T (very hard, several threshold concepts)
**Threshold concept:** P vs NP (11.1); Lambda Calculus (11.12); Quantum Computing (11.16)
**Prerequisite modules:** 01–10 (all prior modules)
**Feeds into:** Research and professional practice

### 11 Topic Map

| # | Topic | Prereq Topics | Concepts | New Words | Difficulty |
|---|-------|---------------|----------|-----------|------------|
| 11.1 | Advanced Complexity Theory | 10.1, 5.11, 5.5 | 2 | 5 | T |
| 11.2 | Randomised Algorithms | 11.1, 8.3, 8.4 | 2 | 5 | H |
| 11.3 | Approximation Algorithms | 11.1, 11.2, 9.10 | 1 | 5 | H |
| 11.4 | Advanced Graph Theory | 6.6, 10.10, 8.1 | 2 | 5 | H |
| 11.5 | Statistical Learning Theory | 8.9, 8.11, 11.2 | 2 | 5 | T |
| 11.6 | Probabilistic Graphical Models | 11.5, 8.3, 6.6 | 2 | 5 | T |
| 11.7 | Advanced Optimisation for ML | 9.9, 9.10, 11.2 | 2 | 5 | H |
| 11.8 | Multivariable Calculus for Deep Learning | 9.8, 9.3, 7.3 | 2 | 5 | H |
| 11.9 | Linear Algebra for Representation Learning | 7.5, 7.9, 7.12 | 2 | 5 | H |
| 11.10 | Numerical Methods and Stability | 10.4, 9.6, 7.10 | 2 | 5 | H |
| 11.11 | Category Theory for CS Intro | 10.11, 5.10 | 2 | 5 | T |
| 11.12 | Lambda Calculus and Formal Semantics | 11.11, 10.11, 5.10 | 2 | 5 | T |
| 11.13 | Finite Fields and Polynomial Arithmetic | 6.2, 6.12, 6.1 | 2 | 5 | H |
| 11.14 | Elliptic Curve Cryptography | 11.13, 10.6, 6.12 | 2 | 5 | T |
| 11.15 | Lattice-Based Cryptography | 11.13, 7.3, 10.6 | 2 | 5 | T |
| 11.16 | Quantum Computing Maths Intro | 7.4, 7.5, 7.9 | 2 | 5 | T |
| 11.17 | Information Theory for ML and Compression | 8.3, 8.4, 11.5 | 2 | 5 | H |
| 11.18 | Research Methods and Mathematical Writing | 10.12, 5.10, 11.17 | 2 | 5 | M |

### 11 Dependency Chain Analysis

**Chain quality:** ❌ Significant reference errors and impossible prerequisites.

**Breaks found:**
- ❌ **Systematic error:** Many topics reference prerequisite topics that do not exist in the vault:
  - 11.2 references "8.3 Discrete Distributions" → actual is "8.3 Bayes Theorem" and "8.5 Discrete Distributions"
  - 11.4 references "8.1 Probability Foundations" → actual is "8.1 Probability Basics"
  - 11.5 references "8.9 Regression and Correlation" → actual is "8.8 Correlation and Regression"
  - 11.6 references "8.5 Bayes' Theorem" → actual is "8.3 Bayes Theorem"
  - 11.9 references "7.9 Singular Value Decomposition" → actual is "7.11 Matrix Decompositions"
  - 11.10 references "7.10 Solving Linear Systems" → actual is "7.6 Solving Linear Systems with Matrices"
  - 11.13 references "6.12 Number Theory Basics" → actual is "6.12 Computability and Decidability"
  - 11.16 references "7.4 Complex Numbers" → this topic does NOT exist anywhere in the vault!
- ❌ **Missing prerequisite:** 11.16 Quantum Computing needs complex numbers — but there is NO topic on complex numbers anywhere in the vault. This is a **critical gap**.
- ⚠️ 11.3 Approximation Algorithms has only **1 Concept section** (Greedy Set Cover). The New Words includes "LP rounding" and "hardness of approximation" which are not explained in any concept.
- ⚠️ 11.9 references "7.12 Matrix Decompositions" → actual is "7.11 Matrix Decompositions LU QR SVD". Off-by-one.

**Recommended breadcrumb counts:**
- 11.1 P vs NP: **8 breadcrumbs** (reductions are hard)
- 11.12 Lambda Calculus: **10 breadcrumbs** (beta reduction, Church numerals, fixed-points)
- 11.13 Finite Fields: **8 breadcrumbs** (GF(p) and GF(2^k) each need space)
- 11.16 Quantum Computing: **10 breadcrumbs** (needs complex numbers prerequisite — must add a complex numbers topic)
- 11.11 Category Theory: **8 breadcrumbs**
- All others: 5-6 each

---

## Summary of All Chain Breaks

### Critical ( ❌ ) — Must Fix

| Break | Location | Problem | Fix |
|-------|----------|---------|-----|
| Non-existent topic | 7.1, 7.7 | References "5.3 Tuples and Vectors" | Create topic or fix link to 4.8 Vectors |
| Non-existent topic | 7.6 | References "3.2 Solving Equations" | Fix link to 2.5 Solving Linear Equations |
| Non-existent topic | 9.1 | References "4.6 Trig Functions Basics" | Fix link to 4.5 Trig Ratios |
| Non-existent topic | 9.8 | References "8.1 Probability Foundations" | Fix link to 8.1 Probability Basics |
| Non-existent topic | 10.6 | References "6.12 Number Theory Basics" | Create Number Theory topic or fix link |
| Non-existent topic | 10.11 | References "5.9 Predicate Logic" | Fix link to 5.7 Implication & Equivalence |
| Non-existent topic | 10.12 | Forward-links to "11.1 Advanced Probability" etc. | Fix links to actual 11.* topics |
| Non-existent topic | 11.16 | References "7.4 Complex Numbers" — NO COMPLEX NUMBERS topic anywhere | **Add complex numbers topic** (could be in 07 after vectors) |
| Wrong prerequisite | 10.1 | Prereq "9.10 Convex Optimisation" — should be 3.5/6.1 | Link to 6.1 Sequences, 3.5 Polynomials |
| Forward reference | 5.11 | Prereq "6.1 Sequences" — but 6 is after 05 | Either move 6.1 to 05 or teach sequences in 5.11 |
| Forward reference | 8.6 | Prereq "9.5 Integration Basics" — but 09 is after 08 | Make 8.6 intuitive or reorder modules |
| Complex numbers | 11.16 | Used but never taught | Add topic 7.4 Complex Numbers (after 4.8 Vectors) |

### Warning ( ⚠️ ) — Should Fix

| Break | Location | Problem |
|-------|----------|---------|
| Wrong prereq | 2.1 | Lists 1.13 which is not needed |
| Off-by-one | 7.9 | Forward-links to 10.10 (wrong topic) |
| Off-by-one | 11.9 | References 7.12 instead of 7.11 |
| Insufficient concepts | 9.6 | Only 2 concepts for 5 new words |
| Insufficient concepts | 9.7 | Only 2 concepts for differential equations |
| Insufficient concepts | 11.3 | Only 1 concept — needs more |
| Circular order | 4.6→4.7 | 4.6 needs 4.7 first (study order mismatch) |
| Glossary placeholders | All | 607 term files say "Add your own definition" |

---

## Total Current Inventory

| Module | Topics | Concepts | New Words | Mini-Quiz Qs | Recommended Breadcrumbs |
|--------|--------|----------|-----------|-------------|----------------------|
| 01 | 13 | ~78 | 65 | 130 | ~78 |
| 02 | 11 | ~55 | 55 | 110 | ~60 |
| 03 | 10 | ~50 | 50 | 100 | ~60 |
| 04 | 10 | ~50 | 50 | 100 | ~70 |
| 05 | 11 | ~55 | 55 | 110 | ~75 |
| 06 | 12 | ~60 | 60 | 120 | ~80 |
| 07 | 12 | 53 | 60 | 120 | ~70 |
| 08 | 11 | 42 | 55 | 110 | ~65 |
| 09 | 10 | 31 | 50 | 100 | ~70 |
| 10 | 12 | 25 | 60 | 120 | ~70 |
| 11 | 18 | 35 | 90 | 180 | ~110 |
| **Total** | **130** | **~534** | **650** | **1300** | **~808** |

**Worked Examples current count:** ~130 files (one per topic), need ~808 to match breadcrumb count.

---

## Dependency Graph (Module Level)

```
01 Number Foundations
  ├──→ 02 Algebra
  │     ├──→ 03 Functions & Graphs
  │     │     ├──→ 04 Geometry & Trigonometry
  │     │     │     ├──→ 07 Linear Algebra
  │     │     │     │     ├──→ 08 Probability & Statistics (partial — 8.8 needs 7.10)
  │     │     │     │     └──→ 10 CS Applications
  │     │     │     └──→ 09 Calculus
  │     │     │           ├──→ 10 CS Applications
  │     │     │           └──→ 08 Probability & Statistics (8.6 needs 9.5)
  │     │     └──→ 05 Sets, Logic & Proof
  │     │           ├──→ 06 Discrete Mathematics
  │     │           │     ├──→ 08 Probability & Statistics
  │     │           │     └──→ 10 CS Applications
  │     │           └──→ 11 Advanced Topics
  │     └──→ 08 Probability & Statistics (partial)
  └──→ 10 CS Applications (10.3 directly)
```

**Issue:** Current numbering suggests linear study order (01→02→...→11), but the actual dependency graph is a DAG with cross-module edges. Some chains are:
- Linear: 01 → 02 → 03 → 05 → 06 → 10
- Branch: 03 → 04 → 07 → 10
- Branch: 03 → 09 → 10
- Cross: 06 → 08; 07 → 08; 09 → 08

**Recommended study order (respecting actual dependencies, not numbers):**
1. 01 Number Foundations (all)
2. 02 Algebra (all)
3. 03 Functions & Graphs (all)
4. 04 Geometry & Trigonometry (all)
5. 05 Sets, Logic & Proof (5.1–5.10; delay 5.11 until after 6.1)
6. 06 Discrete Mathematics (6.1 first, then rest)
7. 05.11 Proof by Induction (now that 6.1 is done)
8. 07 Linear Algebra (all)
9. 09 Calculus (all)
10. 08 Probability & Statistics (all — now 9.5 is done for 8.6)
11. 10 CS Applications (all)
12. 11 Advanced & Masters-Level Topics (all)

---

## Appendix: Recommended New/Broken Topics

### Topics That Need Creating

| Topic | Why Needed | Placement | Feeds Into |
|-------|-----------|-----------|------------|
| **Complex Numbers** | 11.16 needs them; 7.9 eigenvalues use them | After 4.8 Vectors, before 7.9 | 7.9, 11.16 |
| **Number Theory Basics** | Referenced by 10.6, 11.13, 11.14 but doesn't exist | After 6.3 Modular Arithmetic | 10.6, 11.13, 11.14 |

### Topics That Need Significant Breadcrumb Expansion

| Topic | Current Concepts | Recommended | Reason |
|-------|-----------------|-------------|--------|
| 3.7 Logarithms | ~5 | 10 | Threshold concept |
| 4.5 Trig Ratios | ~5 | 10 | First contact with sin/cos/tan |
| 4.6 Unit Circle | ~5 | 12 | Threshold — connects ratios to coordinates |
| 5.4 Infinity & Countability | ~5 | 12 | Paradox topic — Cantor's diagonal |
| 5.11 Proof by Induction | ~5 | 10 | Threshold — "assume true for k" is hard |
| 6.6 Recurrence Relations | ~5 | 10 | Abstract pattern recognition |
| 6.11 Formal Languages | ~5 | 12 | DFA/NFA/regex each need own breadcrumb |
| 7.3 Matrix Multiplication | 5 | 8 | Non-commutativity needs careful treatment |
| 7.9 Eigenvalues | 4 | 10 | "Why eigenvectors?" is the key question |
| 9.1 Limits | 5 | 10 | "Approaches but never reaches" |
| 9.2 Differentiation | 3 | 10 | First principles + notation + simple rules |
| 9.5 Integration | 3 | 10 | FTC needs careful explanation |
| 10.6 Cryptography | 2 | 10 | RSA needs many breadcrumbs |
| 11.12 Lambda Calculus | 2 | 10 | Beta reduction, Church numerals |
| 11.16 Quantum Computing | 2 | 10 | Needs complex numbers first |

---

*End of Curriculum Matrix. Next step: use this matrix to guide the rewrite of each topic, starting from Module 01 and working forward, fixing chain breaks as encountered.*
