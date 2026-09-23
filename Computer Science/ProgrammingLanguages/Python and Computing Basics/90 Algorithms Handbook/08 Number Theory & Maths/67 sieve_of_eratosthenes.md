# sieve_of_eratosthenes

sieve_of_eratosthenes(limit) FUNCTION
Return every prime ≤ limit.
REMEMBER Write out 2..limit; take the next unmarked number, cross out its multiples (starting at its SQUARE), repeat up
to sqrt(limit).
WHEN TO USE Many primes in a range; repeated primality queries below a limit.
AVOID WHEN Testing one huge number (use trial division / Miller-Rabin); very large limits (memory O(limit)).
REQUIRES limit is an integer.
TIME O(n log log n). SPACE O(n).
USED FOR Prime tables, number-theory contests, hashing table sizes.
def sieve_of_eratosthenes(limit):
if limit < 2:
return []
is_prime_flag = [True] * (limit + 1)
is_prime_flag[0] = is_prime_flag[1] = False
candidate = 2
while candidate * candidate <= limit:
if is_prime_flag[candidate]:
for multiple in range(candidate * candidate, limit + 1, candidate):
is_prime_flag[multiple] = False
candidate += 1
return [number for number, flag in enumerate(is_prime_flag) if flag]
INPUT sieve_of_eratosthenes(30)
OUTPUT [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
IN PRODUCTION — the call you would actually write
THIRD-PARTY sympy.primerange pip install sympy
Generates primes lazily in a range (upper bound exclusive). For raw speed on huge ranges people also write a NumPy sieve.
CODE import sympy
list(sympy.primerange(2, 31)) # primes below 31
OUTPUT [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
CS Algorithms Toolkit Number theory & maths
67
