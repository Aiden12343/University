# 17.36 Exercises

### 17.36.1 Problem formulation

1. Rewrite five vague prediction requests as task specifications containing unit, prediction time, input window, target, horizon, population, output, decision, and harm.
2. For each specification, identify at least three features that would leak future or target information.
3. Construct a loss table for false positives and false negatives under unequal costs. Derive the decision rule for calibrated probabilities under those assumed costs.
4. Distinguish estimand, estimator, estimate, model parameter, and hyperparameter in one regression study.

### 17.36.2 Evaluation

5. Create data containing repeated entities. Compare a random row split with a group-held-out split and explain the performance difference.
6. Create a temporal dataset with drift. Compare shuffled cross-validation with forward validation.
7. Demonstrate preprocessing leakage numerically by scaling or selecting features before splitting. Then repair it with a pipeline.
8. Implement nested cross-validation for a small hyperparameter grid. State what the inner and outer scores estimate.
9. For an imbalanced classification problem, calculate confusion matrix, precision, recall, specificity, accuracy, ROC AUC, average precision, Brier score, and log loss. Explain a decision each metric can and cannot support.
10. Choose a threshold under an explicit capacity limit. Evaluate it on data not used to choose it.

### 17.36.3 Models

11. Fit constant, linear, ridge, tree, and forest baselines to the same regression problem. Compare errors, variance across splits, fitting time, prediction time, and artifact size.
12. Derive the one-parameter squared-error gradient used in Worked example 17.7. Verify it against a central finite difference for several weights.
13. Implement binary logistic prediction from arithmetic and <code>math.exp</code>. Address overflow for extreme scores.
14. Train decision trees over a range of depths. Plot training and validation loss and identify underfitting and overfitting regions without claiming a universal optimum.
15. Construct two geometrically distinct clusterings of the same points by changing scale or distance. Explain why neither is algorithmically “false.”

### 17.36.4 Neural computation

16. Calculate a two-layer network forward pass by hand for one input and fixed small matrices.
17. Draw its computation graph and derive every parameter gradient by the chain rule.
18. Reproduce the gradients with an automatic-differentiation framework and compare numerical values.
19. Write a training loop with separate training, validation, and final test phases. Verify mode switching, gradient clearing, non-leaking transforms, checkpoint criteria, and deterministic configuration.
20. Profile CPU and accelerator versions with correct synchronisation. Explain transfer and batch-size effects.

### 17.36.5 Initial synthesis

21. Define a socially or operationally realistic prediction task. Create a model card stating intended use, exclusions, population, features, label process, loss, validation design, baseline, selected model, calibration, threshold policy, subgroup performance with uncertainty, privacy, security, monitoring, and retirement. Package the complete preprocessing and estimator pipeline; reproduce it from a clean environment; expose a validated prediction boundary; simulate distribution shift; and demonstrate rollback. The report must separate predictive association from causal claims.

### 17.36.6 Representation and data quality

