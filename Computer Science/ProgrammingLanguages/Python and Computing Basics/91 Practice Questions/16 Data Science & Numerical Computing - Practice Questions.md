# 16.30 Exercises

### 16.30.1 Representation and arrays

1. For a three-axis array, define the meaning of every axis before writing code. Predict the shapes produced by reduction over each possible axis set, then verify with NumPy.
2. Construct an int8 boundary table. For every arithmetic operation tested, distinguish mathematical result, representable range, documented library result, and warning or exception behaviour.
3. Create a base array, basic slice, transposed view, Boolean selection, and explicit copy. Draw the object-and-buffer ownership graph. Verify memory sharing with supported inspection functions.
4. Given shapes <code>(5, 1, 7)</code>, <code>(3, 7)</code>, and <code>(5, 3, 1)</code>, determine which pairs broadcast and the result shapes. Explain each trailing-axis comparison.
5. Implement row standardisation while handling zero-variance rows under an explicit policy. Test shape, dtype, non-mutation, missingness, and floating tolerances.
6. Compare a Python loop, NumPy expression, and chunked implementation for a representative operation. Report environment, correctness oracle, median timing, dispersion, peak memory, and limitations.

### 16.30.2 Tables and relational reasoning

7. Design a schema for a transport timetable. Include units, key constraints, nullable fields, time zones, and rules spanning columns.
8. Construct an integer-labelled Series for which <code>loc</code> and <code>iloc</code> return different values. Explain why both are correct.
9. Create one-to-one, one-to-many, and many-to-many tables. Predict each join’s row count by key before executing it. Enforce the expected cardinality.
10. Take a wide repeated-measures table into long form and restore it. Introduce a duplicate identifier/occasion pair and explain why ordinary pivot becomes undefined.
11. Model missing sensor data using both one sentinel and an explicit reason column. List questions that become answerable only in the second representation.
12. Write a group aggregation whose result differs when using <code>size</code> rather than <code>count</code>. State which answers the substantive question.

### 16.30.3 Statistical reasoning

13. For a skewed five-value sample, compute mean, median, range, sample variance, and quartiles manually. Change one value to an extreme magnitude and recompute.
14. Build a 10,000-case frequency table for a diagnostic test with chosen prevalence, sensitivity, and false-positive rate. Calculate both conditional directions and explain the difference.
15. Simulate repeated sample means for several sample sizes. Plot their empirical distributions and describe how spread changes without calling simulation a proof.
16. Construct a dataset with a strong nonlinear relationship but near-zero Pearson correlation. Plot it and explain why one coefficient is insufficient.
17. Give three causal explanations for an observed association between two variables. For each, identify data or design evidence that would discriminate it from alternatives.
18. Critique a published chart: reconstruct its encoding, population, aggregation, scale, omissions, and uncertainty. Redesign only where the claim becomes more faithful.

### 16.30.4 Integrated branch capstone

19. Obtain a legally usable public dataset. Freeze an identified input version; write a data dictionary and provenance statement; validate schema and keys; quantify missingness by cause where possible; construct at least two tested transformations; perform one cardinality-validated join; report descriptive magnitude and uncertainty; create an accessible visualisation; and rebuild the output from a clean virtual environment. The report must distinguish observed fact, model assumption, implementation behaviour, and substantive inference.

### 16.30.5 Data, measurement, and provenance

