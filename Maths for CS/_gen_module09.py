#!/usr/bin/env python3
"""Generate complete Module 09 Calculus topic bundles."""
import os

BASE = "/home/Marau/Marau/University/Maths for CS"
CALC = os.path.join(BASE, "09 Calculus")
WE = os.path.join(BASE, "90 Worked Examples")
PQ = os.path.join(BASE, "91 Practice Questions")
MT = os.path.join(BASE, "92 Mastery Tests")
ANS = os.path.join(BASE, "93 Answers and Mark Schemes")
GLO = os.path.join(BASE, "00 Glossary/Terms")

TOPICS = [
    {
        "id": "9.1", "name": "Limits and Continuity",
        "tags": "#maths/calculus #maths/limits #cs/numerical",
        "prereq": "[[8.11 Information Theory]]",
        "used_later": "[[9.2 Differentiation Basics]], [[10.4 Floating Point and Rounding Error]]",
        "plain": "A **limit** asks what value a function gets closer and closer to as the input moves toward some point — even if the function never actually reaches that point. **Continuity** means the graph has no jumps, holes, or breaks at that point: what you approach is exactly what you get.",
        "words": [
            ("limit", "the value a function approaches as the input gets closer to a target, even if the function is undefined there"),
            ("approach", "to get arbitrarily close to a number without necessarily reaching it"),
            ("continuity", "a function is continuous at a point when the limit equals the actual output there and the graph has no break"),
            ("one-sided limit", "the limit taken from only the left or only the right side of a point on the number line"),
            ("undefined point", "an input where a function has no valid output, often shown as a hole or vertical asymptote on the graph"),
        ],
        "backward": ["[[1.2 Place Value and Number Lines]]", "[[3.1 Coordinates and Axes]]", "[[3.2 Function Notation and Mapping]]", "[[3.3 Linear Functions and Gradient]]"],
        "forward": "[[9.2 Differentiation Basics]]",
        "cs_items": ["floating-point convergence checks", "animation frame interpolation", "numerical root-finding (Newton's method)", "rate limiter smoothing", "epsilon comparisons in unit tests"],
        "cs_conn": "Limits make rates of change and numerical approximations precise.",
    },
    {
        "id": "9.2", "name": "Differentiation Basics",
        "tags": "#maths/calculus #maths/derivatives #cs/optimisation",
        "prereq": "[[9.1 Limits and Continuity]], [[3.2 Function Notation and Mapping]]",
        "used_later": "[[9.3 Differentiation Rules]], [[10.9 Neural Network Maths]]",
        "plain": "The **derivative** measures how fast a function's output changes when the input changes by a tiny amount. It is the slope of the tangent line at a point — the **instantaneous rate of change**.",
        "words": [
            ("derivative", "the instantaneous rate of change of a function with respect to its input"),
            ("gradient function", "the rule f'(x) that gives the derivative at every point x in the domain"),
            ("tangent", "a straight line that touches a curve at exactly one point locally and has the same slope as the curve there"),
            ("rate of change", "how much the output increases or decreases per unit increase in the input"),
            ("first principles", "finding a derivative directly from the limit definition before using shortcut rules"),
        ],
        "backward": ["[[9.1 Limits and Continuity]]", "[[3.2 Function Notation and Mapping]]", "[[3.3 Linear Functions and Gradient]]"],
        "forward": "[[9.3 Differentiation Rules]]",
        "cs_items": ["velocity from position in game engines", "loss curve slope in ML training", "marginal cost in economics simulations", "automatic differentiation in PyTorch/TensorFlow", "gradient of a cost function"],
        "cs_conn": "Derivatives drive optimisation, graphics motion, and ML training.",
    },
    {
        "id": "9.3", "name": "Differentiation Rules",
        "tags": "#maths/calculus #maths/derivatives #cs/autodiff",
        "prereq": "[[9.2 Differentiation Basics]], [[3.2 Function Notation and Mapping]]",
        "used_later": "[[9.4 Applications of Differentiation]], [[11.8 Multivariable Calculus for Deep Learning]]",
        "plain": "Once you know the **first principles** definition, shortcut **rules** let you differentiate common expressions quickly: powers, products, quotients, chains, and implicit relations.",
        "words": [
            ("power rule", "for f(x)=x^n, the derivative is n·x^(n-1)"),
            ("product rule", "the derivative of u·v is u'·v + u·v'"),
            ("quotient rule", "the derivative of u/v is (u'·v − u·v') / v²"),
            ("chain rule", "the derivative of a composite function f(g(x)) is f'(g(x))·g'(x)"),
            ("implicit differentiation", "differentiating both sides of an equation when y is not written explicitly as a function of x"),
        ],
        "backward": ["[[9.2 Differentiation Basics]]", "[[2.9 Indices and Powers]]", "[[3.2 Function Notation and Mapping]]"],
        "forward": "[[9.4 Applications of Differentiation]]",
        "cs_items": ["automatic differentiation (autograd)", "backpropagation in neural networks", "symbolic differentiation in computer algebra", "gradient computation in optimisation libraries", "computational graph traversal"],
        "cs_conn": "Automatic differentiation uses structured differentiation rules.",
    },
    {
        "id": "9.4", "name": "Applications of Differentiation",
        "tags": "#maths/calculus #maths/optimisation #cs/scheduling",
        "prereq": "[[9.3 Differentiation Rules]], [[3.2 Function Notation and Mapping]]",
        "used_later": "[[9.5 Integration Basics]], [[9.9 Gradient Descent and Optimisation]]",
        "plain": "Derivatives tell you where a curve rises, falls, or turns. Setting the derivative to zero finds **stationary points** — candidates for **maxima** and **minima** that matter in optimisation.",
        "words": [
            ("turning point", "a point where a curve changes from increasing to decreasing or vice versa"),
            ("maximum", "a point where the function value is greater than or equal to all nearby values"),
            ("minimum", "a point where the function value is less than or equal to all nearby values"),
            ("stationary point", "a point where the first derivative equals zero"),
            ("second derivative", "the derivative of the derivative, used to classify stationary points as max, min, or inflection"),
        ],
        "backward": ["[[9.3 Differentiation Rules]]", "[[3.4 Quadratic Functions]]", "[[3.2 Function Notation and Mapping]]"],
        "forward": "[[9.5 Integration Basics]]",
        "cs_items": ["hyperparameter tuning", "resource allocation", "path smoothing in robotics", "profit maximisation models", "curve fitting in data science"],
        "cs_conn": "Optimisation appears in scheduling, ML, graphics, and resource allocation.",
    },
    {
        "id": "9.5", "name": "Integration Basics",
        "tags": "#maths/calculus #maths/integration #cs/probability",
        "prereq": "[[9.4 Applications of Differentiation]], [[3.2 Function Notation and Mapping]]",
        "used_later": "[[9.6 Integration Techniques]], [[8.5 Continuous Random Variables]]",
        "plain": "Integration reverses differentiation. It measures **accumulation** — total area under a curve, total distance from speed, total probability from a density.",
        "words": [
            ("integral", "the accumulated sum of infinitely many tiny contributions, written ∫f(x)dx"),
            ("area under curve", "the geometric interpretation of a definite integral between two x-values"),
            ("antiderivative", "a function F whose derivative is f; also called an indefinite integral"),
            ("constant of integration", "the +C added because many antiderivatives differ by a constant"),
            ("definite integral", "an integral with lower and upper limits that gives a number, not a family of functions"),
        ],
        "backward": ["[[9.4 Applications of Differentiation]]", "[[3.2 Function Notation and Mapping]]", "[[1.2 Place Value and Number Lines]]"],
        "forward": "[[9.6 Integration Techniques]]",
        "cs_items": ["probability density integration", "physics engine impulse calculations", "Monte Carlo area estimation", "cumulative distribution functions", "signal processing (area under waveform)"],
        "cs_conn": "Integration appears in probability, physics engines, and continuous models.",
    },
    {
        "id": "9.6", "name": "Integration Techniques",
        "tags": "#maths/calculus #maths/integration #cs/simulation",
        "prereq": "[[9.5 Integration Basics]], [[3.2 Function Notation and Mapping]]",
        "used_later": "[[9.7 Differential Equations Intro]], [[11.10 Numerical Methods and Stability]]",
        "plain": "Not every integral is a simple reverse power rule. **Substitution**, **integration by parts**, **partial fractions**, and **numerical methods** handle harder integrals that appear in science and engineering.",
        "words": [
            ("substitution", "changing the integration variable to simplify the integrand, reversing the chain rule"),
            ("integration by parts", "∫u dv = uv − ∫v du, reversing the product rule"),
            ("partial fractions", "decomposing a rational function into simpler fractions before integrating"),
            ("trig integral", "an integral involving sine, cosine, or other trigonometric functions"),
            ("numerical integration", "approximating a definite integral using finitely many sample points (trapezium, Simpson's rule)"),
        ],
        "backward": ["[[9.5 Integration Basics]]", "[[9.3 Differentiation Rules]]", "[[4.5 Trigonometry Basics]]"],
        "forward": "[[9.7 Differential Equations Intro]]",
        "cs_items": ["Simpson's rule in scientific computing", "quadrature in numerical libraries (SciPy)", "physics simulation time steps", "rendering area calculations", "Bayesian inference normalising constants"],
        "cs_conn": "Numerical integration supports simulation and scientific computing.",
    },
    {
        "id": "9.7", "name": "Differential Equations Intro",
        "tags": "#maths/calculus #maths/differential-equations #cs/modelling",
        "prereq": "[[9.6 Integration Techniques]]",
        "used_later": "[[9.8 Multivariable Functions]], [[11.10 Numerical Methods and Stability]]",
        "plain": "A **differential equation** relates a quantity to how fast it changes. Given an **initial condition**, you find the **solution curve** that models growth, decay, or motion over time.",
        "words": [
            ("differential equation", "an equation involving a function and one or more of its derivatives"),
            ("initial condition", "a known value at a starting time or position that picks one solution from a family"),
            ("solution curve", "the function y(t) or y(x) that satisfies the differential equation everywhere in its domain"),
            ("growth model", "a differential equation where the rate of change is proportional to the current amount (dy/dt = ky)"),
            ("decay model", "a growth model with negative rate constant, modelling radioactive decay or cooling"),
        ],
        "backward": ["[[9.6 Integration Techniques]]", "[[9.5 Integration Basics]]", "[[3.2 Function Notation and Mapping]]"],
        "forward": "[[9.8 Multivariable Functions]]",
        "cs_items": ["population dynamics in simulations", "queueing theory (M/M/1 models)", "PID control loops", "epidemic SIR models", "exponential backoff in networking"],
        "cs_conn": "Population models, queues, physics, and control systems use differential equations.",
    },
    {
        "id": "9.8", "name": "Multivariable Functions",
        "tags": "#maths/calculus #maths/multivariable #cs/machine-learning",
        "prereq": "[[9.7 Differential Equations Intro]]",
        "used_later": "[[9.9 Gradient Descent and Optimisation]], [[10.8 Machine Learning Vectors and Matrices]]",
        "plain": "Real models rarely depend on one input. A **multivariable function** takes several inputs and produces one output. **Partial derivatives** measure change in one direction while holding others fixed.",
        "words": [
            ("partial derivative", "the derivative of a multivariable function with respect to one variable, treating others as constants"),
            ("gradient vector", "the vector of all partial derivatives, pointing in the direction of steepest increase"),
            ("level curve", "a curve where the function has a constant value, like contour lines on a map"),
            ("surface", "the 3D graph z = f(x,y) of a function of two variables"),
            ("Jacobian", "the matrix of all first-order partial derivatives of a vector-valued function"),
        ],
        "backward": ["[[9.7 Differential Equations Intro]]", "[[7.1 Vectors in 2D and 3D]]", "[[3.2 Function Notation and Mapping]]"],
        "forward": "[[9.9 Gradient Descent and Optimisation]]",
        "cs_items": ["loss functions with many weights", "image height maps (surfaces)", "sensor fusion with multiple inputs", "Jacobian in backpropagation", "contour plots for visualising loss landscapes"],
        "cs_conn": "ML models depend on many variables at once.",
    },
    {
        "id": "9.9", "name": "Gradient Descent and Optimisation",
        "tags": "#maths/calculus #maths/optimisation #cs/machine-learning",
        "prereq": "[[9.8 Multivariable Functions]], [[3.2 Function Notation and Mapping]]",
        "used_later": "[[9.10 Convex Optimisation Basics]], [[10.9 Neural Network Maths]], [[11.7 Advanced Optimisation for ML]]",
        "plain": "**Gradient descent** repeatedly steps in the direction opposite to the **gradient** of an **objective function**, using a **learning rate** to control step size, until the values **converge** toward a **local minimum**.",
        "words": [
            ("objective function", "the function whose value you want to minimise (or maximise) during optimisation"),
            ("learning rate", "a positive step-size parameter controlling how far each gradient descent update moves"),
            ("gradient descent", "an iterative algorithm that updates parameters in the direction of steepest decrease of a loss function"),
            ("local minimum", "a point where the function is lowest in its immediate neighbourhood but not necessarily globally"),
            ("convergence", "the property that successive iterates get arbitrarily close to a limit point or optimum"),
        ],
        "backward": ["[[9.8 Multivariable Functions]]", "[[9.4 Applications of Differentiation]]", "[[3.2 Function Notation and Mapping]]"],
        "forward": "[[9.10 Convex Optimisation Basics]], [[10.9 Neural Network Maths]], [[11.7 Advanced Optimisation for ML]]",
        "cs_items": ["SGD in PyTorch/TensorFlow", "weight updates in neural networks", "learning rate schedulers", "mini-batch training loops", "loss convergence monitoring"],
        "cs_conn": "Gradient descent is central to modern machine learning.",
    },
    {
        "id": "9.10", "name": "Convex Optimisation Basics",
        "tags": "#maths/calculus #maths/optimisation #cs/convex",
        "prereq": "[[9.9 Gradient Descent and Optimisation]], [[3.2 Function Notation and Mapping]]",
        "used_later": "[[10.1 Big O Theta and Omega]], [[11.7 Advanced Optimisation for ML]]",
        "plain": "A **convex function** curves upward like a bowl — any local minimum is also the **global minimum**. **Convex sets** and **constraints** let you solve optimisation problems where gradient descent is guaranteed to succeed.",
        "words": [
            ("convex function", "a function whose graph lies below every chord connecting two points on the curve"),
            ("convex set", "a set where the line segment between any two points in the set stays inside the set"),
            ("global minimum", "the lowest value of a function over its entire domain, not just locally"),
            ("constraint", "a condition that limits which input values are allowed in an optimisation problem"),
            ("Lagrange multiplier", "a scalar introduced to incorporate equality constraints into an unconstrained optimisation"),
        ],
        "backward": ["[[9.9 Gradient Descent and Optimisation]]", "[[9.4 Applications of Differentiation]]", "[[3.2 Function Notation and Mapping]]"],
        "forward": "[[10.1 Big O Theta and Omega]], [[11.7 Advanced Optimisation for ML]]",
        "cs_items": ["SVM hinge loss (convex)", "linear programming in OR-Tools", "Lasso regression", "portfolio optimisation", "support vector machines"],
        "cs_conn": "Convex optimisation appears in ML, operations research, and resource allocation.",
    },
]

