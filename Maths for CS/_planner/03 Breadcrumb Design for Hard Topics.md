# Breadcrumb Design — Hard & Threshold Topics

> Detailed design for topics that need extra breadcrumbs.
> Each breadcrumb introduces ≤1 new term and defers to prior breadcrumbs for everything else.

---

## 3.7 Logarithms (Current: ~5 concepts → Target: 10)

Logarithms are a **threshold concept** because the definition is inverse-based — you cannot understand log without first understanding exponential.

| # | Breadcrumb | New Terms | Prereq Breadcrumbs | Notes |
|---|-----------|-----------|-------------------|-------|
| 1 | Repeated multiplication grows fast | Repeated multiplication | 1.4.2 | Show 2, 4, 8, 16, 32... |
| 2 | Exponents describe repeated multiplication | exponent, base, power | 2.9.1 | Formalize 2³ = 8 |
| 3 | The inverse question: "what power?" | (uses exponent) | 3.7.2 | "2 raised to what = 8?" → 3 |
| 4 | Introducing log notation | log, logarithm | 3.7.3 | log₂(8) = 3 means "2³ = 8" |
| 5 | Logs on a calculator | (uses log notation) | 3.7.4 | Show log₁₀ and ln buttons |
| 6 | Log laws: product | log law (product) | 3.7.4, 2.9.4 | log(ab) = log(a) + log(b) |
| 7 | Log laws: power and quotient | (uses log law) | 3.7.6 | log(aᵇ) = b·log(a) |
| 8 | Solving with logs | (uses log laws) | 3.7.7 | 2ˣ = 50 → x = log₂(50) |
| 9 | Semi-log plots (CS preview) | log scale | 3.7.4 | Algorithm complexity graphs |
| 10 | Why CS uses log₂ | binary, bits | 3.7.4, 10.3.1 | log₂(n) ≈ number of bits |

---

## 4.5 Trig Ratios SOHCAHTOA (Target: 10 breadcrumbs)

First contact with sin/cos/tan — must relate to right triangles, not introduce the unit circle yet.

| # | Breadcrumb | New Terms | Prereq Breadcrumbs | Notes |
|---|-----------|-----------|-------------------|-------|
| 1 | Right triangles have a fixed shape | right triangle, hypotenuse | 4.1.4 | Show ratio of sides is constant for fixed angle |
| 2 | Introducing sine | sine (sin) | 4.5.1 | sin(θ) = opposite/hypotenuse |
| 3 | Introducing cosine | cosine (cos) | 4.5.2 | cos(θ) = adjacent/hypotenuse |
| 4 | Introducing tangent | tangent (tan) | 4.5.3 | tan(θ) = opposite/adjacent |
| 5 | SOHCAHTOA mnemonic | (uses sin, cos, tan) | 4.5.2, 4.5.3, 4.5.4 | Memory aid |
| 6 | Finding a side with sin | (uses sin) | 4.5.2 | Given angle and hyp, find opposite |
| 7 | Finding a side with cos | (uses cos) | 4.5.3 | Given angle and adj, find hyp |
| 8 | Finding an angle (inverse trig) | inverse sin/cos/tan | 4.5.6 | arcsin, arccos, arctan |
| 9 | Calculator practice | (uses all trig) | 4.5.8 | Work through examples |
| 10 | Why CS uses trig | (uses all trig) | 4.5.9 | Rotation, graphics, game physics |

---

## 5.4 Infinity and Countability (Target: 12 breadcrumbs)

This is a **paradox topic** — Cantor's diagonal argument is famously counterintuitive. Must be drip-fed very gradually.

