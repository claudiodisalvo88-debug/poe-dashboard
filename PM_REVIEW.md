# PM_REVIEW.md

Scopo:
registrare la validazione PM/verifier prima che Codex modifichi o committi.

## Latest PM reviews

## PM-REVIEW-M-002-OPEN-FORMULA-CANDIDATE-RESEARCH-PHASE

Related task: M-002-OPEN-FORMULA-CANDIDATE-RESEARCH-PHASE
Decision: ACCEPTED
Reason: Repository state confirms M-001 CLOSED / COMPLETED, RQ-023 already established the formula candidate research opening boundary, PD-000 through PD-023 are validated, and M-002 may be opened only as a strictly research-only milestone boundary.
Required changes: create `M-002_FORMULA_CANDIDATE_RESEARCH_PHASE_OPENING.md`; update `POE_STATE.md`, `AGENT_QUEUE.md`, `PM_REVIEW.md` and `README.md` to mark M-002 opened as research-only while keeping active research at NONE.
Forbidden Codex actions: no code, API, database, dashboard, `poe.db`, `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`, `POE_PROTOCOL_KERNEL.md`, closed RQ documents, RQ-024 creation, formula candidates, final formula, formula syntax, weights, coefficients, scalar score, total score, ranking, leaderboard, incentives, rewards, tokens, token rights, payout, economic allocation or implementation.
Commit allowed: yes, if only authorized Markdown files are staged.
Next action: separate human approval is required to decide whether to create RQ-024 as a research-framing task only.

## PM-REVIEW-M-001-CLOSE-PROTOCOL-KERNEL-MILESTONE

Related task: M-001-CLOSE-PROTOCOL-KERNEL-MILESTONE
Decision: ACCEPTED
Reason: Repository state confirms RQ-001 through RQ-023 completed or explicitly handled, with RQ-009 postponed and PD-000 through PD-023 validated. The Protocol Kernel is sufficiently bounded to close M-001 without opening M-002.
Required changes: create `M-001_PROTOCOL_KERNEL_MILESTONE_CLOSURE.md`; update `POE_STATE.md`, `README.md`, `POE_PROTOCOL_KERNEL.md`, `AGENT_QUEUE.md` and `PM_REVIEW.md` to mark M-001 closed and keep implementation blocked.
Forbidden Codex actions: no code, API, database, dashboard, `poe.db`, formula candidates, final formula, formula syntax, weights, coefficients, scalar score, total score, ranking, leaderboard, incentives, rewards, tokens, token rights, payout or economic allocation.
Commit allowed: yes, if only authorized Markdown files are staged.
Next action: explicit human approval is required either to open a strictly research-only formula-candidate phase or to stop with an operational recap.

## PM-REVIEW-M-001-PROTOCOL-KERNEL-CONSOLIDATION

Related task: M-001-PROTOCOL-KERNEL-CONSOLIDATION
Decision: ACCEPTED
Reason: After RQ-023 / PD-023, PoE needed a consolidated protocol kernel and updated repository README before continuing toward any future formula-candidate research phase.
Required changes: Create POE_PROTOCOL_KERNEL.md, update README.md, update POE_STATE.md with consolidation note, register completed task in AGENT_QUEUE.md.
Forbidden Codex actions: no code, API, database, dashboard, poe.db, formula candidates, final formula, formula syntax, weights, coefficients, scalar score, ranking, incentives, tokens, payout or economic allocation.
Commit allowed: yes, if only authorized files are staged.
Next action: PM decides whether to close M-001 or open M-002 as strictly research-only formula-candidate phase.

## PM-REVIEW-RQ-023-DOCUMENTATION

