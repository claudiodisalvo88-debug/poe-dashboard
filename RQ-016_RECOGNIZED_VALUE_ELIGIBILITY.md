# RQ-016 — Recognized value eligibility after measured reduction, attribution and cross-IE safety

Status:
VALIDATED / CLOSED

Decision:
PD-016

Question:
When can a verified measured reduction become recognized value in PoE V1 without collapsing measured reduction into value, reputation, incentive, token logic or scoring?

Context:
RQ-015 validated ACR_net, NPSR_net and UFR_net only as quantitative measured-reduction metrics.
RQ-015 did not validate recognized value.
RQ-016 defines the eligibility gate between measured reduction and recognized value.
Implementation remains blocked.

## PD-003 clarification

PD-003 remains valid as a compact early definition, but it is clarified by PD-008 and PD-016.
Measured reduction alone does not equal recognized value.
"Riduzione verificabile" in PD-003 must now be read as protocol-qualified reduction, not raw measured reduction.

Binding object separation:
Use PD-008:
CONTRIBUTO, RIDUZIONE and VALORE are distinct objects.

Binding metric chain:
Use PD-009:
observable behavior
-> candidate contribution
-> measured reduction
-> reduction verification
-> attribution to contribution
-> recognized value

Recognized value definition:
Recognized value in PoE V1 is the protocol-eligible status of a verified measured reduction of a primitive inefficiency that is attributable to a candidate contribution, system-relevant, boundary-consistent, non-duplicated and not invalidated by unbounded material cross-IE harm.

Recognized value is not:

* raw behavior
* candidate contribution
* measured reduction alone
* reputation
* incentive
* token issuance
* economic allocation
* final scoring
* implementation logic

Eligibility conditions:
A verified measured reduction can become recognized value only if all minimum conditions hold:

1. Primitive IE relevance:
   The reduction targets one of the PoE V1 primitive inefficiencies:

* IE-002 Consumo evitabile
* IE-003 Punte di carico
* IE-005 Mancanza di flessibilita

2. Valid measured reduction:
   The measured reduction passes the relevant safety gate:

* PD-010 for IE-002
* PD-011 for IE-003
* PD-012 for IE-005

3. Object separation:
   The measured reduction remains distinct from contribution and value under PD-008.

4. Metric-chain compliance:
   The claim follows the PD-009 metric chain:
   observable behavior
   -> candidate contribution
   -> measured reduction
   -> reduction verification
   -> attribution to contribution
   -> recognized value

5. Attribution:
   The measured reduction is attributable to a candidate contribution under PD-013.

6. Cross-IE safety:
   The reduction does not create unbounded material harm in another primitive IE under PD-014.

7. Boundary integrity:
   The reduction is assessed within the relevant system boundary and does not merely shift inefficiency outside the relevant window, node, meter, asset, local boundary or system boundary.

8. System relevance:
   The reduction improves a relevant energy-system condition and is not merely private local optimization with no systemic effect.

9. Non-duplication:
   The same physical effect is not recognized twice as separate value.

10. Evidence sufficiency:
    If required evidence is insufficient, recognized value is postponed, not assumed.

Failure conditions:

Rejected:
Recognized value is rejected when a required condition is known to be false.

Rejection applies when:

* attribution fails
* the target IE is not primitive IE-002, IE-003 or IE-005
* measured reduction fails its IE-specific safety gate
* the reduction is caused by baseline manipulation, artificial peaks, fake flexibility or service degradation
* the claimed reduction is merely displacement across time, node or boundary
* unbounded material cross-IE harm is confirmed
* the same physical effect is already recognized as the same value elsewhere
* the claimed value is only private local optimization with no systemic relevance

Zero:
Recognized value is zero when the eligible measured reduction is zero after the relevant metric and safety gates apply.

Zero applies when:

* ACR_net is zero after rebound, shifted-consumption or invalid-function checks
* NPSR_net is zero after rebound, displacement or artificial-peak checks
* UFR_net is zero after baseline-response, fake-flexibility or rebound checks
* numerical reduction exists but no eligible system-relevant reduction remains

Capped:
Recognized value is capped only when the safe, attributable, non-harmful portion of a measured reduction can be bounded.

Capping is not final scoring.
Capping is an eligibility limitation.
Only the bounded safe portion may proceed as recognized value.

Capping is allowed only if the harmful, duplicated, unattributed or displaced portion can be separated from the valid portion.

If the invalid portion cannot be separated, recognition must be postponed or rejected.

Postponed:
Recognized value is postponed when a required condition is unresolved but not proven false.

Postponement applies when:

* evidence is incomplete
* attribution is plausible but not yet separable
* cross-IE harm is plausible but not bounded
* boundary integrity is unclear
* rebound or displacement windows are insufficient
* duplicate claims are unresolved
* system relevance is plausible but weakly evidenced
* multi-actor shares cannot be separated

Attack cases:
Document these attack cases and expected protocol response:

1. Measured reduction without attribution:
   Rejected or postponed under PD-013.
   No recognized value exists without attribution.

2. Local improvement with system harm:
   Rejected or postponed under boundary integrity and PD-014.
   Local improvement alone is insufficient.

3. Cross-IE harm:
   Rejected, capped or postponed under PD-014.
   A target IE reduction cannot become recognized value if unbounded material harm is created in another primitive IE.

4. Double counting:
   Rejected or postponed unless distinct measured reductions and attribution paths are proven.
   The same effect cannot be recognized twice as separate value.

5. Weak system relevance:
   Rejected or postponed.
   Recognized value requires relevance to a primitive energy-system inefficiency.

6. Incomplete evidence:
   Postponed.
   Evidence gaps do not create assumed value.

7. Baseline manipulation:
   Rejected if confirmed.
   Postponed if unresolved.

8. Rebound/displacement:
   Subtracted, capped, rejected or postponed depending on whether the invalid portion is bounded.
   Unbounded rebound or displacement blocks recognized value.

9. Same effect claimed under multiple IE labels:
   Rejected or postponed unless each IE claim independently passes its own metric, safety gate, attribution and non-duplication checks.
   Relabeling one effect is not separate recognized value.

Conclusion:
RQ-016 validates recognized-value eligibility only.
It does not define reputation, incentives, token logic, economic allocation, final scoring or implementation logic.
Implementation remains BLOCKED.
