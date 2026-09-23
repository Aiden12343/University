# 12.25 Exercises

### 12.25.1 Requirements and tests

1. Convert five vague quality claims into measurable acceptance criteria with environment and percentile or failure conditions.
2. Partition inputs for a date parser, including leap years, timezone absence, invalid calendar days, and Unicode lookalike digits.
3. Write pytest parameterisations whose cases each protect a distinct boundary; annotate the risk.
4. Build fixture dependencies for a temporary database, schema, and seeded account. Choose scopes and prove test isolation.
5. Replace an over-mocked unit test with a fake and an adapter contract test.

### 12.25.2 Advanced evidence

6. Write a property-based round-trip test for one serialisation schema and state what it cannot prove.
7. Define three metamorphic relations for sorting, aggregation, or normalisation.
8. Run mutation testing against a small module and explain each surviving mutant.
9. Reach full line coverage with an intentionally weak suite, then strengthen it with independent assertions to demonstrate the distinction.

### 12.25.3 Debugging and observability

10. Take an existing defect and produce a hypothesis ledger: observation, candidate causes, discriminating experiments, first divergence, repair, and regression.
11. Design structured log events for a request path. Include correlation and redaction, and eliminate duplicated propagation logs.
12. Create one deterministic and one deliberately flaky test, identify the uncontrolled input in the latter, and inject control.

### 12.25.4 Git and integration

13. Create two coherent commits from a working tree containing three unrelated edits. Use the index to select content and review each staged diff.
14. Construct a merge conflict, resolve semantic intent, and show tests that distinguish a correct merge from choosing either side blindly.
15. Explain commit, tree, blob, branch, and `HEAD` by inspecting a small repository’s object relationships.
16. Simulate secret introduction without using a real secret. Explain rotation and history-response procedure.

### 12.25.5 Types and documentation

17. Define a structural repository protocol, in-memory fake, and production adapter. Run strict static analysis across all.
18. Explain invariance of mutable list and covariance of read-only sequence with a concrete mutation counterexample.
19. Remove unjustified `Any` values by validating one dynamic JSON boundary.
20. Produce reference, how-to, explanation, and tutorial fragments for one API; make their purposes visibly different.

### 12.25.6 Integrated exercise

21. Engineer a new ledger import capability from requirement through clean-wheel CI. Submit acceptance criteria, risk partitions, unit/integration/property tests, static typing, structured diagnostics, atomic file handling, Git commit series, API documentation, build artefact evidence, review argument, and a post-integration observation plan. Every test must name its oracle and protected risk.

### 12.25.7 Contracts, architecture, and risk

22. For a command that deletes an account, write preconditions, success postconditions, failure guarantees, authorisation rules, audit effects, and a recovery policy. Distinguish deletion, deactivation, and anonymisation.
23. Model a library-loan operation as a state machine. Include available, reserved, loaned, overdue, lost, and withdrawn states; identify at least three illegal transitions.
24. Take the requirement “search must be fast” and produce two alternative operational definitions for an interactive system and a nightly batch process. Explain why neither definition transfers unchanged.
25. Identify stakeholders for a university assessment system, including people who do not operate it directly. Record one legitimate conflict of interest and its decision authority.
26. Construct a traceability graph for password reset from user need through requirement, threat, control, implementation boundary, verification, deployment, and metric.
27. Write a risk register for report export with at least eight scenarios. Include probability uncertainty, impact distribution, prevention, detection, response, and residual-risk owner.
28. Analyse “duplicate order” as five different possible equivalence relations. For each, state a false-merge and false-separation consequence.
29. Define a contract matrix for a file upload that is cancelled midway. Address temporary storage, quota accounting, malware scanning, audit, retry identity, and client response.
30. Compare a modular monolith and two-service design for the same small ledger. Evaluate transaction boundary, operational cost, failure isolation, deployment, and team ownership without declaring one universally superior.
31. Draw three architectural views of one program: context, responsibility/component, and runtime failure sequence. State what each view intentionally omits.
32. Write an ADR selecting an embedded database for a desktop application. Include two rejected alternatives, measurable assumptions, disadvantages, and a reconsideration trigger.
33. Refactor a function that performs parsing, policy, persistence, and notification into explicit boundaries. Show which tests belong at each boundary and which integration remains.
34. Define cohesion and coupling for three modules in an existing project. Find one apparently “decoupled” global dependency and make its direction explicit.
35. Review an accessibility requirement as both a functional and quality concern. Produce acceptance cases that do not depend on a single automated score.

