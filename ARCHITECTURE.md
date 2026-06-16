# ARCHITECTURE.md

## Ruolo
Descrizione architettura tecnica PoE.

---

## Architettura MVP cloud attuale

Render backend FastAPI
    ├── api.py
    ├── internal_generator.py
    ├── db.py
    ├── services.py
    ├── schemas.py
    ├── poe.db
    ↓
API endpoints
    ├── /health
    ├── /live
    ├── /history
    ├── /kpi
    ├── /ranking
    └── /ingest
    ↓
Streamlit Cloud dashboard
    └── https://poe-dashboard.streamlit.app

---

## Backend

URL:
https://poe-backend-roqn.onrender.com

Servizio:
poe-backend

Repo:
claudiodisalvo88-debug/poe-dashboard

Branch:
main

---

## Dashboard

URL:
https://poe-dashboard.streamlit.app

Funzione:
visualizzare KPI, ranking, grafici e dataset PoE.

---

## Database

Database MVP:
poe.db

Tipo:
SQLite

Uso:
storage dati energetici nodi.

---

## Generatore dati

File:
internal_generator.py

Funzione:
genera dati demo per:
- NODE_01
- NODE_02
- NODE_03

Variabili ambiente:
- POE_ENABLE_INTERNAL_GENERATOR=true
- POE_INTERNAL_SEND_INTERVAL_SECONDS=5

---

## Flusso dati attuale

internal_generator.py su Render
    ↓
ingest_node_data(payload)
    ↓
poe.db
    ↓
services.py
    ↓
api.py
    ↓
dashboard.py su Streamlit Cloud

---

## Stato CSV

poe_data.csv:
solo archivio legacy, non fonte live principale.

---

## Nota Render free

Render free instance può andare in sleep.
Al primo accesso può servire attendere il risveglio backend.
Questo non blocca la demo.

---

## STEP 5C — ARCHITETTURA REALE PoE

Data: 2026-06-16

### Evoluzione architettura

PoE non è più alimentato esclusivamente da generatori simulati.

È stato integrato il primo nodo energetico reale.

Nodo attivo:

REAL_NODE_01_MAIN

Device:

Shelly Pro EM-50

### Architettura attuale

Shelly Pro EM-50
    ↓
shelly_adapter.py
    ↓
edge_collector.py
    ↓
/ingest
    ↓
SQLite
    ↓
KPI
    ↓
Dashboard

### Layer architetturali

Layer 1 — Device

Responsabilità:

- acquisizione dati fisici
- misure energetiche reali

Esempio:

- Shelly Pro EM-50

Layer 2 — Device Adapter

Responsabilità:

- tradurre protocollo dispositivo
- normalizzare dati

Esempio:

- shelly_adapter.py

Layer 3 — Edge Collector

Responsabilità:

- orchestrazione polling
- costruzione payload PoE
- invio a /ingest

Esempio:

- edge_collector.py

Layer 4 — Backend PoE

Responsabilità:

- validazione payload
- persistenza
- KPI
- ranking

Componenti:

- FastAPI
- SQLite

Layer 5 — Presentation

Responsabilità:

- dashboard
- monitoraggio

Componenti:

- Streamlit

### Stato operativo

Modalità:

HYBRID_VALIDATION

Attualmente convivono:

- simulatori
- nodo reale

### Direzione futura

Architettura target:

Multi-device Architecture

Possibili nodi:

- consumption
- production
- storage
- grid

Ogni device deve essere integrato tramite adapter dedicato.

Il backend non deve conoscere dettagli hardware specifici.

### Decisione

Device-specific logic fuori dal backend.

Backend PoE riceve esclusivamente payload normalizzati.
