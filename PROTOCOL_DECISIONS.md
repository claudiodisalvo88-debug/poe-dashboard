# PROTOCOL_DECISIONS.md

## PD-016

Recognized value is distinct from measured reduction, contribution, reputation, incentive, token issuance, economic allocation and final scoring.

A verified measured reduction becomes eligible for recognized value only if all conditions below hold:

1. The reduction targets a PoE V1 primitive inefficiency: IE-002, IE-003 or IE-005.
2. The measured reduction passes the relevant safety gate:

   * PD-010 for IE-002;
   * PD-011 for IE-003;
   * PD-012 for IE-005.
3. The measured reduction follows the PD-009 metric structure.
4. The measured reduction remains distinct from contribution and value under PD-008.
5. Attribution to a candidate contribution passes under PD-013.
6. Cross-IE harm checks pass under PD-014.
7. The reduction is boundary-consistent and does not merely shift inefficiency outside the relevant window, node or system boundary.
8. The reduction is system-relevant and not merely private local optimization.
9. The same physical effect is not recognized twice as separate value.
10. Required evidence is sufficient.

If any required condition is false, recognized value is rejected.

If the eligible measured reduction is zero after safety gates, recognized value is zero.

If only a bounded safe portion of the measured reduction is eligible, recognized value is capped to that eligible portion.

If any required condition is unresolved and materially affects eligibility, recognized value is postponed.

Measured reduction alone never equals recognized value.

RQ-016 validates recognized-value eligibility only.
It does not validate reputation scoring, incentives, tokens, economic allocation, final scoring or implementation logic.

STATUS: VALIDATED

## PD-015

Quantitative measured-reduction metrics for PoE V1 are validated only as measured-reduction quantities for the three primitive inefficiencies IE-002, IE-003 and IE-005.

They do not define recognized value, reputation, incentives, token issuance, economic allocation or final scoring.

For IE-002, the validated candidate measured-reduction metric is:

ACR_net = max(0, E_base(W | F,C) - E_obs(W) - E_rebound(R) - E_shifted)

ACR_net is valid only if PD-010 baseline, function-preservation, context-equivalence, rebound, shifted-consumption and boundary-integrity checks pass.

For IE-003, the validated candidate measured-reduction metrics are:

PeakStress(W) = integral over W of max(0, P(t) - P_threshold(t)) dt

NPSR_net = max(0, PeakStress_base(Wc) - PeakStress_obs(Wc) - PeakStress_rebound(Wr) - PeakStress_displaced)

NPSR_net is valid only if PD-011 critical-window, peak-threshold, baseline peak-profile, rebound/displacement and artificial-peak rejection checks pass.

For IE-005, the validated candidate measured-reduction metrics are:

UFR_delivered = integral over T of min(abs(DeltaP_obs(t)), abs(Req(t))) dt

UFR_net = max(0, UFR_delivered - UFR_baseline - Response_rebound_penalty)

UFR_net is valid only if PD-012 system-need, response-profile, useful-response, timing, direction, magnitude, duration, fake-flexibility and rebound checks pass.

All three measured-reduction metrics remain invalid or postponed for value recognition unless PD-013 attribution passes and PD-014 cross-IE harm checks do not reject the reduction.

RQ-015 validates quantitative measured-reduction metrics only.
It does not validate recognized value, reputation scoring, incentives, tokens, economic allocation, final scoring or implementation logic.

STATUS: VALIDATED

## PD-014

A verified measured reduction of one primitive inefficiency can become recognized value only if it does not create unbounded material harm in another primitive inefficiency and is not merely a transfer of inefficiency across time, node, boundary or IE label.

For cross-IE harm:

* target IE measured reduction is necessary but not sufficient for recognized value;
* attribution must pass before value recognition;
* material harm to IE-002, IE-003 or IE-005 must be excluded, bounded or explicitly handled by a non-duplicative protocol rule;
* local improvement is insufficient if aggregate or relevant-boundary system effect worsens;
* local improvement must not hide harm shifted to another node, boundary or time window;
* the same measured effect must not be recognized twice as separate value;
* if material cross-IE harm is confirmed and unbounded, recognized value is rejected;
* if material cross-IE harm is plausible but unknown, recognized value is postponed.

RQ-014 validates cross-IE harm rejection and postponement rules only.
It does not validate final scoring rules, materiality thresholds, tokens, incentives or reputation scoring.

STATUS: VALIDATED

## PD-013

A measured reduction can be attributed to a candidate contribution only when the candidate contribution is observable, temporally aligned with the verified reduction, causally plausible, inside the same measurement boundary, not explained by external causes, not double-counted, and supported by sufficient attribution evidence.

For attribution:

* raw behavior is not attribution;
* raw reduction is not attribution;
* coincidence is not attribution;
* reduction can exist without attribution;
* recognized value cannot exist without attribution;
* full recognition must not be given to multiple actors for the same reduction without allocation evidence;
* aggregate-only evidence is insufficient for individual attribution when individual value recognition is requested;
* external-cause uncertainty postpones validation;
* double-claiming uncertainty postpones or rejects validation.

RQ-013 validates attribution safety rules only.
It does not validate final scoring rules, tokens, incentives or reputation scoring.

STATUS: VALIDATED

## PD-012

IE-005 measured reduction is valid only when behavior variation is a useful, timely, correctly directed, sufficiently large and sufficiently sustained response to a verified system need, inside the relevant boundary, distinguishable from normal variation, net of rebound, free from fake-flexibility patterns, and attributable to the candidate contribution.

For IE-005:

* raw behavior variation is not sufficient;
* raw response events are not sufficient;
* participant-declared system need alone is invalid;
* response profile defined after the response is invalid;
* wrong-direction response invalidates reduction;
* late response invalidates reduction when it misses the useful deadline;
* insufficient magnitude invalidates or postpones validation;
* insufficient duration invalidates or postpones validation;
* normal variation must not be counted as flexibility;
* fake flexibility invalidates reduction;
* harmful rebound invalidates or reduces measured reduction;
* missing or material uncertainty postpones validation.

RQ-012 validates IE-005 system-need, response-profile and useful-response rules only.
It does not validate final UFR_net formula, scoring rules, tokens, or incentives.

STATUS: VALIDATED

## PD-000

PoE misura il contributo energetico verificabile.

STATUS: VALIDATED

## PD-011

IE-003 measured reduction is valid only when peak stress is reduced during a valid system-relevant critical window, against a valid peak baseline and threshold, with rebound/displacement checks, artificial-peak rejection, data-quality checks, and sufficient evidence for attribution.

For IE-003:

* raw kW reduction is not sufficient;
* not every peak window is critical;
* participant-declared critical window alone is invalid;
* previous peak alone is not a valid baseline peak profile;
* arbitrary or cherry-picked peak threshold is invalid;
* artificial peak creation invalidates reduction;
* temporal displacement invalidates reduction when it recreates equivalent stress;
* cross-node displacement invalidates reduction when stress is transferred outside the measured boundary;
* full rebound invalidates reduction;
* partial rebound reduces measured reduction;
* missing or material uncertainty postpones validation.

RQ-011 validates IE-003 critical-window, peak-threshold, baseline peak-profile and rebound/displacement rules only.
It does not validate final NPSR_net formula, scoring rules, tokens, or incentives.

STATUS: VALIDATED

## PD-010

IE-002 measured reduction is valid only when lower energy consumption is shown for the same necessary function under equivalent context, net of rebound and shifted consumption, against a non-gamed baseline, with sufficient evidence for attribution.

For IE-002:

* raw lower consumption is not sufficient;
* previous consumption alone is not a valid baseline;
* participant-declared baseline alone is invalid;
* function loss invalidates reduction;
* material service degradation invalidates reduction;
* shifted consumption invalidates reduction;
* full rebound invalidates reduction;
* partial rebound reduces measured reduction;
* missing or material uncertainty postpones validation.

RQ-010 validates IE-002 baseline and function-preservation rules only.
It does not validate final ACR_net formula, thresholds, scoring rules, tokens, or incentives.

STATUS: VALIDATED

## PD-001

Gerarchia PoE:
INEFFICIENZA
RIDUZIONE
CONTRIBUTO
VALORE
REPUTAZIONE
INCENTIVO

STATUS: VALIDATED

## PD-002

Un contributo energetico e un comportamento osservabile e verificabile che produce un miglioramento misurabile del sistema energetico.

STATUS: VALIDATED

## PD-003

Il valore nel protocollo PoE e la riduzione verificabile di una inefficienza del sistema energetico.

Clarification:
PD-003 is an early compact definition. After PD-008, PD-009, PD-013, PD-014 and PD-015, "riduzione verificabile" must not be interpreted as raw measured reduction or measured reduction alone. In PoE V1, value means protocol-qualified reduction: verified, attributable, system-relevant, boundary-consistent, non-duplicated, not invalidated by unbounded material cross-IE harm, and supported by sufficient evidence. PD-016 defines the recognized-value eligibility gate.

STATUS: VALIDATED

## PD-004

La reputazione PoE e dinamica e aggiornata continuamente in base al valore sistemico verificato generato dal nodo.

STATUS: VALIDATED

## PD-005

La reputazione PoE misura la capacita dimostrata di un soggetto di generare valore sistemico nel tempo.

STATUS: VALIDATED

## PD-006

Proof of Energy identifica inefficienze energetiche, misura il contributo dei partecipanti alla loro riduzione e trasforma tale contributo in valore verificabile.

STATUS: VALIDATED

## PD-007

Le inefficienze primitive del protocollo PoE V1 sono:

IE-002 Consumo evitabile
IE-003 Punte di carico
IE-005 Mancanza di flessibilita

Le seguenti inefficienze sono classificate come derivate:

IE-001 Energia sprecata
IE-004 Energia rinnovabile non utilizzata
IE-006 Instabilita locale

STATUS: VALIDATED

## PD-008

CONTRIBUTO, RIDUZIONE e VALORE sono oggetti protocollari distinti.

RIDUZIONE:
delta osservabile e verificabile di una inefficienza catalogata rispetto a baseline, finestra temporale e contesto validati.

CONTRIBUTO:
comportamento osservabile, verificabile e attribuibile a un nodo o soggetto che partecipa causalmente alla riduzione.

VALORE:
proprieta protocollare derivata da una riduzione verificata, attribuita e sistemicamente rilevante di una inefficienza catalogata.

VALORE non e identico alla RIDUZIONE grezza.
VALORE e RIDUZIONE qualificata dal protocollo tramite verifica, attribuzione, rilevanza sistemica e controllo contro manipolazioni.

STATUS: VALIDATED

## PD-009

For each primitive inefficiency, PoE V1 metrics must separate:

1. observable behavior;
2. candidate contribution;
3. measured reduction;
4. reduction verification;
5. attribution to contribution;
6. recognized value.

IE-002, IE-003 and IE-005 must each define:

* metric target;
* observable inputs;
* baseline requirement;
* valid reduction;
* invalid reduction;
* attribution rule;
* value condition;
* attack vectors;
* minimum verification rule.

RQ-008 validates the conceptual metric structure only.
It does not validate final quantitative formulas, thresholds, scoring rules, tokens, or incentives.

STATUS: VALIDATED