def topic_note(t):
    tid, name = t["id"], t["name"]
    wlinks = "\n".join(f"- [[{w[0]}]] - {w[1]}." for w in t["words"])
    bw = ", ".join(t["backward"])
    cs_list = "\n".join(f"- {c}" for c in t["cs_items"])
    fn = f"{tid} {name}.md"
    concepts = make_concepts(t)
    return f"""# {tid} {name}

Tags: {t["tags"]}

## Position in the Course
Prerequisites: {t["prereq"]}

Used later in: {t["used_later"]}

Mastery threshold: 85% overall, and 100% on the New Words section.

> [!tip] How to study this note
> Read one concept, cover it, then explain it aloud in your own words. After each example, copy the problem onto paper and solve it again without looking.

## Plain-English Idea
{t["plain"]}

> [!example] Everyday idea
> Think of {name.lower()} as a precise tool: you name the objects, apply the rule step by step, and check whether the answer makes sense in context.

## New Words
{wlinks}

You pass this topic only when you can define all five terms without looking.

{concepts}

## Why This Works
Maths works by preserving meaning while changing form. Each step in {name.lower()} keeps the original problem equivalent to the new line. The permission for each step comes from earlier topics: {bw}.

If you cannot explain why a step is legal, slow down and return to the prerequisite notes.

## Worked Examples
For fully worked solutions, use [[{tid} {name} - Worked Examples]].

## Common Mistakes
- Plugging the limit value directly into an expression when the function is undefined there — use the limit definition or algebra instead.
- Forgetting the constant of integration (+C) in indefinite integrals.
- Confusing a local minimum with a global minimum on non-convex functions.
- Applying the chain rule but forgetting to multiply by the inner derivative.
- Using a learning rate that is too large, causing divergence in gradient descent.
- Treating a special example as if it proves every case.

> [!failure] Mistake pattern
> If your derivative or integral looks right but fails a quick check, substitute a simple value or differentiate your answer back — the inverse operation catches most sign and coefficient errors.

## Where This Shows Up in CS
{t["cs_conn"]}

Specific programming objects:

{cs_list}

## Checkpoint Questions
Answer these before using the practice sheet.

1. What is the main problem {name.lower()} helps you solve?
2. Define {t["words"][0][0]} in your own words.
3. Define {t["words"][1][0]} in your own words.
4. Define {t["words"][2][0]} in your own words.
5. Give one tiny example and label every part.
6. What prerequisite idea would you revisit if this topic felt confusing?
7. How does this topic connect to {t["cs_items"][0]}?
8. What is the difference between {t["words"][3][0]} and {t["words"][4][0]}?
9. Write one sentence explaining why this topic belongs in a CS maths course.
10. Which later topic depends most directly on this one?

## Mini-Quiz
1. Write the plain-English meaning of {tid} {name}.
2. Define all five New Words from memory.
3. Solve a basic problem from this topic without looking at notes.
4. Make one deliberate mistake, then explain why it is wrong.
5. Create a harder example by changing one number or condition.
6. Check your answer using a second method.
7. Explain where this topic appears in computer science.
8. State which later topic depends on this one.
9. Draw or sketch a diagram that illustrates the main idea.
10. Write a two-sentence explanation for someone who has never seen this topic.

## Pass Gate
You may move to {t["forward"].split(",")[0].strip()} only when you can:

- define every term in [[#New Words]]
- solve one worked example from a blank page
- explain one CS use case in plain English
- answer at least 9 out of 10 mini-quiz questions correctly
- complete [[{tid} {name} - Mastery Test]] with at least 85%

## Related Notes
Backward links: {bw}

Forward links: {t["forward"]}

Assessment links: [[{tid} {name} - Worked Examples]], [[{tid} {name} - Practice Questions]], [[{tid} {name} - Mastery Test]], [[{tid} {name} - Answers]]
"""