### 12.25.8 Pytest mechanics and fixture design

36. Create a new project with one intentionally misnamed test. Compare ordinary execution with <code>--collect-only</code>, then add a CI assertion preventing an empty collection.
37. Write a test containing a compound assertion and observe pytest’s rewritten diagnostic. Split it into semantic assertions and compare the information supplied by each failure.
38. Parameterise the complete boundaries of a slice-like interval contract. Give every case an identifier expressing its risk rather than its literal values.
39. Construct a parameter table whose Cartesian decorators create redundant combinations. Replace it with deliberate paired cases and justify the reduced set.
40. Test exact exception type, structured attributes, causal exception, and unchanged state for one parser failure. Keep setup outside the raises context.
41. Add a deprecation path to a function. Test its warning category, message fragment, stack attribution, replacement behaviour, and eventual strict removal policy.
42. Register <code>integration</code> and <code>slow</code> marks in project configuration. Demonstrate that a misspelled mark fails collection under strict markers.
43. Create one strict expected-failure test for a known defect. Repair the defect and show that the unexpected pass forces removal of the mark.
44. Build a three-level fixture graph for service, repository, and seeded account. Diagram acquisition and reverse cleanup order.
45. Make a fixture fail after acquiring its first resource. Use <code>ExitStack</code> or nested context managers to prove the resource is still released.
46. Compare function- and session-scoped mutable fixtures by running tests in two orders. Explain the contamination mechanism and repair it without arbitrary ordering.
47. Separate session lifetime of a database process from function lifetime of schema/data. Measure the time saved and demonstrate isolation.
48. Write a factory fixture that creates several external resources and cleans only those it owns. Make cleanup idempotent and test partial creation failure.
49. Design a test-data builder with valid defaults. Then find one test whose meaning is hidden by a default and make the relevant field explicit.
50. Use <code>tmp_path</code> to test exact bytes, filename, absence of temporary residue, and pre-existing destination preservation for an exporter.
51. Use <code>monkeypatch</code> to control an environment setting read at call time. Contrast with a module that captures the setting at import time and explain the binding.
52. Patch a name in the module of definition and then at the lookup site. Demonstrate why only one patch controls a prior from-import.
53. Use <code>capsys</code> and <code>capfd</code> against Python output and a subprocess/file-descriptor write. State why their observation boundaries differ.
54. Capture log records and assert stable event fields, level, logger, and redaction. Avoid asserting a formatter-dependent timestamp.
55. Write a small pytest plugin or hook in a disposable project that reports one project-specific invariant. Document its effect on collection and its supply-chain trust.

### 12.25.9 Doubles, contracts, and integration

