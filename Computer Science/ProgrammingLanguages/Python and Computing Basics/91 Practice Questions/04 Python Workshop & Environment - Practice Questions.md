# 4.14 Exercises

### 4.14.1 Environment identity

1. Record the full identity of the interpreter selected by your shell. Include command, executable path, implementation, version, platform, and CWD.
2. Find every Python command your shell can resolve using that shell’s documented resolution mechanism. Explain any differences.
3. Create two separate virtual environments from the same base interpreter. Demonstrate that changing installed distributions in one does not necessarily change the other.
4. Invoke an environment interpreter without activation and prove its identity from inside the process.

### 4.14.2 REPL and source

5. Construct a three-step REPL experiment whose final expression depends on hidden earlier state. Restart and demonstrate the dependency.
6. Move the same script into a nested directory, launch it from two CWDs, and record both `Path.cwd()` and `__file__`.
7. Create one syntax failure, one anticipated runtime failure, and one logic failure. State the distinct evidence each produces.

### 4.14.3 Project construction

8. Reconstruct the `text-census` project from a new empty directory using only your README. Record every missing or ambiguous instruction and repair the README.
9. Design fixtures for empty content, one line without a terminal newline, blank lines, Windows-style line endings, non-ASCII text, invalid UTF-8, missing file, and directory-as-input. State the risk protected by each.
10. Capture stdout, stderr, and exit status separately for success, command-use failure, and resource failure.
11. Explain which claims in the transcript are Python-language facts, CPython facts, standard-library contracts, operating-environment conditions, and experimental observations.

### 4.14.4 Integrated exercise

12. Deliver a fresh-process workshop dossier for `text-census`. Another reader must be able to construct the environment and reproduce every stated case without access to your shell history, unsaved editor buffers, global packages, home-directory path, or verbal explanation.

### 4.14.5 Resolution and launch analysis

13. Construct a hypothetical search path containing three Python executables. For two orderings, derive which executable a first-match resolver selects. Then state why aliases and shell caches can invalidate a search-path-only prediction.
14. Run the launch probe with no arguments, one ordinary argument, one argument containing whitespace, and redirected stdout. Record <code>sys.argv</code> and terminal-status observations. Explain which transformations were performed by the shell and which by Python.
15. From two different CWDs, invoke one script using the same absolute script path and the same relative input spelling. Predict both resolved input paths before execution.
16. Set a non-secret project environment variable only in one shell, launch two child interpreters before and after changing it, and explain the inheritance results. Do not enumerate the entire environment.
17. Compare normal completion, explicit <code>SystemExit(7)</code>, an unhandled exception, and external interruption. Record statuses and stream output under your platform, labelling every platform-specific conclusion.

### 4.14.6 Source representation

18. Create UTF-8 source containing an identifier with a non-ASCII letter and a string containing the same visible letter. Inspect its bytes and code points. Explain why identifier policy and user-data policy are separate questions.
19. Construct one logical expression spanning four physical lines with parentheses. Then create an otherwise equivalent backslash continuation and identify two maintenance hazards of the latter.
20. Create controlled files using the platform’s common newline conventions. Determine whether the Python source reader admits each, then compare their raw bytes and hashes. Explain why successful parsing does not imply byte equality.
21. Produce one <code>IndentationError</code> and, where the implementation detects it, one <code>TabError</code>. Record the exact source bytes needed to reproduce each.
22. Investigate whether the project’s filesystem treats two case-different filenames as distinct. Do not generalise the observation to other filesystems; state the portability rule for imports.

### 4.14.7 Environment and dependency reasoning

23. Draw the provenance chain from a base interpreter through environment creation, build frontend, build backend, distribution artefact, installation record, and imported module. At each arrow, state what evidence could identify the transformation.
24. Given five candidate dependency versions and three intersecting constraints, compute the admissible set by hand. Add a platform constraint that makes the set empty and distinguish resolution failure from build failure.
25. Explain why <code>python -m pip</code> reduces one ambiguity but does not establish package authenticity, compatible behaviour, or correct import origin.
26. Create two environments from the same base interpreter. Install the project editably in one and as a built wheel in the other. Modify an authored source line without reinstalling. Predict and then compare which environment observes the change.
27. Design separate runtime, test, documentation, and development dependency groups for a hypothetical library. Justify every placement and identify which groups belong in a production image.
28. Write a reproducibility matrix for Linux on x86-64 and Windows on x86-64. Identify which artefacts may differ while semantic output remains equivalent.
29. Design an offline-reconstruction test. List every input that must be mirrored and explain how denying network access exposes an incomplete archive.

### 4.14.8 Diagnostics and handoff

30. For a chained <code>ConfigurationError</code>, identify outer type, outer message, explicit cause, and every project-owned frame. Propose a concise user diagnostic that preserves the full internal traceback.
31. Reduce a deliberately failing ten-line script to a minimal reproduction by deleting one element at a time. Retain a log of deletions that changed or removed the failure.
32. Write three oracles for <code>text-census</code>: an exact-byte success oracle, a semantic diagnostic oracle, and a side-effect oracle. Explain why one cannot substitute for all three.
33. Give the project to a clean-room operator or simulate one with a new user-owned temporary directory and environment. Convert every undocumented assumption into a README statement or executable configuration.
34. Extend the computational dossier from Chapter 3 with the workshop manifest, dependency-resolution record, import-origin evidence, and clean reconstruction transcript. State exactly which correctness claims still remain unproved.
