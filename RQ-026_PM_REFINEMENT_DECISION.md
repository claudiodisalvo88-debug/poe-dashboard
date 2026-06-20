# RQ-026 PM refinement decision

Status:
ACCEPT_WITH_CONSTRAINTS

Scope status:
research-framing only

Related task:
M-002-RQ-026-PM-REFINEMENT

RQ status impact:
`RQ-026` remains OPEN / RESEARCH-FRAMING.
`PD-026` is not created.
`RQ-026` is not closed.
`RQ-027` is not opened.
Implementation remains blocked.

Decision:
Refined A/B/D can support later `RQ-026` documentation only as research-framing directions, not as final protocol properties.

Accepted refined directions:

## A. Referential structure

Accepted direction:
L'unita possiede una struttura referenziale verso un'entita di dominio.
La ricerca indaga l'esistenza di tale struttura come proprieta, non la qualita, disambiguazione o validita del riferimento.

Excluded leakage:
no registry
no whitelist
no ambiguity filter
no validation rule
no operational filter

## B. Temporal structure

Accepted direction:
L'unita possiede una struttura che la colloca in una dimensione temporale.
La ricerca indaga l'esistenza di tale struttura come proprieta, non precisione, formato, timestamp schema, freshness o validita.

Excluded leakage:
no temporal standard
no precision threshold
no implementation timer rule

## D. Independent consideration from aggregative context

Accepted direction:
L'unita puo essere oggetto di considerazione indipendente da un contesto aggregativo.
La ricerca indaga se questa proprieta puo esistere strutturalmente, senza definire cosa sia un aggregato, senza operazioni di aggregazione, senza filtri di isolamento.

Excluded leakage:
no aggregate classifier
no operational aggregation rule

## C. Non-derivability

Status:
excluded from active `RQ-026`

Reason:
It introduces dependency graph, computation, functional relation, hidden ordering, formula-structure leakage and implementation-facing structure.

Boundary:
C may remain only as future `RQ-027` candidate.
This file does not open `RQ-027`.

Mandatory interpretation:

* A/B/D are not final protocol properties
* A/B/D are not checklist items
* A/B/D are not validation rules
* A/B/D are not thresholds
* A/B/D are not operational filters
* A/B/D are not implementation logic
* C is not accepted inside `RQ-026`
* C is only future `RQ-027` candidate

Hard exclusions:

* no PD-026
* no RQ-026 closure
* no RQ-027 opening
* no checklist
* no formula
* no formula structure
* no score
* no ranking
* no ordering
* no weighting
* no economics
* no incentives
* no tokens
* no payout
* no economic allocation
* no implementation

Next required step:
Decide whether `RQ-026` can be documented as research-framing complete without creating `PD-026`.