56. Implement stub, fake, spy, and interaction mock variants for a notification sender. For each, state the exact testing purpose and information it cannot provide.
57. Replace an unconstrained mock with an autospecced mock. Introduce a misspelled method and incompatible arguments to compare failure timing.
58. Convert an interaction-heavy test into state verification without weakening its contract. Record which internal refactorings cease to break it.
59. Write a negative-interaction test proving invalid local input never calls an external gateway. Enumerate all other channels that would be required for a system-wide absence claim.
60. Build a fake monotonic clock and scheduler for retry policy. Test exact deadline, just-before-deadline, and clock-advance behaviour without sleeping.
61. Design a fake repository that accidentally differs from the real database on duplicate keys. Write a shared contract case that reveals the divergence.
62. Apply one repository contract suite to an in-memory implementation and a real ephemeral database adapter. List behaviour that remains adapter-specific.
63. Demonstrate why transaction rollback isolation fails to test an after-commit hook. Add a clean-database integration case.
64. Create a migration test beginning from the immediately previous released schema, applying the actual migration, and reading existing rows with new code.
65. Test a database uniqueness rule under two concurrent connections. Explain why a pre-query followed by insert is insufficient without a database constraint.
66. Implement a local fake HTTP server that emits valid response, malformed JSON, slow headers, truncated body, redirect, and 503 with retry metadata.
67. Compare the fake-server evidence with one provider-sandbox test. State which DNS, TLS, authentication, and service semantics remain different.
68. Write a system test through an installed command-line entry point. Ensure it imports the installed wheel rather than the repository checkout.
69. Create a side-effect ledger for an end-to-end rejection: database, queue, email, file, log, metric, audit, and response. Verify every forbidden channel feasible in the test environment.
70. Define a project-specific unit/component/integration/system taxonomy and classify ten existing tests. Resolve ambiguous cases by naming real and replaced boundaries.

### 12.25.10 Generative, coverage, mutation, and fuzz testing

71. Write four independent properties for a normalisation function. Construct a wrong implementation that satisfies any one property and show why conjunction is stronger.
72. Design a Hypothesis strategy for valid ledger transactions whose entries balance exactly. Avoid filtering randomly generated unbalanced records.
73. Generate invalid transactions by violating exactly one invariant at a time. Explain why arbitrary corruption makes diagnosis and partition coverage weaker.
74. Preserve and interpret a shrunk counterexample. Add a named example only if it protects a semantically important boundary not guaranteed by future generation.
75. Test idempotence of one normaliser and explain why idempotence alone permits a constant-output defect.
76. Define a metamorphic relation for unit conversion, search ranking, and aggregation. State the assumptions under which each relation holds.
77. Differentially test two CSV parsers over a deliberately restricted common dialect. Classify disagreements as defect, extension, or specification ambiguity.
78. Build a stateful model test for create, update, fetch, and delete operations. Include illegal transitions and compare a simple model with a real adapter.
79. Measure statement and branch coverage of a Boolean decision. Construct a suite with complete statement coverage but a missing decision outcome.
80. Derive MC/DC pairs for a three-condition safety decision. Compare their number with exhaustive truth-table cases and explain what neither proves.
81. Investigate every uncovered line in a small module. Classify each as missing test, unreachable code, platform path, defensive branch, generated code, or instrumentation issue.
82. Configure a changed-line coverage gate and exhibit a critical unchanged path it misses. Add risk-based evidence outside the metric.
83. Run mutation testing on a boundary-heavy function. For every survivor, classify weak test, ambiguous requirement, equivalent mutant, or tool limitation.
84. Write a byte-oriented fuzz harness for a parser. Bound memory and time, catch only specified rejections, and retain a corpus input for each distinct discovered defect.
85. Combine coverage-guided fuzzing with a semantic round-trip invariant. Explain why reaching every parser branch would still not prove interoperability.

### 12.25.11 Debugging, logging, and incidents

