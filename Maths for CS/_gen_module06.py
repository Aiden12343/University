#!/usr/bin/env python3
"""Generate complete Module 06 Discrete Mathematics topic bundles."""
from pathlib import Path

BASE = Path("/home/Marau/Marau/University/Maths for CS")
MOD = BASE / "06 Discrete Mathematics"
WE = BASE / "90 Worked Examples"
PQ = BASE / "91 Practice Questions"
MT = BASE / "92 Mastery Tests"
ANS = BASE / "93 Answers and Mark Schemes"
GLO = BASE / "00 Glossary/Terms"

TOPICS = [
    {
        "id": "6.1", "slug": "6.1 Sequences and Series", "title": "Sequences and Series",
        "tags": "#maths/discrete #maths/sequences #cs/loops",
        "prereq": "[[5.11 Proof by Induction]]",
        "forward": "[[6.2 Summation and Product Notation]]",
        "backward_body": "[[5.11 Proof by Induction]], [[1.3 Addition and Subtraction]], [[1.4 Multiplication and Times Tables]]",
        "plain": "A **sequence** is an ordered list of numbers. A **series** is what you get when you add those numbers together. Sequences model patterns that grow step by step — like loop counters, monthly downloads, or recursive function calls.",
        "words": [
            ("sequence", "an ordered list of numbers, one after another, often written a₁, a₂, a₃, …"),
            ("term", "one individual number in a sequence, identified by its position"),
            ("series", "the sum of the terms of a sequence"),
            ("arithmetic sequence", "a sequence where each term differs from the previous one by a fixed amount d"),
            ("geometric sequence", "a sequence where each term is multiplied by a fixed ratio r"),
        ],
        "glossary_builds": [
            ("sequence", "[[1.1 Counting and Number Sense]]"),
            ("term", "[[1.2 Place Value and Number Lines]]"),
            ("series", "[[1.3 Addition and Subtraction]]"),
            ("arithmetic sequence", "[[1.3 Addition and Subtraction]]"),
            ("geometric sequence", "[[1.4 Multiplication and Times Tables]]"),
        ],
        "glossary_cs": [
            ("sequence", "Loop counters, array elements, and recursive call stacks all follow sequence-like ordering."),
            ("term", "Array indexing treats each element as a term at position i."),
            ("series", "Summing loop iterations or total work in an algorithm is a series calculation."),
            ("arithmetic sequence", "Linear growth in memory allocation often follows an arithmetic pattern."),
            ("geometric sequence", "Exponential backoff in networking doubles retry delays — a geometric sequence."),
        ],
        "cs": "Loop counters, recursive stacks, and generated data streams are sequences. Summing loop work gives series used in algorithm analysis.",
        "cs_objects": "for-loops, recursion stacks, array indexing, cumulative download counters",
    },
    {
        "id": "6.2", "slug": "6.2 Summation and Product Notation", "title": "Summation and Product Notation",
        "tags": "#maths/discrete #maths/notation #cs/complexity",
        "prereq": "[[6.1 Sequences and Series]]",
        "forward": "[[6.3 Modular Arithmetic]]",
        "backward_body": "[[6.1 Sequences and Series]], [[1.3 Addition and Subtraction]], [[1.4 Multiplication and Times Tables]]",
        "plain": "Summation (Σ) and product (Π) notation compress long chains of addition or multiplication into a single compact expression. Instead of writing 1 + 2 + 3 + … + n, you write Σᵢ₌₁ⁿ i.",
        "words": [
            ("sigma notation", "compact notation Σ for adding a sequence of terms indexed by i"),
            ("product notation", "compact notation Π for multiplying a sequence of terms indexed by i"),
            ("index", "the variable (usually i or k) that runs through the terms being added or multiplied"),
            ("bound", "the lower and upper limits that tell the index where to start and stop"),
            ("closed form", "a single formula that gives the result without needing to add or multiply term by term"),
        ],
        "glossary_builds": [
            ("sigma notation", "[[6.1 Sequences and Series]]"),
            ("product notation", "[[1.4 Multiplication and Times Tables]]"),
            ("index", "[[1.1 Counting and Number Sense]]"),
            ("bound", "[[1.2 Place Value and Number Lines]]"),
            ("closed form", "[[6.1 Sequences and Series]]"),
        ],
        "glossary_cs": [
            ("sigma notation", "Big-O analysis sums loop iterations: Σᵢ₌₁ⁿ 1 = n."),
            ("product notation", "Counting passwords uses products: Π choices per position."),
            ("index", "Loop variable i in for i in range(n) is a summation index."),
            ("bound", "Array bounds [0, n-1] mirror summation lower and upper limits."),
            ("closed form", "Closed forms like n(n+1)/2 let compilers and analysts evaluate sums in O(1)."),
        ],
        "cs": "Algorithm analysis uses summations to count loop iterations. Product notation counts combinations of independent choices.",
        "cs_objects": "for-loops, range(), factorial computation, complexity formulas",
    },
]

# Script continues - will append full generator logic
print("Partial script - needs completion")
