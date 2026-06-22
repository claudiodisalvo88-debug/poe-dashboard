# M-002 PM decision on RQ-026 A / B / D route

Status:
COMPLETED

Scope:
PM / Verifier route decision only

Reviewed materials:
`RQ-026_PM_REFINEMENT_DECISION.md`
`RQ-026_DOCUMENTATION_READINESS_DECISION.md`
`M-002_PM_ROUTE_SELECTION_AFTER_RQ_026_027_028.md`

Decision:
A / B / D should be split into multiple future separate research questions.
Do not open those future research questions in this task.

Core PM finding:
Keeping A / B / D only inside `RQ-026` would preserve them as one bundled positive block.
That bundle is the main residual safety risk because it can be re-read later as an implicit multi-part admissibility package.
The safer route is to avoid a composite route and preserve separation between the three directions before any future positive research continuation.

Reasoning by direction:

## A. Referential structure

PM finding:
A remains research-framing only, but it carries a distinct leakage vector toward registry, whitelist, ambiguity-filter and reference-validity logic.
It should not advance later inside a bundled A / B / D package.

## B. Temporal structure

PM finding:
B remains research-framing only, but it carries a distinct leakage vector toward timestamp standard, freshness rule, temporal precision and timer logic.
It should not advance later inside a bundled A / B / D package.

## D. Independent consideration from aggregative context

PM finding:
D remains research-framing only, but it carries a distinct leakage vector toward aggregate definition, isolation filter, aggregate classifier and aggregation rule.
It is the highest-leakage direction among A / B / D and should not advance later inside a bundled package.

Route interpretation:

* `RQ-026` remains OPEN / RESEARCH-FRAMING
* `RQ-026` Decision remains `NONE`
* A / B / D remain refined research-framing material only
* A / B / D are not final protocol properties
* A / B / D are not checklist items
* A / B / D are not validation rules
* A / B / D are not thresholds
* A / B / D are not operational filters
* A / B / D are not implementation logic
* A / B / D must not become formula candidate material
* `RQ-027` remains OPEN / RESEARCH-FRAMING with Decision `NONE`
* `RQ-028` remains OPEN / RESEARCH-FRAMING with Decision `NONE`
* no `PD-026`
* no `PD-027`
* no `PD-028`
* no new `RQ`

Rejected route options:

* do not keep A / B / D as the only future positive bundle inside `RQ-026`
* do not split A / B / D into one single future separate research question
* do not reject A / B / D as unsafe in absolute terms
* do not define formula candidate
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

Exact next required PM action:
Decide the order in which future separate research questions should eventually be considered for A, B and D, while keeping all three directions non-binding, keeping `RQ-026`, `RQ-027` and `RQ-028` OPEN / RESEARCH-FRAMING with Decision `NONE`, and without opening any of those future RQs in the same task.