86. Take a traceback from a controlled defect and annotate exception, propagation frames, first invalid value, invariant-enforcement point, and likely causal origin.
87. Write a complete reproduction record for a platform-dependent path defect. Remove all irrelevant environmental facts only after experiments show irrelevance.
88. Reduce a large failing input by halves while preserving a specific failure predicate. Plot size against reduction steps and explain the logarithmic ideal and deviations.
89. Maintain a hypothesis ledger with at least four competing explanations for one failure. Design an experiment that distinguishes two in one run.
90. Use <code>breakpoint()</code> or <code>pdb</code> to inspect a nested call stack. Record any expression evaluation that could mutate or execute program state.
91. Create a defect that disappears when a print is added. Determine whether buffering, timing, or ordering changes; do not name it a Heisenbug without evidence.
92. Use Git bisection with an automated focused test in a disposable repository. Include one unbuildable commit and document the skip’s effect on certainty.
93. Design a concurrency test using barriers to force a lost-update interleaving. Repair the shared invariant and show why one local lock per instance fails.
94. Distinguish deadlock, livelock, starvation, and data race with one minimal scenario each. State the relevant progress and memory assumptions.
95. Convert free-form logs for a request into structured events. Define field types, units, cardinality, redaction, and schema-evolution rules.
96. Configure a library logger that emits records without choosing application handlers. Demonstrate duplicate output caused by handler propagation and repair the configuration boundary.
97. Design counter, gauge, and histogram metrics for a job system. Reject at least two tempting high-cardinality labels.
98. Calculate an SLI from a supplied event table, then show how excluding timeouts from the denominator creates a misleading result.
99. Trace one asynchronous producer–consumer flow with correlation and link relations. Explain why wall-clock order alone cannot establish causality across hosts.
100. Write a post-incident review for a synthetic duplicate-charge event. Include timeline confidence, containment, contributing factors, corrective controls, owners, and verification.

### 12.25.12 Git data, histories, and collaboration

101. In a disposable repository, create a file and inspect its blob, containing tree, and commit using plumbing commands. Relate every identifier to hashed content.
102. Change only a commit message and compare old and new commit identifiers, trees, and parent relationships.
103. Rename a file and inspect the commit’s trees. Demonstrate that rename presentation is derived by comparison rather than stored as a mandatory rename object.
104. Create distinct working-tree, index, and <code>HEAD</code> contents for one path. Predict and then run the three principal diff comparisons.
105. Stage one hunk from a file containing two conceptual changes. Verify the staged snapshot builds while the remaining working change stays visible.
106. Enter detached <code>HEAD</code>, create a commit, switch away, and recover it by creating a named branch through reflog inspection. Use only disposable content.
107. Fetch from a second local repository and show that the remote-tracking reference changes only on fetch, not when the other repository commits.
108. Construct a fast-forward merge and a true three-way merge. Draw the parent graph and explain why chronological timestamps do not define ancestry.
109. Create a clean textual merge with a semantic defect like mismatched units. Write a test or type check that detects it.
110. Resolve a textual conflict by reconstructing post-merge requirements. Compare the correct resolution with mechanically choosing each side.
111. Rebase two unpublished commits onto a new base. Map original commits to replayed commits and explain identifier changes.
112. Compare merge, rebase, squash merge, and cherry-pick on equivalent source changes. Evaluate topology, attribution, bisection, and later integration.
113. Revert a non-merge commit after an intervening modification. Explain why the resulting tree is not necessarily an old snapshot.
114. In a disposable repository, compare reset modes conceptually and observe their effects on reference, index, and working tree. Preserve a recovery branch before each experiment.
115. Use two worktrees for a release branch and a feature branch. Document shared and per-worktree administrative state.
116. Create 64 sequential commits with one introduced regression and locate it through automated bisection. Compare observed test count with <code>ceil(log2(64))</code>.
117. Design an expand–migrate–contract commit series for a database-column rename that supports mixed application versions.
118. Create an annotated tag in a disposable repository and inspect the tag object. Distinguish author metadata, tagger metadata, and cryptographic identity.
119. Use <code>git check-ignore -v</code> to explain rules for nested build output, a negated retained file, and a user-global editor pattern.
120. Conduct a tabletop secret-commit incident using an inert token. Produce rotation, scope, history-rewrite, clone coordination, cache, log, and prevention steps.

### 12.25.13 Style, refactoring, and documentation

