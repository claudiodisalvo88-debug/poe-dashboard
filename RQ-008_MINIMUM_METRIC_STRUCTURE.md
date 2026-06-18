# RQ-008 — Minimum metric structure for IE-002, IE-003, IE-005

Status:
VALIDATED / CLOSED

Decision:
PD-009

## Binding constraints

* PD-008 is binding.
* CONTRIBUTO, RIDUZIONE and VALORE are distinct objects.
* Observed behavior is only candidate contribution until linked to verified reduction, attribution and systemic relevance.
* No contribution dimensions are used as operative protocol objects.

## Shared minimum metric structure

1. observable behavior
2. candidate contribution
3. measured reduction
4. reduction verification
5. attribution to contribution
6. recognized value

## IE-002 Consumo evitabile

* metric target:
avoidable consumption relative to an equivalent baseline with no necessary loss of function.
* observable input:
measured consumption, service or function delivered, time window, operating context, node identity.
* baseline requirement:
an equivalent comparison condition must exist for the same function, context and time logic.
* valid reduction:
observed lower consumption versus baseline while preserving the necessary function.
* invalid reduction:
apparent reduction caused by loss of function, outage, missing service, manipulated baseline or shifted consumption outside the observed window.
* attribution rule:
the reduction can be linked to a specific observed behavior by the same node or subject in the validated window.
* value condition:
value exists only if the IE-002 reduction is verified, attributed and not contradicted by worsening of the same target through hidden rebound inside the validated context.
* main attack vectors:
baseline inflation, hidden service degradation, temporal shifting, rebound after window, false efficiency claims.
* minimum verification rule:
verify equivalent function, validated baseline, measured delta and absence of obvious invalidation in the comparison window.

## IE-003 Punte di carico

* metric target:
peak load intensity, duration or frequency in system-relevant critical windows.
* observable input:
time series of load, timing of peak windows, node or aggregate identity, operating context, observed intervention behavior.
* baseline requirement:
a validated reference profile for comparable peak conditions and comparable time windows must exist.
* valid reduction:
lower peak intensity, shorter peak duration or lower peak frequency in a relevant critical window versus baseline.
* invalid reduction:
apparent peak reduction created by previous peak fabrication, export of load to another nearby window, hidden transfer to another node or non-comparable baseline conditions.
* attribution rule:
the observed behavior must precede or coincide with the measured peak reduction and be causally linked to that reduction in the same critical window.
* value condition:
value exists only if the IE-003 reduction is verified for the specific peak event and is not just displacement that recreates equivalent stress elsewhere in the validated context.
* main attack vectors:
peak fabrication, temporal displacement, cross-node shifting, selective windowing, event cherry-picking.
* minimum verification rule:
verify comparable peak window, measured peak delta, event relevance and absence of obvious recreated peak stress in the validated comparison scope.

## IE-005 Mancanza di flessibilita

* metric target:
observed ability to modify consumption, production or storage in response to relevant system conditions within the required time.
* observable input:
system signal or condition, response timing, response magnitude, direction of adjustment, node identity, operating context.
* baseline requirement:
a validated reference of non-response, lower response or required response capability must exist for equivalent conditions.
* valid reduction:
measured improvement in timely and relevant response capability versus baseline under system-relevant conditions.
* invalid reduction:
claimed flexibility shown only in non-relevant conditions, simulated response without real constraint, response too late to matter or response that worsens another inefficiency without verified benefit on IE-005.
* attribution rule:
the measured response must be directly attributable to the observed behavior of the same node or subject under the validated condition.
* value condition:
value exists only if the IE-005 reduction is verified as real flexibility improvement in a relevant condition and not as a nominal or staged response.
* main attack vectors:
fake dispatchability, irrelevant test conditions, delayed response, pre-programmed show events, response masking external support.
* minimum verification rule:
verify relevant trigger condition, actual response timing, actual response magnitude and comparison against an equivalent validated baseline.

## Cross-IE falsification checks

* A behavior may reduce IE-002 but worsen IE-003.
* A behavior may reduce IE-003 without reducing IE-002.
* A behavior may reduce IE-005 without reducing IE-002 or IE-003.
* Value must always be tied to the specific inefficiency reduced.
* Any metric that jumps directly from observable behavior to value is unsafe.

## Final verdict

RQ-008: VALIDATED / CLOSED.

Scope: conceptual metric structure only, not final quantitative specification.