22. For a hospital readmission proposal, identify the unit of observation, prediction time, observation window, horizon, target event, censoring rule, and action. Show how changing only the prediction time changes which features are lawful.
23. Translate a business request to “predict valuable customers” into three inequivalent supervised tasks. For each, state whose value is represented, how labels arise, and one harm hidden by the original phrase.
24. Construct a small table in which two rows refer to the same person at different times. Give one valid row-wise task and one task for which treating the rows as independent is invalid.
25. Design a feature dictionary for ten variables. Include semantic type, storage dtype, units, allowed range, missingness meaning, provenance, availability time, and owner.
26. Create examples of nominal, ordinal, interval-like, ratio-scale, cyclic, free-text, and timestamp features. Explain why a storage dtype alone cannot determine a valid encoding.
27. Encode one categorical column by ordinal integers and one-hot vectors. Calculate Euclidean distances and show which unsupported geometry ordinal encoding introduces.
28. Implement an encoder that maps known categories to fixed columns and unseen categories to an explicit unknown column. Test missing values, new categories, and stable column ordering.
29. Compare standardisation, robust scaling, and no scaling on data with one extreme outlier. State what each transformation learns and why its fitted statistics belong inside validation.
30. Construct missingness that is independent of all variables, missingness related to observed variables, and missingness related to an unobserved value. Compare complete-case and indicator-plus-imputation estimates without claiming universal identification.
31. Build a target whose recorded labels contain symmetric and class-dependent noise. Measure how accuracy, log loss, and calibration respond as noise grows.
32. Create duplicated and near-duplicated records. Show how they alter effective sample size and how a random split can place copies on both sides.
33. Hash raw records after canonicalisation and use the digests to audit exact overlap among train, validation, and test partitions. Explain why different digests do not prove semantic independence.
34. Represent a document collection with a sparse term matrix and calculate its density and approximate dense versus sparse storage. Identify operations that would accidentally densify it.
35. Compare a hand-designed feature, a one-hot representation, and a learned embedding for one task. State what information each representation can and cannot preserve.
36. Construct a feature available in the warehouse today but unavailable at the historical decision time. Write a point-in-time availability test that rejects it.
37. Define a sample-weighting scheme for unequal inclusion probabilities. Derive the weighted empirical risk and discuss how extreme weights affect variance.
38. Simulate label censoring caused by an intervention: outcomes are observed only when a prior policy accepts an applicant. Explain why ordinary supervised learning cannot identify rejected applicants’ outcomes without assumptions.
39. Write a data-validation function checking schema, dtype, unit range, category set, uniqueness constraint, temporal order, and target domain. Supply one failing test for each invariant.
40. Produce a data card for a synthetic dataset. Document generation, population, exclusions, row semantics, feature timing, label construction, known biases, privacy, licence, maintenance, and prohibited uses.

### 17.36.7 Splitting, preprocessing, and leakage

41. Generate grouped observations with strong within-group similarity. Compare row-wise <code>KFold</code> with <code>GroupKFold</code>, reporting the group overlap and explaining the score difference.
42. Generate monthly data with an abrupt regime change. Compare shuffled cross-validation, expanding-window validation, and a final future holdout.
43. Define a prediction problem with spatial autocorrelation. Design blocked spatial validation and state which deployment geography it estimates.
44. Demonstrate direct target leakage, post-outcome leakage, global preprocessing leakage, duplicate leakage, and selection leakage as five distinct executable examples.
45. Fit a mean imputer before and inside cross-validation. Instrument its learned mean in each fold and explain why the first procedure gives the model information about held-out inputs.
46. Select the best 20 of 5,000 random features on the complete dataset before splitting. Compare this result with feature selection inside a pipeline.
47. Implement target mean encoding naively, then implement out-of-fold encoding for training rows and training-only encoding for validation rows. Verify that a unique identifier cannot memorise its own target.
48. Build a <code>ColumnTransformer</code> for numeric, ordinal, nominal, and text inputs. Inspect output names, sparse format, and unknown-category behaviour.
49. Write a custom scikit-learn transformer whose <code>fit</code> learns medians and whose <code>transform</code> preserves row count and column order. Pass estimator compliance checks relevant to its interface.
50. Show that calling <code>fit_transform</code> separately on training and test categorical data can produce incompatible columns. Repair the boundary with one fitted encoder.
51. Compare stratified and unstratified folds for a rare binary target. Explain which variance stratification reduces and which dependencies it leaves untouched.
52. Design a split for household members, clinics, and calendar time simultaneously. State which generalisation claim each held-out dimension supports and what cannot be estimated from one design.
53. Give an example in which a random train/test split is appropriate. Defend it by reference to the sampling unit, deployment mechanism, and absence of relevant dependence.
54. Simulate repeated tuning against one validation set. Plot its apparent improvement against performance on an untouched confirmation set.
55. Implement nested cross-validation with preprocessing and a conditional hyperparameter grid. Record the configuration selected in each outer fold and interpret disagreement.
56. Compare leave-one-out, five-fold, and repeated five-fold validation for a stable linear model and an unstable tree. Measure computation and score variance.
57. Audit a pipeline for metadata routing of sample weights and groups. Verify which steps consume, transform, or reject each item.
58. Create a time-aware feature such as “events in the preceding 30 days.” Implement it without allowing the current or future event into its own history.
59. Construct an adversarial leakage test: randomly permute labels, run the complete development procedure, and investigate any performance materially above chance.
60. Write a split manifest containing immutable row identifiers, group identifiers, event times, random seed, splitter version, and digests. Recreate exactly the same partitions in a clean process.

