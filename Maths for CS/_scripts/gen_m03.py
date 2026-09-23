#!/usr/bin/env python3
"""Generate remaining Module 03 assessment bundles and glossary."""
from pathlib import Path

ROOT = Path("/home/Marau/Marau/University/Maths for CS")
GLOSS = ROOT / "00 Glossary" / "Terms"

def w(path, content):
    path = ROOT / path if not str(path).startswith("/") else Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return path

def gloss(term, defn, topic, builds, cs):
    w(GLOSS / f"{term}.md", f"""# {term}
{defn}
First introduced in: [[{topic}]]
Builds on: {builds}
Used in CS: {cs}
## Related Notes
Search backlinks in Obsidian to see every topic that uses [[{term}]].
""")

# --- Glossary terms 3.3-3.10 ---
GLOSSARY = [
    ("gradient", "The steepness of a line, found as change in y divided by change in x.", "3.3 Linear Functions and Gradient", "[[3.1 Coordinates and Axes]], [[1.6 Fractions]]", "Slopes in graphics, learning rates, and trend lines all use gradient as rate of change."),
    ("intercept", "The value where a graph crosses an axis, usually the y-value when x equals zero.", "3.3 Linear Functions and Gradient", "[[3.1 Coordinates and Axes]]", "Base fees, bias terms in ML, and y-axis crossing points are intercepts."),
    ("slope", "Another name for gradient: how much y changes for each unit increase in x.", "3.3 Linear Functions and Gradient", "[[gradient]]", "Screen slopes, ramp angles in games, and linear trends share the same rise-over-run idea."),
    ("rate of change", "How fast one quantity changes relative to another; constant for linear functions.", "3.3 Linear Functions and Gradient", "[[1.12 Ratio Proportion and Units]]", "Throughput, frames per second, and bandwidth are rates of change in systems."),
    ("y equals mx plus c", "The standard linear form y = mx + c where m is gradient and c is y-intercept.", "3.3 Linear Functions and Gradient", "[[2.1 Variables Expressions and Equations]]", "Affine pricing and timing formulas in code often match y = mx + c."),
    ("parabola", "The U-shaped graph of a quadratic function.", "3.4 Quadratic Functions", "[[3.3 Linear Functions and Gradient]]", "Projectile paths, loss curves, and quadratic Bezier segments form parabolas."),
    ("turning point", "The highest or lowest point on a parabola where the curve changes direction.", "3.4 Quadratic Functions", "[[3.4 Quadratic Functions]]", "Optimisation finds turning points to minimise cost or maximise score."),
    ("roots", "The x-values where a function equals zero, also called x-intercepts.", "3.4 Quadratic Functions", "[[2.5 Solving Linear Equations]]", "Finding where an equation hits zero is like finding when a buffer empties or profit is zero."),
    ("axis of symmetry", "The vertical line that splits a parabola into two mirror-image halves.", "3.4 Quadratic Functions", "[[3.1 Coordinates and Axes]]", "Symmetric UI layouts and mirrored animations use the same symmetry idea."),
    ("quadratic coefficient", "The number a in ax squared plus bx plus c that controls how wide or narrow the parabola is.", "3.4 Quadratic Functions", "[[2.9 Indices and Powers]]", "Curvature weights in physics engines and ML regularisation tie to quadratic terms."),
    ("polynomial", "A sum of terms with non-negative whole-number powers of a variable.", "3.5 Polynomials", "[[3.4 Quadratic Functions]]", "Hash polynomials, CRC codes, and curve fitting use polynomial expressions."),
    ("degree", "The highest power of the variable in a polynomial.", "3.5 Polynomials", "[[2.9 Indices and Powers]]", "Polynomial degree bounds complexity in error-correction and interpolation algorithms."),
    ("coefficient", "The numerical factor multiplying a variable or power in an algebraic term.", "3.5 Polynomials", "[[2.1 Variables Expressions and Equations]]", "Weights in neural networks and terms in cost functions are coefficients."),
    ("root", "A value of the variable that makes a polynomial equal to zero.", "3.5 Polynomials", "[[roots]]", "Finding roots locates zeros of equations in numerical solvers and graphics clipping."),
    ("leading term", "The term with the highest degree in a polynomial, written first in standard form.", "3.5 Polynomials", "[[degree]]", "Leading-term behaviour dominates growth for large inputs in algorithm analysis."),
    ("exponential growth", "Increase by a fixed multiplier per step, modelled by y equals a times b to the power x.", "3.6 Exponential Functions", "[[2.9 Indices and Powers]]", "Viral spread, compound interest, and memory doubling show exponential growth."),
    ("growth factor", "The multiplier b greater than 1 applied each step in exponential growth.", "3.6 Exponential Functions", "[[2.9 Indices and Powers]]", "Replication factors and per-step scaling in simulations use growth factors."),
    ("decay factor", "The multiplier between 0 and 1 that shrinks a quantity each step in exponential decay.", "3.6 Exponential Functions", "[[2.9 Indices and Powers]]", "Half-life models and cache eviction rates use decay factors."),
    ("base", "The number raised to a power in an exponential or logarithmic expression.", "3.6 Exponential Functions", "[[2.9 Indices and Powers]]", "Binary base 2, natural base e, and decimal base 10 appear throughout CS."),
    ("asymptote", "A line a graph approaches but never reaches as x or y grows very large.", "3.6 Exponential Functions", "[[3.3 Linear Functions and Gradient]]", "Horizontal limits in probability and vertical caps in rendering behave like asymptotes."),
    ("logarithm", "The inverse of exponentiation: the power you raise a base to in order to get a given number.", "3.7 Logarithms", "[[3.6 Exponential Functions]]", "Logarithms measure tree depth, entropy, and log-scale chart axes in CS."),
    ("power", "The exponent in an expression base raised to power, also the result of repeated multiplication.", "3.7 Logarithms", "[[2.9 Indices and Powers]]", "Powers describe bit counts, memory sizes, and repeated loop nesting."),
    ("inverse operation", "An operation that undoes another, such as log undoing exponentiation.", "3.7 Logarithms", "[[1.3 Addition and Subtraction]]", "Decode reverses encode; decrypt reverses encrypt — inverse operations in security."),
    ("log laws", "Rules for simplifying logarithms of products, quotients, and powers.", "3.7 Logarithms", "[[3.6 Exponential Functions]]", "Log laws simplify complexity expressions like log(n squared) equals 2 log n."),
    ("inverse function", "A function f inverse that undoes f so f inverse of f of x equals x.", "3.8 Inverse and Composite Functions", "[[3.2 Function Notation and Mapping]]", "Encoding and decoding, encrypt and decrypt pairs are inverse functions."),
    ("composition", "Applying one function to the result of another, written f of g of x.", "3.8 Inverse and Composite Functions", "[[3.2 Function Notation and Mapping]]", "Data pipelines chain functions: parse then validate then store."),
    ("identity function", "The function f of x equals x that returns each input unchanged.", "3.8 Inverse and Composite Functions", "[[3.2 Function Notation and Mapping]]", "Identity maps and no-op middleware act as identity functions in software."),
    ("one-to-one", "A function where different inputs always give different outputs, required for a full inverse.", "3.8 Inverse and Composite Functions", "[[3.2 Function Notation and Mapping]]", "Injective hash functions and bijective encodings need one-to-one behaviour."),
    ("nested function", "A function applied inside another, such as f of g of x.", "3.8 Inverse and Composite Functions", "[[composition]]", "Nested callbacks and composed higher-order functions mirror nested function notation."),
    ("translation", "A shift of a graph horizontally or vertically without changing its shape.", "3.9 Transformations of Graphs", "[[3.1 Coordinates and Axes]]", "Sprite offsets and camera panning translate objects on screen."),
    ("reflection", "A flip of a graph across an axis, turning points into mirror images.", "3.9 Transformations of Graphs", "[[3.1 Coordinates and Axes]]", "Flipping textures and mirroring UI elements are reflections."),
    ("stretch", "A transformation that multiplies coordinates, making a graph taller, wider, or both.", "3.9 Transformations of Graphs", "[[scale factor]]", "Non-uniform scaling of sprites and normalising features stretch data."),
    ("scale factor", "The number multiplying a coordinate during a stretch transformation.", "3.9 Transformations of Graphs", "[[1.4 Multiplication and Times Tables]]", "Zoom levels and DPI scaling use scale factors on coordinates."),
    ("transformation", "Any rule that moves, flips, or stretches a graph or shape to a new position or size.", "3.9 Transformations of Graphs", "[[3.9 Transformations of Graphs]]", "Matrix transforms in graphics apply translation, rotation, and scale together."),
    ("piecewise rule", "A function defined by different formulas on different input intervals.", "3.10 Piecewise and Step Functions", "[[2.7 Inequalities]]", "If-else chains and tiered pricing implement piecewise rules in code."),
    ("interval", "A continuous range of input values, often shown with inequality notation.", "3.10 Piecewise and Step Functions", "[[2.7 Inequalities]]", "Valid index ranges and timeout windows are intervals in programming."),
    ("step function", "A piecewise constant function whose graph looks like steps.", "3.10 Piecewise and Step Functions", "[[piecewise rule]]", "Tax brackets and quantised levels produce step-function behaviour."),
    ("floor function", "The greatest integer less than or equal to x, written floor of x.", "3.10 Piecewise and Step Functions", "[[3.2 Function Notation and Mapping]]", "Integer division and array indexing often use floor-like rounding down."),
    ("ceiling function", "The smallest integer greater than or equal to x, written ceiling of x.", "3.10 Piecewise and Step Functions", "[[3.2 Function Notation and Mapping]]", "Allocating enough memory pages uses ceiling to round up to whole blocks."),
]

written = []
for term, defn, topic, builds, cs in GLOSSARY:
    gloss(term, defn, topic, builds, cs)
    written.append(str(GLOSS / f"{term}.md"))

print(f"Glossary: {len(GLOSSARY)} terms")
print("Script part 1 done - glossary written")