Related task: M-001-RQ-023-DOCUMENTATION
Reviewed output: PM documentation instruction for RQ-023 / PD-023
Decision: ACCEPTED
Reason: RQ-023 passed Innovator stress-test after stale-state correction and can be documented as the opening boundary for future formula-candidate research-only phase.
Required changes: Document formula candidate research opening boundary as non-economic, non-implementative and non-computational opening condition only.
Allowed Codex actions: update `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`, `POE_STATE.md`, `AGENT_QUEUE.md`, `PM_REVIEW.md` and create `RQ-023_FORMULA_CANDIDATE_RESEARCH_OPENING_BOUNDARY.md`.
Forbidden Codex actions: code, API, database, `poe.db`, Python files, dashboard, formula candidates, final formula, formula syntax, weights, coefficients, scalar score, total score, ranking, leaderboard, incentives, tokens, payout, economic allocation.
Commit allowed: yes, if only authorized Markdown files are staged.
Next action: PM verifies commit and decides next research question.

## PM-REVIEW-RQ-023-INNOVATOR-OUTPUT

Related task: M-001-RQ-023-INNOVATOR
Reviewed output: Innovator Agent output for RQ-023 formula candidate research opening boundary
Original agent verdict: POSTPONE
PM verdict: ACCEPT WITH REFINEMENT
Stale-state correction: Agent verdict was based on outdated repository view. Real repository confirms RQ-022 VALIDATED / CLOSED, PD-000 to PD-022 VALIDATED, M-001-RQ-023-INNOVATOR ACTIVE and Implementation BLOCKED.
Reason: The substantive reasoning is valid. Formula candidate research opening boundary is needed to define when PoE may open a future research-only formula-candidate phase without proposing formulas.
Accepted content:

* formula candidate research opening boundary definition
* boundary distinction between admissible constraints, opening boundary, future candidates and future formula
* opening conditions
* blocking conditions
* failure outcomes
* anti-leakage rules
* risks against formula creep, syntax creep, hidden weights, score laundering, ranking leakage, economic leakage, implementation creep, cross-IE wash, false precision and gaming target creation
Required refinement: Documentation must reject the stale POSTPONE recommendation and preserve only the corrected PM verdict.
Allowed next action: open M-001-RQ-023-DOCUMENTATION as the next controlled Codex task.
Forbidden next action: do not define formula candidates, final formula, formula syntax, weights, coefficients, scalar score, total score, ranking, leaderboard, incentives, tokens, payout, economic allocation, API, database, dashboard or implementation.
Commit allowed: yes, if only AGENT_OUTPUTS.md, PM_REVIEW.md and AGENT_QUEUE.md are staged.

## PM-PREP-RQ-023-INNOVATOR

Related task: M-001-RQ-023-INNOVATOR
Decision: PREPARED
Reason: RQ-022 / PD-022 closed admissible formula constraints. The next required protocol step is to define the boundary for opening future formula-candidate research without yet defining formula candidates, final formula, formula syntax, weights, coefficients, scalar score, ranking, incentives, tokens, payout, economic allocation or implementation.
Allowed Codex actions: register M-001-RQ-023-INNOVATOR in AGENT_QUEUE.md and record this PM preparation note.
Forbidden Codex actions: do not update PROTOCOL_DECISIONS.md, RESEARCH_QUEUE.md, POE_KNOWLEDGE_BASE.md or POE_STATE.md; do not create RQ-023 document; do not define PD-023; do not modify code, API, database, dashboard or `poe.db`.
Next action: user runs Innovator Agent with the M-001-RQ-023-INNOVATOR prompt and returns output to PM for verdict.

## PM-REVIEW-RQ-022-DOCUMENTATION

Related task: M-001-RQ-022-DOCUMENTATION
Reviewed output: PM documentation instruction for RQ-022 / PD-022
Decision: ACCEPTED
Reason: RQ-022 passed Innovator stress-test after stale-state correction and can be documented as the admissibility constraint layer before any future reputation formula candidates.
Required changes: Document admissible formula constraints as non-economic, non-implementative and non-computational constraints for future formula research only.
Allowed Codex actions: update `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`, `POE_STATE.md`, `AGENT_QUEUE.md`, `PM_REVIEW.md` and create `RQ-022_REPUTATION_FORMULA_ADMISSIBILITY_CONSTRAINTS.md`.
Forbidden Codex actions: code, API, database, `poe.db`, Python files, dashboard, formula candidates, final formula, formula syntax, weights, coefficients, scalar score, total score, ranking, leaderboard, incentives, tokens, payout, economic allocation.
Commit allowed: yes, if only authorized Markdown files are staged.
Next action: PM verifies commit and decides next research question.

