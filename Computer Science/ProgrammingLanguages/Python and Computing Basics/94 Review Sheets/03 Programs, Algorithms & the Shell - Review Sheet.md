# 3.14 Common misconceptions consolidated

1. **“Problem, algorithm, and program are interchangeable.”** The problem asks; the specification constrains; the algorithm gives a method; the program expresses machinery; the execution is one history.
2. **“If tests pass, correctness is proved.”** Tests cover selected executions. They are essential evidence but generally not a universal proof.
3. **“Turing-complete means infinitely powerful.”** It classifies expressibility under ideal resources and includes undecidable questions and impractical computations.
4. **“The terminal and shell are the same thing.”** The terminal transports and displays text; the shell interprets command language.
5. **“The script’s directory is automatically the CWD.”** Process working directory and source location are independent unless a launcher establishes a relationship.
6. **“Printed error text is enough to signal failure.”** Automation requires truthful exit status and channel separation.
7. **“A path is a file.”** A path is location syntax resolved against filesystem state; the open resource and its content have separate identity and lifetime.
8. **“Data can safely be placed into source if quoted.”** Correct quoting is language-specific. Preserving a data/source boundary is the stronger design.