20. Choose a familiar administrative record and distinguish the real-world entity, event, measurement instrument, record, field, and encoded value. Identify at least three places where information is lost.
21. For a proposed “one row per customer” table, list every event that can create two rows for one customer or one row representing several people. Write a precise observational-grain statement.
22. Design a data dictionary for five variables. For each, include operational definition, unit, representation, allowed domain, missing reasons, temporal reference, and issuing authority.
23. Given identifiers from two organisations, specify a canonicalisation policy. Construct two examples where lower-casing or punctuation removal creates a false match, and defend a safer linkage procedure.
24. Compare a target population, sampling frame, invited sample, responding sample, and analysed sample for a university survey. Draw the exclusions and state which transitions can create selection bias.
25. Describe a census that still gives a biased answer. Separate coverage error, measurement error, item non-response, processing error, and mismatch between census time and target time.
26. Construct a proxy measure for an unobservable concept. Explain construct validity, criterion validity, reliability, differential measurement error, and a group for which the proxy may fail.
27. Write Python dataclasses representing a source artefact, canonical dataset, and analysis output. Include immutable identifiers and hashes without storing the dataset itself.
28. Given a revised source file with the same name, design a manifest that makes the two deliveries distinguishable. Explain what a byte hash proves and what it cannot prove.
29. Specify a rule for handling late-arriving events. Compare correction-in-place, append-only revisions, and snapshot tables with respect to reproducibility and query complexity.
30. Audit a dataset licence and consent statement for a proposed analysis. Separate technical accessibility from legal permission, ethical legitimacy, and disclosure risk.
31. Construct a composite key for a longitudinal sensor table. Write tests for uniqueness, null components, clock collisions, device replacement, and identifier reuse.
32. Invent three malformed records that pass dtype checks but violate semantics. Implement validation that returns row identifiers and reason codes rather than one bare assertion.
33. Model a unit conversion as a pure function. Test inverse conversion, missingness preservation, key preservation, numerical tolerance, and rejection of incompatible units.
34. Integrate Chapters 10–12: package a schema validator as an importable module, document its exceptions, write unit and integration tests, and commit the change in a git branch with an explanatory history.

### 16.30.6 Descriptive statistics and probability

35. For the multiset (1,1,2,2,2,9), compute empirical probabilities, mean, median, modes, variance under both divisors, standard deviation, IQR, and MAD by hand; then verify in Python.
36. Construct two datasets with the same mean and variance but visibly different shapes. Explain which summaries distinguish them and which do not.
37. Show numerically that the mean minimises squared deviations and a median minimises absolute deviations for a five-point sample. Evaluate the objective on a fine grid and then prove the claim informally.
38. Give an example in which averaging subgroup rates gives the wrong overall rate. Derive the ratio-of-sums result and state the necessary weights.
39. Implement a weighted mean using <code>math.fsum</code>. Reject negative weights, mismatched lengths, non-finite values, and zero total weight under explicit policies.
40. Compare range, IQR, MAD, and standard deviation after replacing one observation by a value one million times larger. Relate each response to robustness.
41. Standardise a variable using population and sample standard deviations. Explain why resulting numerical comparability does not establish comparable meaning or reliability.
42. Derive the geometric mean as the exponentiated arithmetic mean of logarithms for positive values. Give an example where it is appropriate for multiplicative growth and one where zeros make it undefined.
43. Represent a finite sample space using Python sets. Verify the complement and inclusion–exclusion identities for two events using exact <code>Fraction</code> probabilities.
44. Build a probability mass function as a mapping. Validate non-negativity and total mass exactly, then compute expectation and variance from definitions.
45. Numerically integrate a simple probability density over intervals and distinguish density height from interval probability. Demonstrate how changing units changes density values but not corresponding probabilities.
46. For two dependent binary variables, calculate the joint, marginal, and conditional distributions. Verify the multiplication rule and show the factorisation that independence would require.
47. Use Bayes’ rule to update disease probability after a positive test at prevalences of 0.1%, 1%, and 20%. Hold sensitivity and specificity fixed and explain the changing positive predictive value.
48. Construct three events that are pairwise independent but not mutually independent. Enumerate all outcomes and verify both claims.
49. Simulate Bernoulli sample means at increasing sizes using independent spawned streams. Report empirical error against the square-root law without presenting simulation as proof.
50. State a version of the law of large numbers and central limit theorem in plain language, listing conditions and conclusions separately. Give one heavy-tailed or dependent setting where casual invocation is unsafe.