## PM-REVIEW-RQ-022-INNOVATOR-OUTPUT

Related task: M-001-RQ-022-INNOVATOR
Reviewed output: Innovator Agent output for RQ-022 reputation formula admissibility constraints
Original agent verdict: POSTPONE
PM verdict: ACCEPT WITH REFINEMENT
Stale-state correction: Agent verdict was based on outdated repository view. Real repository confirms RQ-021 VALIDATED / CLOSED, PD-000 to PD-021 VALIDATED, M-001-RQ-022-INNOVATOR ACTIVE and Implementation BLOCKED.
Reason: The substantive reasoning is valid. Admissible formula constraints are needed as a non-economic, non-implementative and non-computational constraint layer before future formula candidates.
Accepted content:

* admissible formula constraints definition
* boundary distinction between formula-ready structure, admissible constraints, formula candidates and future formula
* minimum constraints
* failure outcomes
* anti-leakage rules
* risks against hidden formula, hidden weights, hidden score, hidden ranking, incentive leakage, token leakage, economic leakage, false precision, gaming optimization and implementation creep
Required refinement: Documentation must reject the stale POSTPONE recommendation and preserve only the corrected PM verdict.
Allowed next action: open M-001-RQ-022-DOCUMENTATION as the next controlled Codex task.
Forbidden next action: do not define formula candidates, final formula, formula syntax, weights, coefficients, scalar score, total score, ranking, leaderboard, incentives, tokens, payout, economic allocation, API, database, dashboard or implementation.
Commit allowed: yes, if only AGENT_OUTPUTS.md, PM_REVIEW.md and AGENT_QUEUE.md are staged.

## PM-PREP-RQ-022-INNOVATOR

Related task: M-001-RQ-022-INNOVATOR
Decision: PREPARED
Reason: RQ-021 / PD-021 closed the boundary between PoE Reputation object and formula-ready reputation structure. The next required protocol step is to define admissibility constraints for any future reputation formula before formula candidates, weights, scalar score, ranking, incentives, tokens, payout, economic allocation or implementation can be considered.
Allowed Codex actions: register M-001-RQ-022-INNOVATOR in AGENT_QUEUE.md and record this PM preparation note.
Forbidden Codex actions: do not update PROTOCOL_DECISIONS.md, RESEARCH_QUEUE.md, POE_KNOWLEDGE_BASE.md or POE_STATE.md; do not create RQ-022 document; do not define PD-022; do not modify code, API, database, dashboard or `poe.db`.
Next action: user runs Innovator Agent with the M-001-RQ-022-INNOVATOR prompt and returns output to PM for verdict.

## PM-REVIEW-RQ-021-DOCUMENTATION

Related task: M-001-RQ-021-DOCUMENTATION
Reviewed output: PM documentation instruction for RQ-021 / PD-021
Decision: ACCEPTED
Reason: RQ-021 passed Innovator stress-test after stale-state correction and can be documented as the boundary between PoE Reputation object and future reputation formula.
Required changes: Document formula-ready reputation structure as non-economic, non-numeric and non-ordering readiness layer.
Allowed Codex actions: update `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`, `POE_STATE.md`, `AGENT_QUEUE.md`, `PM_REVIEW.md` and create `RQ-021_REPUTATION_FORMULA_READINESS_BOUNDARY.md`.
Forbidden Codex actions: code, API, database, `poe.db`, Python files, dashboard, final formula, weights, coefficients, scalar score, ranking, leaderboard, incentives, tokens, payout, economic allocation.
Commit allowed: yes, if only authorized Markdown files are staged.
Next action: PM verifies commit and decides next research question.

## PM-REVIEW-RQ-021-INNOVATOR-OUTPUT