### 17.36.8 Metrics, calibration, and decisions

61. From a stated confusion matrix, calculate prevalence, sensitivity, specificity, precision, negative predictive value, false-positive rate, false-negative rate, accuracy, balanced accuracy, and \(F_1\) by hand.
62. Hold sensitivity and specificity fixed while varying prevalence. Calculate precision and explain why it changes without any change in conditional test performance.
63. Construct two classifiers whose ROC curves cross. Identify operating regions in which each is preferred and show why one AUC cannot settle the decision.
64. Plot precision–recall curves for identical conditional score distributions under three prevalences. Explain the changed baseline and interpretation.
65. Compute log loss and Brier score for confident correct, uncertain, confident incorrect, and clipped predictions. Compare their penalty geometry.
66. Decompose a multiclass confusion matrix into one-versus-rest components. Compare macro, micro, and weighted averaging under class imbalance.
67. For a multilabel task, compare subset accuracy, Hamming loss, per-label macro \(F_1\), and example-wise \(F_1\). Give two predictions ranked oppositely by these metrics.
68. Create equal-width and equal-frequency reliability diagrams. Display bin counts and explain how binning can conceal local miscalibration.
69. Implement expected calibration error under two bin schemes. Demonstrate that it is an estimator dependent on bins rather than a uniquely defined population truth.
70. Fit sigmoid and isotonic calibration on a separate calibration partition. Compare calibration and discrimination, and explain why calibrating on training predictions is optimistic.
71. Derive the optimal binary action threshold for calibrated probabilities with false-positive cost \(C_{FP}\) and false-negative cost \(C_{FN}\). State the assumptions under which the derivation holds.
72. Select a threshold subject to a review capacity of 100 cases per week. Estimate uncertainty in the achieved recall when weekly volume and prevalence vary.
73. Add an abstain option with a fixed review cost. Derive score regions for negative, review, and positive actions under a simple cost table.
74. Compare mean absolute error and root mean squared error on residuals containing one extreme value. Relate each metric to its implied loss.
75. Demonstrate why mean absolute percentage error is unstable near zero and asymmetric under over- and under-prediction. Propose a domain-appropriate alternative.
76. For a count outcome, compare squared error, Poisson deviance, and a zero-inflated setting. Identify which distributional assumptions require examination.
77. Create prediction intervals with nominal 90% coverage. Evaluate marginal coverage, width, and coverage across important subgroups and target ranges.
78. Bootstrap a metric by rows and by groups on clustered data. Compare intervals and identify the correct resampling unit.
79. Calculate a paired bootstrap interval for the score difference between two models evaluated on the same cases. Contrast it with an invalid unpaired analysis.
80. Define a metric whose average conceals catastrophic failure in a small group. Add a slice metric and a worst-group criterion, discussing sample uncertainty.
81. Evaluate calibration after a prevalence shift. Separate changed calibration-in-the-large, discrimination, and threshold utility.
82. Write an evaluation report that distinguishes descriptive estimates, confidence intervals, selection-adjusted evidence, practical significance, and limits of external validity.

### 17.36.9 Linear, logistic, and regularised models

