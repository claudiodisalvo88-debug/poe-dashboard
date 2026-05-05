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