### 16.30.7 Array representations and dtypes

51. Construct arrays with zero, one, and two axes, including an empty axis. Record <code>ndim</code>, <code>shape</code>, <code>size</code>, <code>dtype</code>, <code>itemsize</code>, and <code>nbytes</code>, and explain every result.
52. Compare <code>array</code>, <code>asarray</code>, <code>copy</code>, <code>zeros</code>, <code>empty</code>, <code>arange</code>, and <code>linspace</code>. State allocation, initialisation, dtype, and endpoint semantics.
53. Attempt to create a ragged numeric array from unequal-length lists. Explain the failure and implement two honest representations: padding plus mask, and a list of separate arrays.
54. Build an object-dtype array containing mutable lists. Copy the array, mutate one nested list, and draw the two levels of aliasing that explain the result.
55. For each signed and unsigned integer dtype, obtain bounds with <code>iinfo</code>. Test addition, multiplication, and casting at boundaries and record version-dependent warnings or errors.
56. Sum a large int8 array with and without an explicit accumulator dtype. Distinguish elementwise overflow from reduction accumulator promotion.
57. Use <code>result_type</code>, <code>promote_types</code>, and <code>can_cast</code> to build a casting table for selected integer, floating, Boolean, and complex dtypes. Explain safe, same-kind, and unsafe policies.
58. Investigate NumPy scalar promotion by combining arrays with Python integers and floats near dtype limits. Relate observed behaviour to the documented NumPy 2 promotion rules.
59. Use <code>finfo</code> and <code>nextafter</code> to find adjacent representable float32 and float64 values near 1, (10^{20}), and (10^{-20}). Explain non-uniform spacing.
60. Demonstrate catastrophic cancellation using mathematically equivalent formulas. Reformulate the calculation and compare relative error against a higher-precision reference.
61. Create NaN, positive infinity, and negative infinity through explicit constructors and controlled <code>errstate</code>. Test arithmetic, comparisons, sorting, reductions, and finiteness predicates.
62. Explain why <code>NaN == NaN</code> is false but <code>isnan</code> detects NaN. Construct tests that treat matching-NaN arrays under both strict and equal-NaN policies.
63. Convert values between little-endian and big-endian dtypes. Separate byte swapping from changing dtype interpretation, and verify round-trip values.
64. Define a structured dtype for a fixed binary record. Inspect field offsets, total item size, alignment, and raw bytes; then explain the portability risks.
65. Create <code>datetime64</code> arrays at day and nanosecond units. Inspect representable ranges and show how unit conversion can overflow or truncate.
66. Compare fixed-width Unicode, byte-string, object, and pandas string representations for a small multilingual corpus. Measure stated buffer sizes and list omitted indirect costs.
67. Write a function accepting the array protocol through <code>np.asarray</code>. Specify whether it copies, required dtype, dimensionality, finiteness, and mutation policy.
68. Pass a non-contiguous view to a routine requiring C-contiguous float64 storage. Implement a checked conversion and report whether a copy occurred.
69. Design a dtype-selection policy for monetary quantities, physical measurements, identifiers, categorical codes, and timestamps. Defend where fixed-point decimal or integer minor units are preferable to binary float.
70. Integrate Chapters 5, 7, and 12: implement a typed wrapper that validates an ndarray contract, raises domain-specific exceptions, and has property-based boundary tests.

### 16.30.8 Strides, views, indexing, and broadcasting