def make_concepts(t):
    """Generate 6 concept sections per topic."""
    tid, name = t["id"], t["name"]
    w = [x[0] for x in t["words"]]
    sections = []

    if tid == "9.1":
        sections = [
            ("Concept 1 - What a Limit Asks", w[0], w[1],
             "Question: What is $\\lim_{x \\to 2} (3x + 1)$?\n\nStep 1: As $x$ **approaches** 2, the expression $3x+1$ approaches $3(2)+1$.\n\nStep 2: Substitute $x=2$: $3(2)+1 = 7$.\n\nAnswer: The **limit** is **7**.",
             "tip", "A limit asks what value the output gets close to — not necessarily what the output equals at that exact input."),
            ("Concept 2 - Limits on the Number Line", w[1], w[3],
             "Question: Describe $\\lim_{x \\to 0^+} \\frac{1}{x}$ using the [[number line]].\n\nStep 1: $x \\to 0^+$ means $x$ approaches 0 from the right (positive side).\n\nStep 2: As $x$ gets smaller but stays positive, $\\frac{1}{x}$ grows without bound.\n\nAnswer: The **one-sided limit** is $+\\infty$.",
             "important", "The notation $0^+$ means approach from the right on the [[number line]] from [[1.2 Place Value and Number Lines]]."),
            ("Concept 3 - Functions and Their Graphs", w[0], w[4],
             "Question: For $f(x) = \\frac{x^2 - 1}{x - 1}$, what is $\\lim_{x \\to 1} f(x)$?\n\nStep 1: At $x=1$, the denominator is 0 — the point is **undefined**.\n\nStep 2: Factor: $\\frac{(x-1)(x+1)}{x-1} = x+1$ for $x \\neq 1$.\n\nStep 3: As $x \\to 1$, $x+1 \\to 2$.\n\nAnswer: The limit is **2** even though $f(1)$ is undefined.",
             "example", "A [[function]] from [[3.2 Function Notation and Mapping]] can have a limit at a point even when the function value does not exist there."),
            ("Concept 4 - One-Sided Limits", w[3], w[0],
             "Question: For $f(x) = |x|/x$, find the left and right limits at 0.\n\nStep 1: For $x > 0$, $|x|/x = 1$. So $\\lim_{x \\to 0^+} = 1$.\n\nStep 2: For $x < 0$, $|x|/x = -1$. So $\\lim_{x \\to 0^-} = -1$.\n\nStep 3: Left and right limits differ.\n\nAnswer: The two-sided limit **does not exist**.",
             "warning", "A two-sided limit exists only when both one-sided limits exist and are equal."),
            ("Concept 5 - Continuity", w[2], w[4],
             "Question: Is $f(x) = x^2$ continuous at $x = 3$?\n\nStep 1: $f(3) = 9$.\n\nStep 2: $\\lim_{x \\to 3} x^2 = 9$.\n\nStep 3: Limit equals function value.\n\nAnswer: Yes, $f$ is **continuous** at $x=3$.",
             "important", "**Continuity** at $a$ requires: (1) $f(a)$ is defined, (2) the limit exists, (3) they are equal."),
            ("Concept 6 - Limits in CS", w[0], w[1],
             "Question: A loop computes $s_n = \\sum_{i=1}^{n} \\frac{1}{2^i}$. What value does $s_n$ approach?\n\nStep 1: This is a geometric series with ratio $\\frac{1}{2}$.\n\nStep 2: As $n \\to \\infty$, the sum approaches $\\frac{1/2}{1 - 1/2} = 1$.\n\nAnswer: The sequence **converges** to **1** — like a limit in code checking `abs(s - 1) < epsilon`.",
             "example", "Floating-point loops test convergence the same way: stop when the change is below a tolerance."),
        ]
    elif tid == "9.2":
        sections = [
            ("Concept 1 - Rate of Change", w[3], w[0],
             "Question: A car's position is $s(t) = t^2$ metres. What is its speed at $t=3$?\n\nStep 1: Speed is the **rate of change** of position.\n\nStep 2: We need the **derivative** $s'(t) = 2t$.\n\nStep 3: $s'(3) = 6$ m/s.\n\nAnswer: Speed at $t=3$ is **6 m/s**.",
             "tip", "The derivative answers: how fast is the output changing right now?"),
            ("Concept 2 - The Tangent Line", w[2], w[0],
             "Question: Find the slope of the tangent to $y = x^2$ at $x = 2$.\n\nStep 1: The derivative is $2x$.\n\nStep 2: At $x=2$: slope = $2(2) = 4$.\n\nStep 3: The **tangent** line is $y - 4 = 4(x - 2)$.\n\nAnswer: Slope is **4**.",
             "example", "The tangent touches the curve at one point and has the same slope as the curve there."),
            ("Concept 3 - First Principles", w[4], w[0],
             "Question: Find $\\frac{d}{dx}(x^2)$ from **first principles**.\n\nStep 1: $f'(x) = \\lim_{h \\to 0} \\frac{(x+h)^2 - x^2}{h}$.\n\nStep 2: Expand: $\\frac{x^2 + 2xh + h^2 - x^2}{h} = \\frac{2xh + h^2}{h} = 2x + h$.\n\nStep 3: As $h \\to 0$: $f'(x) = 2x$.\n\nAnswer: $\\frac{d}{dx}(x^2) = 2x$.",
             "important", "First principles uses the [[limit]] from [[9.1 Limits and Continuity]]."),
            ("Concept 4 - The Gradient Function", w[1], w[0],
             "Question: If $f(x) = 3x^2 - 2x + 1$, find $f'(x)$.\n\nStep 1: Differentiate term by term: $6x - 2$.\n\nStep 2: The constant 1 differentiates to 0.\n\nAnswer: $f'(x) = 6x - 2$.",
             "tip", "The **gradient function** gives the slope at every point in one formula."),
            ("Concept 5 - Notation", w[0], w[1],
             "Question: If $y = x^3$, write the derivative in three notations.\n\nStep 1: $\\frac{dy}{dx} = 3x^2$.\n\nStep 2: Also written $y' = 3x^2$ or $f'(x) = 3x^2$.\n\nAnswer: All three mean the same **derivative**.",
             "warning", "Do not confuse $\\frac{dy}{dx}$ (derivative) with $\\frac{\\Delta y}{\\Delta x}$ (average rate over an interval)."),
            ("Concept 6 - Derivatives in CS", w[3], w[0],
             "Question: Loss $L(w) = (w - 3)^2$. What is $\\frac{dL}{dw}$ at $w=1$?\n\nStep 1: $L'(w) = 2(w-3)$.\n\nStep 2: $L'(1) = 2(1-3) = -4$.\n\nAnswer: Slope is **-4** — loss decreases if we increase $w$.",
             "example", "In ML, the derivative of the loss tells you which direction to adjust each weight."),
        ]
    elif tid == "9.3":
        sections = [
            ("Concept 1 - Power Rule", w[0], w[4],
             "Question: Differentiate $f(x) = x^5$.\n\nStep 1: Apply the **power rule**: bring the power down, reduce by 1.\n\nStep 2: $f'(x) = 5x^4$.\n\nAnswer: $f'(x) = 5x^4$.",
             "tip", "For $x^n$: derivative is $nx^{n-1}$. Works for any real $n$."),
            ("Concept 2 - Product Rule", w[1], w[0],
             "Question: Differentiate $f(x) = x^2 \\cdot \\sin x$.\n\nStep 1: Let $u = x^2$, $v = \\sin x$. Then $u' = 2x$, $v' = \\cos x$.\n\nStep 2: $f' = u'v + uv' = 2x\\sin x + x^2\\cos x$.\n\nAnswer: $f'(x) = 2x\\sin x + x^2\\cos x$.",
             "example", "The **product rule**: $(uv)' = u'v + uv'$."),
            ("Concept 3 - Quotient Rule", w[2], w[1],
             "Question: Differentiate $f(x) = \\frac{x}{x+1}$.\n\nStep 1: $u = x$, $v = x+1$. $u' = 1$, $v' = 1$.\n\nStep 2: $f' = \\frac{1 \\cdot (x+1) - x \\cdot 1}{(x+1)^2} = \\frac{1}{(x+1)^2}$.\n\nAnswer: $f'(x) = \\frac{1}{(x+1)^2}$.",
             "important", "Quotient rule: $\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$."),
            ("Concept 4 - Chain Rule", w[3], w[0],
             "Question: Differentiate $f(x) = (3x + 1)^4$.\n\nStep 1: Outer function: $u^4$, inner: $u = 3x+1$.\n\nStep 2: $f' = 4(3x+1)^3 \\cdot 3 = 12(3x+1)^3$.\n\nAnswer: $f'(x) = 12(3x+1)^3$.",
             "warning", "Never forget the inner derivative — that is the most common chain rule mistake."),
            ("Concept 5 - Implicit Differentiation", w[4], w[3],
             "Question: If $x^2 + y^2 = 25$, find $\\frac{dy}{dx}$.\n\nStep 1: Differentiate both sides: $2x + 2y\\frac{dy}{dx} = 0$.\n\nStep 2: Solve: $\\frac{dy}{dx} = -\\frac{x}{y}$.\n\nAnswer: $\\frac{dy}{dx} = -x/y$.",
             "example", "**Implicit differentiation** treats $y$ as a function of $x$ without solving for $y$ first."),
            ("Concept 6 - Rules in Autograd", w[3], w[1],
             "Question: In a computational graph, $z = x \\cdot y$ with $x=2, y=3$. If $\\frac{\\partial L}{\\partial z} = 5$, find $\\frac{\\partial L}{\\partial x}$.\n\nStep 1: By product rule in reverse: $\\frac{\\partial L}{\\partial x} = \\frac{\\partial L}{\\partial z} \\cdot y$.\n\nStep 2: $= 5 \\cdot 3 = 15$.\n\nAnswer: $\\frac{\\partial L}{\\partial x} = 15$.",
             "example", "Automatic differentiation applies the same rules in reverse during backpropagation."),
        ]
    elif tid == "9.4":
        sections = [
            ("Concept 1 - Stationary Points", w[3], w[0],
             "Question: Find stationary points of $f(x) = x^3 - 3x$.\n\nStep 1: $f'(x) = 3x^2 - 3 = 0$.\n\nStep 2: $x^2 = 1$, so $x = \\pm 1$.\n\nAnswer: **Stationary points** at $x = -1$ and $x = 1$.",
             "tip", "Set $f'(x) = 0$ to find candidates for maxima and minima."),
            ("Concept 2 - Classifying with Second Derivative", w[4], w[1],
             "Question: Classify the stationary points of $f(x) = x^3 - 3x$.\n\nStep 1: $f''(x) = 6x$.\n\nStep 2: At $x=-1$: $f''(-1) = -6 < 0$ → **maximum**.\n\nStep 3: At $x=1$: $f''(1) = 6 > 0$ → **minimum**.\n\nAnswer: Maximum at $(-1, 2)$, minimum at $(1, -2)$.",
             "important", "$f'' > 0$ → minimum; $f'' < 0$ → maximum; $f'' = 0$ → inconclusive."),
            ("Concept 3 - Turning Points", w[0], w[3],
             "Question: Where does $f(x) = x^2 - 4x + 3$ turn?\n\nStep 1: $f'(x) = 2x - 4 = 0$ → $x = 2$.\n\nStep 2: $f(2) = 4 - 8 + 3 = -1$.\n\nAnswer: **Turning point** (minimum) at $(2, -1)$.",
             "example", "A **turning point** is where the curve changes direction."),
            ("Concept 4 - Optimisation Problems", w[1], w[2],
             "Question: A rectangle has perimeter 20. What dimensions maximise area?\n\nStep 1: Let sides be $x$ and $10-x$. Area $A = x(10-x) = 10x - x^2$.\n\nStep 2: $A' = 10 - 2x = 0$ → $x = 5$.\n\nStep 3: $A'' = -2 < 0$ → maximum.\n\nAnswer: Square with sides **5** gives maximum area **25**.",
             "tip", "Express the quantity to optimise as a function of one variable."),
            ("Concept 5 - Increasing and Decreasing", w[3], w[0],
             "Question: Where is $f(x) = x^3 - 3x$ increasing?\n\nStep 1: $f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$.\n\nStep 2: $f' > 0$ when $x < -1$ or $x > 1$.\n\nAnswer: Increasing on $(-\\infty, -1) \\cup (1, \\infty)$.",
             "warning", "Use a sign table for $f'$ to find where the function rises or falls."),
            ("Concept 6 - Optimisation in CS", w[1], w[2],
             "Question: A server cost is $C(n) = n^2 - 10n + 100$ for $n$ threads. Find optimal $n$.\n\nStep 1: $C'(n) = 2n - 10 = 0$ → $n = 5$.\n\nStep 2: $C'' = 2 > 0$ → minimum cost.\n\nAnswer: Use **5 threads** for minimum cost.",
             "example", "Setting the derivative to zero finds optimal parameters in resource allocation."),
        ]
    elif tid == "9.5":
        sections = [
            ("Concept 1 - Integration Reverses Differentiation", w[2], w[0],
             "Question: Find $\\int 2x \\, dx$.\n\nStep 1: What function has derivative $2x$? Answer: $x^2$.\n\nStep 2: Check: $\\frac{d}{dx}(x^2) = 2x$. ✓\n\nAnswer: $\\int 2x \\, dx = x^2 + C$.",
             "tip", "An **antiderivative** is any function whose derivative gives the integrand."),
            ("Concept 2 - The Constant of Integration", w[3], w[2],
             "Question: Why is $\\int 2x \\, dx = x^2 + C$ and not just $x^2$?\n\nStep 1: $\\frac{d}{dx}(x^2 + 5) = 2x$ too.\n\nStep 2: Any constant works because its derivative is 0.\n\nAnswer: **+C** captures all possible antiderivatives.",
             "important", "Never forget **+C** in indefinite integrals."),
            ("Concept 3 - Definite Integrals and Area", w[4], w[1],
             "Question: Find $\\int_0^2 2x \\, dx$.\n\nStep 1: Antiderivative is $x^2$.\n\nStep 2: Evaluate: $[x^2]_0^2 = 4 - 0 = 4$.\n\nAnswer: The **definite integral** is **4** — the **area under the curve** $y=2x$ from 0 to 2.",
             "example", "A definite integral gives a number: the signed area between the curve and the x-axis."),
            ("Concept 4 - Basic Integration Rules", w[0], w[2],
             "Question: Find $\\int (3x^2 + 1) \\, dx$.\n\nStep 1: $\\int 3x^2 \\, dx = x^3$.\n\nStep 2: $\\int 1 \\, dx = x$.\n\nAnswer: $x^3 + x + C$.",
             "tip", "Integrate term by term. Reverse the power rule: $\\int x^n \\, dx = \\frac{x^{n+1}}{n+1} + C$."),
            ("Concept 5 - Area Interpretation", w[1], w[4],
             "Question: What does $\\int_1^3 x \\, dx$ represent geometrically?\n\nStep 1: Compute: $[\\frac{x^2}{2}]_1^3 = \\frac{9}{2} - \\frac{1}{2} = 4$.\n\nStep 2: This is the area of a trapezium under $y=x$ from 1 to 3.\n\nAnswer: **Area = 4** square units.",
             "warning", "If the curve goes below the x-axis, the integral gives negative area — watch the sign."),
            ("Concept 6 - Integration in Probability", w[0], w[4],
             "Question: A PDF is $f(x) = 2x$ on $[0,1]$. Verify it integrates to 1.\n\nStep 1: $\\int_0^1 2x \\, dx = [x^2]_0^1 = 1$.\n\nAnswer: Valid PDF — total probability is **1**.",
             "example", "Continuous probability requires the integral of the density over the whole domain to equal 1."),
        ]
    elif tid == "9.6":
        sections = [
            ("Concept 1 - Integration by Substitution", w[0], w[4],
             "Question: Find $\\int 2x(x^2 + 1)^3 \\, dx$.\n\nStep 1: Let $u = x^2 + 1$, so $du = 2x \\, dx$.\n\nStep 2: $\\int u^3 \\, du = \\frac{u^4}{4} + C$.\n\nStep 3: Substitute back: $\\frac{(x^2+1)^4}{4} + C$.\n\nAnswer: $\\frac{(x^2+1)^4}{4} + C$.",
             "tip", "**Substitution** reverses the chain rule — look for a function and its derivative together."),
            ("Concept 2 - Integration by Parts", w[1], w[0],
             "Question: Find $\\int x e^x \\, dx$.\n\nStep 1: Let $u = x$, $dv = e^x dx$. Then $du = dx$, $v = e^x$.\n\nStep 2: $\\int u \\, dv = uv - \\int v \\, du = xe^x - \\int e^x dx$.\n\nStep 3: $= xe^x - e^x + C = e^x(x-1) + C$.\n\nAnswer: $e^x(x-1) + C$.",
             "important", "Choose $u$ using LIATE: Log, Inverse trig, Algebraic, Trig, Exponential — pick $u$ earlier in the list."),
            ("Concept 3 - Partial Fractions", w[2], w[0],
             "Question: Find $\\int \\frac{1}{x^2 - 1} \\, dx$.\n\nStep 1: $\\frac{1}{x^2-1} = \\frac{1/2}{x-1} - \\frac{1/2}{x+1}$.\n\nStep 2: $\\int = \\frac{1}{2}\\ln|x-1| - \\frac{1}{2}\\ln|x+1| + C$.\n\nAnswer: $\\frac{1}{2}\\ln\\left|\\frac{x-1}{x+1}\\right| + C$.",
             "example", "**Partial fractions** decompose a rational function into simpler pieces."),
            ("Concept 4 - Trigonometric Integrals", w[3], w[0],
             "Question: Find $\\int \\sin x \\, dx$.\n\nStep 1: Antiderivative of $\\sin x$ is $-\\cos x$.\n\nAnswer: $-\\cos x + C$.",
             "tip", "Memorise: $\\int \\sin x \\, dx = -\\cos x + C$ and $\\int \\cos x \\, dx = \\sin x + C$."),
            ("Concept 5 - Numerical Integration", w[4], w[1],
             "Question: Approximate $\\int_0^1 x^2 \\, dx$ using the trapezium rule with 2 strips.\n\nStep 1: $h = 0.5$. Points: $x=0, 0.5, 1$. Values: 0, 0.25, 1.\n\nStep 2: $\\approx \\frac{h}{2}(0 + 2(0.25) + 1) = 0.25(1.5) = 0.375$.\n\nStep 3: Exact value: $\\frac{1}{3} \\approx 0.333$.\n\nAnswer: Trapezium estimate **0.375** (slightly high).",
             "warning", "More strips generally improve accuracy but cost more computation."),
            ("Concept 6 - Numerical Integration in Code", w[4], w[0],
             "Question: Why use numerical integration when symbolic methods exist?\n\nStep 1: Many real integrals have no closed-form antiderivative.\n\nStep 2: Numerical methods work for any integrable function given sample points.\n\nAnswer: Libraries like SciPy use adaptive quadrature for integrals that cannot be solved by hand.",
             "example", "Bayesian normalising constants and physics simulations often require numerical integration."),
        ]
    elif tid == "9.7":
        sections = [
            ("Concept 1 - What Is a Differential Equation?", w[0], w[2],
             "Question: Is $\\frac{dy}{dx} = 2x$ a differential equation?\n\nStep 1: It relates $y$ to its derivative $\\frac{dy}{dx}$.\n\nStep 2: Yes — it is a **differential equation**.\n\nAnswer: **Yes**. The **solution** is $y = x^2 + C$.",
             "tip", "A DE contains unknown functions and their derivatives."),
            ("Concept 2 - Initial Conditions", w[1], w[2],
             "Question: Solve $\\frac{dy}{dx} = 2x$ with $y(0) = 3$.\n\nStep 1: General solution: $y = x^2 + C$.\n\nStep 2: $y(0) = 3$ gives $C = 3$.\n\nAnswer: Particular **solution curve**: $y = x^2 + 3$.",
             "important", "An **initial condition** picks one solution from the family."),
            ("Concept 3 - Growth Models", w[3], w[0],
             "Question: Solve $\\frac{dP}{dt} = 0.05P$ with $P(0) = 1000$.\n\nStep 1: This is exponential **growth**: $P = P_0 e^{kt}$.\n\nStep 2: $P(t) = 1000 e^{0.05t}$.\n\nAnswer: Population grows exponentially: $P(t) = 1000e^{0.05t}$.",
             "example", "The **growth model** $\\frac{dy}{dt} = ky$ has solution $y = y_0 e^{kt}$."),
            ("Concept 4 - Decay Models", w[4], w[3],
             "Question: Solve $\\frac{dN}{dt} = -0.1N$ with $N(0) = 500$.\n\nStep 1: Negative rate → **decay**.\n\nStep 2: $N(t) = 500 e^{-0.1t}$.\n\nAnswer: $N(t) = 500e^{-0.1t}$ — halves roughly every 6.93 time units.",
             "warning", "Decay is growth with negative $k$."),
            ("Concept 5 - Separable Equations", w[0], w[1],
             "Question: Solve $\\frac{dy}{dx} = xy$ with $y(0) = 2$.\n\nStep 1: Separate: $\\frac{dy}{y} = x \\, dx$.\n\nStep 2: Integrate: $\\ln|y| = \\frac{x^2}{2} + C$.\n\nStep 3: $y(0) = 2$ → $C = \\ln 2$.\n\nAnswer: $y = 2e^{x^2/2}$.",
             "tip", "Separable DEs let you put all $y$ terms on one side and all $x$ terms on the other."),
            ("Concept 6 - DEs in CS", w[3], w[4],
             "Question: A cache hit rate decays as $\\frac{dH}{dt} = -0.2H$. If $H(0) = 1$, find $H(5)$.\n\nStep 1: $H(t) = e^{-0.2t}$.\n\nStep 2: $H(5) = e^{-1} \\approx 0.368$.\n\nAnswer: Hit rate drops to about **37%** after 5 time units.",
             "example", "Exponential decay models cache eviction, radioactive decay, and network packet loss."),
        ]
    elif tid == "9.8":
        sections = [
            ("Concept 1 - Functions of Two Variables", w[3], w[0],
             "Question: If $f(x,y) = x^2 + y^2$, find $f(3,4)$.\n\nStep 1: Substitute: $f(3,4) = 9 + 16 = 25$.\n\nAnswer: $f(3,4) = 25$.",
             "tip", "A multivariable function takes several inputs and gives one output."),
            ("Concept 2 - Partial Derivatives", w[0], w[1],
             "Question: Find $\\frac{\\partial f}{\\partial x}$ and $\\frac{\\partial f}{\\partial y}$ for $f(x,y) = x^2y + 3y$.\n\nStep 1: $\\frac{\\partial f}{\\partial x} = 2xy$ (treat $y$ as constant).\n\nStep 2: $\\frac{\\partial f}{\\partial y} = x^2 + 3$.\n\nAnswer: $\\frac{\\partial f}{\\partial x} = 2xy$, $\\frac{\\partial f}{\\partial y} = x^2 + 3$.",
             "important", "A **partial derivative** differentiates with respect to one variable, holding others fixed."),
            ("Concept 3 - The Gradient Vector", w[1], w[0],
             "Question: Find the gradient of $f(x,y) = x^2 + y^2$ at $(1,2)$.\n\nStep 1: $\\nabla f = (2x, 2y)$.\n\nStep 2: At $(1,2)$: $\\nabla f = (2, 4)$.\n\nAnswer: **Gradient vector** is $(2, 4)$ — points uphill steepest.",
             "example", "The gradient points in the direction of steepest increase."),
            ("Concept 4 - Level Curves", w[2], w[3],
             "Question: Sketch level curves of $f(x,y) = x^2 + y^2$.\n\nStep 1: Set $x^2 + y^2 = c$ for constant $c$.\n\nStep 2: These are circles centred at the origin.\n\nAnswer: **Level curves** are concentric circles — like contour lines on a hill.",
             "tip", "Level curves never cross (for continuous functions) and the gradient is perpendicular to them."),
            ("Concept 5 - Surfaces", w[3], w[2],
             "Question: Describe the surface $z = x^2 + y^2$.\n\nStep 1: At each $(x,y)$, height is $x^2+y^2$.\n\nStep 2: Minimum at origin, rises in all directions.\n\nAnswer: A bowl-shaped **surface** (paraboloid).",
             "example", "The graph $z = f(x,y)$ is a surface in 3D space."),
            ("Concept 6 - The Jacobian in ML", w[4], w[1],
             "Question: For $\\mathbf{f}(x,y) = (x+y, xy)$, write the Jacobian matrix.\n\nStep 1: $\\frac{\\partial f_1}{\\partial x} = 1$, $\\frac{\\partial f_1}{\\partial y} = 1$.\n\nStep 2: $\\frac{\\partial f_2}{\\partial x} = y$, $\\frac{\\partial f_2}{\\partial y} = x$.\n\nAnswer: $J = \\begin{pmatrix} 1 & 1 \\\\ y & x \\end{pmatrix}$.",
             "example", "The **Jacobian** generalises the gradient to vector-valued functions."),
        ]
    elif tid == "9.9":
        sections = [
            ("Concept 1 - The Objective Function", w[0], w[3],
             "Question: In ML, $L(w) = (w - 4)^2 + 1$ is the loss. What is the minimum?\n\nStep 1: Minimum where $L'(w) = 2(w-4) = 0$ → $w = 4$.\n\nStep 2: $L(4) = 1$.\n\nAnswer: **Objective function** minimum is **1** at $w = 4$.",
             "tip", "The objective function is what you minimise — often called loss or cost in ML."),
            ("Concept 2 - The Gradient Descent Update", w[2], w[1],
             "Question: Minimise $f(x) = x^2$ starting at $x_0 = 3$ with learning rate $\\alpha = 0.1$.\n\nStep 1: $f'(x) = 2x$. At $x_0=3$: gradient = 6.\n\nStep 2: $x_1 = x_0 - \\alpha f'(x_0) = 3 - 0.6 = 2.4$.\n\nAnswer: After one step: $x_1 = 2.4$.",
             "important", "Update rule: $x_{n+1} = x_n - \\alpha \\nabla f(x_n)$."),
            ("Concept 3 - Learning Rate", w[1], w[4],
             "Question: With $\\alpha = 1.1$ on $f(x)=x^2$ starting at $x=1$, what happens?\n\nStep 1: $x_1 = 1 - 1.1(2) = -1.2$.\n\nStep 2: $|x_1| > |x_0|$ — overshoots and diverges.\n\nAnswer: Too large a **learning rate** prevents **convergence**.",
             "warning", "If $\\alpha$ is too large, gradient descent oscillates or diverges. Too small, and it is slow."),
            ("Concept 4 - Local vs Global Minimum", w[3], w[0],
             "Question: $f(x) = x^4 - 4x^2$ has critical points at $x = 0, \\pm\\sqrt{2}$. Which are local minima?\n\nStep 1: $f'(x) = 4x^3 - 8x = 4x(x^2-2)$.\n\nStep 2: $f''(\\pm\\sqrt{2}) > 0$ → local minima. $f''(0) = 0$ → inconclusive.\n\nAnswer: **Local minima** at $x = \\pm\\sqrt{2}$. Global minimum at $x = \\pm\\sqrt{2}$ with $f = -4$.",
             "example", "Gradient descent may find a **local minimum** that is not the **global minimum**."),
            ("Concept 5 - Multivariable Gradient Descent", w[2], w[1],
             "Question: Minimise $f(x,y) = x^2 + y^2$ from $(3,4)$ with $\\alpha = 0.1$.\n\nStep 1: $\\nabla f = (2x, 2y)$. At $(3,4)$: $(6, 8)$.\n\nStep 2: $(x_1, y_1) = (3,4) - 0.1(6,8) = (2.4, 3.2)$.\n\nAnswer: After one step: **(2.4, 3.2)**.",
             "tip", "In multiple dimensions, update all variables simultaneously using the gradient vector."),
            ("Concept 6 - Links to Neural Networks", w[2], w[4],
             "Question: How does gradient descent connect to [[10.9 Neural Network Maths]]?\n\nStep 1: A neural network defines a loss function of thousands of weights.\n\nStep 2: Backpropagation computes the gradient; gradient descent updates weights.\n\nAnswer: Training a neural network IS gradient descent on a high-dimensional **objective function**. See also [[11.7 Advanced Optimisation for ML]] for Adam, momentum, and other optimisers.",
             "example", "SGD, Adam, and RMSprop are all variants of gradient descent used in [[10.9 Neural Network Maths]] and studied further in [[11.7 Advanced Optimisation for ML]]."),
        ]
    elif tid == "9.10":
        sections = [
            ("Concept 1 - Convex Functions", w[0], w[2],
             "Question: Is $f(x) = x^2$ convex?\n\nStep 1: $f''(x) = 2 > 0$ for all $x$.\n\nStep 2: Second derivative non-negative → convex.\n\nAnswer: **Yes**, $x^2$ is convex (bowl-shaped).",
             "tip", "A **convex function** curves upward — any chord lies above the graph."),
            ("Concept 2 - Convex Sets", w[1], w[3],
             "Question: Is the set $\\{(x,y) : x^2 + y^2 \\leq 1\\}$ convex?\n\nStep 1: This is a filled disc.\n\nStep 2: Any line segment between two points in the disc stays inside.\n\nAnswer: **Yes**, a disc is a **convex set**.",
             "example", "Half-spaces, discs, and rectangles are convex sets."),
            ("Concept 3 - Global Minimum of Convex Functions", w[2], w[0],
             "Question: Why does gradient descent on $f(x) = x^2$ always find the global minimum?\n\nStep 1: $x^2$ is convex.\n\nStep 2: For convex functions, every local minimum is the global minimum.\n\nAnswer: Convexity guarantees the **global minimum** at $x = 0$.",
             "important", "This is why convex optimisation is so powerful — local = global."),
            ("Concept 4 - Constraints", w[3], w[1],
             "Question: Minimise $f(x,y) = x^2 + y^2$ subject to $x + y = 1$.\n\nStep 1: Substitute $y = 1 - x$: $f = x^2 + (1-x)^2 = 2x^2 - 2x + 1$.\n\nStep 2: $f' = 4x - 2 = 0$ → $x = 0.5$, $y = 0.5$.\n\nAnswer: Minimum **0.5** at $(0.5, 0.5)$ with the **constraint** satisfied.",
             "warning", "Constraints reduce the feasible region — check that your answer satisfies them."),
            ("Concept 5 - Lagrange Multipliers", w[4], w[3],
             "Question: Use Lagrange multipliers for min $x^2+y^2$ s.t. $x+y=1$.\n\nStep 1: $\\mathcal{L} = x^2+y^2 - \\lambda(x+y-1)$.\n\nStep 2: $\\frac{\\partial \\mathcal{L}}{\\partial x} = 2x - \\lambda = 0$, $\\frac{\\partial \\mathcal{L}}{\\partial y} = 2y - \\lambda = 0$.\n\nStep 3: $x = y$, with $x+y=1$ → $x=y=0.5$.\n\nAnswer: Minimum at $(0.5, 0.5)$ with $\\lambda = 1$.",
             "example", "A **Lagrange multiplier** converts a constrained problem into an unconstrained one."),
            ("Concept 6 - Convex Optimisation in CS", w[0], w[2],
             "Question: Why is SVM training a convex optimisation problem?\n\nStep 1: The SVM objective is a convex quadratic function.\n\nStep 2: The feasible region (margin constraints) is a convex set.\n\nAnswer: Convexity guarantees a unique **global minimum** — any local optimum is the best.",
             "example", "Linear programming, Lasso, and SVM all exploit convexity for reliable optimisation."),
        ]

    out = []
    for title, w1, w2, example, callout_type, callout_text in sections:
        out.append(f"""## {title}
This concept uses [[{w1}]] and connects to [[{w2}]].

> [!{callout_type}] Key idea
> {callout_text}

### Chunked Example
{example}
""")
    return "\n".join(out)


