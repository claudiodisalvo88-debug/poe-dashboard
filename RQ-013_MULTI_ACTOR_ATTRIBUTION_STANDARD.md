# RQ-013 — Multi-actor attribution standard across IE-002, IE-003, IE-005

Status:
VALIDATED / CLOSED

Decision:
PD-013

## Context

* RQ-010 validated IE-002 measurement safety rules.
* RQ-011 validated IE-003 measurement safety rules.
* RQ-012 validated IE-005 measurement safety rules.
* RQ-013 defines attribution rules required before verified measured reduction can become recognized value.

## Validated attribution rule

A measured reduction can be attributed to a candidate contribution only when the candidate contribution is observable, temporally aligned with the verified reduction, causally plausible, inside the same measurement boundary, not explained by external causes, not double-counted, and supported by sufficient attribution evidence.

## Attribution rule

* Attribution links candidate contribution to verified measured reduction.
* Raw behavior is not attribution.
* Raw reduction is not attribution.
* Coincidence is not attribution.
* Reduction can exist without attribution.
* Recognized value cannot exist without attribution.
* If attribution is materially uncertain, value recognition must be postponed.
* If attribution is false or contradicted, value recognition must be rejected.

## Single-actor attribution

Single-actor attribution is valid only if:

* the actor/node is identified;
* the behavior is observed;
* the reduction is verified;
* timestamps align;
* behavior precedes or coincides with the reduction;
* boundary is consistent;
* external causes are excluded or bounded;
* no invalidation condition exists.

## Multi-actor attribution

Multi-actor attribution requires evidence that separates or allocates causal participation.

When multiple actors contribute:

* full recognition must not be given to all actors for the same reduction;
* aggregator and node cannot both claim the full same reduction;
* signal provider and responder must not be collapsed into one actor;
* operator, device and automated system roles must be distinguished when material;
* if shares are not separable and attribution is material, validation must be postponed.

## Double-counting rejection

Reject or postpone value recognition when:

* the same reduction is claimed by multiple actors without allocation evidence;
* the same measured event is claimed under multiple IEs without distinct reduced inefficiencies;
* aggregate-only evidence cannot identify participant contribution;
* external demand drop explains the reduction;
* timestamps or boundaries are unclear.

## Minimum attribution evidence

Attribution evidence must include:

* target inefficiency;
* node or actor identity;
* observed candidate contribution;
* verified measured reduction;
* timestamp alignment;
* measurement boundary;
* baseline or counterfactual reference;
* external-cause exclusion or bounding;
* rebound/displacement exclusion where relevant;
* double-claiming prevention evidence;
* data completeness sufficient for attribution.

## Cross-IE attribution rule

* One behavior may reduce multiple primitive inefficiencies only if each IE has its own verified measured reduction.
* One measured reduction must not be counted twice as different IE value.
* IE-003 peak reduction must not be misclassified as IE-002 avoidable consumption reduction.
* IE-005 flexibility response must not be misclassified as IE-003 peak reduction unless peak stress is independently verified as reduced.
* If one behavior reduces one IE but materially worsens another, recognized value must be rejected, reduced, or postponed until cross-IE harm is resolved.

## Formal minimum attribution rule

Attribution is valid only if all conditions below are true:

1. target inefficiency is identified;
2. measured reduction is verified;
3. candidate contribution is observable;
4. actor or node identity is known;
5. candidate contribution is temporally aligned with reduction;
6. causal participation is plausible and evidenced;
7. measurement boundary is consistent;
8. external causes are excluded or bounded;
9. double counting is prevented;
10. multi-actor shares are separable or immaterial;
11. data quality is sufficient;
12. no invalidation condition exists.

## Negative rule

* If attribution is false, value recognition is rejected.
* If attribution is materially uncertain, value recognition is postponed.
* If attribution exists only at aggregate level and cannot be assigned safely, individual value recognition is postponed.
* If double claiming cannot be resolved, value recognition is postponed or rejected.

## Final verdict

RQ-013: VALIDATED / CLOSED

## Scope limitation

This validates attribution safety rules only.
It does not validate final scoring, token allocation, incentives, reputation scoring or implementation logic.