121. Rename variables in a parsing function to distinguish bytes, text, tokens, parsed values, and domain objects. Explain each model boundary.
122. Apply an automated formatter to deliberately irregular code. Separate its semantic non-achievements from the mechanical improvements.
123. Classify twenty linter diagnostics as likely defect, security context warning, maintainability heuristic, or style policy. Justify every suppression.
124. Measure cyclomatic complexity for a function, then construct a one-line equivalent that is harder to understand. Discuss the measure’s abstraction limit.
125. Refactor a nested authorisation decision into coherent predicates while preserving a decision-table suite. Inspect for changed short-circuit effects.
126. Characterise a legacy function, refactor it, and identify one captured behaviour that is probably a defect. Separate descriptive from normative tests.
127. Write tutorial, how-to, reference, and explanation passages for the same cache API. Make the reader question and structure of each unmistakable.
128. Produce a complete docstring for a timeout-bearing function: units, zero/negative policy, clock, combined phases, exception, cancellation, and side effects.
129. Replace ten syntax-restating comments with names or remove them. Add three comments explaining non-obvious invariants or compatibility constraints.
130. Add doctest examples to a deterministic pure function, then identify why exact output comparison is unsuitable for a timestamped or unordered result.
131. Create context, component, data, runtime, and security views for one small service. Give each a legend and omission statement.
132. Write an operational runbook for a failed migration. Include authority, prerequisites, read-only diagnosis, abort threshold, recovery, and verification.
133. Configure documentation example and link checks in CI. Demonstrate a false pass caused by importing the checkout instead of the released wheel.

### 12.25.14 Type design and static analysis

134. Annotate a function once with <code>Any</code> and once with <code>object</code>. Compare which unsafe operations the checker permits and add correct narrowing.
135. Parse an arbitrary decoded JSON value into a frozen domain model. Confine <code>Any</code> to the boundary and test every rejection category.
136. Design a discriminated union for queued, running, succeeded, failed, and cancelled jobs. Add exhaustiveness checking and then introduce a new variant.
137. Compare a transparent type alias, <code>NewType</code>, frozen dataclass, and subclass for account identifiers. Evaluate static distinction, runtime validation, memory, and interoperability.
138. Define a <code>TypedDict</code> for an external payload with required and optional fields. Show why constructing it from a cast does not validate JSON.
139. Write a generic <code>pairwise</code> function whose output element relationships are preserved. Compare with an <code>object</code>-typed version.
140. Express a literal-dependent return through overloads. Write implementation and type-check tests for every overload and for a non-literal Boolean.
141. Type a signature-preserving decorator with <code>ParamSpec</code>. Verify metadata preservation and document the decorator’s runtime side effects.
142. Define the narrowest useful structural protocol for a byte consumer. Test two implicit implementations and one near miss.
143. Add <code>@runtime_checkable</code> to a protocol and demonstrate a runtime object that passes member-presence checking while violating the intended signature.
144. Use <code>Self</code> in a base class and subclass. Contrast a valid fluent method with a factory that incorrectly always returns the base.
145. Model a recursive JSON-like value and state where the type admits values a strict interoperable JSON encoder may reject.
146. Configure mypy strict checking for source and tests with one narrow legacy override. Record all effective versions and enabled options.
147. Use <code>reveal_type</code> to inspect narrowing through identity, <code>isinstance</code>, and pattern matching. Remove diagnostic forms from shipped runtime code.
148. Replace an unjustified cast with runtime validation. For one justified cast, document the evidence the checker cannot express and add a regression test.
149. Write a <code>.pyi</code> stub that intentionally disagrees with runtime on optionality. Produce both a false static rejection and a missed runtime defect, then repair it.
150. Demonstrate covariance of a producer, contravariance of a handler, and invariance of a mutable cell with concrete subtype substitutions.

### 12.25.15 CI, review, and release engineering