def worked_examples(t):
    tid, name = t["id"], t["name"]
    w = t["words"]
    return f"""# {tid} {name} - Worked Examples

Theory note: [[{tid} {name}]]

Practice questions: [[{tid} {name} - Practice Questions]]

> [!tip] How to use these
> Cover the solution, attempt the question on paper, then uncover one step at a time.

## Example 1 - Vocabulary in Context
**Question:** Explain {name.lower()} using [[{w[0][0]}]], [[{w[1][0]}]], and [[{w[2][0]}]].

**Worked solution:**
1. A [[{w[0][0]}]] is: {w[0][1]}.
2. [[{w[1][0]}]] means: {w[1][1]}.
3. [[{w[2][0]}]] means: {w[2][1]}.
4. Together, these ideas let you {t["plain"][:80].lower()}...
5. This matters because {t["cs_conn"].lower()}

## Example 2 - Basic Procedure
**Question:** Solve a standard problem from {name.lower()}.

**Worked solution:**
1. Read the problem and identify the given information.
2. Write down the relevant definition or rule from [[{tid} {name}]].
3. Apply the rule one step at a time.
4. Simplify the result.
5. Check by substitution or a different method.

## Example 3 - Harder Problem
**Question:** A harder variant requiring two or more steps.

**Worked solution:**
1. Break the problem into smaller parts.
2. Apply the first technique and write the intermediate result.
3. Apply the second technique to complete the solution.
4. Verify the answer satisfies all conditions.
5. State the final answer clearly with units if applicable.

## Example 4 - Spot the Mistake
**Question:** A student gives an incorrect answer. Identify and fix the error.

**Worked solution:**
1. Read the student's working line by line.
2. Find the first line where the rule is misapplied.
3. Explain why that step is wrong in plain English.
4. Redo the step correctly.
5. Complete the solution and confirm the corrected answer.

## Example 5 - CS Transfer
**Question:** Show how {name.lower()} appears in a programming context.

**Worked solution:**
1. Name the CS object: {t["cs_items"][0]}.
2. Name the mathematical object: [[{w[0][0]}]].
3. Explain the link: {t["cs_conn"]}
4. Write a short pseudocode or formula showing the connection.
5. State why getting this wrong would cause a bug or incorrect result.

## Example 6 - Mixed Review
**Question:** Combine this topic with a prerequisite concept.

**Worked solution:**
1. Identify which prerequisite applies: {t["backward"][0]}.
2. Set up the combined problem.
3. Apply the prerequisite technique first.
4. Apply the current topic's technique second.
5. Verify the final answer makes sense in context.
"""