71. For a two-dimensional C-contiguous array, calculate byte addresses of four elements from base pointer and strides; confirm them using array metadata without dereferencing arbitrary memory.
72. Transpose the array and repeat the address calculation. Explain why values move logically without their bytes being rearranged.
73. Create a negative-stride reversed view and a zero-stride broadcasted view. Explain address reuse and why writing through broadcasted views is constrained.
74. Compare <code>reshape</code>, <code>ravel</code>, and <code>flatten</code> on contiguous and transposed inputs. Test memory sharing rather than inferring it from method names.
75. Traverse a large C-order matrix by rows and by columns in Python and in vectorised reductions. Benchmark carefully and relate differences to cache locality and interpreter overhead.
76. Draw the ownership graph for a base array, two overlapping slices, a transpose, and a copy. Predict which mutations become visible through each name.
77. Use <code>shares_memory</code> and <code>may_share_memory</code> on simple and difficult views. Explain exact versus conservative answers and why neither replaces an ownership design.
78. Mark a view read-only while retaining a writable alias. Demonstrate why the flag on one view does not make the underlying buffer immutable.
79. Compare scalar, slice, integer-array, and Boolean indexing. For each, state result shape, axis ordering, copy/view relationship, and repeated-index behaviour.
80. Assign through repeated advanced indices using ordinary assignment and <code>np.add.at</code>. Explain why buffered assignment does not accumulate as a sequential Python loop would.
81. Given a three-axis array, use <code>take</code>, <code>compress</code>, and explicit advanced indexing to express the same selection. Compare shape semantics and readability.
82. Derive the broadcast result for five pairs of shapes, including a failure. Validate with <code>broadcast_shapes</code> and explain every aligned trailing axis.
83. Use <code>newaxis</code> to compute an outer difference and a pairwise distance matrix. Label the meaning of each output axis and calculate output memory before allocation.
84. Contrast pairwise and elementwise operations for two equally shaped arrays. Construct a case where an accidental broadcast runs successfully but answers the wrong question.
85. Implement a blockwise pairwise-distance minimum that never materialises the complete matrix. Prove the peak temporary shape and compare with the fully broadcast expression.
86. Use <code>broadcast_to</code> and <code>tile</code> to represent repeated data. Compare shape, strides, writeability, memory sharing, and downstream materialisation.
87. Construct a function whose input may have a leading batch shape and whose last axis contains features. Validate and document the generalised broadcasting contract.
88. Integrate Chapters 8 and 13: implement an iterator over array blocks, use it in a streaming numerical algorithm, and analyse time, auxiliary space, aliasing, and exception safety.

### 16.30.9 Universal functions, reductions, randomness, and linear algebra

89. Inspect a ufunc’s arity, supported type signatures, identity, and methods. Use <code>reduce</code>, <code>accumulate</code>, <code>outer</code>, and <code>at</code> on one coherent example.
90. Reimplement a multi-step expression using <code>out</code> buffers. Prove that aliases are safe, compare peak memory, and test numerical equivalence with justified tolerances.
91. Use a ufunc’s <code>where</code> argument with a preinitialised output. Show why uninitialised locations are otherwise semantically dangerous.
92. Benchmark <code>np.vectorize</code>, a Python comprehension, and a genuine ufunc for a scalar Python function. Explain why convenience vectorisation need not produce native speed.
93. Compute sums over every axis combination of a shape <code>(2, 3, 4)</code> array. Predict shape with and without <code>keepdims</code> before execution.
94. Implement row normalisation using <code>keepdims=True</code>. Define policies for zero totals, negative values, NaN, infinity, and empty axes.
95. Compare naive one-pass variance, two-pass variance, and Welford’s algorithm on values with a large offset and small spread. Use a high-precision oracle.
96. Investigate <code>sum</code>, <code>nansum</code>, masked arrays, and pandas nullable reductions on all-missing and partially missing data. State each identity and minimum-count policy.
97. Design an <code>isclose</code> tolerance from measurement and algorithm error budgets. Demonstrate how default absolute tolerance can be too permissive near zero.
98. Compare elementwise closeness, a vector norm bound, and an application-level invariant for validating a numerical result. Explain what each can miss.
99. Construct an explicit BitGenerator and Generator. Save and restore state, then show how inserting one random call changes all later draws.
100. Refactor a stochastic function that seeds internally so it accepts a Generator. Test deterministic replication and successive non-duplicate calls.
101. Spawn one random stream per semantic task and show that results remain stable when tasks are assigned to a different number of workers.
102. Estimate a Monte Carlo quantity at four draw counts. Report estimated Monte Carlo standard error and verify approximate inverse-square-root scaling across independent streams.
103. Build a simulation with a known analytic special case. Test conserved quantities, impossible states, convergence, and sensitivity to the time-step parameter.
104. Explain why scientific PRNGs are unsuitable for authentication tokens. Write separate interfaces using <code>numpy.random</code> and <code>secrets</code> for their proper purposes.
105. Multiply arrays representing vectors, row matrices, column matrices, and batches. Predict every <code>@</code> output shape and identify invalid products.
106. Solve a well-conditioned and nearly singular linear system. Report condition number, scaled residual, solution sensitivity to perturbed input, and meaningful digits.
107. Fit a line with <code>lstsq</code>, inspect rank and singular values, and compare against explicitly formed normal equations on an ill-conditioned design.
108. Integrate Chapters 12–14: package a benchmarked numerical solver with shape/dtype contracts, reference tests, error budgets, profiling evidence, and documentation of native threading.

