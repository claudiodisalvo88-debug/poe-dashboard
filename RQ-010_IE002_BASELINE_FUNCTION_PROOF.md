# RQ-010 — IE-002 baseline and function-preservation proof

Status:
VALIDATED / CLOSED

Decision:
PD-010

## Context

* RQ-009 was POSTPONED because candidate quantitative metrics could not be validated until baseline, equivalence, attribution and cross-IE rules were defined.
* RQ-010 solves only the IE-002 blocker: baseline and function-preservation proof.

## Validated IE-002 rule

IE-002 lower consumption is protocol-safe only when it is lower energy consumption for the same necessary function under equivalent context, net of rebound and shifted consumption, against a non-gamed baseline, with sufficient evidence for attribution.

## Baseline rule

* Baseline consumption is expected energy consumption required to deliver the same necessary function under equivalent context, assuming the candidate contribution had not occurred.
* Baseline is not simply previous consumption.
* Baseline is not participant-declared normal use.
* Baseline must be constrained by observable data, historical behavior, equivalent context, external or independent evidence where available, and rejection rules.
* A self-declared baseline alone is invalid.

## Baseline invalidity

A baseline is invalid if:

* function is not equivalent;
* context is not equivalent;
* baseline window is cherry-picked;
* historical baseline period is abnormal;
* device state differs materially;
* consumption was artificially inflated;
* missing data affects comparison;
* baseline depends only on participant declaration;
* function demand was fake or exaggerated;
* consumption was hidden outside the measured node;
* rebound or shifted consumption is not observable.

## Function-preservation rule

* Function is the useful service, output or operational purpose that energy consumption exists to provide.
* Necessary function is the minimum required useful service or output that must be delivered under the relevant context.
* Lower consumption caused by function loss is invalid.
* Lower consumption caused by material service degradation is invalid.
* Equivalent function means the observation window delivered materially the same necessary service or output as the baseline window.
* Equivalence does not require identical behavior, but requires no necessary loss of function.

## Minimum function evidence

Minimum evidence must show:

* what function was required;
* what function was delivered in the baseline window;
* what function was delivered in the observation window;
* that delivered function was materially equivalent;
* that quality, duration, availability and relevant service level did not materially degrade;
* that lower consumption did not result from lower demand, outage, shutdown or suppressed output.

## Context-equivalence rule

Context equivalence means baseline and observation windows are comparable enough that lower consumption can plausibly be attributed to avoided consumption rather than different operating conditions.

Required context variables:

* time window;
* device state;
* operating schedule;
* data completeness;
* hidden parallel consumption boundary.

Asset-specific context variables:

* weather;
* occupancy;
* production level;
* external demand;
* maintenance state;
* user comfort or service quality;
* safety constraint.

Optional context variables:

* tariff or price signal;
* system condition.

## Rebound and shifted-consumption rule

* Rebound is later additional consumption caused by or materially linked to the earlier reduction.
* Shifted consumption is energy use moved outside the observation window, outside the measured node, or into another process while preserving the same underlying demand.
* A universal rebound window is unsafe.
* The rebound window must be asset-specific or duty-cycle-specific.
* Full rebound invalidates IE-002 measured reduction.
* Partial rebound reduces measured reduction.
* Shifted consumption invalidates IE-002 measured reduction unless the measurement boundary proves consumption was truly avoided.

## Baseline-gaming rejection

Reject or postpone validation when there is:

* pre-baseline overconsumption;
* selective baseline window;
* abnormal historical period;
* missing data;
* manipulated device state;
* fake function demand;
* context cherry-picking;
* hidden consumption outside the node.

## Formal minimum validation rule

IE-002 measured reduction is valid only if all conditions below are true:

1. target inefficiency is IE-002;
2. baseline consumption is valid;
3. baseline and observation windows preserve equivalent necessary function;
4. baseline and observation contexts are equivalent or validly normalized;
5. observed consumption is lower than valid baseline consumption;
6. lower consumption is not caused by function loss;
7. lower consumption is not caused by service degradation;
8. lower consumption is not caused by shifted consumption;
9. rebound checks pass;
10. baseline inflation checks pass;
11. data quality is sufficient;
12. attribution to candidate contribution is possible;
13. no invalidation condition exists.

## Negative rule

* If any required condition fails, lower consumption must not become verified measured reduction.
* If a required condition is unknown but potentially material, validation must be postponed.
* If a required condition is known to be false, validation must be rejected.

## Minimum evidence package

* energy consumption during baseline and observation windows;
* function delivered during both windows;
* evidence that necessary function was preserved;
* context variables sufficient for equivalence;
* device or process state evidence;
* baseline-window validity evidence;
* observation-window validity evidence;
* rebound-window evidence;
* shifted-consumption boundary evidence;
* data completeness evidence;
* attribution evidence linking lower consumption to candidate contribution.

## Final verdict

RQ-010: VALIDATED / CLOSED

## Scope limitation

This validates IE-002 measurement safety rules only.
It does not validate final ACR_net formula, asset-specific thresholds, tolerance bands, proxy evidence standards, or universal rebound windows.