def practice_questions(t):
    tid, name = t["id"], t["name"]
    w = [x[0] for x in t["words"]]
    return f"""# {tid} {name} - Practice Questions

Theory note: [[{tid} {name}]]

Answers: [[{tid} {name} - Answers]]

> [!warning] Paper-first rule
> Attempt every question on paper before checking the answers. If you only read the solutions, you train recognition, not recall.

## A. Vocabulary
1. Define [[{w[0]}]] in one sentence.
2. Define [[{w[1]}]] in one sentence.
3. Define [[{w[2]}]] in one sentence.
4. Define [[{w[3]}]] in one sentence.
5. Define [[{w[4]}]] in one sentence.
6. What is the plain-English idea of {name.lower()}?

## B. Core Skills
7. Solve a basic problem from this topic (create from notes).
8. Solve a problem requiring two steps.
9. Solve a problem requiring three steps.
10. Find the answer and verify by a second method.
11. Sketch or describe a diagram for this topic.
12. Apply the main rule to a new example.
13. Solve with different numbers from the worked examples.
14. Explain each step of your solution in words.

## C. Spot the Mistake
15. A student makes a common error. Identify what is wrong.
16. Correct the student's working and give the right answer.
17. Explain why the mistake leads to an incorrect result.
18. Write a checklist to avoid this mistake in future.

## D. Mixed Practice
19. Combine this topic with {t["backward"][0]}.
20. A problem requiring both calculation and explanation.
21. Create your own problem and solve it.
22. Solve a problem with a constraint or special condition.
23. Compare two methods for the same problem.
24. Explain which method is more efficient and why.

## E. Computer Science Transfer
25. Name one CS application of {name.lower()}.
26. Write pseudocode showing the mathematical idea.
27. Explain what bug could occur if a programmer ignores this topic.
28. Connect this topic to {t["cs_items"][1]}.
29. Write a test case that checks a program uses this maths correctly.
30. Explain in two sentences why this topic belongs in a CS maths course.
"""