### 16.30.10 Series, DataFrames, missingness, and selection

109. Create a Series whose label order differs from value-construction order. Demonstrate selection, sorting, reindexing, and alignment while preserving index meaning.
110. Build a duplicate-labelled Series. Catalogue operations that return a scalar under unique labels but a Series under duplicates, and convert the implicit key into an explicit composite key.
111. Align two partially overlapping Series using ordinary arithmetic and <code>fill_value</code>. For two domains, explain why interpreting absence as zero is valid in one and invalid in the other.
112. Assign a reordered Series and a same-length NumPy array to two DataFrame columns. Explain label versus positional semantics and write assertions that expose the difference.
113. Construct a MultiIndex from entity and occasion. Perform a slice, group operation, and unstack; then implement the same task with ordinary columns and compare auditability.
114. Read a CSV with identifiers containing leading zeros, literal “NA” categories, locale-formatted numbers, and UTC timestamps. Write explicit parser and post-parse rules that preserve meaning.
115. Make a parsing failure report containing source row, column, raw token, rule, and reason. Ensure invalid tokens are not conflated with genuine missing observations.
116. Compare NumPy int64, pandas nullable Int64, float-with-NaN, and object representations for an integer field with missing values. Test arithmetic, equality, serialisation, and memory.
117. Define an ordered categorical dtype and show how order affects sorting, minimum, group output, and comparison. Reject unrecognised categories with a report.
118. Convert a heterogeneous DataFrame to NumPy. Identify lost labels and coerced dtypes, then design a boundary object that retains the row and feature mappings.
119. Test shallow selection and mutation under the pandas versions available to you. Document copy-on-write assumptions without relying on private memory-manager internals.
120. Construct truth tables for nullable Boolean AND, OR, NOT, equality, and reduction. Compare with Python Boolean and IEEE NaN behaviour.
121. Show the difference among an empty group, an all-missing group, and a group summing to zero using <code>sum</code>, <code>count</code>, <code>size</code>, and <code>min_count</code>.
122. Invent data plausibly missing completely at random, at random conditional on an observed variable, and not at random. State assumptions, not just patterns.
123. Compare complete-case, mean-imputed, indicator-augmented, and multiple-imputation analyses conceptually. State how each changes target and uncertainty.
124. Produce a missingness audit by column, reason, time, source, and group. Include counts and denominators, and distinguish structural inapplicability from unknown values.
125. Demonstrate <code>loc</code>’s inclusive label slicing and <code>iloc</code>’s half-open positional slicing on an integer-labelled index.
126. Apply a reversed-index Boolean Series mask to a DataFrame. Explain alignment, then reject a mask with missing or duplicate labels under a strict contract.
127. Compare scalar, Series-aligned, and array-positional assignment. Check values, dtype changes, labels, and rows outside the target.
128. Integrate Chapters 9–12: design an immutable schema class and a validated DataFrame loader with typed interfaces, domain exceptions, fixtures, unit tests, integration tests, and API documentation.