83. Derive the normal equations from the squared-error objective using component-wise differentiation, then verify the residual orthogonality condition numerically.
84. Solve one least-squares problem using an explicit inverse, QR-based <code>lstsq</code>, and an SVD pseudoinverse. Increase collinearity and compare numerical error.
85. Construct a rank-deficient design matrix. Find two coefficient vectors with identical fitted values and explain what the pseudoinverse selects.
86. Change a predictor from metres to millimetres. Derive the coefficient change and verify identical predictions.
87. Add a product interaction to a linear model. Calculate the marginal slope of one feature at three values of the other and interpret the intercept after centring.
88. Fit polynomial regressions of increasing degree within a pipeline. Plot interpolation range and extrapolation range separately.
89. Simulate heteroskedastic errors. Compare residual plots and ordinary versus heteroskedasticity-robust coefficient intervals using an appropriate statistical library.
90. Fit a predictive model to confounded observational data. Show that excellent held-out prediction does not recover an intervention effect.
91. Derive the ridge normal equations. Demonstrate that a positive ridge penalty yields a unique slope solution for a singular design when the intercept is handled separately.
92. Compare ridge, lasso, and elastic-net coefficient paths on correlated features. Repeat over bootstrap samples and quantify selection instability.
93. Show why regularisation depends on feature scale by fitting lasso before and after standardisation. Keep preprocessing inside validation.
94. Compare penalising and not penalising an intercept on uncentred data. Identify the library convention used.
95. Implement a numerically stable sigmoid for scalar and array inputs. Test values near the overflow limits of ordinary exponentiation.
96. Derive binary log loss from the Bernoulli likelihood and its gradient with respect to one logit.
97. Fit logistic regression to completely separable data with decreasing regularisation. Track coefficient magnitude and predicted probabilities.
98. Interpret one logistic coefficient as a log-odds and odds ratio, then demonstrate why this is not a constant probability difference.
99. Compare multinomial logistic regression with independent one-versus-rest classifiers. Inspect probability normalisation and decision boundaries.
100. Use class weights in logistic regression. Determine how ranking, intercept, probability calibration, and a fixed threshold change.
101. Construct a full linear-model study with preregistered features, nested penalty selection, final calibration where relevant, coefficient stability analysis, and an untouched temporal evaluation.

### 17.36.10 Trees, ensembles, neighbours, and unsupervised learning

102. Calculate every candidate threshold and impurity reduction for a six-row one-feature classification tree; identify the selected split by hand.
103. Fit trees at increasing depth and minimum leaf size. Compare training error, validation error, number of leaves, and prediction discontinuities.
104. Find two training samples differing by one row that yield different root splits. Use the result to illustrate tree instability.
105. Compare cost-complexity pruning selected inside validation with choosing a displayed tree after inspecting test performance.
106. Implement a bootstrap sampler and estimate the expected fraction of unique rows. Compare simulation with \(1-e^{-1}\).
107. Fit a bagging ensemble while increasing the number of estimators. Track individual-tree variance, correlation, ensemble variance, and computation.
108. Compare out-of-bag estimates with an independent holdout. Identify cases that receive few out-of-bag predictions.
109. Compare random forests with and without feature subsampling on datasets containing redundant and dominant features.
110. Trace three iterations of gradient boosting on a tiny squared-error dataset, calculating residual targets and the additive update manually.
111. Tune a boosted-tree model under a fixed compute budget. Examine interactions among learning rate, tree depth, estimator count, and early stopping.
112. Build a stacking model using in-sample base predictions and observe leakage; repair it with out-of-fold base predictions.
113. Compare impurity-based and permutation feature importance when one feature has high cardinality and two are correlated.
114. Implement brute-force \(k\)-nearest-neighbour classification. Test tie handling, distance weighting, and the effect of standardisation.
115. Measure neighbour distance contrast as dimensionality grows for random points. Relate the result to the curse of dimensionality without claiming all high-dimensional data are uniform.
116. Compare exact and approximate neighbour search by recall, build time, query latency, memory, and downstream metric.
117. Implement Lloyd’s \(k\)-means updates. Run several initialisations and report objective, cluster sizes, and sensitivity to scale.
118. Construct elongated and unequal-density clusters for which \(k\)-means is misleading. Compare another clustering objective and state its assumptions.
119. Compute PCA by centred SVD. Verify orthogonality, explained variance, reconstruction error, and the effect of standardisation.
120. Compare isolation, density, and reconstruction-based anomaly scores on injected anomalies. Choose a threshold without treating the score as an event probability.