def mastery_test(t):
    tid, name = t["id"], t["name"]
    w = [x[0] for x in t["words"]]
    nxt = t["forward"].split(",")[0].strip()
    return f"""# {tid} {name} - Mastery Test

Theory note: [[{tid} {name}]]

Answers: [[{tid} {name} - Answers]]

Pass mark: 85%. You must score full marks on Section A before moving on.

> [!danger] Test condition
> Do this without looking at the topic note, worked examples, or answers. Use paper. Mark it afterwards.

## Section A - Definitions (5 marks, 100% required)
Each answer must be in your own words. 1 mark each.

1. Define [[{w[0]}]].
2. Define [[{w[1]}]].
3. Define [[{w[2]}]].
4. Define [[{w[3]}]].
5. Define [[{w[4]}]].

## Section B - Core Skills (10 marks)
6. (2 marks) Solve a standard problem from this topic.
7. (2 marks) Solve a problem requiring two steps.
8. (2 marks) Solve a harder problem from this topic.
9. (2 marks) Verify your answer to question 8 by a second method.
10. (2 marks) Explain each step of your solution to question 8 in words.

## Section C - Spot the Mistake (4 marks)
11. (2 marks) A student gives an incorrect solution. Identify the error.
12. (2 marks) Correct the solution and give the right answer.

## Section D - Mixed Application (3 marks)
13. (3 marks) Combine this topic with a prerequisite concept and solve.

## Section E - Computer Science Transfer (3 marks)
14. (1 mark) Name one CS application of this topic.
15. (1 mark) Explain what could go wrong in code if this maths is wrong.
16. (1 mark) Write one sentence linking this topic to {t["cs_items"][0]}.

## Marking
Total: 25 marks.

Pass:
- Section A: 5 out of 5 required.
- Overall: at least 22 out of 25 (88% rounds to pass at 85% threshold).

Decision:
- [ ] Pass — move to {nxt}.
- [ ] Review — create a correction note in [[94 Review Sheets]] and retake tomorrow.
- [ ] Restart — reread [[{tid} {name}]] and redo the worked examples.
"""


