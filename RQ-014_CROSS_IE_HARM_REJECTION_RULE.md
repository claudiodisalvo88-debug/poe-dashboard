# RQ-014 — Cross-IE harm rejection rule for primitive inefficiency reductions

Status:
VALIDATED / CLOSED

Decision:
PD-014

## Context

* RQ-010 validated IE-002 measurement safety rules.
* RQ-011 validated IE-003 measurement safety rules.
* RQ-012 validated IE-005 measurement safety rules.
* RQ-013 validated attribution safety rules.
* RQ-014 defines when a verified measured reduction cannot become recognized value because it creates material harm in another primitive inefficiency.

## Validated cross-IE harm rule

A primitive IE reduction can become recognized value only when it is not merely a transfer of inefficiency into another primitive IE.

## Cross-IE harm definition

* Cross-IE harm is a worsening of one primitive inefficiency caused by, enabled by, hidden behind, or materially linked to a behavior that claims reduction of another primitive inefficiency.
* Cross-IE harm is not a new primitive inefficiency.
* Cross-IE harm is a rejection or postponement condition for unsafe value recognition.
* Cross-IE harm can preserve the fact that a measured target IE reduction occurred, but can block the right to recognize that reduction as value.

## Material harm rule

* Material harm is cross-IE worsening large enough to affect the systemic relevance of the claimed reduction.
* Material harm exists when the behavior worsens another primitive IE in the same boundary, another relevant boundary, a later linked window, or a causally connected operating cycle.
* Material harm also exists when the claimed reduction is only displacement of the inefficiency into another IE.
* If material cross-IE harm is confirmed and not bounded, recognized value must be rejected.
* If material cross-IE harm is plausible but unknown, recognized value must be postponed.
* If harm is evidenced as immaterial or bounded, recognition may proceed only under a rule that prevents false net value.

## IE-002 interaction rules

1. IE-002 reduction that worsens IE-003:

* Example: consumption is reduced overall but shifted into a critical peak window.
* IE-002 measured reduction may remain valid only if consumption was truly avoided, not shifted.
* Recognized value must be rejected if shifted load creates material IE-003 harm.
* Recognition must be postponed if peak-window evidence is missing.

2. IE-002 reduction that worsens IE-005:

* Example: consumption is minimized by disabling control capability, storage readiness or operational responsiveness.
* IE-002 measured reduction may remain valid only if necessary function is preserved and disabled flexibility was not part of necessary function.
* Recognized value must be rejected if the behavior materially worsens IE-005.
* Recognition must be postponed if system-need impact cannot be bounded.

## IE-003 interaction rules

1. IE-003 reduction that worsens IE-002:

* Example: peak is flattened by consuming more total avoidable energy.
* IE-003 measured reduction may remain valid if peak stress is genuinely reduced in the critical window.
* Recognized value must be rejected if added avoidable consumption is material and unbounded.
* Recognition must be postponed if total avoidable consumption impact is unknown.

2. IE-003 reduction that worsens IE-005:

* Example: peak is avoided by locking the node into an inflexible state.
* IE-003 measured reduction may remain valid if peak stress reduction passes IE-003 rules.
* Recognized value must be rejected if flexibility loss is material to a verified or foreseeable system need.
* Recognition must be postponed if IE-005 impact cannot be observed or bounded.

## IE-005 interaction rules

1. IE-005 useful response that worsens IE-002:

* Example: flexible response requires avoidable extra consumption such as inefficient standby, unnecessary pre-positioning, or energy-intensive readiness.
* IE-005 measured reduction may remain valid if the response truly satisfies a valid system need.
* Recognized value must be rejected if avoidable consumption harm is material and not bounded.
* Recognition must be postponed if readiness energy and lower-consumption alternatives cannot be assessed.

2. IE-005 useful response that worsens IE-003:

* Example: useful response now creates a rebound peak later.
* IE-005 measured reduction may remain valid only if rebound does not cancel useful response or create material peak stress.
* Recognized value must be rejected if rebound creates material IE-003 harm.
* Recognition must be postponed if rebound window data is missing.

## Local value vs system harm rule

* Local improvement is insufficient for recognized value unless the relevant system boundary also avoids material harm.
* Local boundary improvement must be rejected or postponed if it depends on shifting consumption, peak stress or rigidity outside the measured boundary.
* If aggregate system effect worsens, recognized value must be rejected even if local measured reduction is real.
* Harm shifted to another node invalidates recognition when the receiving node or boundary suffers material worsening of IE-002, IE-003 or IE-005.
* Harm outside the observation window is still relevant if causally linked to the claimed contribution.
* Target IE verification is necessary but not sufficient for recognized value.

## Double recognition rule

* One behavior may genuinely reduce two primitive IEs only if each IE-specific measured reduction is independently verified.
* Separate recognition is allowed only if the same physical effect is not counted twice as the same value.
* One behavior reducing one IE but only appearing to reduce another must be recognized only for the IE whose specific rules pass.
* The same measured reduction must not be counted twice as independent recognized value.
* Duplicate recognition must be rejected unless the protocol can demonstrate distinct reductions, distinct IE targets and non-overlapping attribution.
* If IE effects cannot be separated, attribution and value recognition must be postponed.

## Minimum cross-IE evidence

Cross-IE evidence must include:

* target IE measured reduction;
* attribution for target IE;
* monitoring of other primitive IEs;
* rebound window;
* displacement window;
* boundary consistency;
* temporal spillover evidence;
* external cause exclusion;
* data completeness;
* IE-specific evidence where relevant:

  * function preservation evidence for IE-002;
  * critical-window evidence for IE-003;
  * system-need and response-profile evidence for IE-005.
* cross-node boundary evidence when harm may move to another node or boundary;
* asset operating cycle when rebound or delayed harm depends on duty cycle.

Not enough data:

* participant self-declaration alone;
* raw lower kWh;
* raw lower kW;
* raw response event.

## Formal cross-IE harm rule

Recognized value is valid only if all conditions below are true:

1. target IE measured reduction is verified;
2. attribution to candidate contribution passes;
3. material harm to the other primitive IEs is excluded, bounded or explicitly handled by a non-duplicative protocol rule;
4. rebound checks pass;
5. displacement checks pass;
6. boundary-shift checks pass;
7. temporal spillover checks pass;
8. external causes are excluded or bounded;
9. double recognition is prevented;
10. no invalidation condition exists.

## Negative rule

* If material cross-IE harm is confirmed and not bounded, recognized value must be rejected.
* If material cross-IE harm is plausible but unknown, recognized value must be postponed.
* If one behavior appears to affect multiple IEs, each IE claim must pass its own measurement, verification and attribution rules independently.
* The same measured effect must not be recognized twice as separate value.
* Local improvement cannot become recognized value if it shifts material harm to another node, boundary, time window or primitive IE.

## Final verdict

RQ-014: VALIDATED / CLOSED

## Scope limitation

This validates cross-IE harm rejection and postponement safety rules only.
It does not validate final scoring, token allocation, incentives, reputation scoring, materiality thresholds, final economic allocation, or final cross-unit comparison.