### 17.36.11 Calculus, gradients, and optimisation

121. Derive the derivative of \(x^3\) from the limit definition by algebraic expansion.
122. Give functions that are continuous but non-differentiable, differentiable once but not twice, and discontinuous. Plot and analyse their relevant points.
123. Calculate the gradient and Hessian of a two-variable quadratic. Classify stationary points from Hessian eigenvalues.
124. Compute a Jacobian for a vector-valued function by hand and verify Jacobian–vector products against finite directional differences.
125. Compare forward, backward, and central finite differences across step sizes and dtypes. Plot truncation and rounding regimes.
126. Implement gradient descent on a scalar quadratic. Derive the exact step-size range for convergence and demonstrate boundary behaviour.
127. Optimise a two-dimensional ill-conditioned quadratic. Compare raw coordinates, standardised coordinates, and a matrix preconditioner.
128. Construct a convex function, a strictly convex function, and a non-convex function. Identify local and global minima without relying only on plots.
129. Implement fixed, exponential-decay, step-decay, and cosine learning-rate schedules. Compare updates at equal compute.
130. Define three stopping criteria based on objective change, gradient norm, and validation patience. Produce a case where each stops misleadingly.
131. Prove that a uniformly sampled per-example gradient is unbiased for empirical risk. Then show how non-uniform sampling changes the expectation.
132. Measure mini-batch gradient variance across batch sizes. Distinguish variance per update from total compute to reach a target loss.
133. Implement momentum from its recurrence. On a narrow quadratic valley, compare its trajectory with plain gradient descent.
134. Implement scalar RMSProp and Adam, including bias correction. Unit-test the first two updates against hand calculations.
135. Compare coupled \(L_2\) regularisation with decoupled weight decay for an adaptive optimiser on a two-parameter problem.
136. Save and restore model parameters without optimiser state halfway through training; contrast the trajectory with exact state restoration.
137. Build a computation graph for \(L=(\sin(wx)+b-y)^2\). Perform a complete forward and reverse table containing every primal and adjoint.
138. Implement a minimal scalar reverse-mode automatic-differentiation class supporting addition, multiplication, power, and topological backpropagation. Test shared subexpressions.
139. Compare reverse-mode cost for one scalar output and many inputs with forward finite differences. State memory and computation trade-offs.
140. Create a deliberate gradient defect through broadcasting or detachment. Locate it with shape assertions, anomaly checks, and finite-difference comparison.

### 17.36.12 Neural networks and framework semantics

141. Calculate the parameter count and every intermediate shape for a three-layer dense network, including batch and bias broadcasting dimensions.
142. Show algebraically that a composition of affine layers without nonlinear activations is one affine map; verify numerically.
143. Initialise a deep network with overly small, overly large, Xavier-style, and He-style scales. Measure activation and gradient variance by layer.
144. Compare sigmoid, tanh, ReLU, leaky ReLU, and a smooth rectifier by value and derivative over a wide range. Identify saturation and kink conventions.
145. Implement stable binary cross-entropy from logits and compare it with a naive sigmoid-plus-log implementation at extreme scores.
146. Pair output layers and losses for regression, binary, exclusive multiclass, and multilabel tasks. Create a test that catches an invalid pairing.
147. Train a small NumPy multilayer perceptron with one hidden layer, manual backpropagation, mini-batches, and a held-out validation set.
148. Recreate Exercise 147 in an automatic-differentiation framework. Compare parameters after one deterministic update to the manual implementation.
149. Demonstrate gradient accumulation over unequal mini-batches. Derive the weighting needed to match one full-batch mean gradient.
150. Add gradient-norm clipping and record pre- and post-clipping norms. Diagnose rather than conceal deliberately induced exploding gradients.
151. Compare training and evaluation behaviour for dropout and batch normalisation. Write tests that fail when module mode is incorrect.
152. Save a complete checkpoint including optimiser, scheduler, random generators, epoch, and sampler progress. Verify an interrupted run reproduces the uninterrupted next update.
153. Benchmark one tensor operation correctly on CPU and an available accelerator, including warm-up and synchronisation. Report shapes, dtypes, transfers, and uncertainty.
154. Create a non-contiguous transposed tensor. Test view, reshape, contiguous conversion, storage sharing, mutation, and gradient behaviour.
155. Compute a one-dimensional cross-correlation by hand and in a framework. Derive output length and receptive field for a three-layer convolutional stack.
156. Implement scaled dot-product attention with padding and causal masks. Test row sums, forbidden weights, all-masked rows, and numerical stability.
157. Tokenise multilingual and unusual Unicode examples with an available subword tokeniser. Compare character, byte, word, and token lengths, documenting normalisation and special tokens.

