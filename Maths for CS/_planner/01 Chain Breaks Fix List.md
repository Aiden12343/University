# Chain Breaks — Fix List

> All places where a topic uses a term/concept that has not yet been defined.
> Each fix specifies the exact file, the broken reference, and the correct replacement.

---

## Critical Fixes (Blocking — must fix before content rewrite)

### 1. Missing Topic: Complex Numbers

| Field | Value |
|-------|-------|
| **Used in** | 7.9 Eigenvalues (characteristic equation), 11.16 Quantum Computing (qubit state) |
| **Current state** | No complex numbers topic exists anywhere in the vault |
| **Fix** | Create `07 Linear Algebra/7.4 Complex Numbers.md` (renumber 7.4→7.13 or insert as 7.4a) |
| **Prerequisites** | 2.10 Surds and Roots, 4.8 Vectors Basics |
| **Concepts needed** | i as √(-1), arithmetic, complex plane, polar form, Euler's formula |
| **Feeds into** | 7.9, 11.16 |

### 2. Non-existent Topic References (Fix links)

| File | Broken Reference | Correct Reference |
|------|-----------------|-------------------|
| `7.1 Matrix Notation and Shape.md` | `[[5.3 Tuples and Vectors]]` | `[[4.8 Vectors Basics]]` or `[[5.1 Set Theory Basics]]` |
| `7.7 Vector Spaces Span and Basis.md` | `[[5.3 Tuples and Vectors]]` | `[[4.8 Vectors Basics]]` |
| `7.6 Solving Linear Systems.md` | `[[3.2 Solving Equations]]` | `[[2.5 Solving Linear Equations]]` |
| `9.1 Limits and Continuity.md` | `[[4.6 Trig Functions Basics]]` | `[[4.5 Trig Ratios SOHCAHTOA]]` |
| `9.8 Multivariable Functions.md` | `[[8.1 Probability Foundations]]` | `[[8.1 Probability Basics]]` |
| `10.6 Cryptography RSA.md` | `[[6.12 Number Theory Basics]]` | `[[6.3 Modular Arithmetic]]` (or create Number Theory topic) |
| `10.11 Type Theory.md` | `[[5.9 Predicate Logic]]` | `[[5.7 Implication and Equivalence]]` |
| `11.16 Quantum Computing.md` | `[[7.4 Complex Numbers]]` | `[[7.4 Complex Numbers]]` (create this topic) |

### 3. Wrong Prerequisite Links

| File | Wrong Prereq | Correct Prereq |
|------|-------------|----------------|
| `2.1 Variables.md` | `1.13 Estimation and Error Checking` | `1.3 Addition and Subtraction` |
| `6.3 Modular Arithmetic.md` | `2.7 Inequalities` (not needed) | Remove; only 1.5 Division and 1.4 Multiplication needed |
| `10.1 Big O.md` | `9.10 Convex Optimisation Basics` | `6.1 Sequences and Series`, `3.5 Polynomials` |

### 4. Forward References (topic from later module needed now)

| File | Needs | Problem | Fix |
|------|-------|---------|-----|
| `5.11 Proof by Induction.md` | `6.1 Sequences` | Sequences taught after induction | Teach arithmetic/geometric sequences within 5.11 as a breadcrumb, OR move 6.1 to precede 5.11 |
| `8.6 Continuous Distributions.md` | `9.5 Integration Basics` | Calculus taught after probability | Make 8.6 use intuitive area arguments, not formal integration; add note "formal treatment after 9.5" |

### 5. Forward-linked Non-existent Topics

| File | Broken Forward Link | Correct Link |
|------|--------------------|--------------|
| `7.9 Eigenvalues.md` | `[[10.10 Dimensionality Reduction PCA]]` | `[[11.9 Linear Algebra for Representation Learning]]` |
| `9.9 Gradient Descent.md` | `[[10.12 Computer Vision Maths]]` | `[[10.9 Neural Network Maths]]` |
| `10.12 Research Paper Maths.md` | `[[11.1 Advanced Probability for CS]]` | `[[11.1 Advanced Complexity Theory]]` |
| `10.12 Research Paper Maths.md` | `[[11.2 Information Theory in Depth]]` | `[[11.17 Information Theory for ML and Compression]]` |

---

## Secondary Fixes (Quality — fix during module rewrite)

### Insufficient Breadcrumbs

| File | Concepts | Need | Reason |
|------|----------|------|--------|
| `9.6 Integration Techniques.md` | 2 | 6 | 5 new words but only 2 concepts — partial fractions and trig integrals need their own sections |
| `9.7 Differential Equations.md` | 2 | 5 | Separable equations only — needs direction fields, integrating factors |
| `9.10 Convex Optimisation.md` | 2 | 5 | Has "Lagrangian duality" in new words but no concept for it |
| `11.3 Approximation Algorithms.md` | 1 | 4 | Only has Greedy Set Cover — needs LP rounding, PTAS definition |

### Off-by-One Topic Number Errors

| File | Reference | Should Be |
|------|-----------|-----------|
| `11.9 Linear Algebra for Rep Learning.md` | `7.12 Matrix Decompositions` | `7.11 Matrix Decompositions LU QR SVD` |
| `10.11 Type Theory.md` | `11.3 Lambda Calculus` | `11.12 Lambda Calculus and Formal Semantics` |

### Glossary Placeholders

| Scope | Current State | Fix |
|-------|--------------|-----|
| All 607 term files in `00 Glossary/Terms/` | "Add your own definition after studying it" | Write one-line plain-English definition per term, with "First introduced in: [[topic]]" and "Builds on: [[prior term]]" |

---

## Study Order Fix (Modules 05, 06, 08, 09)

Current numbering suggests linear 01→02→...→11, but actual dependencies require:

```
01 → 02 → 03 → 04 → 05.1-5.10
                  ↘         ↘
                   07 → 06.1 → 05.11
                    ↘        ↘
                     09 → 08 → 10 → 11
```

**Recommendation:** Update Progress Tracker and MOC files to reflect non-linear study order. Add notes to topics like "Study this after completing [module.topic]".
