# Full deep-dive output template

Adapt this template to the user's question. Omit sections that add no value; do not fill headings mechanically.

## 1. One-sentence thesis

State the hard problem, the central insight, and the paper's intervention in one sentence.

## 2. What problem is the paper really solving?

- Desired capability or scientific question
- Why it is difficult
- Prior method and precise bottleneck
- Scope the paper actually tests

## 3. The key insight

Explain the observation or hypothesis that makes the method plausible. Distinguish the authors' statement from your interpretation.

## 4. Design-rationale chain

Use a readable chain or compact table:

| Goal | Prior failure | Design action | Mechanism | Evidence | New tradeoff / next fix | Support |
|---|---|---|---|---|---|---|

For staged systems, explain checkpoint transitions as natural experiments.

## 5. Mechanism and mathematics

For each central equation or algorithm:

- purpose before notation;
- inputs and outputs;
- step-by-step operation;
- why it should work;
- simple alternative;
- toy example or edge case;
- implementation-sensitive detail.

## 6. How success is evaluated

Explain the important metrics and protocols before showing scores.

| Claim | Metric and meaning | Comparator / control | Result | What it supports | What it does not prove |
|---|---|---|---|---|---|

Surface regressions, negative results, and missing controls.

## 7. Counterfactuals and ablations

For each major design choice, explain what should happen without it, what was actually tested, and whether the result shows usefulness, necessity, mechanism, or unique justification.

## 8. Limitations

### Author-stated

List limitations explicitly acknowledged by the paper.

### Evidence limitations

State what the evaluation cannot establish.

### Structural limitations

Explain inferred failure modes and label them as analysis.

## 9. Research lineage

Show:

```text
important ancestor and its gap
→ this paper's contribution
→ residual gap
→ verified follow-up, extension, correction, or parallel solution
```

Separate verified later work from proposed future directions.

## 10. What to remember

Give three to five durable takeaways:

- why the paper matters;
- why the method has this shape;
- strongest piece of evidence;
- largest unresolved uncertainty;
- where the idea is likely to generalize or fail.

## 11. Teach-back

Ask one or two questions that require explaining the causal design logic, not recalling a score or definition.