### 17.36.13 Selection, shift, fairness, explanation, and operations

158. Define a mixed log-uniform, integer, categorical, and conditional hyperparameter space. Compare grid and random search coverage under the same trial budget.
159. Simulate selection among increasing numbers of equally good noisy configurations. Plot the winning validation score and untouched test score as search breadth grows.
160. Run nested cross-validation for two complete learning procedures on paired outer folds. Report differences, uncertainty, compute, and a practical-equivalence margin.
161. Simulate pure covariate shift with support overlap. Estimate density-ratio-weighted risk and show variance as overlap weakens.
162. Simulate label shift and concept drift separately. Determine which observable unlabeled statistics can distinguish them and which require labels or assumptions.
163. Design a monitoring table containing service, schema, drift, score, delayed-outcome, calibration, subgroup, feedback, and human-report signals, with owner and response for each.
164. Trace a recommendation feedback loop using a causal diagram. Identify exposure bias and propose an exploration or evaluation design.
165. For one confusion matrix per group, calculate demographic parity, equal opportunity, equalised odds components, predictive parity, and calibration evidence. Describe the incompatible objectives.
166. Add uncertainty intervals to group metrics under unequal group sizes. Investigate an intersectional subgroup whose aggregate parent groups appear adequate.
167. Compare a shared threshold, group-specific thresholds, and an abstention policy under explicit benefits, harms, legal constraints, and capacity.
168. Compute permutation importance with independent and correlated features. Compare held-out importance, training importance, and coefficient magnitude.
169. Produce partial-dependence and individual-conditional-expectation plots for an interacting model. Highlight unsupported feature combinations.
170. Generate local surrogate, Shapley-style, and counterfactual explanations for one prediction. Change the background or distance definition and measure instability.
171. Threat-model model artifacts, prediction inputs, training data, dependency supply chain, extraction attacks, denial of service, and sensitive logs. Specify controls and residual risks.
172. Design shadow, canary, staged expansion, and rollback plans for a model plus its feature and threshold versions. State acceptance and emergency-stop criteria.
173. Build a prediction service boundary with schema validation, bounded resources, model identity, structured errors, privacy-aware logging, health checks, and property-based tests.
174. Reproduce an experiment in a clean environment from a manifest. Compare exact, tolerance-based, statistical, and substantive equivalence and record every divergence.

### 17.36.14 Final integrated branch capstone

175. Conduct an end-to-end machine-learning study whose question has genuine operational consequences. Pre-register the unit, time boundary, target, population, action, harms, validation design, baseline, primary metric, and practical margin. Build point-in-time-correct data with a versioned schema and data card; implement all learned preprocessing inside a pipeline; compare classical and, only if justified, neural candidates through nested or temporally external validation; evaluate discrimination, calibration, thresholds, uncertainty, subgroup behaviour, latency, memory, and failure cases; preserve every material trial; construct a signed, versioned artifact and model card; expose it behind a validated and observable prediction boundary; test shadow release, drift, delayed labels, feedback, incident response, and rollback; reproduce the result from a clean environment; and defend, in a formal report, why the system should be deployed, restricted, redesigned, or rejected. Distinguish association, prediction, intervention, and normative judgement throughout.
