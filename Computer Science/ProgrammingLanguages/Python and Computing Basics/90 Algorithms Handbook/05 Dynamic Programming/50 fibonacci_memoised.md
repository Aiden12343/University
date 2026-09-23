# fibonacci_memoised

5 DYNAMIC PROGRAMMING
Use DP when: (1) the problem splits into SUB-PROBLEMS, (2) the same sub-problems recur (overlap), (3) the best answer is built from best
sub-answers (optimal substructure). Recipe: define the state → write the recurrence → pick the order → return the right cell.
fibonacci_memoised(position, remembered_results=None) FUNCTION
Top-down DP: recursion + a notebook of answers already computed.
REMEMBER fib(n) = fib(n-1) + fib(n-2), but check the notebook first and write every new answer into it. fib(0)=0, fib(1)=1.
WHEN TO USE Recursive definition is natural; not all sub-problems needed.
AVOID WHEN Very large n (Python recursion limit) — use bottom-up.
REQUIRES position ≥ 0.
TIME O(n) (naive is O(2n
)). SPACE O(n).
USED FOR Teaching memoisation; template for any overlapping recursion.
def fibonacci_memoised(position, remembered_results=None):
if remembered_results is None:
remembered_results = {0: 0, 1: 1}
if position not in remembered_results:
remembered_results[position] = (
fibonacci_memoised(position - 1, remembered_results)
+ fibonacci_memoised(position - 2, remembered_results))
return remembered_results[position]
INPUT fibonacci_memoised(50)
OUTPUT 12586269025
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY functools.cache (Python 3.9+) no install needed
One decorator adds the notebook of remembered answers to any pure function. lru_cache(maxsize=N) does the same with a size limit.
Recursion depth is still limited to about 1000 frames.
CODE from functools import cache
@cache
def fibonacci(position):
return position if position < 2 else fibonacci(position - 1) + fibonacci(position - 2)
fibonacci(50)
OUTPUT 12586269025
CS Algorithms Toolkit Dynamic programming
50
