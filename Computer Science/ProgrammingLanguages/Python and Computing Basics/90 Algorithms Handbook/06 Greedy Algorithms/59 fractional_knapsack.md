# fractional_knapsack

fractional_knapsack(items_as_weight_value_pairs, capacity) FUNCTION
Return the max value when items may be split into fractions.
REMEMBER Rank items by value-per-weight and take the best ratios first, slicing the last one to fill the bag exactly.
WHEN TO USE Divisible goods (grain, liquid, CPU time).
AVOID WHEN Indivisible items — greedy FAILS there, use knapsack_01 (DP).
REQUIRES Weights > 0.
TIME O(n log n). SPACE O(n).
def fractional_knapsack(items_as_weight_value_pairs, capacity):
total_value = 0.0
remaining_capacity = capacity
ranked_items = sorted(items_as_weight_value_pairs,
key=lambda pair: pair[1] / pair[0], reverse=True)
for item_weight, item_value in ranked_items:
if remaining_capacity <= 0:
break
weight_taken = min(item_weight, remaining_capacity)
total_value += item_value * (weight_taken / item_weight)
remaining_capacity -= weight_taken
return total_value
INPUT weight_value_pairs = [(10, 60), (20, 100), (30, 120)]
fractional_knapsack(weight_value_pairs, 50) # capacity 50
OUTPUT 240.0
IN PRODUCTION — the call you would actually write
THIRD-PARTY scipy.optimize.linprog pip install scipy
Fractional knapsack is a linear program, so a solver handles it (and any extra constraints). The greedy version is still the fastest when the
problem is exactly this simple.
CODE from scipy.optimize import linprog
weights, values = [10, 20, 30], [60, 100, 120]
result = linprog(c=[-value for value in values], A_ub=[weights], b_ub=[50], bounds=(0, 1))
(round(-result.fun, 6), result.x.round(3).tolist()) # (best value, fraction taken)
OUTPUT (240.0, [1.0, 1.0, 0.667])
CS Algorithms Toolkit Greedy algorithms
59
