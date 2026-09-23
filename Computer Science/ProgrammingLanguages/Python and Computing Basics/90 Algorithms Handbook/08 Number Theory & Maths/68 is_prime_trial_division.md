# is_prime_trial_division

is_prime_trial_division(number) FUNCTION
Return True if number is prime (check divisors up to sqrt(number)).
REMEMBER A composite has a factor ≤ its square root; rule out evens, then try odd divisors only.
WHEN TO USE A single, moderately sized number (up to ~1012
).
AVOID WHEN Huge numbers (use Miller-Rabin); many numbers (use the sieve).
TIME O(√n). SPACE O(1).
def is_prime_trial_division(number):
if number < 2:
return False
if number < 4:
return True
if number % 2 == 0:
return False
divisor = 3
while divisor * divisor <= number:
if number % divisor == 0:
return False
divisor += 2
return True
INPUT (is_prime_trial_division(97), is_prime_trial_division(91)) # 91 = 7 * 13
OUTPUT (True, False)
IN PRODUCTION — the call you would actually write
THIRD-PARTY sympy.isprime pip install sympy
Uses fast primality tests (Miller-Rabin, plus a Lucas test for very large inputs) instead of trial division, so it copes with numbers far beyond
1012
.
CODE import sympy
(sympy.isprime(97), sympy.isprime(91), sympy.isprime(2**61 - 1)) # last one: a huge prime
OUTPUT (True, False, True)
CS Algorithms Toolkit Number theory & maths
68