| # | Breadcrumb | New Terms | Prereq Breadcrumbs | Notes |
|---|-----------|-----------|-------------------|-------|
| 1 | Sets can be finite or infinite | finite set, infinite set | 5.1.1 | {1,2,3} vs ℕ |
| 2 | Counting the size of a set | cardinality | 5.1.5 | |{a,b,c}| = 3 |
| 3 | What makes two sets the same size? | bijection, one-to-one correspondence | 5.4.2, 1.1.2 | Pairing elements |
| 4 | ℕ and ℤ are the same size | countable | 5.4.3 | 0↔1, 1↔2, -1↔3, 2↔4, -2↔5... |
| 5 | ℕ and ℚ are the same size | (uses bijection) | 5.4.4 | Diagonal enumeration of rationals |
| 6 | Wait — are all infinite sets the same size? | (uses cardinality) | 5.4.5 | This seems suspicious... |
| 7 | Introducing decimal expansions | decimal expansion | 1.7.2 | 0.5, 0.333..., 0.142857... |
| 8 | Listing all numbers between 0 and 1 | (uses decimal) | 5.4.7 | Suppose we made a list... |
| 9 | Cantor's diagonal: the idea | (uses listing) | 5.4.8 | Change the diagonal digit |
| 10 | Cantor's diagonal: the contradiction | contradiction | 5.4.9 | The new number is NOT on the list |
| 11 | Uncountable sets | uncountable, continuum | 5.4.10 | ℝ is bigger than ℕ |
| 12 | Implications for CS | (uses uncountable) | 5.4.11 | Most real numbers are uncomputable |

---

## 5.11 Proof by Induction (Target: 10 breadcrumbs)

Induction is a threshold concept because "assume true for k, prove for k+1" feels circular at first.

| # | Breadcrumb | New Terms | Prereq Breadcrumbs | Notes |
|---|-----------|-----------|-------------------|-------|
| 1 | Dominoes: if one falls, all fall | domino effect | 1.1.5 | Physical analogy |
| 2 | The two parts of induction | base case, inductive step | 5.11.1 | Must prove BOTH |
| 3 | Why we need a base case | (uses base case) | 5.11.2 | Without it, nothing starts |
| 4 | Induction on natural numbers: sum formula | (uses inductive step) | 5.11.2, 6.1.2 | Prove 1+2+...+n = n(n+1)/2 |
| 5 | Step-by-step: proving the sum formula | inductive hypothesis | 5.11.4 | Walk through every line |
| 6 | Induction on divisibility | (uses induction) | 5.11.5 | Prove 7ⁿ - 1 is divisible by 6 |
| 7 | Induction on inequalities | (uses induction) | 5.11.6 | Prove 2ⁿ > n for n ≥ 1 |
| 8 | Strong induction | strong induction | 5.11.2 | Assume ALL prior cases, not just k |
| 9 | Common induction mistakes | (uses induction) | 5.11.8 | Skipping base case, wrong hypothesis |
| 10 | Induction in CS: loop invariants | loop invariant | 5.11.9 | Proving a while loop is correct |

---

## 6.11 Formal Languages and Automata (Target: 12 breadcrumbs)

Very abstract — must build from concrete examples.

| # | Breadcrumb | New Terms | Prereq Breadcrumbs | Notes |
|---|-----------|-----------|-------------------|-------|
| 1 | What is a language? (in CS) | language, alphabet, string | 5.5.1 | Set of strings over an alphabet |
| 2 | Building strings from rules | rule, production | 6.11.1 | Grammar informally |
| 3 | Finite automaton: a machine that reads input | finite automaton, state | 6.11.2 | Simple on/off machine |
| 4 | Drawing a DFA | DFA, transition | 6.11.3 | Start state, accept state |
| 5 | A DFA that detects "01" | (uses DFA) | 6.11.4 | Specific example worked through |
| 6 | Language of a DFA | (uses DFA, language) | 6.11.5 | The set of strings it accepts |
| 7 | Nondeterminism (NFA) | NFA, nondeterminism | 6.11.6 | Multiple possible paths |
| 8 | DFA = NFA in power | (uses both) | 6.11.7 | Every NFA can be converted to DFA |
| 9 | Regular expressions | regex | 6.11.8 | a*b*, (01)* |
| 10 | Regex ≡ DFA | (uses regex, DFA) | 6.11.9 | They describe the same languages |
| 11 | Limitations: pumping lemma intro | pumping lemma | 6.11.10 | Some languages aren't regular |
| 12 | Why this matters for CS | (uses all) | 6.11.11 | Lexing, parsing, pattern matching |

---

## 7.9 Eigenvalues and Eigenvectors (Target: 10 breadcrumbs)

