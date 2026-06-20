# RQ-026 Critic structural property leakage review

Status:
REFINE_REQUIRED

Scope status:
research-framing only

Related task:
M-002-RQ-026-CRITIC

RQ status impact:
`RQ-026` remains OPEN / RESEARCH-FRAMING.
`PD-026` is not created.
`RQ-026` is not closed.
Implementation remains blocked.

Critic outcome:

## A. Referential integrity

Status:
REFINE

Safer research direction:
L'unita possiede una struttura referenziale verso un'entita di dominio? La ricerca indaga l'esistenza di tale struttura come proprieta, non la qualita, disambiguazione o validita del riferimento.

Leakage rejected:
hidden binary validation
ambiguity filter
registry / whitelist leakage
implementation-facing reference validation

## B. Temporal delimitation

Status:
REFINE

Safer research direction:
L'unita possiede una struttura che la colloca in una dimensione temporale? La ricerca indaga l'esistenza di tale struttura come proprieta, non la precisione, il formato o la validita della collocazione.

Leakage rejected:
hidden temporal standard
timestamp expectation
schema expectation
implicit temporal checklist
implementation-facing timestamp validation

## C. Non-derivability

Status:
SPLIT REQUIRED

Reason:
This direction is too risky for `RQ-026` because it introduces dependency graph, computation, functional relation, hidden ordering, formula-structure leakage and direct implementation leakage.

Outcome:
C must not advance inside `RQ-026`.
C is recorded only as future `RQ-027` candidate.
`RQ-027` is not opened by this file.

Candidate future wording:
"E possibile definire una nozione di primitivita per un'unita di evidenza reputazionale che non richieda computazione di dipendenze, costruzione di grafi, ordinamento o formula structure?"

## D. Contextual isolability

Status:
REFINE

Safer research direction:
L'unita puo essere oggetto di considerazione indipendente da un contesto aggregativo? La ricerca indaga se questa proprieta esiste strutturalmente, senza definire cosa costituisce un aggregato, senza operazioni di aggregazione, senza filtri di isolamento.

Leakage rejected:
aggregate operational definition
aggregation operations
isolation filter
implementation-facing aggregate classifier

Hard exclusions:

* no PD-026
* no protocol closure
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

Decision boundary:
A/B/D are refined research directions only.
C is split required and future `RQ-027` candidate only.
Nothing in this file is a final protocol property.
