# prime_factorisation

prime_factorisation(number) FUNCTION
Return the prime factors of number (with repeats) in ascending order.
REMEMBER Divide out each divisor from 2 upward as many times as it fits; whatever is left above 1 at the end is itself
prime.
REQUIRES number ≥ 2.
TIME O(√n). SPACE O(log n).
USED FOR Simplifying roots, counting divisors, cryptography basics.
def prime_factorisation(number):
prime_factors = []
divisor = 2
while divisor * divisor <= number:
while number % divisor == 0:
prime_factors.append(divisor)
number //= divisor
divisor += 1
if number > 1:
prime_factors.append(number)
return prime_factors
INPUT prime_factorisation(360)
OUTPUT [2, 2, 2, 3, 3, 5]
IN PRODUCTION — the call you would actually write
THIRD-PARTY sympy.factorint pip install sympy
factorint returns a {prime: exponent} dict, or a list with multiple=True. It uses smarter algorithms than trial division for big inputs.
CODE import sympy
(sympy.factorint(360), sympy.factorint(360, multiple=True))
OUTPUT ({2: 3, 3: 2, 5: 1}, [2, 2, 2, 3, 3, 5])
CS Algorithms Toolkit Number theory & maths
69