### 16.30.11 Grouping, joining, reshaping, and time

129. Group a categorical column containing an unobserved level and a missing key. Compare every combination of relevant <code>observed</code> and <code>dropna</code> policies.
130. For the same groups, compare <code>size</code>, <code>count</code>, Boolean sum, and <code>nunique</code>. Attach a distinct substantive question to each result.
131. Implement one aggregation, one transformation, one whole-group filter, and one general apply. State result cardinality and index contract before execution.
132. Sort longitudinal records by entity and time, then calculate lag and difference. Introduce a duplicate time and specify a deterministic tie policy rather than accepting arbitrary order.
133. Compare two-row and two-hour rolling means on irregular observations. Vary closure, alignment, and minimum-period options and explain boundary differences.
134. Predict exact output rows for one-to-one, many-to-one, one-to-many, and many-to-many joins with matched, unmatched, and duplicate keys; verify using <code>validate</code>.
135. Add null keys to both join inputs. Quantify pandas’ null-to-null matches and implement a domain policy that prevents unknown identities from matching.
136. Write reconciliation checks for an enrichment join: row count, key multiset, unmatched keys, duplicate suffix columns, and a conserved measure.
137. Implement semi-join and anti-join semantics with an indicator merge. Ensure duplicate right keys cannot multiply left rows.
138. Use an as-of join to attach the latest configuration known before each event. Test sorting, grouping, tolerance, exact matches, and prevention of future leakage.
139. Melt a table whose column names encode measure and period. Parse the names, validate generated keys, and restore the original modulo an explicitly stated column order.
140. Supply duplicate pivot coordinates. Compare rejecting them, adding a missing identifier, and aggregating with <code>pivot_table</code>; explain which information each preserves.
141. Explode a list-valued column while carrying an entity-level amount. Demonstrate double counting and implement two defensible allocation policies.
142. Localise naive civil times across spring and autumn clock transitions. Test nonexistent and ambiguous policies and preserve original labels for audit.
143. Contrast adding 24 hours, one calendar day, and one month to aware timestamps. Explain results in terms of instants, civil time, and calendar rules.
144. Resample event counts into hourly bins with boundary events. Vary <code>closed</code>, <code>label</code>, <code>origin</code>, and zone, and state the exact interval represented by each output label.
145. Build a point-in-time-correct feature table with occurrence, availability, ingestion, and revision timestamps. Prove through tests that no value available after a prediction cutoff enters the feature set.

### 16.30.12 Inference, testing, association, and causality

