# 3.15 Exercises

### 3.15.1 Specifications and algorithms

1. For “remove duplicates”, write three materially different valid specifications by varying order, equality, and mutation requirements.
2. State precondition, postcondition, effect, and failure behaviour for division of two integers.
3. Prove the partial correctness and termination of repeated subtraction for computing a quotient under the precondition (a\geq0) and (b>0).
4. Construct an algorithm that preserves a plausible invariant but returns the wrong answer. Explain why invariant usefulness, not mere preservation, matters.
5. Explain why accepting floating-point NaN can invalidate an assumption of consistent total ordering in a maximum algorithm. “NaN” may be treated here as a special numeric value for which ordinary comparisons do not behave as a total order; its representation is deferred.

### 3.15.2 Computability and evidence

6. Explain Turing-completeness without using the phrases “can do anything” or “infinite computer”.
7. Restate the halting contradiction in your own program names, preserving both branches of the contradiction.
8. Give two useful restricted analyses that do not contradict undecidability of the general halting problem.
9. For a palindrome checker, design five test cases and state the distinct risk each protects. Then explain what those cases do not prove.

### 3.15.3 Shell and process interfaces

10. Given a command containing a filename with spaces, describe the argument sequence the target must receive. Then write correctly scoped Bash and PowerShell invocations, checking the relevant shell documentation rather than assuming identical quoting.
11. Design stdout, stderr, and status contracts for a command that converts temperatures from an input stream. Include malformed rows and partial progress.
12. Starting from two possible CWDs, resolve the same relative path and show why one succeeds while the other fails.
13. Explain how a shell pipeline demonstrates interface composition and why diagnostic contamination breaks it.

### 3.15.4 Integrated exercise

14. Design, but do not yet implement, a command that reads transactions and reports an account balance. Produce the full computational dossier: input grammar, semantic rules, numeric representation assumptions, invalid-input policy, algorithm, invariant, termination measure, resource bounds, command syntax, working-directory policy, stream contract, exit statuses, test fixtures, independent oracles, and an evidence table distinguishing proof, static reasoning, and observed execution.
