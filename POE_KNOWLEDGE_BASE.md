# POE_KNOWLEDGE_BASE.md

Rule:
Only consolidated knowledge goes here.

Current consolidated knowledge:
- PD-000: VALIDATED
- PD-001: VALIDATED
- PD-002: VALIDATED
- PD-003: VALIDATED
- PD-004: VALIDATED
- PD-005: VALIDATED
- PD-006: VALIDATED
- PD-007: VALIDATED
- PD-008: VALIDATED
- PD-009: VALIDATED
- PD-010: VALIDATED
- PD-011: VALIDATED
- PD-012: VALIDATED
- PD-013: VALIDATED
- PD-014: VALIDATED
- PD-015: VALIDATED
- PD-016: VALIDATED
- PD-017: VALIDATED
- PD-018: VALIDATED
- PD-019: VALIDATED
- PD-020: VALIDATED

Primitive Inefficiencies PoE V1

IE-002 Consumo evitabile
IE-003 Punte di carico
IE-005 Mancanza di flessibilita

Validated by:
RQ-005B
PD-007

Formal object distinction PoE V1

CONTRIBUTO, RIDUZIONE e VALORE sono oggetti protocollari distinti.

RIDUZIONE:
delta osservabile e verificabile di una inefficienza catalogata rispetto a baseline, finestra temporale e contesto validati.

CONTRIBUTO:
comportamento osservabile, verificabile e attribuibile a un nodo o soggetto che partecipa causalmente alla riduzione.

VALORE:
proprieta protocollare derivata da una riduzione verificata, attribuita e sistemicamente rilevante di una inefficienza catalogata.

VALORE non e identico alla RIDUZIONE grezza.
VALORE e RIDUZIONE qualificata dal protocollo tramite verifica, attribuzione, rilevanza sistemica e controllo contro manipolazioni.

Causal validation:
PD-001 resta valida come gerarchia protocollare, ma non deve essere letta come ordine causale rigido.

Ordine causale minimo per le prossime metriche:
INEFFICIENZA VALIDATA
-> METRICA DELL'INEFFICIENZA
-> BASELINE / CONDIZIONE DI CONFRONTO
-> COMPORTAMENTO OSSERVABILE
-> CONTRIBUTO CANDIDATO
-> RIDUZIONE MISURATA
-> VERIFICA DELLA RIDUZIONE
-> ATTRIBUZIONE AL CONTRIBUTO
-> VALORE
-> REPUTAZIONE

Regola:
Un comportamento osservato non e automaticamente contributo valido. Prima e contributo candidato. Diventa contributo valido solo se collegato a riduzione verificata, attribuzione e rilevanza sistemica.

Validated by:
RQ-007
PD-008

Minimum metric structure PoE V1:
For each primitive inefficiency, metrics must separate:

* observable behavior;
* candidate contribution;
* measured reduction;
* reduction verification;
* attribution to contribution;
* recognized value.

RQ-008 validates only the conceptual metric structure.
Quantitative formulas remain undefined.

Validated by:
RQ-008
PD-009

IE-002 measurement safety rule:
Lower consumption becomes verified IE-002 measured reduction only if baseline is valid, necessary function is preserved, context is equivalent or validly normalized, rebound and shifted consumption checks pass, baseline gaming is rejected, data quality is sufficient, and attribution to candidate contribution is possible.

Raw kWh reduction is not sufficient.
Self-declared baseline alone is invalid.
Function loss, service degradation, shifted consumption and full rebound invalidate IE-002 measured reduction.

Validated by:
RQ-010
PD-010

IE-003 measurement safety rule:
Peak reduction becomes verified IE-003 measured reduction only if the critical window is valid, peak threshold is valid, baseline peak profile is valid, observed peak stress is lower in the system-relevant window, rebound and displacement checks pass, artificial peak creation is rejected, data quality is sufficient, and attribution to candidate contribution is possible.

Raw kW reduction is not sufficient.
Not every peak window is critical.
Participant-declared critical window alone is invalid.
Previous peak alone is not a valid baseline.
Artificial peak creation, equivalent rebound, temporal displacement and cross-node displacement invalidate IE-003 measured reduction.

Validated by:
RQ-011
PD-011

IE-005 measurement safety rule:
Behavior variation becomes verified IE-005 measured reduction only if a valid system need exists, a valid response profile exists before or at the event, the response is useful, timely, correctly directed, sufficiently large, sufficiently sustained, inside the relevant boundary, distinguishable from normal variation, net of rebound, free from fake-flexibility patterns, and attributable to the candidate contribution.

Raw behavior variation is not sufficient.
Raw response events are not sufficient.
Participant-declared system need alone is invalid.
Post-hoc response profile is invalid.
Wrong direction, late response, insufficient magnitude, insufficient duration, normal variation, fake flexibility and harmful rebound invalidate or postpone IE-005 measured reduction.

Validated by:
RQ-012
PD-012

Attribution safety rule:
A measured reduction becomes attributable only if the candidate contribution is observable, temporally aligned with the verified reduction, causally plausible, inside the same measurement boundary, not explained by external causes, not double-counted, and supported by sufficient attribution evidence.

Raw behavior is not attribution.
Raw reduction is not attribution.
Coincidence is not attribution.
Reduction can exist without attribution.
Recognized value cannot exist without attribution.
Multi-actor reductions require separable attribution or validation must be postponed.

