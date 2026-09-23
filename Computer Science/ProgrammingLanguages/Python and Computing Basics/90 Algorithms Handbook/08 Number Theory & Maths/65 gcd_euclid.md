# gcd_euclid

8 NUMBER THEORY & MATHS
gcd_euclid(first_number, second_number) FUNCTION
Return the greatest common divisor.
REMEMBER gcd(a, b) = gcd(b, a mod b); stop when b is 0, answer is a.
REQUIRES Integers.
TIME O(log min(a, b)). SPACE O(1).
USED FOR Simplifying fractions, LCM, modular inverses, RSA key setup.
def gcd_euclid(first_number, second_number):
while second_number != 0:
first_number, second_number = second_number, first_number % second_number
return abs(first_number)
INPUT gcd_euclid(48, 18)
OUTPUT 6
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY math.gcd no install needed
Built in since Python 3.5 and accepts many arguments from 3.9.
CODE import math
math.gcd(48, 18)
OUTPUT 6
lcm(first_number, second_number) FUNCTION
Return the least common multiple.
REMEMBER lcm = |a × b| / gcd(a, b).
TIME O(log min(a, b)).
USED FOR Adding fractions, scheduling repeating events.
def lcm(first_number, second_number):
if first_number == 0 or second_number == 0:
return 0
return abs(first_number * second_number) // gcd_euclid(first_number, second_number)
INPUT lcm(4, 6)
OUTPUT 12
IN PRODUCTION — the call you would actually write
STANDARD LIBRARY math.lcm (Python 3.9+) no install needed
Also accepts any number of arguments.
CODE import math
math.lcm(4, 6)
OUTPUT 12
CS Algorithms Toolkit Number theory & maths
65
