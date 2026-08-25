# Design-rationale reconstruction

Use this reference to recover the paper's decision process rather than summarize its components.

## Table of contents

1. Problem hierarchy
2. Design-decision cards
3. Counterfactual tests
4. Checkpoints as natural experiments
5. Evidence grading
6. Common failure modes

## 1. Problem hierarchy

Separate three levels before analyzing the method:

- **Research problem**: the durable scientific or engineering problem.
- **Operational obstacle**: what prevents current methods from solving it.
- **Paper objective**: the tractable target this paper actually tests.

Do not let a benchmark name substitute for the research problem. State the desired capability, the constraint, and why previous methods fail under that constraint.

## 2. Design-decision cards

Create one card for every consequential module, loss term, data stage, inference procedure, or system component.

```text
Decision: [what was introduced or changed]
Local goal: [what immediate problem it targets]
Prior failure: [observed failure, theoretical limitation, or resource constraint]
Insight: [observation or hypothesis that motivates the decision]
Mechanism: [causal path from intervention to expected effect]
Prediction: [what should change if the explanation is right]
Evidence: [table, figure, equation, ablation, or example]
Counterfactual: [what should happen without this decision]
Tradeoff: [new cost or failure created]
Next decision: [how the next component responds]
Support: [strong / moderate / plausible / under-supported]
```

Preserve the paper's actual chronology only when chronology reflects dependency. Reorder exposition when the paper introduces pieces before explaining their motivation.

## 3. Counterfactual tests

Test the authors' rationale against alternatives:

- Remove the component.
- Replace it with the simplest baseline.
- Keep parameter count, compute, data, and tuning effort comparable.
- Change one decision while holding the rest fixed.
- Predict which metric should move and in what direction.

Distinguish four conclusions:

- **Useful**: adding the component improves an outcome.
- **Necessary in this setup**: removing it reliably causes failure under matched conditions.
- **Mechanistically validated**: intermediate observations match the proposed causal explanation.
- **Uniquely justified**: plausible alternatives were tested and performed worse.

Most ablations establish only the first, occasionally the second, and rarely the third or fourth.

## 4. Checkpoints as natural experiments

Treat staged systems and model checkpoints as a debugging history.

For each transition A → B, record:

```text
Changed variables:
Held-constant variables:
Targeted failure:
Metrics expected to improve:
Metrics expected to stay stable:
Observed gains:
Observed regressions:
Confounders:
Conclusion justified by this transition:
```

Do not attribute a change to one component when data, compute, initialization, evaluation, or decoding also changed.

## 5. Evidence grading

Use the following rubric consistently:

- **Strongly supported**: matched counterfactual or controlled ablation, replicated across relevant settings, with mechanism-consistent intermediate evidence.
- **Moderately supported**: direct result with partial controls, limited tasks, or one important confounder.
- **Plausible**: theory, qualitative examples, or indirect patterns support the explanation, but no decisive test exists.
- **Under-supported**: missing counterfactual, mismatched baseline, contradictory evidence, or a conclusion broader than the evaluation domain.

Grade the rationale, not the paper's overall quality.

## 6. Common failure modes

Avoid these shortcuts:

- “The paper uses X, therefore X is important.”
- “Performance rose after X, therefore X caused the rise.”
- “The full system beats a baseline, therefore every component is necessary.”
- “The mechanism sounds reasonable, therefore the experiment proves it.”
- “A later stage fixes a problem” when it merely hides or trades off that problem.

When evidence is absent, state the missing experiment that would most efficiently resolve the uncertainty.
