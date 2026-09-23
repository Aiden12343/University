# 17.35 Common misconceptions consolidated

1. **“Machine learning lets the computer decide what matters.”** Humans define task, data, target, loss, model class, and use.
2. **“Training accuracy measures learning.”** It measures fit to training cases and can reward memorisation.
3. **“Random splitting is neutral.”** It can violate time, group, spatial, and deployment boundaries.
4. **“Leakage only means including the target column.”** Any improper information path can contaminate evaluation.
5. **“Cross-validation proves future performance.”** It estimates a procedure under a chosen resampling design and assumptions.
6. **“Accuracy is the classification metric.”** Its usefulness depends on prevalence and error costs.
7. **“Probability 0.8 means the event will occur.”** It is a graded forecast whose calibration is a population property.
8. **“Logistic regression is a regression model rather than a classifier.”** It models log-odds for a categorical target; the historical name refers to the parametric relation.
9. **“A tree explains itself.”** Visible rules can still encode proxies, artefacts, and complex institutional meanings.
10. **“Feature importance is causal importance.”** It is conditional on model, metric, data, and perturbation.
11. **“Clusters are discovered natural kinds.”** They are solutions relative to representation and objective.
12. **“The gradient gives the globally best direction.”** It gives local first-order sensitivity and can lead to different outcomes across landscapes.
13. **“Backpropagation is biological learning.”** It is reverse-mode derivative accumulation on a computation graph.
14. **“An accelerator makes every tensor operation faster.”** Transfer, launch, synchronisation, and small workloads can dominate.
15. **“A better benchmark score means a better deployed system.”** Distribution shift, calibration, harms, latency, and workflow can reverse the judgement.
16. **“Removing a sensitive field makes a model fair.”** Proxy information and structural bias can remain.
17. **“A saved model is just data.”** Many formats are executable or version-coupled artifacts and require supply-chain controls.
18. **“More data always improves a model.”** Additional rows can be biased, duplicated, stale, mislabeled, or drawn from the wrong population.
19. **“A feature is a fact about the world.”** It is a represented measurement produced by a collection and transformation process.
20. **“Missing values are merely blanks to fill.”** Missingness can reveal collection mechanisms and can change between training and use.
21. **“One-hot encoding makes categories objective.”** The categories, grouping, reference, and treatment of unseen values remain modelling choices.
22. **“A high-dimensional embedding preserves all relevant meaning.”** An embedding retains relations favoured by its training objective and data.
23. **“A loss function measures real-world harm directly.”** It is a numerical proxy whose units, weighting, and omissions require justification.
24. **“Class imbalance must be fixed by balancing the dataset.”** Sampling changes the fitted objective and perhaps probability calibration; threshold and metric choices may address a different problem.
25. **“A test set can be reused because its rows never enter gradient descent.”** Adaptive inspection transfers information from the test results into model selection.
26. **“Stratification makes a split representative.”** It preserves selected marginal proportions, not group independence, time order, covariate structure, or deployment conditions.
27. **“Five-fold cross-validation supplies five independent experiments.”** The training sets overlap and scores are statistically dependent.
28. **“Standardisation is required by every model.”** Its relevance depends on geometry and optimisation; it can be immaterial to ordinary tree splits.
29. **“Imputation recovers the unknown true value.”** It supplies a model-compatible replacement and can add uncertainty or bias.
30. **“A coefficient near zero proves no relationship.”** Scale, correlation, regularisation, interactions, uncertainty, and misspecification affect coefficients.
31. **“A small p-value would prove useful prediction.”** Inferential evidence about a parameter and out-of-sample decision performance are different questions.
32. **“Lasso is an automatic scientific variable selector.”** Its selected set can be unstable under correlation and is conditional on representation and penalty.
33. **“A predicted probability is calibrated by definition.”** Scores between zero and one require empirical calibration assessment on relevant new data.
34. **“ROC AUC tells how a deployed threshold will perform.”** It averages ranking behaviour across thresholds and does not specify one operating point or its costs.
35. **“Precision and recall are properties of a model alone.”** They depend on threshold, population prevalence, label definition, and evaluation sample.
36. **“Random forests cannot overfit.”** Averaging reduces some variance, but depth, leakage, selection, noise, and shift still matter.
37. **“Boosting only combines weak models and must improve them.”** It sequentially optimises a specified objective and can fit noise or fail under unsuitable settings.
38. **“Nearest neighbours have no training phase.”** They store and index training data, choose a representation and metric, and can incur substantial fit-time construction.
39. **“PCA selects the most predictive directions.”** It maximises represented input variance without using a supervised target.
40. **“An anomaly score is a probability of fraud or failure.”** It is a model-relative unusualness score unless separately calibrated to a defined event.
41. **“The learning rate controls only training speed.”** It can change stability, implicit regularisation, and the solution reached.
42. **“A larger batch is a strictly better gradient estimate.”** It lowers some sampling variance but changes update count, memory, hardware use, and optimisation dynamics.
43. **“A low training loss proves that backpropagation worked correctly.”** A flawed target, broadcasting error, or leakage can be optimised successfully.
44. **“Neural networks learn features without human assumptions.”** Architecture, tokenisation, augmentation, objective, and data encode extensive assumptions.
45. **“Dropout should remain active to improve every prediction.”** Ordinary inference disables it; stochastic inference is a separate uncertainty procedure requiring validation.
46. **“Attention eliminates sequence-length limitations.”** Full attention has quadratic pair structure and every implementation has context, memory, and positional limits.
47. **“A deterministic run is scientifically reproducible.”** It can deterministically repeat a biased sample, invalid evaluation, or software defect.
48. **“Drift can be solved by adding the newest data.”** New data may lack mature labels, reflect feedback, or sacrifice important historical regimes.
49. **“An explanation makes an automated decision accountable.”** Accountability also requires authority, evidence, appeal, governance, and the ability to change the system.
50. **“Monitoring average accuracy is enough after deployment.”** Delayed labels, subgroup failures, calibration, service defects, feedback, and rare severe harms require distinct observability.
