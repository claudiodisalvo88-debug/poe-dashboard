# POE_OPERATING_LOOP_V1

## 1. Purpose
Far avanzare PoE con task piccoli, repo-grounded e verificabili.

## 2. Source of truth
- GitHub main
- `POE_STATE.md`

## 3. Standard loop
1. Read state.
2. Identify next required step.
3. Check allowed scope.
4. Execute only that step.
5. Update state files.
6. Commit and push.
7. Output a compact report.

## 4. Codex role
- Executor only.
- No autonomous protocol decisions.
- No scope expansion.

## 5. ChatGPT role
- Verifier / PM only.
- No long prompt generation unless required.

## 6. Human CEO role
- Authorizes scope changes.
- Authorizes formula, RQ, PD and implementation work when needed.

## 7. Allowed automatic Codex action
Execute the next required step only if it is already recorded and within current authorization.

## 8. Hard stops
- formula candidate
- RQ / PD action
- implementation
- code / API / database / runtime
- unclear next step
- conflicting state

## 9. Output format
- files read
- files modified
- files created
- commit hash
- push result
- action completed
- next required step

## 10. Next operating rule
ChatGPT should only verify outputs and issue CEO decisions when scope changes are needed.