def answers(t):
    tid, name = t["id"], t["name"]
    w = t["words"]
    wdefs = "\n".join(f"{i}. **[[{w[i][0]}]]**: {w[i][1]}." for i in range(5))
    return f"""# {tid} {name} - Answers

Theory note: [[{tid} {name}]]

Practice questions: [[{tid} {name} - Practice Questions]]

Mastery test: [[{tid} {name} - Mastery Test]]

> [!note] Marking guidance
> Some explanation answers can be worded differently. Mark them correct if the meaning is precise and the learner could use the idea without help.

## Practice Answers

### A. Vocabulary
{wdefs}
6. {t["plain"]}

### B. Core Skills
7–14. Worked solutions depend on the specific problems chosen. Each should show every step on its own line and state the final answer clearly. Verify by substitution or inverse operation.

### C. Spot the Mistake
15–18. The common errors are listed in [[{tid} {name}#Common Mistakes]]. Each correction should identify the first wrong line, explain why it is wrong, and redo from that point.

### D. Mixed Practice
19–24. Solutions should reference {t["backward"][0]} where appropriate and show all working.

### E. Computer Science Transfer
25. {t["cs_items"][0]}
26. Pseudocode should mirror the mathematical update rule from the topic note.
27. Possible bugs: incorrect convergence, wrong sign, missing constant, off-by-one in numerical methods, or divergence from bad parameters.
28. {t["cs_items"][1]} — {t["cs_conn"]}
29. Test case should input known values and assert the output matches the mathematical result within a tolerance.
30. {t["cs_conn"]} Programs force exactness; this topic provides the precise rule.

## Mastery Test Answers

### Section A - Definitions (5 marks)
{wdefs}

### Section B - Core Skills (10 marks)
6. (2 marks) 1 mark for correct method, 1 mark for correct answer with working.
7. (2 marks) 1 mark for each correct step; deduct 1 for arithmetic error with correct method.
8. (2 marks) Full marks for correct final answer with complete working.
9. (2 marks) Second method stated and applied; 1 mark if method correct but arithmetic error.
10. (2 marks) Each step explained in plain English; 1 mark if answer correct but explanation missing.

### Section C - Spot the Mistake (4 marks)
11. (2 marks) 1 mark for identifying the wrong line, 1 mark for explanation.
12. (2 marks) 1 mark for corrected working, 1 mark for correct final answer.

### Section D - Mixed Application (3 marks)
13. (3 marks) 1 mark for identifying prerequisite, 1 mark for method, 1 mark for correct answer.

### Section E - CS Transfer (3 marks)
14. (1 mark) Any valid application from the topic note CS section.
15. (1 mark) Must name a specific failure mode (divergence, wrong optimum, incorrect area, etc.).
16. (1 mark) Must link the mathematical object to the CS object by name.

> [!failure] Common wrong answers
> Accept equivalent wording for definitions. Deduct only if the meaning is wrong or incomplete.
"""


