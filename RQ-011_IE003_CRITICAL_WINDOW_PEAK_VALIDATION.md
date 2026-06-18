# RQ-011 — IE-003 critical-window, peak-threshold and rebound/displacement validation rules

Status:
VALIDATED / CLOSED

Decision:
PD-011

## Context

* RQ-009 was POSTPONED because candidate quantitative metrics could not be validated until baseline, equivalence, attribution and cross-IE rules were defined.
* RQ-010 solved only the IE-002 blocker.
* RQ-011 solves only the IE-003 blocker: critical window, peak threshold, baseline peak profile, rebound/displacement and artificial peak rejection.

## Validated IE-003 rule

IE-003 measured reduction is protocol-safe only when peak stress is reduced during a valid system-relevant critical window, against a valid peak baseline and threshold, with rebound/displacement checks, artificial-peak rejection, and sufficient evidence for attribution.

## Critical-window rule

* A critical window is a time interval where peak load is system-relevant because it can create or worsen stress on the local or aggregate energy system.
* Not every peak window is critical.
* A participant cannot unilaterally define the critical window.
* The critical window must be constrained by observable system condition, historical peak stress, capacity limits, grid/local constraint evidence, or protocol-defined event criteria.
* If critical-window relevance cannot be shown, validation must be postponed or rejected.

## Peak-threshold rule

* A peak threshold defines the level above which load contributes to IE-003 peak stress.
* The threshold may be based on local capacity, historical percentile, validated baseline profile, system signal, or protocol-defined stress condition.
* A universal threshold is unsafe.
* A threshold is invalid if it is arbitrary, participant-declared only, cherry-picked, too low to create fake peaks, or unrelated to system stress.

## Baseline peak-profile rule

* Baseline peak profile is the expected time-series peak behavior under comparable critical-window conditions if the candidate contribution had not occurred.
* Previous peak alone is not sufficient.
* Baseline must include time-series shape, peak magnitude, peak duration, peak frequency, context and event relevance.
* Artificial or inflated peaks must be rejected.
* If the baseline peak profile depends on manipulated or non-comparable events, validation must be postponed or rejected.

## Rebound and displacement rule

* Rebound peak is later peak stress caused by or materially linked to the earlier reduction.
* Displaced peak is peak stress moved outside the critical window, outside the measured node, or into another constrained period.
* Temporal displacement means the same stress appears in another time window.
* Cross-node displacement means the stress is transferred to another node, asset, site or actor.
* A universal rebound/displacement window is unsafe.
* Full rebound or equivalent displacement invalidates IE-003 measured reduction.
* Partial rebound reduces measured reduction.
* If rebound/displacement cannot be observed and may be material, validation must be postponed.

## Artificial-peak rejection

Reject or postpone validation when there is:

* pre-event peak inflation;
* intentional peak creation;
* selective peak-window choice;
* artificial load spike;
* hidden transfer to another node;
* rebound after event;
* reduction of non-critical peak;
* aggregate attribution theft;
* double-claiming shared peak reduction.

## Formal minimum validation rule

IE-003 measured reduction is valid only if all conditions below are true:

1. target inefficiency is IE-003;
2. critical window is valid;
3. peak threshold is valid;
4. baseline peak profile is valid;
5. observed peak stress is lower than valid baseline peak stress;
6. reduction occurs in a system-relevant window;
7. reduction is not artificial peak reversal;
8. reduction is not temporal displacement;
9. reduction is not cross-node displacement;
10. rebound checks pass;
11. data quality is sufficient;
12. attribution to candidate contribution is possible;
13. no invalidation condition exists.

## Negative rule

* If any required condition fails, lower peak stress must not become verified measured reduction.
* If a required condition is unknown but potentially material, validation must be postponed.
* If a required condition is known to be false, validation must be rejected.

## Minimum evidence package

* time-series load data during baseline and observation windows;
* evidence that the window was system-relevant;
* evidence for the peak threshold;
* baseline peak profile evidence;
* observed peak profile evidence;
* rebound/displacement window evidence;
* boundary evidence against cross-node displacement;
* data completeness evidence;
* attribution evidence linking peak reduction to candidate contribution.

## Cross-IE rule

* IE-003 value may exist without IE-002 reduction if peak stress is genuinely reduced.
* IE-003 reduction must not be misclassified as IE-002 value.
* IE-003 measured reduction must be rejected or reduced if it creates material harm to another primitive inefficiency.
* If cross-IE harm cannot be assessed and may be material, validation must be postponed.

## Final verdict

RQ-011: VALIDATED / CLOSED

## Scope limitation

This validates IE-003 measurement safety rules only.
It does not validate final NPSR_net formula, universal peak thresholds, final scoring, or universal rebound/displacement windows.