The key is answering "why should I care?" before the calculation.

| # | Breadcrumb | New Terms | Prereq Breadcrumbs | Notes |
|---|-----------|-----------|-------------------|-------|
| 1 | A matrix multiplies a vector | matrix-vector multiply | 7.3.3 | Am × n × vn × 1 = result |
| 2 | Most vectors get rotated | (uses transformation) | 7.8.1 | Show random vectors changing direction |
| 3 | Special vectors: direction preserved | eigenvector | 7.9.2 | Av = λv |
| 4 | The scaling factor: eigenvalue | eigenvalue | 7.9.3 | λ is how much it stretches |
| 5 | Finding eigenvectors: (A - λI)v = 0 | (uses eigenvector) | 7.9.4 | The system has non-trivial solutions |
| 6 | Characteristic equation | characteristic polynomial | 7.9.5, 7.5.1 | det(A - λI) = 0 |
| 7 | 2×2 example: full walkthrough | (uses all above) | 7.9.6 | Work through [[3,1],[1,3]] |
| 8 | Complex eigenvalues (if complex numbers exist) | complex eigenvalue | 7.4.5, 7.9.7 | Rotation in 2D |
| 9 | Diagonalisation | diagonalisation | 7.9.7 | A = PDP⁻¹ |
| 10 | PCA: eigenvalues find important directions | (uses eigenvalue) | 7.9.9 | Covariance matrix → eigenvectors = principal components |

---

## 10.1 Big O Theta and Omega (Target: 8 breadcrumbs)

Currently has wrong prerequisite (9.10). True chain: 6.1 Sequences → 3.5 Polynomials → 10.1.

| # | Breadcrumb | New Terms | Prereq Breadcrumbs | Notes |
|---|-----------|-----------|-------------------|-------|
| 1 | Counting operations | operation count | 1.1.1 | Each line of code costs 1 step |
| 2 | Input size matters | input size n | 6.1.1 | More data → more steps |
| 3 | The dominant term | dominant term | 3.5.4 | n² + 3n + 1 ≈ n² for large n |
| 4 | Big O: upper bound | Big O | 10.1.3 | f(n) ≤ c·g(n) for n ≥ n₀ |
| 5 | Big Omega: lower bound | Big Omega | 10.1.4 | f(n) ≥ c·g(n) |
| 6 | Big Theta: tight bound | Big Theta | 10.1.5 | Both O and Ω simultaneously |
| 7 | Common growth rates (table) | constant, linear, quadratic, log, exponential | 10.1.6 | 1, log n, n, n log n, n², 2ⁿ |
| 8 | Why constant factors don't matter | (uses Big O) | 10.1.7 | 100n and n are both O(n) |

---

## 10.6 Cryptography RSA (Target: 10 breadcrumbs)

Currently 2 concepts — needs full treatment.

| # | Breadcrumb | New Terms | Prereq Breadcrumbs | Notes |
|---|-----------|-----------|-------------------|-------|
| 1 | Secret messages: the problem | plaintext, ciphertext | 1.1.1 | Caesar cipher as motivation |
| 2 | Modular arithmetic review | (uses mod) | 6.3.1 | a mod m = remainder |
| 3 | Modular exponentiation | modular exponentiation | 10.6.2, 2.9.2 | 3⁵ mod 7 = ? |
| 4 | Prime numbers and factoring | factoring | 1.10.3 | Multiplying is easy, factoring is hard |
| 5 | Euler's totient φ(n) | Euler's totient | 10.6.4, 1.10.5 | φ(pq) = (p-1)(q-1) |
| 6 | Euler's theorem | Euler's theorem | 10.6.5 | a^φ(n) ≡ 1 mod n |
| 7 | Key generation (RSA) | public key, private key | 10.6.6 | Pick p, q → compute n, φ, e, d |
| 8 | Encryption and decryption | encrypt, decrypt | 10.6.7 | c = mᵉ mod n, m = cᵈ mod n |
| 9 | Why RSA is secure | trapdoor function | 10.6.8 | Without d, you must factor n |
| 10 | Worked example: small primes | (uses all) | 10.6.9 | Full walkthrough with p=11, q=13 |
