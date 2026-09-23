#!/usr/bin/env python3
"""Generate complete Module 03 Functions and Graphs topic bundles."""
from pathlib import Path

ROOT = Path("/home/Marau/Marau/University/Maths for CS")
GLOSSARY = ROOT / "00 Glossary" / "Terms"

TOPICS = {
    "3.2 Function Notation and Mapping": {
        "file": "3.2 Function Notation and Mapping",
        "tags": "#maths/functions #maths/graphs #cs/functions",
        "prereq": "[[3.1 Coordinates and Axes]], [[2.1 Variables Expressions and Equations]]",
        "used_later": "[[3.3 Linear Functions and Gradient]], [[3.8 Inverse and Composite Functions]], [[10.1 Big O Theta and Omega]]",
        "threshold": "90%",
        "plain": "A **function** is a rule that takes each allowed input and produces exactly one output.",
        "everyday": "A vending machine: you put in money (input), press a code, and get one snack (output). The same input always gives the same output.",
        "words": [
            ("function", "a rule that assigns exactly one output to each allowed input."),
            ("input", "the value you put into a function, often written as x."),
            ("output", "the value a function returns for a given input, often written as f(x) or y."),
            ("domain", "the set of all input values a function is allowed to accept."),
            ("range", "the set of all output values the function can actually produce."),
        ],
        "builds_on": {
            "function": "[[3.1 Coordinates and Axes]], [[2.1 Variables Expressions and Equations]]",
            "input": "[[2.1 Variables Expressions and Equations]]",
            "output": "[[2.1 Variables Expressions and Equations]]",
            "domain": "[[5.1 Set Theory Basics]]",
            "range": "[[5.1 Set Theory Basics]]",
        },
        "cs": [
            "Python `def` functions and return values",
            "API endpoints mapping request → response",
            "hash functions mapping data → fixed-size digest",
            "activation functions in neural networks",
        ],
        "next": "[[3.3 Linear Functions and Gradient]]",
        "backward": "[[3.1 Coordinates and Axes]], [[2.1 Variables Expressions and Equations]]",
    },
    "3.3 Linear Functions and Gradient": {
        "file": "3.3 Linear Functions and Gradient",
        "tags": "#maths/functions #maths/graphs #cs/linear",
        "prereq": "[[3.2 Function Notation and Mapping]], [[2.5 Solving Linear Equations]]",
        "used_later": "[[3.4 Quadratic Functions]], [[7.10 Orthogonality and Least Squares]], [[9.9 Gradient Descent and Optimisation]]",
        "threshold": "90%",
        "plain": "A **linear function** has a constant rate of change. Its graph is a straight line.",
        "everyday": "If a taxi charges £3 plus £2 per mile, the total cost grows by £2 for every extra mile — that steady add-on is linear.",
        "words": [
            ("gradient", "the steepness of a line; change in y divided by change in x."),
            ("intercept", "where a graph crosses an axis, often the y-value when x = 0."),
            ("slope", "another name for gradient — how much y changes per unit change in x."),
            ("rate of change", "how fast one quantity changes relative to another; constant for linear functions."),
            ("y equals mx plus c", "the standard form y = mx + c where m is gradient and c is y-intercept."),
        ],
        "builds_on": {
            "gradient": "[[3.1 Coordinates and Axes]], [[1.6 Fractions]]",
            "intercept": "[[3.1 Coordinates and Axes]]",
            "slope": "[[gradient]]",
            "rate of change": "[[1.12 Ratio Proportion and Units]]",
            "y equals mx plus c": "[[2.1 Variables Expressions and Equations]]",
        },
        "cs": [
            "linear interpolation between keyframes",
            "Big-O lines on log-log plots",
            "affine transforms in graphics",
            "simple regression and trend lines",
        ],
        "next": "[[3.4 Quadratic Functions]]",
        "backward": "[[3.2 Function Notation and Mapping]], [[2.5 Solving Linear Equations]]",
    },
}

# Script continues - we'll append more topics via separate writes and run
print("Partial script - run full version")
