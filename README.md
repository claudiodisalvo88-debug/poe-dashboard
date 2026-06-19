# Proof of Energy (PoE)

## What it is

Proof of Energy is an experimental protocol for recognizing verified energy contributions and building Energy Reputation from measurable energy behavior.

PoE works by separating observed behavior, measured reduction, attribution, recognized value and reputation, without prematurely collapsing them into score, ranking, token or incentive logic.

## Current status

* Protocol research active under M-001
* Last closed research: RQ-023
* PD-000 to PD-023 validated
* Implementation blocked for protocol reputation logic
* MVP backend/dashboard exists but is not the full protocol

## Repository structure

* `POE_STATE.md`: operational state
* `POE_PROTOCOL_KERNEL.md`: protocol kernel summary
* `PROTOCOL_DECISIONS.md`: validated protocol decisions
* `RESEARCH_QUEUE.md`: research queue
* `POE_KNOWLEDGE_BASE.md`: consolidated knowledge
* `AGENTS.md`, `WORKFLOW_RUNBOOK.md`, `AGENT_QUEUE.md`, `AGENT_OUTPUTS.md`, `PM_REVIEW.md`: agent workflow files

## Technical MVP

A technical MVP exists with FastAPI, SQLite and Streamlit dashboard.
It is useful as infrastructure, but the protocol reputation layer remains blocked until validated implementation gates.

Relevant runtime files:

* `api.py`
* `db.py`
* `dashboard.py`
* `services.py`

## Current hard blocks

* No formula candidates
* No final formula
* No weights
* No scalar score
* No ranking
* No incentive
* No token
* No payout
* No economic allocation
* No implementation of reputation protocol logic

## Links / local runtime

Technical MVP only, not full protocol execution:

```bash
uvicorn api:app --reload
streamlit run dashboard.py
```

Local URLs:

* `http://127.0.0.1:8000/docs`
* `http://localhost:8501`

Legacy CSV live source is no longer the protocol source.

## Source of truth

For current project state, read `POE_STATE.md` first.
