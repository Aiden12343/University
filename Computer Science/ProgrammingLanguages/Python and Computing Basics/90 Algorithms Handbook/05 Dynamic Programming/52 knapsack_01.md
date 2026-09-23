# knapsack_01

knapsack_01(item_weights, item_values, capacity) FUNCTION
Return the maximum total value that fits in the bag (each item once).
REMEMBER best[c] = best value using capacity c. For each item, go through capacities BACKWARDS from full to the
item's weight: best[c] = max(best[c], best[c - weight] + value). Backwards = each item can only be used once.
WHEN TO USE Choose a subset under a budget: take-it-or-leave-it items.
AVOID WHEN Items can be split (use greedy fractional knapsack); huge capacity (time is O(n × capacity): "pseudo-polynomial").
REQUIRES Integer weights ≥ 1 and integer capacity ≥ 0.
TIME O(n × capacity). SPACE O(capacity).
USED FOR Budget allocation, cargo loading, portfolio picking.
def knapsack_01(item_weights, item_values, capacity):
best_value_for_capacity = [0] * (capacity + 1)
for item_index in range(len(item_weights)):
item_weight = item_weights[item_index]
item_value = item_values[item_index]
for remaining_capacity in range(capacity, item_weight - 1, -1):
value_if_taken = best_value_for_capacity[remaining_capacity - item_weight] + item_value
if value_if_taken > best_value_for_capacity[remaining_capacity]:
best_value_for_capacity[remaining_capacity] = value_if_taken
return best_value_for_capacity[capacity]
INPUT item_weights = [10, 20, 30]
item_values = [60, 100, 120]
knapsack_01(item_weights, item_values, 50) # capacity 50
OUTPUT 220
IN PRODUCTION — the call you would actually write
THIRD-PARTY scipy.optimize.milp pip install scipy numpy
Real packing/budget problems are handed to an integer-programming solver, which also copes with extra constraints. Bounds 0..1 and
integrality make each item all-or-nothing. (Google OR-Tools is another popular choice.)
CODE import numpy
from scipy.optimize import milp, LinearConstraint, Bounds
item_weights, item_values, capacity = [10, 20, 30], [60, 100, 120], 50
result = milp(c=-numpy.array(item_values), # milp minimises, so negate the values
constraints=LinearConstraint([item_weights], ub=capacity),
integrality=numpy.ones(3), bounds=Bounds(0, 1))
(round(-result.fun), result.x.round().tolist()) # (best value, 1 = item taken)
OUTPUT (220, [0.0, 1.0, 1.0])
CS Algorithms Toolkit Dynamic programming
52