Related task: M-001-RQ-021-INNOVATOR
Reviewed output: Innovator Agent output for RQ-021 reputation formula readiness boundary
Original agent verdict: POSTPONE
PM verdict: ACCEPT WITH REFINEMENT
Stale-state correction: Agent verdict was based on outdated repository view. Real repository confirms RQ-020 VALIDATED / CLOSED, PD-000 to PD-020 VALIDATED, M-001-RQ-021-INNOVATOR ACTIVE and Implementation BLOCKED.
Reason: The substantive reasoning is valid. Formula-ready reputation structure is useful only as a non-economic, non-numeric and non-ordering readiness layer between PoE Reputation object and future formula.
Accepted content:

* formula-ready reputation structure definition
* boundary distinction between object, formula-ready structure and future formula
* minimum gates
* failure outcomes
* anti-leakage rules
* risks against hidden formula, hidden score, hidden ranking, economic leakage and implementation creep
Required refinement: Documentation must reject the stale POSTPONE recommendation and preserve only the corrected PM verdict.
Allowed next action: open M-001-RQ-021-DOCUMENTATION as the next controlled Codex task.
Forbidden next action: do not define formula, weights, scalar score, ranking, leaderboard, incentives, tokens, payout, economic allocation, API, database, dashboard or implementation.
Commit allowed: yes, if only AGENT_OUTPUTS.md, PM_REVIEW.md and AGENT_QUEUE.md are staged.

## PM-PREP-RQ-021-INNOVATOR

Related task: M-001-RQ-021-INNOVATOR
Decision: PREPARED
Reason: RQ-020 / PD-020 closed the non-economic PoE Reputation object boundary. The next required protocol step is to test the boundary between PoE Reputation object and formula-ready reputation structure before any formula, weights, score, ranking, incentive, token, payout or economic scoring can be considered.
Allowed Codex actions: register `M-001-RQ-021-INNOVATOR` in `AGENT_QUEUE.md` and record this PM preparation note.
Forbidden Codex actions: do not update `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md` or `POE_STATE.md`; do not create `RQ-021` document; do not define `PD-021`; do not modify code, API, database, dashboard or `poe.db`.
Next action: user runs Innovator Agent with the `M-001-RQ-021-INNOVATOR` prompt and returns output to PM for verdict.

## PM-REVIEW-RQ-020-DOCUMENTATION

Related task: M-001-RQ-020-DOCUMENTATION
Reviewed output: PM documentation instruction for RQ-020 / PD-020
Decision: ACCEPTED
Reason: RQ-020 has passed Innovator stress-test with PM correction and can be documented as the non-economic PoE Reputation object boundary before future formula, ranking or incentive.
Required changes: Document RQ-020 / PD-020 without formula, ranking, incentives, tokens, economic scoring or implementation.
Allowed Codex actions: update `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`, `POE_STATE.md`, `AGENT_QUEUE.md`, `PM_REVIEW.md` and create `RQ-020_POE_REPUTATION_OBJECT_BOUNDARY.md`.
Forbidden Codex actions: code, API, database, `poe.db`, Python files, dashboard, final formula, ranking, incentives, tokens.
Commit allowed: yes, if only authorized Markdown files are staged.
Next action: PM verifies commit and decides next research question.

## PM-REVIEW-RQ-020-INNOVATOR-OUTPUT

Related task: M-001-RQ-020-INNOVATOR
Reviewed output: OUTPUT-RQ-020-INNOVATOR-001
Decision: ACCEPTED WITH CHANGES
Reason: Innovator analysis is protocol-useful and correctly identifies the PoE Reputation object boundary, but its formal verdict was based on stale repository state claiming PD-017, PD-018 and PD-019 were not consolidated. Current repository state confirms RQ-019 and PD-019 are validated.
Required changes: Replace final verdict "RQ-020 NEEDS REFINEMENT" with "RQ-020 READY FOR PM REVIEW". Preserve minimal object components, separation rules, comparability rule, conflict representation, partial/capped/conditional representation, staleness representation, failure outcomes and anti-leakage rule.
Allowed Codex actions: update `AGENT_OUTPUTS.md`, `PM_REVIEW.md` and `AGENT_QUEUE.md` only.
Forbidden Codex actions: code, API, database, `poe.db`, `POE_STATE.md`, protocol decisions, RQ files, `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`.
Commit allowed: yes, if only `AGENT_OUTPUTS.md`, `PM_REVIEW.md` and `AGENT_QUEUE.md` are staged.
Next action: open documentation task for formal RQ-020 / candidate PD-020.

