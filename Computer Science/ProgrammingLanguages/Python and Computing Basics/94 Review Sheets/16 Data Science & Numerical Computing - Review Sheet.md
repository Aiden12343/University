# 16.29 Common misconceptions consolidated

1. **“Data are raw facts.”** Records are constructed representations with provenance, definitions, and failure modes.
2. **“A larger sample repairs a biased design.”** It can reduce sampling variability while estimating the wrong population quantity more precisely.
3. **“The mean is the normal average.”** Mean, median, mode, and other summaries answer different questions.
4. **“A seed creates randomness.”** It initialises a deterministic generator state; it primarily supports repeatability.
5. **“An ndarray is a nested Python list.”** It is an array object described by shape, dtype, strides, and storage relationships.
6. **“NumPy changes Big-O.”** Native kernels often reduce overhead and improve locality; they do not repeal the operation’s growth class.
7. **“Reshape and transpose always copy.”** Many transformations can be views; layout constraints can nevertheless force copies.
8. **“Broadcasting repeats arrays for free.”** It can avoid repeated input storage but may define an enormous materialised result.
9. **“pandas indices are row numbers.”** They are labels participating in alignment and can be duplicated.
10. **“Dropping missing rows is neutral.”** It changes the analysed population and can induce bias.
11. **“A successful join preserved the data.”** Unexpected key multiplicity can duplicate or discard observations without raising unless validated.
12. **“A small p-value proves an important effect.”** It measures incompatibility with a null model under a procedure, not magnitude, truth probability, or importance.
13. **“Correlation establishes causation.”** Association does not identify an intervention effect without causal assumptions or design.
14. **“A chart displays the data without interpretation.”** Every visual encoding and aggregation is a modelled choice.
15. **“A notebook that runs once is reproducible.”** Hidden state, changing inputs, and unrecorded environments can prevent reconstruction.
16. **“Rows are observations by definition.”** The observational unit and grain come from the study design; one unit may occupy several rows and one row may contain several units.
17. **“Identifiers are just strings.”** An identifier has a scope, issuing authority, uniqueness rule, lifetime, normalisation policy, and privacy implications.
18. **“A census eliminates inferential uncertainty.”** It can remove sampling variation for the enumerated frame while retaining coverage, non-response, measurement, processing, and future-population uncertainty.
19. **“An outlier is a point that should be deleted.”** It may be error, rare valid variation, regime change, or the primary phenomenon; investigate provenance and model influence.
20. **“Standardising makes variables comparable in meaning.”** It rescales by selected centres and spreads but does not equalise units, reliability, consequences, or construct validity.
21. **“Independence means unrelated in ordinary language.”** It is a precise factorisation of joint probabilities under a model; pairwise independence can differ from mutual independence.
22. **“The central limit theorem makes all data normal.”** It concerns limiting distributions of particular normalised aggregates under conditions, not the source observations.
23. **“Floating-point error is random harmless noise.”** It is deterministic given an execution and can accumulate, cancel, overflow, or depend on ordering and conditioning.
24. **“A wider dtype always fixes numerical accuracy.”** Greater range or precision can help but cannot recover lost input information or repair unstable formulation and ill-conditioning.
25. **“Object dtype is a flexible universal representation.”** It sacrifices homogeneous native storage, may conceal mixed types, and applies Python-object semantics with substantial cost.
26. **“A one-dimensional array is a row vector.”** NumPy gives it one axis; row-versus-column structure requires an added axis or contextual convention.
27. **“A small linear-system residual proves coefficient accuracy.”** Ill-conditioning and non-identifiability can permit a tiny residual with unstable parameters.
28. **“Independent random seeds create independent random variables.”** Stream allocation requires a documented generator and spawning strategy; model independence is an ideal property.
29. **“More Monte Carlo draws validate a simulation.”** They address finite simulation noise, not model, algorithmic, discretisation, or implementation error.
30. **“A DataFrame loaded successfully has a schema.”** Inferred dtypes are only representations; semantic constraints, units, keys, and missingness require explicit validation.
31. **“A pandas Index is guaranteed unique.”** It is a label sequence and can contain duplicates; uniqueness must be asserted when used as a key.
32. **“All nulls are equal and false.”** Missing sentinels differ, nullable Boolean logic has an unknown state, and truth conversion may be invalid.
33. **“Imputation repairs incomplete data.”** It encodes assumptions and must propagate uncertainty; it does not recreate observations.
34. **“A Boolean mask always filters by visible order.”** A pandas Series mask aligns by labels; an array-like mask is positional.
35. **“groupby has one obvious result.”** Key missingness, categorical levels, order, aggregation, and empty groups alter the defined partition and output.
36. **“Chunk medians can be averaged into the global median.”** Median lacks the count-and-sum composability of a mean; exact streaming selection needs richer state or external algorithms.
37. **“Null join keys never match.”** pandas equality joins can match null keys to null keys, potentially creating a many-to-many product.
38. **“pivot_table is a convenient pivot that tolerates duplicates.”** It resolves duplicate coordinates by aggregation and therefore changes information.
39. **“A time zone is formatting.”** It supplies date-dependent rules connecting civil labels with instants; conversion and localisation are different operations.
40. **“One day always contains 24 hours.”** Civil days can have different elapsed durations across clock changes; calendar and duration arithmetic differ.
41. **“A confidence interval reports the probability that the fixed parameter is inside.”** Frequentist coverage describes a repeated procedure under assumptions; posterior probability requires a Bayesian model.
42. **“A standard error is the standard deviation of observations.”** It is the standard deviation of an estimator’s sampling distribution, estimated under a design and model.
43. **“Bootstrap means resample whatever rows happen to be stored.”** Resampling must preserve the true observational and dependence units.
44. **“No significant difference means no difference.”** It can reflect weak information; equivalence needs a margin and an appropriate test.
45. **“Multiple-testing correction legitimises exploration after the fact.”** It needs the full selection family and cannot compensate for hidden outcomes or model choices.
46. **“Controlling for every variable removes confounding.”** Adjustment for mediators or colliders can change the target or introduce bias.
47. **“A predictive feature is a causal lever.”** Prediction exploits association at deployment; intervention effects require causal identification.
48. **“Error bars have an obvious meaning.”** They may encode standard deviation, standard error, confidence, credibility, prediction, or quantiles and must be labelled.
49. **“A logarithmic axis merely compresses large numbers.”** It changes visual distance to represent ratios and imposes domain restrictions on zero and negative values.
50. **“Copy-on-write means copies consume no memory.”** It defers some physical copying until mutation; dtype conversion and interoperability can still allocate large buffers.
51. **“Parallelism multiplies performance by core count.”** Serial work, memory bandwidth, coordination, imbalance, and nested native threads constrain scaling.
52. **“A container captures the whole computer.”** It packages user space while sharing a host kernel and depending on external hardware, data, registries, and services.
53. **“A cryptographic hash proves data quality.”** It identifies bytes with high confidence; it says nothing about measurement validity, permissions, or semantic correctness.
54. **“Reproducibility and correctness are synonyms.”** Reproducibility enables inspection of a specified process; a perfectly reproducible process can answer the wrong question.
