# RQ-015 — Quantitative measured-reduction metrics after safety rules PD-010 to PD-014

Status:
VALIDATED / CLOSED

Decision:
PD-015

Question:
Can PoE V1 validate quantitative measured-reduction metrics for IE-002, IE-003 and IE-005 after PD-010 to PD-014 safety rules?

## Context

* RQ-009 was POSTPONED because candidate quantitative metrics could not be validated before baseline, function-preservation, attribution and cross-IE harm rules existed.
* RQ-015 is not a reopening of RQ-009 as the same research object.
* RQ-009 remains historically POSTPONED.
* RQ-015 validates formulas only after PD-010 to PD-014.

## Binding object separation

Use PD-008:
CONTRIBUTO, RIDUZIONE and VALORE are distinct objects.

## Binding metric chain

Use PD-009:
observable behavior
-> candidate contribution
-> measured reduction
-> reduction verification
-> attribution to contribution
-> recognized value

## Validated metrics

### IE-002 — Avoidable Consumption Reduction

ACR_net = max(0, E_base(W | F,C) - E_obs(W) - E_rebound(R) - E_shifted)

Define:

* E_base(W | F,C): expected energy consumption in window W for the same necessary function F under equivalent context C if the candidate contribution had not occurred.
* E_obs(W): observed energy consumption in window W.
* E_rebound(R): additional consumption in rebound window R caused by or materially linked to the earlier reduction claim.
* E_shifted: consumption moved outside window W, outside the measured node, or into another process while preserving the same underlying demand.

Validity rule:
ACR_net is valid only if PD-010 checks pass:

* baseline validity
* function preservation
* equivalent context
* no material service degradation
* rebound excluded or subtracted
* shifted consumption excluded or subtracted
* boundary manipulation rejected

Failure rule:
ACR_net is zero, invalid or postponed if any required PD-010 gate fails.

### IE-003 — Net Peak Stress Reduction

PeakStress(W) = integral over W of max(0, P(t) - P_threshold(t)) dt

NPSR_net = max(0, PeakStress_base(Wc) - PeakStress_obs(Wc) - PeakStress_rebound(Wr) - PeakStress_displaced)

Define:

* Wc: validated critical window where peak stress is system-relevant.
* Wr: rebound or displacement observation window linked to the claimed peak reduction.
* P_threshold(t): validated time-dependent threshold above which load contributes to IE-003 peak stress.
* PeakStress_base(Wc): expected peak stress in validated critical window Wc if the candidate contribution had not occurred.
* PeakStress_obs(Wc): observed peak stress in validated critical window Wc.
* PeakStress_rebound(Wr): later peak stress caused by or materially linked to the earlier claimed reduction.
* PeakStress_displaced: peak stress moved outside Wc, outside the measured node, or into another constrained period.

Validity rule:
NPSR_net is valid only if PD-011 checks pass:

* valid critical window
* valid peak threshold
* valid baseline peak profile
* artificial peak rejection
* rebound excluded or subtracted
* displacement excluded or subtracted
* boundary integrity

Failure rule:
NPSR_net is zero, invalid or postponed if any required PD-011 gate fails.

### IE-005 — Useful Flexibility Response

UFR_delivered = integral over T of min(abs(DeltaP_obs(t)), abs(Req(t))) dt

Only count intervals where:

* response direction is correct
* response occurs inside useful deadline
* response occurs inside relevant boundary
* response is sustained for required duration
* response matches a validated system need

UFR_net = max(0, UFR_delivered - UFR_baseline - Response_rebound_penalty)

Define:

* UFR_delivered: validated useful response actually delivered against the required response profile during time horizon T.
* UFR_baseline: baseline response or normal variation that would have occurred without the candidate contribution and therefore cannot be counted as IE-005 measured reduction.
* Response_rebound_penalty: later counter-response or linked rebound that reduces or cancels the usefulness of the delivered response.

Validity rule:
UFR_net is valid only if PD-012 checks pass:

* valid system need
* valid response profile
* useful response
* correct direction
* timely response
* sufficient magnitude
* sufficient duration
* relevant boundary
* normal variation excluded
* fake flexibility rejected
* rebound excluded or subtracted

Failure rule:
UFR_net is zero, invalid or postponed if any required PD-012 gate fails.

## Attribution gate

Under PD-013, measured reduction cannot become recognized value unless attribution passes.

## Cross-IE harm gate

Under PD-014, measured reduction cannot become recognized value if it creates unbounded material harm in another primitive inefficiency.

## Non-finality

PD-015 does not define:

* recognized value
* reputation
* incentives
* token issuance
* economic allocation
* final scoring
* implementation logic

## Conclusion

RQ-015 validates quantitative measured-reduction metrics only.
It does not unblock implementation.
Implementation remains BLOCKED.
