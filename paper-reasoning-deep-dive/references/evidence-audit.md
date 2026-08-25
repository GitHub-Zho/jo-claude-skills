# Evidence and evaluation audit

Use this reference to determine what the experiments actually establish.

## Table of contents

1. Claim-evidence ledger
2. Metric interpretation
3. Comparator fairness
4. Ablations and causal claims
5. Reliability and uncertainty
6. Qualitative and human evaluation
7. Reproducibility

## 1. Claim-evidence ledger

Create one row per central claim:

| Claim | Evidence location | Metric and protocol | Comparator | Controls | Result | What follows | What does not follow |
|---|---|---|---|---|---|---|---|

Keep capability claims, efficiency claims, mechanism claims, and generalization claims separate. A result supporting one category does not automatically support another.

## 2. Metric interpretation

For every important metric, explain:

- its unit and aggregation rule;
- what counts as success;
- whether higher or lower is better;
- whether it measures correctness, preference, calibration, robustness, efficiency, or another property;
- the evaluation sample size and variance when reported;
- what the metric does not measure;
- how the metric could be gamed or saturated;
- whether two reported numbers use the same protocol.

Check decoding settings, number of samples, pass@k versus pass@1, self-consistency, tool access, prompt format, test-time compute, and judge model. Do not compare scores produced under different protocols as if they were directly equivalent.

## 3. Comparator fairness

Audit whether baselines receive comparable:

- training data and contamination controls;
- parameter count or model family;
- training and inference compute;
- retrieval, tools, memory, and external resources;
- hyperparameter tuning effort;
- prompt and output constraints;
- test-time sampling budget;
- evaluation dates and benchmark versions.

Call a comparison informative but unmatched when fairness is incomplete. Do not discard useful evidence merely because it is imperfect; narrow the conclusion instead.

## 4. Ablations and causal claims

For each ablation, identify:

1. the intervention;
2. the intended causal variable;
3. other variables that changed;
4. the predicted outcome;
5. the observed outcome;
6. whether the effect is consistent across tasks;
7. whether an interaction with other components is possible.

An ablation can show that a component contributes within the tested system. It does not by itself prove the authors' proposed mechanism or that no simpler substitute works.

Use intermediate measurements to test mechanisms. If a regularizer is said to improve diversity, inspect diversity directly rather than inferring it only from final accuracy.

## 5. Reliability and uncertainty

Check for:

- confidence intervals, standard errors, repeated seeds, or statistical tests;
- small or selectively reported test sets;
- hyperparameter search over the evaluation set;
- benchmark leakage or train-test overlap;
- multiple comparisons and cherry-picking;
- ceiling effects and noisy judges;
- missing failure cases or subgroup analysis;
- results that depend on one model, dataset, language, domain, or scale.

If the paper omits uncertainty, avoid inventing it. State that the stability of the reported difference cannot be assessed from the paper.

## 6. Qualitative and human evaluation

For qualitative examples, ask whether they are representative or illustrative. Look for selection criteria and counterexamples.

For human evaluation, inspect:

- evaluator expertise and blinding;
- rubric clarity;
- number of raters and examples;
- inter-rater agreement;
- ordering effects;
- conflicts of interest;
- whether the judged property matches the paper's claim.

For model-as-judge evaluation, inspect judge identity, prompt, position bias, self-preference, calibration against humans, and reproducibility.

## 7. Reproducibility

Record whether the paper provides:

- code, data, checkpoints, prompts, seeds, and environments;
- exact preprocessing and filtering;
- training budgets and hardware;
- inference and evaluation configuration;
- enough negative results to understand the operating range.

Conclude with the smallest decisive missing experiment: the test that would most reduce uncertainty about the paper's main claim.
