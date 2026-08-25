---
name: paper-reasoning-deep-dive
description: "Use when a user asks to read, understand, analyze, or deeply explain an academic paper, research PDF, or preprint—especially read paper, paper reading, paper deep dive, explain why each design decision, walk through the method, 精读论文, 读懂论文, 讲透论文, 为什么这样设计, 公式推导, 实验评判标准, 消融实验, 前置论文, or 后续论文. Do not use for citation-only lookup, a very short abstract summary, or conventional peer review without a learning goal."
---

# Paper Reasoning Deep Dive

Teach the paper by reconstructing the authors' problem-solving path. Do not merely summarize sections. Make the user able to explain why the method has its particular shape, what evidence supports each step, and where the argument remains weak.

## Establish the task

1. Identify the target paper and the user's desired depth, background, and language from the request.
2. Use the supplied PDF or full text as the primary source. If it is missing, ask for the paper or retrieve the authoritative full text when browsing is available.
3. Prefer the paper, appendix, supplementary material, official code, and author materials over secondary summaries.
4. State when only an abstract, excerpt, or inaccessible copy is available. Never imply a full-paper reading from partial evidence.
5. Match the user's language. Define field-specific terms before relying on them.

## Separate evidence from interpretation

Label important statements by provenance:

- **Paper states**: explicitly claimed or reported by the authors.
- **Evidence shows**: directly supported by a table, figure, equation, ablation, or qualitative example.
- **Analysis**: a mechanism-level interpretation or limitation inferred from the paper.
- **Open question**: unresolved or not testable from the available material.

Attach page, section, figure, table, or equation references whenever the source permits. Do not turn an author's narrative into a proven causal claim.

## Reconstruct the argument

Build an initial map before explaining details:

1. State the real problem in one sentence, including why it is difficult.
2. Identify the prior approach and the precise bottleneck that motivates this paper.
3. State the paper's central insight as an observation or hypothesis, not just a method name.
4. List the main claims and the evidence intended to support each claim.
5. Reconstruct each important module or stage using this chain:

```text
Goal
→ Prior failure or constraint
→ Design action
→ Proposed mechanism
→ Expected observable effect
→ Evidence
→ New failure or tradeoff
→ Next fix
```

Read [design-rationale.md](references/design-rationale.md) whenever the paper has multiple modules, training stages, checkpoints, or ablations, or when the user asks why the method was designed this way.

## Explain mechanisms and mathematics

For each important algorithm, equation, architecture component, or training stage:

1. Explain what problem it solves before introducing notation.
2. Define inputs, outputs, variables, assumptions, and optimization signals.
3. Walk through the operation in causal order.
4. Explain why the mechanism should produce the claimed effect.
5. Compare it with the simplest plausible alternative.
6. Give a small concrete example when it materially improves understanding.
7. Identify edge cases, failure modes, and implementation-sensitive details.

Do not stop at reading symbols aloud. Read [mechanism-and-math.md](references/mechanism-and-math.md) for equation derivations, learning objectives, algorithms, systems, or implementation details.

## Audit the evidence

For each central claim, construct a compact claim-evidence ledger:

```text
Claim
→ Metric and what it measures
→ Dataset or evaluation setting
→ Comparator and controls
→ Result and uncertainty
→ Ablation or counterfactual
→ What the evidence supports
→ Alternative explanations
```

Explain how success is judged, whether higher or lower is better, what the metric misses, and whether it can be gamed. Check baseline fairness, data and compute comparability, evaluation protocol, statistical uncertainty, leakage risk, cherry-picking, and negative results.

Read [evidence-audit.md](references/evidence-audit.md) whenever experiments, benchmarks, human evaluation, ablations, or causal claims matter.

## Test every design decision

Ask for each major choice:

- What would probably happen without it?
- Is there a simpler alternative?
- Does the paper compare against that alternative?
- Does the ablation show usefulness, necessity, or only correlation?
- Which variables changed between checkpoints, and which stayed fixed?
- Did one metric improve while another regressed?

Assign one evidence grade:

- **Strongly supported**: direct controlled evidence and plausible mechanism agree.
- **Moderately supported**: relevant evidence exists but controls or coverage are incomplete.
- **Plausible**: mechanism is reasonable but evidence is indirect.
- **Under-supported**: the paper asserts more than the evidence establishes.

## Identify limitations at three levels

Keep these categories distinct:

1. **Author-stated limitations**: explicitly acknowledged by the paper.
2. **Evidence limitations**: weaknesses in what the experiments can establish.
3. **Structural limitations**: failure modes inferred from the method or assumptions.

Mark categories 2 and 3 as analysis. Include boundary conditions: where should the method work, and where should it fail?

## Build research lineage

Trace the lineage as a sequence of transferred problems and mechanisms:

```text
Ancestor gap
→ Current paper's intervention
→ Gap resolved or only reduced
→ Residual gap
→ Direct follow-up, extension, or parallel solution
→ Remaining open question
```

Read [lineage-and-future.md](references/lineage-and-future.md) when the user requests prior papers, follow-ups, novelty, current state of the field, or future work. Browse for current follow-ups when possible; publication status and “latest” claims are time-sensitive.

## Produce a teaching-oriented answer

Prefer the smallest answer that achieves the requested depth. For a full deep dive, use [output-template.md](references/output-template.md). For a focused question, answer that question directly while preserving the same evidence discipline.

Always include:

- the core problem and central insight;
- the design-rationale chain for the relevant method;
- how the authors evaluated success;
- what is supported versus inferred;
- the most important unresolved limitation.

When useful, end with two checks:

1. **Teach-back**: a short prompt the user can answer to test understanding.
2. **Next depth choice**: offer the most valuable next layer, such as an equation derivation, ablation audit, or lineage map.

## Quality gates

Before answering, verify that the response:

- follows the paper's logic rather than its section order;
- explains why each important design choice exists;
- connects mechanisms to observable predictions and evidence;
- distinguishes outcome improvement from proof of the proposed mechanism;
- interprets metrics instead of listing scores;
- surfaces regressions and negative evidence;
- separates author claims, direct evidence, analysis, and open questions;
- avoids invented citations, predecessors, follow-ups, and implementation details;
- makes uncertainty explicit when the source is incomplete.