Validated by:
RQ-013
PD-013

Cross-IE harm safety rule:
A verified measured reduction of one primitive inefficiency becomes recognized value only if it does not create unbounded material harm in another primitive inefficiency and is not merely a transfer of inefficiency across time, node, boundary or IE label.

Target IE measured reduction is necessary but not sufficient for recognized value.
Attribution must pass.
Material harm to IE-002, IE-003 or IE-005 must be excluded, bounded or explicitly handled.
Local improvement is insufficient if aggregate or relevant-boundary system effect worsens.
The same measured effect must not be recognized twice as separate value.
Confirmed unbounded cross-IE harm rejects recognized value.
Plausible but unknown cross-IE harm postpones recognized value.

Validated by:
RQ-014
PD-014

Quantitative measured-reduction metrics:
ACR_net validates IE-002 measured-reduction quantity only.
NPSR_net validates IE-003 measured-reduction quantity only.
UFR_net validates IE-005 measured-reduction quantity only.
All are gated by PD-010 to PD-014.
None define recognized value, reputation, incentives, tokens, economic allocation or final scoring.

Validated by:
RQ-015
PD-015

Recognized value eligibility:
Recognized value is not measured reduction alone.
PD-016 clarifies PD-003: "riduzione verificabile" means protocol-qualified reduction, not raw measured reduction.
Recognized value requires primitive IE relevance, valid measured reduction, attribution, cross-IE safety, boundary integrity, system relevance, non-duplication and sufficient evidence.
Failure outcomes are rejected, zero, capped or postponed depending on evidence and bounded validity.
PD-016 does not define reputation, incentives, tokens, economic allocation, final scoring or implementation logic.

Validated by:
RQ-016
PD-016

Reputation eligibility after recognized value:
Recognized value is not reputation.
Reputation is not incentive.
Reputation is not token.
Reputation is not economic score.
Only recognized value that passes separate reputation-eligibility gates can become non-economic reputation evidence.
Minimum gates are protocol-valid recognized value, preserved attribution, boundary integrity, sufficient evidence, non-duplication, manipulation resistance, cross-IE safety, intra-IE comparability, persistence or repeatability, and separation from incentives.
Exceptional systemic relevance can only act as a capped exception, not as a shortcut to full reputation eligibility.
Failure outcomes are rejected, zero, capped, postponed or eligible.
Eligibility is only informational admissibility and creates no reward, payout, token right, economic allocation or compensation promise.

Validated by:
RQ-017
PD-017

Aggregated reputation evidence boundaries:
Recognized value is not reputation eligibility.
Reputation eligibility is not aggregated reputation evidence.
Aggregated reputation evidence is not final reputation.
Final reputation is not incentive.
Aggregated reputation evidence is a non-economic, non-final and non-ordering descriptive layer made of multiple reputation-eligible evidence items grouped only within explicit boundaries of node, IE primitive, time window, evidence type and non-duplication.
Primary aggregation remains separated by IE primitive: IE-002 with IE-002, IE-003 with IE-003, IE-005 with IE-005.
Cross-IE aggregation is allowed only as a separated descriptive view and never as a single cumulative value.
Duplicate evidence cannot count twice; correlated or dependent evidence cannot be treated as independent and must be merged, capped or separated.
Negative or conflicting evidence cannot be hidden inside a positive aggregate.
Aggregated reputation evidence cannot define final reputation, ranking, leaderboard, token, incentive, payout, economic allocation or economic scoring.

Validated by:
RQ-018
PD-018

Reputation readiness boundary:
Aggregated reputation evidence is not reputation-ready evidence.
Reputation-ready evidence is not final reputation.
Final reputation is not ranking.
Final reputation is not incentive.
Final reputation is not token.
Final reputation is not economic score.
Reputation-ready evidence is a non-economic informational maturity state in which aggregated reputation evidence is sufficiently coherent, fresh, bounded and non-conflicting to inform a future PoE reputation without becoming final reputation.
Readiness remains separated by IE primitive, node boundary, time window and evidence type.
Cross-IE readiness remains separated unless a future protocol decision explicitly authorizes a non-economic, non-ordering, non-final cross-IE interpretation.
Readiness may be partial-ready, conditional-ready, capped-ready, postponed, not-ready, rejected or reputation-ready.
Stale evidence may remain historically informative but cannot prove full current capacity without sufficient continuity.
Reputation-ready evidence cannot define score, ranking, leaderboard, token, incentive, payout, economic allocation or implementation logic.

Validated by:
RQ-019
PD-019

PoE Reputation object boundary:
Reputation-ready evidence is not PoE Reputation object.
PoE Reputation object is not formula.
PoE Reputation object is not score.
PoE Reputation object is not ranking.
PoE Reputation object is not incentive.
PoE Reputation object is not token.
PoE Reputation object is not economic score.
PoE Reputation object is a non-economic, multidimensional and non-ordering protocol object that represents demonstrated systemic capacities through bounded reputation-ready evidence separated by IE primitive, node boundary, time window, evidence type, readiness status, conflict state, staleness state and source references.
The object may contain descriptive status markers and source links, but not scalar values, totals, coefficients, positions or economic rights.
Objects may be described comparatively only in non-ordinal form and cannot rank nodes before a future explicit protocol decision.
Conflict-marked, partial, capped, conditional and historical states remain visible rather than collapsed into a synthetic score.

Validated by:
RQ-020
PD-020