146. For one population quantity, write an estimand, three possible estimators, and realised estimates. Compare bias, variance, robustness, and computational cost under a simulation model.
147. Simulate the bias–variance–MSE decomposition for a deliberately biased shrinkage estimator and an unbiased estimator. Identify sample sizes where each has lower MSE.
148. Construct an unequal-probability sample. Compare unweighted and inverse-probability-weighted means and explain the population each targets.
149. Simulate clustered observations with varying intracluster correlation. Compare naive and cluster-aware standard errors and relate the result to effective sample size.
150. Bootstrap paired data once by individual values and once by pairs. Show which procedure preserves the estimand and dependence.
151. Compare an ordinary row bootstrap, cluster bootstrap, block bootstrap, and parametric bootstrap for one hypothetical study; state the exchangeability assumption of each.
152. Construct confidence, prediction, tolerance, and Bayesian credible interval interpretations for the same apparent numeric bounds. Explain why the labels cannot be exchanged.
153. Compare a naive Wald interval and Wilson interval for binomial proportions near zero at small sample sizes. Evaluate coverage by simulation under a stated model.
154. Design a test by stating null and alternative, statistic, direction, significance level, stopping rule, and rejection region before generating data.
155. Estimate power across a grid of effect sizes and sample sizes. Explain why one number called “the power of the study” is incomplete.
156. Perform a paired and an incorrectly independent comparison on the same repeated-measures data. Trace the different standard-error assumptions.
157. Simulate ten null tests repeatedly and estimate family-wise error without correction, with Bonferroni, and with Holm. Compare error and power under mixed alternatives.
158. Implement and test Benjamini–Hochberg using sorted p-values. Explain the meaning of FDR and why selecting the displayed family after inspection invalidates the exercise.
159. Define a minimum practically important effect and perform an equivalence analysis. Distinguish “failed to reject difference” from affirmative equivalence evidence.
160. Create a nonlinear deterministic relationship with zero Pearson correlation and a grouped dataset exhibiting Simpson reversal. Use plots and stratified summaries to diagnose both.
161. Draw DAGs for confounding, mediation, and collider selection. For each, predict what adjustment does to the causal estimand and identify an empirical context.
162. Formulate a potential-outcomes estimand for an intervention. State consistency, exchangeability, positivity, interference, measurement, and transport assumptions; then explain why predictive accuracy alone does not identify it.

### 16.30.13 Visualisation, performance, and reproducibility

163. Re-express one dataset with bars, points, lines, and areas. For each mark, state the comparison implied and identify any invented baseline, ordering, or interpolation.
164. Create a histogram, ECDF, box plot, and raw-dot plot for the same skewed sample. Vary bin width or bandwidth and document conclusions that remain stable.
165. Plot a mean confidence interval and an individual prediction interval together. Label them and explain why their widths answer different uncertainty questions.
166. Redesign a colour-only figure for common colour-vision deficiencies and monochrome printing. Add redundant channels and write concise alternative text.
167. Construct a misleading chart using truncated bars, unequal bin widths, or area scaling, then repair it and quantify the original graphical distortion.
168. Benchmark a NumPy operation under representative shapes and dtypes. Separate setup, warm-up, execution, allocation, correctness, and timing dispersion.
169. Calculate the theoretical temporary memory of a chained array expression, measure peak memory, then implement a safe buffered or fused alternative.
170. Demonstrate thread oversubscription using nested process/native thread settings in a controlled environment. Record CPU allocation and explain why more workers can be slower.
171. Implement a chunked mean and variance with mergeable sufficient state. Prove why averaging chunk means fails for unequal chunk sizes and why chunk medians do not determine the global median.
172. Create an environment manifest containing direct requirements, resolved versions, Python/platform details, native numerical configuration, input hashes, parameters, and output hashes without exposing secrets.
173. Take a notebook with hidden out-of-order state, restart and execute it cleanly, move stable logic into an importable module, and add regression and invariant tests.
174. Design a reproducibility package for restricted personal data. Include lawful metadata, synthetic fixtures, controlled-access instructions, deletion/retention policy, code, schemas, and independently verifiable aggregate checks.

### 16.30.14 Comprehensive capstone

175. Design and execute a complete, ethically and legally permissible empirical study. Freeze source identity; define population, unit, estimand, sampling/observation mechanisms, and causal limits; implement versioned schema validation; preserve missing reasons and time availability; use memory-aware arrays and cardinality-checked relational transformations; justify descriptive and inferential procedures; quantify numerical and statistical uncertainty; construct accessible traceable figures; benchmark only a demonstrated bottleneck; package code, tests, environment, manifests, and documentation; conduct a clean-room rebuild; and write a critical report separating measurements, assumptions, computations, associations, causal claims, limitations, and unresolved threats to validity. Integrate version control and review practices from Chapter 12, complexity reasoning from Chapter 13, and concurrency discipline from Chapter 14.
