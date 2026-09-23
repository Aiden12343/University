# 09 Calculus - What This Unlocks in CS

Calculus is the mathematics of change, accumulation, and optimisation. Every topic in this module has a direct programming application.

## Topic-by-Topic CS Connections

### 9.1 Limits and Continuity
- **Maths skill:** A **limit** asks what value a function gets closer and closer to as the input moves toward some poin...
- **CS unlock:** Limits make rates of change and numerical approximations precise.
- **Programming objects:** floating-point convergence checks, animation frame interpolation, numerical root-finding (Newton's method)
### 9.2 Differentiation Basics
- **Maths skill:** The **derivative** measures how fast a function's output changes when the input changes by a tiny am...
- **CS unlock:** Derivatives drive optimisation, graphics motion, and ML training.
- **Programming objects:** velocity from position in game engines, loss curve slope in ML training, marginal cost in economics simulations
### 9.3 Differentiation Rules
- **Maths skill:** Once you know the **first principles** definition, shortcut **rules** let you differentiate common e...
- **CS unlock:** Automatic differentiation uses structured differentiation rules.
- **Programming objects:** automatic differentiation (autograd), backpropagation in neural networks, symbolic differentiation in computer algebra
### 9.4 Applications of Differentiation
- **Maths skill:** Derivatives tell you where a curve rises, falls, or turns. Setting the derivative to zero finds **st...
- **CS unlock:** Optimisation appears in scheduling, ML, graphics, and resource allocation.
- **Programming objects:** hyperparameter tuning, resource allocation, path smoothing in robotics
### 9.5 Integration Basics
- **Maths skill:** Integration reverses differentiation. It measures **accumulation** — total area under a curve, total...
- **CS unlock:** Integration appears in probability, physics engines, and continuous models.
- **Programming objects:** probability density integration, physics engine impulse calculations, Monte Carlo area estimation
### 9.6 Integration Techniques
- **Maths skill:** Not every integral is a simple reverse power rule. **Substitution**, **integration by parts**, **par...
- **CS unlock:** Numerical integration supports simulation and scientific computing.
- **Programming objects:** Simpson's rule in scientific computing, quadrature in numerical libraries (SciPy), physics simulation time steps
### 9.7 Differential Equations Intro
- **Maths skill:** A **differential equation** relates a quantity to how fast it changes. Given an **initial condition*...
- **CS unlock:** Population models, queues, physics, and control systems use differential equations.
- **Programming objects:** population dynamics in simulations, queueing theory (M/M/1 models), PID control loops
### 9.8 Multivariable Functions
- **Maths skill:** Real models rarely depend on one input. A **multivariable function** takes several inputs and produc...
- **CS unlock:** ML models depend on many variables at once.
- **Programming objects:** loss functions with many weights, image height maps (surfaces), sensor fusion with multiple inputs
### 9.9 Gradient Descent and Optimisation
- **Maths skill:** **Gradient descent** repeatedly steps in the direction opposite to the **gradient** of an **objectiv...
- **CS unlock:** Gradient descent is central to modern machine learning.
- **Programming objects:** SGD in PyTorch/TensorFlow, weight updates in neural networks, learning rate schedulers
### 9.10 Convex Optimisation Basics
- **Maths skill:** A **convex function** curves upward like a bowl — any local minimum is also the **global minimum**. ...
- **CS unlock:** Convex optimisation appears in ML, operations research, and resource allocation.
- **Programming objects:** SVM hinge loss (convex), linear programming in OR-Tools, Lasso regression

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
