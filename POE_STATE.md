# POE_STATE.md

Ultimo aggiornamento: 5 maggio 2026

## Ruolo del file

Questo file è la fonte di ingresso del progetto Proof of Energy.
Prima di modificare codice, terminali, deploy o dashboard, leggere sempre questo file.

POE_STATE.md deve restare sintetico.
I dettagli operativi sono nei file modulari:

- TASKS.md
- DECISIONS.md
- ERRORS.md
- CHANGELOG.md
- ARCHITECTURE.md
- BANDO.md

---

## Stato attuale MVP cloud

Stato:
MVP cloud demo stabile e verificato.

Backend Render:
https://poe-backend-roqn.onrender.com

Dashboard Streamlit:
https://poe-dashboard.streamlit.app

Data ultima verifica:
5 maggio 2026

Verifica backend effettuata:
- /health = ok
- /kpi = ok
- /live = ok
- /history?limit=5 = ok
- /ranking = ok

Record verificati al momento del test:
46189

Nodi attivi:
- NODE_01
- NODE_02
- NODE_03

Dashboard pubblica:
verificata ok da browser.

---

## Architettura attuale

Render backend FastAPI
    ├── api.py
    ├── internal_generator.py
    ├── poe.db
    ├── endpoints API
    ↓
Streamlit Cloud dashboard

Il generatore interno cloud è attivo.
Il Mac locale non è necessario per generare dati demo.

Dettagli architettura:
vedi ARCHITECTURE.md

---

## Regola tecnica principale

Non toccare codice se prima non sono verificati:

1. stato progetto
2. backend cloud
3. dashboard pubblica
4. Git status
5. task esatta da fare

---

## File modulari

TASKS.md:
task operative e priorità.

DECISIONS.md:
decisioni tecniche e strategiche.

ERRORS.md:
errori, cause e fix.

CHANGELOG.md:
cronologia modifiche.

ARCHITECTURE.md:
architettura tecnica.

BANDO.md:
documentazione bando, pitch e materiali istituzionali.

---

## Prossima priorità

TASK 1:
aggiornare GitHub con i nuovi file modulari e POE_STATE.md pulito.

TASK 2:
passare alla documentazione demo/bando.

TASK 3:
strumenti AI locali chiusi su Mac Intel:
1. LM Studio scartato
2. Ollama installato e funzionante
3. OpenCode scartato su Mac Intel per errore illegal hardware instruction

Prossimo focus:
documentazione demo/bando

---

## Comandi verifica cloud

curl https://poe-backend-roqn.onrender.com/health
curl https://poe-backend-roqn.onrender.com/kpi
curl https://poe-backend-roqn.onrender.com/live
curl "https://poe-backend-roqn.onrender.com/history?limit=5"
curl https://poe-backend-roqn.onrender.com/ranking

---

## Nota Render free

Render free può andare in sleep.
Al primo accesso il backend può impiegare tempo a risvegliarsi.
Questo non blocca la demo, ma va ricordato in presentazione.

---

## Regola madre

STATO → VERIFICA → MEMORIA → STRUMENTI → CODICE

## Aggiornamento — Sistema agenti PoE

Data: 2026-05-05

Creato file AGENTS.md con struttura del PoE Operating System.

Agenti definiti:
- PM Agent
- Tech Agent
- Bando Agent
- Fornitori Agent
- Pitch Agent
- QA/Verifier Agent
- Memory Agent

Regola operativa:
ogni sessione PoE parte da POE_STATE.md e dichiara l'agente attivo.

Per i preventivi bando:
- fornitore competente > fornitore locale
- preventivo tecnico > preventivo generico
- fase 1 concreta > richiesta vaga per bando

Dettagli completi in AGENTS.md.