151. Draw a CI dependency graph in which formatting, typing, unit tests, integration tests, artefact build, smoke test, and publication have correct dependencies.
152. Make a test command accidentally succeed after a failing subcommand because of shell status handling. Repair it and explain false-green risk.
153. Design a matrix for three Python versions, three operating systems, minimum/latest dependencies, and an optional native feature without running the full Cartesian product. State omissions.
154. Create a cache-key specification incorporating every input affecting a wheel cache. Show one stale reuse caused by an omitted ABI or lock hash.
155. Build the same tiny wheel twice in controlled environments and compare hashes. Investigate timestamp, archive order, path, or tool-version causes of any difference.
156. Threat-model CI for an untrusted contribution. Separate read-only validation identity from protected publication identity and caches.
157. Design a progressive deployment with canary population, success indicators, abort threshold, and rollback limitation. Identify one silent harm the metrics would miss.
158. Review a deliberately mixed change containing formatting, dependency update, generated file, migration, and behaviour. Propose coherent review units without creating undeployable states.
159. Write a merge-request argument covering requirement, design, risks, evidence, compatibility, migration, observability, and rollback. Have another reader locate unsupported assertions.
160. Compare PEP 440 version ordering with a project’s Semantic Versioning policy using pre-release, post-release, and local version examples.
161. Create a deprecation plan spanning two releases. Include warning behaviour, migration guide, typing change, tests, and accelerated security-removal exception.
162. Build source distribution and wheel, inspect contents/metadata, install each through isolated builds, and test from outside the checkout.
163. Define dependency policy separately for a reusable library and deployed application. Test lower bounds, recent resolution, and a locked production environment.
164. Produce a sample SBOM and provenance statement for an inert package. Explain precisely what each proves and does not prove.
165. Write an incident-release procedure for a broken published package: yanking, corrected version, advisory, immutable bytes, cache limits, and retrospective evidence.

### 12.25.16 Cumulative capstones

166. Engineer a transactional file transformer integrating Chapters 5–12. Specify byte/text boundaries, object ownership, iterator behaviour, atomic replacement, error taxonomy, tests, types, documentation, Git history, and built-wheel verification.
167. Build a plugin-capable command-line application. Threat-model imports and third-party execution, define protocols, isolate configuration, test discovery and failure, package entry points, and document extension stability.
168. Refactor a Chapter 9 inheritance hierarchy into composition where justified. Preserve public behaviour through characterisation, type contracts, focused tests, and one real integration.
169. Construct a reproducible data-processing experiment. Version code and inputs, isolate dependencies, record seeds and environment, assert data invariants, and package the exact executable artefact.
170. Design a safe concurrent job runner in preparation for Chapter 14. State what Chapter 12 can verify about state, idempotency, cancellation, logging, and recovery before studying scheduler mechanisms.
171. Perform a full code review of a small open-source-style Python package without changing it. Produce a claim–evidence map, risk-ranked defects, test gaps, type gaps, packaging findings, and reproducible commands.
172. Take one real defect from report to release: minimise it, locate first divergence, add regression and adjacent tests, repair cause, construct coherent commits, review the change, build the wheel, and write a post-release observation plan.
173. Design a library public API and compatibility policy intended for five years of use. Address naming, exceptions, protocols, typing, serialisation, deprecation, Python support, and source/wheel distribution.
174. Conduct a tabletop supply-chain compromise. Trace a malicious build dependency from resolution through CI credentials, artefact provenance, package publication, consumer detection, revocation, and recovery controls.
175. Implement the resumable ledger-import case from §12.23. Its submission must include requirements, ADRs, risk register, traceability, unit/integration/property/fault tests, strict typing, structured diagnostics, bisectable Git history, wheel evidence, runbook, and a claim ledger labelling every important assertion.

### 12.25.17 Exercise evidence protocol

For exercises involving implementation, submit more than source code. Unless an exercise states otherwise, include:

1. the requirement or proposition being evaluated;
2. assumptions and explicit non-goals;
3. the smallest relevant source and configuration;
4. exact commands and tool versions;
5. observed results, including collection/skip counts;
6. an explanation of the oracle;
7. at least one limitation or untested risk;
8. a coherent version-control diff or commit series.

For destructive Git, database, credential, or publication simulations, use disposable local artefacts and inert values. Do not practise history rewriting or secret exposure on a valuable shared repository.