## PM-REVIEW-RQ-020-INNOVATOR

Related task: M-001-RQ-020-INNOVATOR
Reviewed output: PM task definition before Innovator Agent execution
Decision: ACCEPTED
Reason: after PD-019, the next logical protocol risk is defining what PoE Reputation is as an object before any formula, ranking, incentive, token or economic score exists.
Required changes: none before Innovator prompt generation.
Allowed Codex actions: update `AGENT_QUEUE.md` and `PM_REVIEW.md` only.
Forbidden Codex actions: code, API, database, `poe.db`, protocol decisions, RQ files, `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`, `POE_STATE.md`.
Commit allowed: yes, if only `AGENT_QUEUE.md` and `PM_REVIEW.md` are staged.
Next action: PM prepares Innovator Agent prompt for RQ-020.

## PM-REVIEW-RQ-019-DOCUMENTATION

Related task: M-001-RQ-019-DOCUMENTATION
Reviewed output: PM documentation instruction for RQ-019 / PD-019
Decision: ACCEPTED
Reason: RQ-019 has passed Innovator stress-test with PM correction and can be documented as non-economic readiness boundary before future reputation.
Required changes: Document RQ-019 / PD-019 without formula, ranking, incentives, tokens, economic scoring or implementation.
Allowed Codex actions: update `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`, `POE_STATE.md`, `AGENT_QUEUE.md`, `PM_REVIEW.md` and create `RQ-019_REPUTATION_READINESS_BOUNDARY.md`.
Forbidden Codex actions: code, API, database, `poe.db`, Python files, dashboard, final formula, ranking, incentives, tokens.
Commit allowed: yes, if only authorized Markdown files are staged.
Next action: PM verifies commit and decides next research question.

## PM-REVIEW-RQ-019-INNOVATOR-OUTPUT

Related task: M-001-RQ-019-INNOVATOR
Reviewed output: OUTPUT-RQ-019-INNOVATOR-001
Decision: ACCEPTED WITH CHANGES
Reason: Innovator analysis is protocol-useful and correctly identifies readiness risks, but its formal verdict was based on stale repository state claiming PD-018 was not consolidated. Current repository state confirms RQ-018 and PD-018 are validated.
Required changes: Replace final verdict "RQ-019 NEEDS REFINEMENT" with "RQ-019 READY FOR PM REVIEW". Preserve readiness gates, separation rules, partial/conditional/capped readiness rules, conflict rules, staleness/expiry rules, failure outcomes and anti-reputation leakage rule.
Allowed Codex actions: update `AGENT_OUTPUTS.md`, `PM_REVIEW.md` and `AGENT_QUEUE.md` only.
Forbidden Codex actions: code, API, database, `poe.db`, `POE_STATE.md`, protocol decisions, RQ files, `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`.
Commit allowed: yes, if only `AGENT_OUTPUTS.md`, `PM_REVIEW.md` and `AGENT_QUEUE.md` are staged.
Next action: open documentation task for formal RQ-019 / candidate PD-019.

## PM-REVIEW-RQ-019-INNOVATOR

Related task: M-001-RQ-019-INNOVATOR
Reviewed output: PM task definition before Innovator Agent execution
Decision: ACCEPTED
Reason: after PD-018, the next logical protocol risk is determining when aggregated reputation evidence is mature enough to inform future reputation without collapsing into final reputation, ranking, incentive or economic score.
Required changes: none before Innovator prompt generation.
Allowed Codex actions: update `AGENT_QUEUE.md` and `PM_REVIEW.md` only.
Forbidden Codex actions: code, API, database, `poe.db`, protocol decisions, RQ files, `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`, `POE_STATE.md`.
Commit allowed: yes, if only `AGENT_QUEUE.md` and `PM_REVIEW.md` are staged.
Next action: PM prepares Innovator Agent prompt for RQ-019.

