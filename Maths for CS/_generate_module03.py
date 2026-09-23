#!/usr/bin/env python3
"""Generate complete Module 03 Functions and Graphs content bundles."""
import os

BASE = "/home/Marau/Marau/University/Maths for CS"
TOPICS_DIR = os.path.join(BASE, "03 Functions & Graphs")
WE_DIR = os.path.join(BASE, "90 Worked Examples")
PQ_DIR = os.path.join(BASE, "91 Practice Questions")
MT_DIR = os.path.join(BASE, "92 Mastery Tests")
ANS_DIR = os.path.join(BASE, "93 Answers and Mark Schemes")
GLOSS_DIR = os.path.join(BASE, "00 Glossary/Terms")

files_written = []

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    files_written.append(path)

# ─── Glossary definitions (50 terms) ───────────────────────────────────────────
GLOSSARY = {
    "x-axis": ("The horizontal number line in a coordinate plane, where the first value of a coordinate pair is read.", "[[3.1 Coordinates and Axes]]", "[[number line]]", "Screen coordinates, graph axes, and image width all use a horizontal axis like the x-axis."),
    "y-axis": ("The vertical number line in a coordinate plane, where the second value of a coordinate pair is read.", "[[3.1 Coordinates and Axes]]", "[[x-axis]]", "Pixel rows, chart height, and vertical scroll positions map to a y-axis in graphics and UI layout."),
    "origin": ("The point where the x-axis and y-axis cross, with coordinates (0, 0).", "[[3.1 Coordinates and Axes]]", "[[x-axis]]", "The origin is the reference point for transforms in graphics APIs and for normalising data to start at zero."),
    "coordinate pair": ("An ordered pair (x, y) that names one point by its horizontal and vertical positions.", "[[3.1 Coordinates and Axes]]", "[[origin]]", "A GPS fix, mouse click, or graph data point is stored as an ordered pair of numbers."),
    "quadrant": ("One of the four regions of the coordinate plane, numbered I to IV by where x and y are positive or negative.", "[[3.1 Coordinates and Axes]]", "[[coordinate pair]]", "Quadrant signs matter when interpreting slopes, rotations, and signed distances in game physics."),
    "function": ("A rule that assigns exactly one output to each allowed input.", "[[3.2 Function Notation and Mapping]]", "[[variable]]", "Every programming function, hash map lookup, and API endpoint that returns one result per request behaves like a function."),
    "input": ("The value fed into a function before the rule is applied.", "[[3.2 Function Notation and Mapping]]", "[[function]]", "Function arguments, sensor readings, and user form fields are inputs to a computation."),
    "output": ("The value a function produces for a given input.", "[[3.2 Function Notation and Mapping]]", "[[input]]", "Return values, rendered pixels, and model predictions are outputs of a function or pipeline step."),
    "domain": ("The set of all inputs a function is allowed to accept.", "[[3.2 Function Notation and Mapping]]", "[[function]]", "Type systems and input validation enforce domain restrictions so programs reject invalid inputs early."),
    "range": ("The set of all outputs a function can actually produce from its domain.", "[[3.2 Function Notation and Mapping]]", "[[domain]]", "Knowing the range of an activation function tells you what values a neural network layer can output."),
    "gradient": ("The steepness of a straight line, found as change in y divided by change in x.", "[[3.3 Linear Functions and Gradient]]", "[[rate of change]]", "Gradient measures learning rate direction in optimisation and slope in cost-vs-size graphs."),
    "intercept": ("The point where a graph crosses an axis; y-intercept is where x = 0.", "[[3.3 Linear Functions and Gradient]]", "[[gradient]]", "The intercept of a regression line is the predicted value when the independent variable is zero."),
    "slope": ("Another name for gradient: how much y changes when x increases by 1.", "[[3.3 Linear Functions and Gradient]]", "[[gradient]]", "Slopes appear in Big-O comparison graphs when one algorithm's cost rises faster than another's."),
    "rate of change": ("How quickly one quantity changes relative to another; constant for linear functions.", "[[3.3 Linear Functions and Gradient]]", "[[gradient]]", "Download speed (MB per second) and tokens processed per millisecond are rates of change in systems."),
    "y equals mx plus c": ("The standard form of a linear function: y = mx + c, where m is gradient and c is y-intercept.", "[[3.3 Linear Functions and Gradient]]", "[[gradient]]", "Linear models in ML and billing formulas often use y = mx + c to predict cost from usage."),
    "parabola": ("The U-shaped graph of a quadratic function.", "[[3.4 Quadratic Functions]]", "[[quadratic coefficient]]", "Loss surfaces near a minimum and projectile paths in games follow parabolic curves."),
    "turning point": ("The highest or lowest point on a parabola, also called the vertex.", "[[3.4 Quadratic Functions]]", "[[parabola]]", "Optimisation seeks a turning point where a cost or error function reaches its minimum."),
    "roots": ("The input values where a function's output equals zero.", "[[3.4 Quadratic Functions]]", "[[root]]", "Finding roots solves when an equation hits zero, such as when profit or signal strength crosses zero."),
    "axis of symmetry": ("The vertical line through a parabola's turning point that mirrors both sides.", "[[3.4 Quadratic Functions]]", "[[turning point]]", "Symmetry reduces search work in graphics and when locating the peak of a quadratic model."),
    "quadratic coefficient": ("The number multiplying x squared in ax² + bx + c; it controls whether the parabola opens up or down.", "[[3.4 Quadratic Functions]]", "[[coefficient]]", "The sign of the quadratic coefficient tells an optimiser whether a critical point is a minimum or maximum."),
    "polynomial": ("A sum of terms with non-negative whole-number powers of a variable, such as 3x² + 2x + 1.", "[[3.5 Polynomials]]", "[[quadratic coefficient]]", "Hash polynomials, error-correcting codes, and curve interpolation all use polynomial arithmetic."),
    "degree": ("The highest power of the variable in a polynomial.", "[[3.5 Polynomials]]", "[[polynomial]]", "Polynomial degree bounds how many turns a graph can have and how many roots it may possess."),
    "coefficient": ("The number multiplying a variable or power in a term.", "[[3.5 Polynomials]]", "[[constant]]", "Coefficients in a neural network are the learned weights that scale each input feature."),
    "root": ("An input value where a polynomial evaluates to zero.", "[[3.5 Polynomials]]", "[[roots]]", "Finding polynomial roots locates where an error function or signal crosses zero in numerical methods."),
    "leading term": ("The term with the highest degree in a polynomial, which dominates for large inputs.", "[[3.5 Polynomials]]", "[[degree]]", "For large n, algorithm cost is dominated by its leading term, which Big-O notation captures."),
    "exponential growth": ("Change where a quantity is repeatedly multiplied by a fixed factor greater than 1.", "[[3.6 Exponential Functions]]", "[[growth factor]]", "Viral spread, compound interest, and brute-force search trees often grow exponentially."),
    "growth factor": ("The multiplier applied each step in exponential growth, such as 2 in doubling.", "[[3.6 Exponential Functions]]", "[[base]]", "Each extra bit doubles addressable memory, so the growth factor is 2 in bit-capacity problems."),
    "decay factor": ("The multiplier between 0 and 1 applied each step in exponential decay.", "[[3.6 Exponential Functions]]", "[[growth factor]]", "Radioactive decay models and learning-rate schedules use decay factors below 1."),
    "base": ("The number being raised to a power in an exponential or logarithmic expression.", "[[3.6 Exponential Functions]]", "[[exponent]]", "Base-2 exponentials count binary combinations; base-e appears in continuous growth models."),
    "asymptote": ("A line a graph approaches but never reaches as inputs grow very large or very small.", "[[3.6 Exponential Functions]]", "[[exponential growth]]", "Horizontal asymptotes model capacity limits, such as maximum throughput a server approaches."),
    "logarithm": ("The inverse of exponentiation: log_b(a) asks which power of b gives a.", "[[3.7 Logarithms]]", "[[inverse operation]]", "Logarithms convert multiplication into addition and underpin binary search depth and Big-O log n costs."),
    "power": ("An expression like b^n meaning b multiplied by itself n times.", "[[3.7 Logarithms]]", "[[base]]", "Powers describe bit patterns, memory sizes, and the repeated squaring in fast exponentiation."),
    "inverse operation": ("An operation that undoes another, such as log undoing exponentiation.", "[[3.7 Logarithms]]", "[[inverse operations]]", "Decode undoes encode, decrypt undoes encrypt, and log undoes exp in the same structural way."),
    "log laws": ("Rules for simplifying logarithms, such as log(ab) = log(a) + log(b).", "[[3.7 Logarithms]]", "[[logarithm]]", "Log laws let complexity analysts combine costs of sequential and parallel stages in one expression."),
    "inverse function": ("A function f⁻¹ that undoes f so f⁻¹(f(x)) = x for every x in the domain.", "[[3.8 Inverse and Composite Functions]]", "[[function]]", "Encoding and decoding, encrypt and decrypt, and compress and decompress are inverse function pairs."),
    "composition": ("Applying one function after another: (f ∘ g)(x) = f(g(x)).", "[[3.8 Inverse and Composite Functions]]", "[[nested function]]", "Data pipelines, nested function calls, and shader chains are compositions of simpler functions."),
    "identity function": ("The function f(x) = x that returns each input unchanged.", "[[3.8 Inverse and Composite Functions]]", "[[function]]", "Identity mappings in databases and no-op transforms in pipelines behave like the identity function."),
    "one-to-one": ("A function where different inputs always give different outputs.", "[[3.8 Inverse and Composite Functions]]", "[[function]]", "Injective hash functions and reversible encodings must be one-to-one on their valid domain."),
    "nested function": ("A function applied inside another, written f(g(x)).", "[[3.8 Inverse and Composite Functions]]", "[[composition]]", "Nested calls like hash(encrypt(data)) and layered neural network layers are nested functions."),
    "translation": ("A shift of a graph up, down, left, or right without changing its shape.", "[[3.9 Transformations of Graphs]]", "[[transformation]]", "Panning a camera, offsetting sprite positions, and bias terms in ML are translations."),
    "reflection": ("A flip of a graph across an axis, such as replacing y with −y.", "[[3.9 Transformations of Graphs]]", "[[transformation]]", "Mirroring sprites, flipping image coordinates, and sign changes in symmetric models use reflection."),
    "stretch": ("A vertical or horizontal scaling that makes a graph taller, shorter, wider, or narrower.", "[[3.9 Transformations of Graphs]]", "[[scale factor]]", "Zooming axes, amplifying sensor signals, and weight scaling in networks are stretches."),
    "scale factor": ("The number that multiplies coordinates during a stretch or compression.", "[[3.9 Transformations of Graphs]]", "[[stretch]]", "Resolution scaling, normalisation constants, and learning rates act as scale factors on data or updates."),
    "transformation": ("Any rule that moves, flips, or scales a graph or shape.", "[[3.9 Transformations of Graphs]]", "[[translation]]", "Graphics pipelines, data normalisation, and feature scaling are sequences of transformations."),
    "piecewise rule": ("A function defined by different formulas on different input intervals.", "[[3.10 Piecewise and Step Functions]]", "[[interval]]", "Tax brackets, shipping tiers, and if-else pricing in code are piecewise rules."),
    "interval": ("A continuous set of input values, often written with inequality or bracket notation.", "[[3.10 Piecewise and Step Functions]]", "[[number line interval]]", "Valid input ranges, array index bounds, and timeout windows are intervals in programs."),
    "step function": ("A piecewise constant function whose graph looks like steps.", "[[3.10 Piecewise and Step Functions]]", "[[piecewise rule]]", "Quantised levels, threshold classifiers, and Heaviside switches behave like step functions."),
    "floor function": ("The function ⌊x⌋ that rounds down to the greatest integer less than or equal to x.", "[[3.10 Piecewise and Step Functions]]", "[[step function]]", "Integer division, array indexing, and binning data use floor-like rounding down."),
    "ceiling function": ("The function ⌈x⌉ that rounds up to the least integer greater than or equal to x.", "[[3.10 Piecewise and Step Functions]]", "[[floor function]]", "Allocating enough memory pages, pagination, and buffer sizing often use ceiling rounding."),
}

for term, (definition, introduced, builds_on, cs_use) in GLOSSARY.items():
    path = os.path.join(GLOSS_DIR, f"{term}.md")
    content = f"""# {term}
{definition}
## First introduced in
{introduced}
## Builds on
{builds_on}
## Used in CS
{cs_use}
"""
    write(path, content)

print(f"Glossary: {len(GLOSSARY)} terms written")
