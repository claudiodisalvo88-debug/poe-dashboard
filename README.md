# Proof of Energy (PoE) — MVP ufficiale

## Descrizione
Proof of Energy è un MVP per il monitoraggio energetico distribuito con calcolo della Energy Reputation dei nodi.

## Runtime ufficiale
- api.py → backend FastAPI
- db.py → SQLite
- live_data.py → dati live
- dashboard.py → dashboard Streamlit via API

## Avvio
Terminale 1:
uvicorn api:app --reload

Terminale 2:
python3 live_data.py

Terminale 3:
streamlit run dashboard.py

## URL
- http://127.0.0.1:8000/docs
- http://localhost:8501

## Note
- CSV non più usato
- fonte dati: SQLite via API
