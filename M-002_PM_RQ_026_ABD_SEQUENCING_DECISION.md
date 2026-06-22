# M-002 PM sequencing decision for RQ-026 A / B / D

Status:
COMPLETED

Scope:
PM / Verifier sequencing decision only

Reviewed materials:
`RQ-026_PM_REFINEMENT_DECISION.md`
`RQ-026_DOCUMENTATION_READINESS_DECISION.md`
`M-002_PM_ROUTE_SELECTION_AFTER_RQ_026_027_028.md`
`M-002_PM_RQ_026_ABD_ROUTE_DECISION.md`

Decision:
Safest sequencing order for future separate research questions is:
A first, B second, D third.
Do not open any of those future research questions in this task.

Core PM finding:
Sequencing must reduce bundled leakage while also avoiding early exposure to the highest-risk abstraction.
A is the narrowest structural direction and can be bounded without immediately pulling in temporal normalization or aggregative machinery.
B should follow A because it still concerns single-unit structure, but introduces broader leakage toward standards, freshness and precision.
D should remain last because it is the highest-leakage direction and is the closest one to hidden classifier, isolation-filter and aggregation-rule drift.

Reasoning by order:

## 1. A first

PM finding:
Referential structure is the safest first split because its leakage surface is comparatively local:
registry, whitelist, ambiguity filter and reference-validity logic.
This makes A the best first sequencing candidate for bounded future review without immediately importing time-normalization or aggregate-context machinery.

## 2. B second

PM finding:
Temporal structure remains single-unit focused, but it expands leakage risk beyond simple existence of structure.
It can more easily drift toward temporal standardization, freshness requirements, precision expectations and timer logic.
For this reason B should follow A, not precede it.

## 3. D third

PM finding:
Independent consideration from aggregative context is the least safe starting point.
Its leakage surface is the broadest:
aggregate definition, isolation filter, aggregate classifier and aggregation rule.
Because D sits closest to hidden admissibility packaging and operational separation logic, it should be sequenced last.

Rejected sequencing options:

* do not start with D
* do not place D before both A and B
* do not place B before A
* do not keep A / B / D unsequenced
* do not define non-binding placeholders as opened RQs
* do not define protocol properties
* do not define formula candidate material
* do not define formula structure
* do not define scoring
* do not define ranking
* do not define weighting
* do not define checklist
* do not define classifier
* do not define gate
* do not define threshold
* do not define operational filter
* do not define dependency graph
* do not define dependency computation
* do not define incentives
* do not define tokens
* do not define payout
* do not define economic allocation
* do not authorize implementation

Sequencing interpretation:

* `RQ-026` remains OPEN / RESEARCH-FRAMING
* `RQ-026` Decision remains `NONE`
* `RQ-027` remains OPEN / RESEARCH-FRAMING with Decision `NONE`
* `RQ-028` remains OPEN / RESEARCH-FRAMING with Decision `NONE`
* A / B / D remain non-binding research-framing directions only
* A / B / D are not final protocol properties
* A / B / D are not checklist items
* A / B / D are not validation rules
* A / B / D are not thresholds
* A / B / D are not operational filters
* A / B / D are not implementation logic
* A / B / D must not become formula candidate material
* no `PD-026`
* no `PD-027`
* no `PD-028`
* no new `RQ`

Exact next required PM action:
Prepare a future task boundary for the first separated direction, A / referential structure, while keeping that future task unopened in the current step and preserving `RQ-026`, `RQ-027` and `RQ-028` as OPEN / RESEARCH-FRAMING with Decision `NONE`.
