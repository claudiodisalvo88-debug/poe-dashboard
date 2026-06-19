# RQ-022_REPUTATION_FORMULA_ADMISSIBILITY_CONSTRAINTS

## Title

Reputation formula admissibility constraints

## Question

What admissibility constraints must any future PoE reputation formula satisfy before formula candidates, weights, scalar score, ranking, leaderboard, incentives, tokens, payout, economic allocation or implementation can be considered?

## Scope

* Define admissible formula constraints
* Define boundary between formula-ready structure, admissible constraints, future formula candidates and future formula
* Define minimum constraints
* Define failure outcomes
* Define anti-leakage rules
* Preserve non-economic, non-implementative, non-computational status

## Non-scope

* No formula candidates
* No final formula
* No formula syntax
* No weights
* No coefficients
* No normalization
* No scalar score
* No total score
* No ranking
* No leaderboard
* No incentives
* No rewards
* No tokens
* No token issuance
* No token entitlement
* No payout
* No economic allocation
* No economic score
* No API
* No database
* No dashboard
* No poe.db
* No implementation

## Definition

PoE requires an admissible formula constraints layer before any future formula candidates can be researched.

Admissible formula constraints are non-economic, non-implementative and non-computational protocol constraints that any future PoE reputation formula research must satisfy before proposing formula candidates.

This layer must preserve IE primitive separation, node and boundary integrity, time-window integrity, evidence lineage, readiness status preservation, staleness handling, conflict handling, capped / conditional state handling, manipulation resistance and separation from score, ranking, incentive, token, payout, economic allocation and implementation.

This layer does not define formula candidates, final formula, formula syntax, weights, coefficients, normalization, scalar score, total score, ranking, leaderboard, incentives, rewards, tokens, token issuance, token entitlement, payout, economic allocation, economic score, API, database, dashboard or implementation.

## Validated decision

PD-022 - VALIDATED

## Boundary distinctions

* Formula-ready reputation structure prepares inputs for future formula research.
* Admissible formula constraints define what future formula research must preserve and what it must not violate.
* Future formula candidates are later proposed transformations and remain out of scope for RQ-022.
* Future reputation formula is a later validated rule and remains out of scope for RQ-022.

Binding distinction:

* structure prepares
* constraints restrict
* candidates propose
* formula calculates

## Minimum constraints

1. IE separation: future formula research must not collapse IE-002, IE-003 and IE-005 into a hidden cross-IE synthesis at the admissibility stage.
2. Node / boundary integrity: formula research must preserve the validated node, site, asset or aggregator boundary used by upstream layers.
3. Time-window integrity: formula research must preserve validated temporal windows and must not merge incompatible windows by stealth.
4. Evidence lineage: every future formula-research input must remain source-referenced back to bounded protocol evidence.
5. Readiness status preservation: partial, conditional, capped, historical or conflict-marked statuses must remain visible and cannot be silently upgraded.
6. Stale handling: stale or historical evidence must remain marked as such and cannot be treated as current capability without separate validation.
7. Conflict handling: unresolved conflicts must remain explicit and cannot be netted away or hidden inside a positive structure.
8. Capped / conditional state handling: capped and conditional evidence must preserve their limits and cannot be converted into unrestricted inputs.
9. Manipulation resistance: formula research must preserve anti-gaming constraints and must not reopen already-bounded manipulation vectors.
10. No cross-IE netting: no admissible formula research can assume automatic compensation across IE primitives before explicit future protocol validation.
11. No hidden weights: admissibility cannot smuggle relative importance, coefficients or weighting schemes.
12. No hidden scalar score: admissibility cannot compress the structure into a single numeric value.
13. No hidden ranking: admissibility cannot create ordinal comparison between nodes.
14. No hidden incentive: admissibility cannot imply reward logic, preferential treatment or entitlement.
15. No hidden token right: admissibility cannot imply token issuance, token claims or token-backed rights.
16. No economic allocation: admissibility cannot imply payout, allocation, compensation or economic scoring.
17. No implementation binding: admissibility cannot hard-bind future protocol research to API, database, dashboard or code implementation logic.

## Failure outcomes

* formula-research-blocked: the upstream structure is too incomplete or unsafe to allow formula research.
* formula-candidate-inadmissible: a future formula proposal would violate one or more admissibility constraints.
* partial-admissibility: only a bounded subset of the structure is admissible for future formula research.
* conditional-admissibility: admissibility holds only under explicit boundary, time, status or evidence conditions.
* cross-IE-blocked: admissibility fails because the structure would collapse or compensate across IE primitives.
* stale-blocked: admissibility fails because stale evidence is being treated as current without sufficient continuity.
* conflict-blocked: admissibility fails because unresolved conflict remains inside the structure.
* manipulation-risk-blocked: admissibility fails because gaming or manipulation risk remains materially open.
* economic-leakage-blocked: admissibility fails because the structure leaks into payout, allocation, incentive or economic value.
* implementation-blocked: admissibility fails because the structure is prematurely tied to implementation logic.
* formula-candidate-admissible-for-research: the structure may support future formula research, but still does not define any formula candidate.

## Anti-leakage rules

* anti-hidden formula: no constraint layer can act as a de facto formula.
* anti-hidden weights: no implicit coefficient, weighting or priority scheme can be embedded in admissibility.
* anti-hidden score: no scalar score may appear at the admissibility layer.
* anti-hidden ranking: no ordering of nodes may be produced.
* anti-hidden leaderboard: no competitive list or ordinal display may emerge from admissibility.
* anti-hidden incentive: no reward mechanism may be implied.
* anti-hidden token right: no token claim, entitlement or issuance logic may be implied.
* anti-hidden payout: no payout logic may be encoded.
* anti-hidden economic allocation: no capital, revenue or benefit allocation may be implied.
* anti-premature implementation: no API, database, dashboard or code structure may be treated as protocol proof.
* anti-false precision: apparent numeric exactness without validated formula research is forbidden.
* anti-gaming optimization: admissibility must not reward structures that are easy to game but weakly evidential.
* anti-cross-IE collapse: admissibility must not silently compress distinct IE primitives into one combined evaluative signal.

## Risks controlled

* hidden formula
* hidden weights
* hidden score
* hidden ranking
* hidden leaderboard
* hidden incentive
* hidden token right
* hidden payout
* hidden economic allocation
* false precision
* gaming optimization
* cross-IE collapse
* stale laundering
* exceptional-as-ordinary laundering
* implementation creep

## Postponed decisions

* formula candidates
* final formula
* formula syntax
* weights
* coefficients
* normalization
* scalar score
* total score
* ranking
* leaderboard
* incentives
* rewards
* tokens
* token issuance
* token entitlement
* payout
* economic allocation
* economic score
* economic rights
* API
* database
* dashboard
* implementation
* cross-IE quantitative synthesis
* stale-decay formula
* conversion of exceptional/capped evidence into ordinary continuous capacity

## Final boundary rule

Admissible formula constraints restrict future formula research but cannot propose, calculate, score, rank, reward, tokenize, allocate, implement or economically value anything.
