# fast_power

fast_power(base, exponent, modulus=None) FUNCTION
Return base ** exponent (optionally mod modulus) by repeated squaring.
REMEMBER Read the exponent in binary: keep squaring the base; whenever the current bit is 1 (exponent is odd),
multiply it into the result; halve the exponent each round.
WHEN TO USE Huge exponents, especially modular (crypto, hashing).
AVOID WHEN Tiny exponents (just use **); Python's pow(b, e, m) does this.
REQUIRES exponent is an integer ≥ 0.
TIME O(log exponent) multiplications. SPACE O(1).
USED FOR RSA, Diffie-Hellman, Fermat primality tests, matrix powers.
def fast_power(base, exponent, modulus=None):
result = 1
current_power = base # base^(2^k) as k grows
remaining_exponent = exponent
while remaining_exponent > 0:
if remaining_exponent % 2 == 1: # this binary digit is 1
result = result * current_power
if modulus is not None:
result %= modulus
current_power = current_power * current_power
if modulus is not None:
current_power %= modulus
remaining_exponent //= 2
if modulus is not None:
result %= modulus
return result
INPUT fast_power(2, 10) # 2 ** 10
OUTPUT 1024
INPUT fast_power(3, 200, 13) # (3 ** 200) % 13 without a huge number
OUTPUT 9
IN PRODUCTION — the call you would actually write
BUILT-IN the three-argument pow() no install needed
pow(b, e, m) performs modular exponentiation by repeated squaring, in C, without ever building the huge intermediate number. It also
computes modular inverses with pow(a, -1, m) (Python 3.8+).
CODE (pow(2, 10), pow(3, 200, 13), pow(3, -1, 7)) # 2**10, (3**200) mod 13, inverse of 3 mod 7
OUTPUT (1024, 9, 5)
CS Algorithms Toolkit Number theory & maths
66
