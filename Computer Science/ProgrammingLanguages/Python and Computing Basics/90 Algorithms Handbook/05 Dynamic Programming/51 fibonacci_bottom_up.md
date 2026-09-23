# fibonacci_bottom_up

fibonacci_bottom_up(position) FUNCTION
Bottom-up DP: build from the smallest case, keep only what's needed.
REMEMBER Two variables, previous and current; each step slide them forward: (previous, current) = (current, previous +
current).
TIME O(n). SPACE O(1) — the pattern for any DP that only looks
back a fixed number of steps.
def fibonacci_bottom_up(position):
previous_value, current_value = 0, 1
for step in range(position):
previous_value, current_value = current_value, previous_value + current_value
return previous_value
INPUT fibonacci_bottom_up(50)
OUTPUT 12586269025
IN PRODUCTION A loop like this is already production-grade. For memoised recursion see fibonacci_memoised.
CS Algorithms Toolkit Dynamic programming
51