def glossary(t):
    tid, name = t["id"], t["name"]
    out = []
    builds = t["backward"][0].replace("[[", "").replace("]]", "")
    for wname, defn in t["words"]:
        out.append(f"""# {wname}

{defn.capitalize()}.

First introduced in: [[{tid} {name}]]

Builds on: [[{builds}]]

Used in CS: {t["cs_conn"]}

## Related Notes
Search backlinks in Obsidian to see every topic that uses [[{wname}]].
""")
    return out


def cumulative_test():
    qs = []
    for i, t in enumerate(TOPICS, 1):
        qs.append(f"""### Question {i} — {t["id"]} {t["name"]} (10 marks)
1. (3 marks) Define two key terms from [[{t["id"]} {t["name"]}]] in your own words.
2. (4 marks) Solve one representative problem from this topic from memory. Show all working.
3. (3 marks) Give one CS application and explain the link in one sentence.""")
    body = "\n\n".join(qs)
    return f"""# 09 Calculus - Cumulative Test

Use this after completing every topic in [[09 MOC - Calculus]].

Pass target: 85% (85 out of 100 marks).

> [!danger] Test conditions
> No notes. Paper only. Allow 2 hours. Mark using topic answer keys.

## Instructions
- Each question is worth 10 marks.
- You must attempt all 10 questions.
- Section A definitions within each question require precise wording.

{body}

## Reflection (not marked)
- Which three topics felt strongest?
- Which three topics need review?
- Which topic connects most clearly to computer science?
- Which prerequisite from an earlier module should you revisit?

## Marking Summary
| Question | Topic | Marks Available | Your Score |
|----------|-------|-----------------|------------|
| 1 | 9.1 Limits | 10 | |
| 2 | 9.2 Differentiation Basics | 10 | |
| 3 | 9.3 Differentiation Rules | 10 | |
| 4 | 9.4 Applications | 10 | |
| 5 | 9.5 Integration Basics | 10 | |
| 6 | 9.6 Integration Techniques | 10 | |
| 7 | 9.7 Differential Equations | 10 | |
| 8 | 9.8 Multivariable Functions | 10 | |
| 9 | 9.9 Gradient Descent | 10 | |
| 10 | 9.10 Convex Optimisation | 10 | |
| **Total** | | **100** | |

Pass: ≥ 85 marks.

Decision:
- [ ] Pass — proceed to [[10.1 Big O Theta and Omega]].
- [ ] Review — retake failed topics and redo this test in one week.
"""


def printable_summary():
    items = "\n".join(f"- [ ] [[{t['id']} {t['name']}]] — {t['plain'][:70]}..." for t in TOPICS)
    return f"""# 09 Calculus - Printable Summary

One-page revision sheet for Module 09. Print and tick off as you master each skill.

## Core Skills Checklist
{items}

## Key Formulas

### Differentiation
- Power rule: $\\frac{{d}}{{dx}} x^n = nx^{{n-1}}$
- Product rule: $(uv)' = u'v + uv'$
- Quotient rule: $(u/v)' = (u'v - uv')/v^2$
- Chain rule: $\\frac{{d}}{{dx}} f(g(x)) = f'(g(x)) \\cdot g'(x)$

### Integration
- Power rule: $\\int x^n \\, dx = \\frac{{x^{{n+1}}}}{{n+1}} + C$
- By parts: $\\int u \\, dv = uv - \\int v \\, du$
- Definite: $\\int_a^b f(x)\\,dx = F(b) - F(a)$

### Differential Equations
- Growth/decay: $\\frac{{dy}}{{dt}} = ky \\Rightarrow y = y_0 e^{{kt}}$

### Multivariable
- Gradient: $\\nabla f = \\left(\\frac{{\\partial f}}{{\\partial x}}, \\frac{{\\partial f}}{{\\partial y}}\\right)$
- Gradient descent: $\\theta_{{n+1}} = \\theta_n - \\alpha \\nabla L(\\theta_n)$

### Convex Optimisation
- Convex: $f''(x) \\geq 0$ (single variable)
- Lagrange: $\\mathcal{{L}} = f - \\lambda g$

## Folder Pass Gate
Before leaving this folder:
- [ ] Pass every topic mastery test (85%, 100% on definitions).
- [ ] Retake any failed topic after a correction note.
- [ ] Complete [[09 Calculus - Cumulative Test]] with ≥ 85%.
- [ ] Explain how calculus connects to CS using [[09 Calculus - What This Unlocks in CS]].
"""


def what_unlocks():
    items = "\n".join(f"""### {t["id"]} {t["name"]}
- **Maths skill:** {t["plain"][:100]}...
- **CS unlock:** {t["cs_conn"]}
- **Programming objects:** {", ".join(t["cs_items"][:3])}""" for t in TOPICS)
    return f"""# 09 Calculus - What This Unlocks in CS

Calculus is the mathematics of change, accumulation, and optimisation. Every topic in this module has a direct programming application.

## Topic-by-Topic CS Connections

{items}

## Cross-Module Links
- [[9.1 Limits and Continuity]] → [[10.4 Floating Point and Rounding Error]] (convergence and epsilon)
- [[9.3 Differentiation Rules]] → [[11.8 Multivariable Calculus for Deep Learning]] (autograd)
- [[9.9 Gradient Descent and Optimisation]] → [[10.9 Neural Network Maths]] (training loops)
- [[9.9 Gradient Descent and Optimisation]] → [[11.7 Advanced Optimisation for ML]] (Adam, momentum)
- [[9.10 Convex Optimisation Basics]] → [[11.7 Advanced Optimisation for ML]] (constrained training)

## What You Can Build After This Module
After passing Module 09, you should be able to:
1. Read and implement a gradient descent training loop.
2. Understand loss curves and learning rate effects in ML frameworks.
3. Set up and solve basic optimisation problems in code.
4. Model exponential growth/decay in simulations.
5. Approximate integrals numerically when closed forms do not exist.
6. Recognise convex problems where local search guarantees global optima.

## Next Step
After passing this folder, continue to [[10.1 Big O Theta and Omega]] and keep revisiting weak links through [[Progress Tracker]].
"""


def main():
    files_written = []
    for t in TOPICS:
        tid, name = t["id"], t["name"]
        base = f"{tid} {name}"
        # Topic note
        path = os.path.join(CALC, f"{base}.md")
        with open(path, "w") as f:
            f.write(topic_note(t))
        files_written.append(path)
        # Worked examples
        path = os.path.join(WE, f"{base} - Worked Examples.md")
        with open(path, "w") as f:
            f.write(worked_examples(t))
        files_written.append(path)
        # Practice questions
        path = os.path.join(PQ, f"{base} - Practice Questions.md")
        with open(path, "w") as f:
            f.write(practice_questions(t))
        files_written.append(path)
        # Mastery test
        path = os.path.join(MT, f"{base} - Mastery Test.md")
        with open(path, "w") as f:
            f.write(mastery_test(t))
        files_written.append(path)
        # Answers
        path = os.path.join(ANS, f"{base} - Answers.md")
        with open(path, "w") as f:
            f.write(answers(t))
        files_written.append(path)
        # Glossary
        for i, gcontent in enumerate(glossary(t)):
            wname = t["words"][i][0]
            path = os.path.join(GLO, f"{wname}.md")
            with open(path, "w") as f:
                f.write(gcontent)
            files_written.append(path)

    # Folder assessments
    for fname, content in [
        ("09 Calculus - Cumulative Test.md", cumulative_test()),
        ("09 Calculus - Printable Summary.md", printable_summary()),
        ("09 Calculus - What This Unlocks in CS.md", what_unlocks()),
    ]:
        path = os.path.join(CALC, fname)
        with open(path, "w") as f:
            f.write(content)
        files_written.append(path)

    print(f"Total files written: {len(files_written)}")
    for p in sorted(files_written):
        print(p)

if __name__ == "__main__":
    main()