## PM-REVIEW-RQ-018-DOCUMENTATION

Related task: M-001-RQ-018-DOCUMENTATION
Reviewed output: PM documentation instruction for RQ-018 / PD-018
Decision: ACCEPTED
Reason: RQ-018 has passed Innovator stress-test with PM correction and can be documented as non-economic aggregation boundary layer.
Required changes: Document RQ-018 / PD-018 without formula, ranking, incentives, tokens, economic scoring or implementation.
Allowed Codex actions: update `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`, `POE_STATE.md`, `AGENT_QUEUE.md`, `PM_REVIEW.md` and create `RQ-018_REPUTATION_EVIDENCE_AGGREGATION_BOUNDARIES.md`.
Forbidden Codex actions: code, API, database, `poe.db`, Python files, dashboard, final formula, ranking, incentives, tokens.
Commit allowed: yes, if only authorized Markdown files are staged.
Next action: PM verifies commit and decides next research question.

## PM-REVIEW-RQ-018-INNOVATOR-OUTPUT

Related task: M-001-RQ-018-INNOVATOR
Reviewed output: OUTPUT-RQ-018-INNOVATOR-001
Decision: ACCEPTED WITH CHANGES
Reason: Innovator analysis is protocol-useful and correctly identifies aggregation risks, but its formal verdict was based on stale repository state claiming PD-017 was not consolidated. Current repository state confirms RQ-017 and PD-017 are validated.
Required changes: Replace final verdict "RQ-018 NEEDS REFINEMENT" with "RQ-018 READY FOR PM REVIEW". Preserve aggregation gates, separation rules, conflict rules, duplication/correlation rules, failure outcomes and anti-formula rule.
Allowed Codex actions: update `AGENT_OUTPUTS.md`, `PM_REVIEW.md` and `AGENT_QUEUE.md` only.
Forbidden Codex actions: code, API, database, `poe.db`, `POE_STATE.md`, protocol decisions, RQ files, `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`.
Commit allowed: yes, if only `AGENT_OUTPUTS.md`, `PM_REVIEW.md` and `AGENT_QUEUE.md` are staged.
Next action: open documentation task for formal RQ-018 / candidate PD-018.

## PM-REVIEW-RQ-018-INNOVATOR

Related task: M-001-RQ-018-INNOVATOR  
Reviewed output: PM task definition before Innovator Agent execution  
Decision: ACCEPTED  
Reason: after PD-017, the next logical protocol risk is aggregation of multiple reputation-eligible recognized values without collapsing into reputation formula, ranking or incentives.  
Required changes: none before Innovator prompt generation.  
Allowed Codex actions: update `AGENT_QUEUE.md` and `PM_REVIEW.md` only.  
Forbidden Codex actions: code, API, database, `poe.db`, protocol decisions, RQ files, `PROTOCOL_DECISIONS.md`, `RESEARCH_QUEUE.md`, `POE_KNOWLEDGE_BASE.md`.  
Commit allowed: yes, if only `AGENT_QUEUE.md` and `PM_REVIEW.md` are staged.  
Next action: PM prepares Innovator Agent prompt for RQ-018.

## PM-REVIEW-WORKFLOW-001

Related task: M-001-WORKFLOW-001  
Decision: ACCEPTED  
Reason: repository already contains `AGENTS.md` but needs formal queue-based workflow to reduce chat dependency.  
Allowed Codex actions: edit `AGENTS.md`, create `WORKFLOW_RUNBOOK.md`, `AGENT_QUEUE.md`, `AGENT_OUTPUTS.md`, `PM_REVIEW.md`, update `POE_STATE.md` next action only.  
Forbidden Codex actions: code, API, database, `poe.db`, protocol decisions, RQ files.  
Commit allowed: yes, if only Markdown workflow files are staged.

## Review template

## REVIEW-ID

Related task:  
Reviewed output:  
Decision:

* ACCEPTED
* ACCEPTED WITH CHANGES
* REJECTED
* POSTPONED
Reason:  
Required changes:  
Allowed Codex actions:  
Forbidden Codex actions:  
Commit allowed:  
Next action:
