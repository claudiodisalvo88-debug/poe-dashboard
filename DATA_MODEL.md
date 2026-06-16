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

---

## STEP 5A — DATA MODEL REALE PoE

Data: 2026-06-16

### Stato attuale verificato

Il backend MVP salva attualmente:

- timestamp
- node_id
- watt
- energy_wh

Questo schema resta invariato per ora.

### Limite dello schema attuale

Lo schema attuale è sufficiente per ingest MVP, KPI e dashboard base.

Non è sufficiente, da solo, per rappresentare PoE come sistema energetico reale multi-sorgente.

### Modello logico futuro

Ogni nodo PoE dovrà essere classificato con metadati logici:

- source_type
- measurement_scope
- direction
- confidence
- device_type
- physical_location
- status

### source_type

Valori previsti:

- consumption
- production
- storage
- grid

### direction

Valori previsti:

- import
- export
- charge
- discharge
- neutral

### confidence

Valori previsti:

- real
- simulated
- estimated

### Nodo reale attuale

REAL_NODE_01_MAIN:

- source_type: consumption
- measurement_scope: whole_house
- direction: import
- confidence: real
- device_type: shelly_pro_em_50
- status: active

### Decisione

Non modificare ora lo schema SQLite.

Il modello logico viene documentato prima in DATA_MODEL.md.

Eventuali modifiche DB/API saranno valutate solo dopo validazione stabile del nodo reale.
