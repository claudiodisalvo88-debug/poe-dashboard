# RQ-012 — IE-005 system-need, response-profile and useful-response validation rules

Status:
VALIDATED / CLOSED

Decision:
PD-012

## Context

* RQ-009 was POSTPONED because candidate quantitative metrics could not be validated until baseline, equivalence, attribution and cross-IE rules were defined.
* RQ-010 solved the IE-002 blocker.
* RQ-011 solved the IE-003 blocker.
* RQ-012 solves only the IE-005 blocker: system need, response profile, useful response and fake-flexibility rejection.

## Validated IE-005 rule

IE-005 behavior variation is protocol-safe only when it is a useful, timely, correctly directed, sufficiently large and sufficiently sustained response to a verified system need, inside the relevant boundary, distinguishable from normal variation, net of rebound, free from fake-flexibility patterns, and attributable to the candidate contribution.

## System-need rule

* A valid IE-005 system need is an observable condition of the energy system requiring a timely change in consumption, production or storage behavior.
* A system need is not any signal.
* A system need is not any opportunity for a participant to vary behavior.
* A system need must define why adaptation is useful under the given condition.
* A participant cannot unilaterally define system need.
* The need must be constrained by observable system condition, relevant boundary, time window, useful response direction and evidence that non-response would leave the system less adaptable.
* If system need cannot be shown, validation must be postponed or rejected.

## Response-profile rule

* A required response profile is the ex-ante or event-time description of the response needed to reduce IE-005.
* It defines useful adaptation.
* Without a response profile, behavior variation cannot be distinguished from flexibility.
* Response profile must define:
  * response direction;
  * response magnitude;
  * response duration;
  * response deadline;
  * response boundary.
* The profile must not be defined after the response to fit observed behavior.
* A response profile defined only by the participant is invalid.

## Useful-response rule

A response is useful to IE-005 only if:

* it responds to a verified system need;
* it follows the required direction;
* it arrives within the useful deadline;
* its magnitude is sufficient;
* its duration is sufficient;
* it occurs inside the relevant boundary;
* it is distinguishable from normal variation;
* it is attributable to the candidate contribution.

## Invalid response

A response is invalid if:

* no valid system need existed;
* the response profile is invalid;
* direction is wrong;
* response is late;
* response is too small;
* response is too short;
* response is outside the relevant boundary;
* response is normal variation;
* response is fake flexibility;
* response creates harmful rebound;
* attribution is not possible.

## Fake-flexibility rejection

Reject or postpone validation when there is:

* fake dispatchability;
* response without real system need;
* delayed response;
* wrong-direction response;
* too-short response;
* normal variation misclassified as flexibility;
* pre-positioning to exaggerate response;
* rebound after response;
* external support hidden behind the node;
* double-claiming shared flexibility.

## Rebound rule

* Rebound after response reduces measured reduction if it partially offsets usefulness.
* Rebound invalidates IE-005 measured reduction if it cancels usefulness or creates material harm.
* If rebound evidence is incomplete and may be material, validation must be postponed.

## Formal minimum validation rule

IE-005 measured reduction is valid only if all conditions below are true:

1. target inefficiency is IE-005;
2. a valid system need existed;
3. relevant system boundary is defined;
4. valid response profile existed before or at the system-need event;
5. observed response follows required direction;
6. response arrives within useful deadline;
7. response magnitude is sufficient;
8. response duration is sufficient;
9. response occurs inside the relevant boundary;
10. response is distinguishable from normal variation;
11. response is not fake flexibility;
12. rebound checks pass;
13. attribution to candidate contribution is possible;
14. no invalidation condition exists.

## Negative rule

* If any required condition is false, IE-005 measured reduction must be rejected.
* If any required condition is unknown and materially affects validity, IE-005 validation must be postponed.
* Raw behavior variation must not become measured reduction.
* Raw response events must not become recognized value.

## Minimum evidence package

* observed consumption, production or storage behavior before, during and after the response;
* evidence of valid system need;
* relevant boundary definition;
* required response profile;
* response timing evidence;
* response direction evidence;
* response magnitude evidence;
* response duration evidence;
* normal-behavior or non-response baseline evidence;
* rebound-window evidence;
* pre-positioning check;
* evidence excluding hidden external support;
* attribution evidence linking response to candidate contribution;
* evidence preventing double-claiming.

## Cross-IE rule

* IE-005 measured reduction may exist without IE-002 reduction.
* IE-005 measured reduction may exist without IE-003 reduction.
* IE-005 response must not be misclassified as IE-002 or IE-003 value.
* IE-005 measured reduction must be rejected or reduced if it creates material harm to another primitive inefficiency.
* If cross-IE harm cannot be assessed and may be material, validation must be postponed.

## Final verdict

RQ-012: VALIDATED / CLOSED

## Scope limitation

This validates IE-005 measurement safety rules only.
It does not validate final UFR_net formula, universal response deadlines, magnitude thresholds, duration thresholds, final scoring, tokens or incentives.
