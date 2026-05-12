# DATA_MODEL.md

## Ruolo del file

Questo file definisce il modello dati operativo del progetto Proof of Energy.

Serve a mantenere coerenti:

- dati ricevuti dai nodi
- endpoint API
- database
- KPI
- Energy Reputation
- dashboard
- task Codex

Fonte principale:
POE_STATE.md

---

## Modello dati MVP attuale

Il backend PoE riceve dati energetici tramite endpoint `/ingest`.

Dati minimi attuali:

```json
{
  "node_id": "REAL_NODE_01",
  "voltage": 230.0,
  "ampere": 0.40,
  "watt": 92.0,
  "energy_wh": 12.5
}
