# CHANGELOG.md

## Ruolo
Cronologia sintetica modifiche PoE.

---

## 30 aprile 2026

### Fix API/DB
- risolto problema records fermi su API
- aggiunto format="mixed" nel parsing timestamp
- verificato DB > 2080 record
- verificato API /kpi sincronizzata

### Render backend
- backend FastAPI pubblicato su Render
- URL:
  https://poe-backend-roqn.onrender.com
- endpoint verificati:
  - /health
  - /
  - /live
  - /history
  - /kpi
  - /ranking

### Dashboard cloud
- dashboard pubblica Streamlit verificata
- URL:
  https://poe-dashboard.streamlit.app
- rimossi problemi compatibilità width="stretch"
- usato use_container_width=True

### Internal generator
- creato internal_generator.py
- modificato api.py per avviare generatore interno
- aggiunte variabili:
  - POE_ENABLE_INTERNAL_GENERATOR=true
  - POE_INTERNAL_SEND_INTERVAL_SECONDS=5
- commit pushato:
  8990091 Add internal data generator for backend demo

---

## 2 maggio 2026

### Backend cloud autonomo
- verificato backend Render attivo
- verificato internal_generator attivo
- log Render con [INTERNAL OK]
- verificato /kpi crescente
- verificato /history?limit=5

### Fix endpoint
- stabilizzato /history con limit
- stabilizzato /live evitando confronto timestamp
- aggiunte funzioni clean_value e clean_row

### Dashboard pubblica
- verificata dashboard pubblica end-to-end
- nessun errore rosso visibile
- KPI visibili
- grafici visibili
- ranking visibile
- dataset visibile

### Documenti bando
- rigenerati documenti .docx validi
- creati/aggiornati:
  - executive_summary.docx
  - descrizione_progetto_bando.docx
  - business_model.docx
  - pitch_deck_testi.docx

---

## 5 maggio 2026

### Verifica cloud
- backend Render verificato da terminale
- dashboard Streamlit verificata da browser
- /health ok
- /kpi ok
- /live ok con NODE_01, NODE_02, NODE_03
- /history?limit=5 ok
- /ranking ok
- records verificati: 46189
