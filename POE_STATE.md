# POE_STATE.md
Ultimo aggiornamento: 30 aprile 2026

## Ruolo del file
Questo file è la fonte unica di verità tecnica del progetto Proof of Energy.
Prima di modificare codice, leggere questo file.
Dopo ogni modifica importante, aggiornare questo file.

---

## Architettura reale attuale

Il progetto attuale NON usa più il CSV come sorgente live principale.

Architettura reale:

live_data.py → poe.db → db.py → services.py → api.py → dashboard.py

Il file poe_data.csv esiste ancora, ma va considerato archivio storico/vecchio, non fonte live principale.

---

## Cartella progetto attiva

/Users/franco/Desktop/POE_MASTER/poe_progetto

---

## File attivi principali

- live_data.py
- db.py
- services.py
- schemas.py
- api.py
- dashboard.py
- poe.db
- requirements.txt
- Procfile

---

## Stato live_data.py

live_data.py genera dati continui e li scrive nel database SQLite poe.db.

Segnale atteso nel terminale:

LIVE DB START
write DB
write DB
write DB

Verifica DB:

python3 -c "from db import read_data; print(len(read_data()))"

Se il numero cresce, live_data.py sta funzionando.

---

## Stato DB

Database attivo:

poe.db

Nota:
poe_test.db esiste ma non deve essere considerato sorgente principale.
poe_data.csv esiste ma non deve essere considerato sorgente live.

---

## Stato API locale

Backend FastAPI locale:

http://127.0.0.1:8000

Endpoint vecchi già presenti:

- /health
- /nodes
- /summary
- /reputation
- /ingest

Endpoint target nuovi da standardizzare:

- /health
- /live
- /history
- /kpi
- /ranking
- /ingest

Test API:

curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/kpi
curl http://127.0.0.1:8000/ranking

Problema riscontrato:
in alcuni test API restava ferma a records = 910 mentre il DB cresceva oltre 1600 record.
Possibile causa: processo uvicorn vecchio, porta 8000 sporca, API lanciata da cartella sbagliata o versione backend non allineata.

---

## Stato dashboard.py

Dashboard Streamlit locale:

streamlit run dashboard.py

URL locale:

http://localhost:8501

Modifiche già fatte su dashboard.py:

- rimossa cache principale @st.cache_data(ttl=20)
- auto refresh impostato a True
- endpoint cambiati:
  - /nodes → /history
  - /reputation → /ranking
  - aggiunto /kpi
- KPI letti da API:
  - total_energy = kpi["total_energy"]
  - avg_power = kpi["avg_power"]
  - node_count = kpi["nodes"]
  - record_count = kpi["records"]

Problema attuale:
dashboard risulta statica perché API locale /kpi non vedeva i record aggiornati.

Conclusione:
prima di toccare dashboard.py, risolvere allineamento API ↔ DB.

---

## Stato Render

Da verificare.

Possibile backend Render creato/preparato in sessione precedente, ma URL non ancora registrato in questo file.

Cose da recuperare:

- URL Render backend
- nome servizio Render
- start command
- branch GitHub collegato
- variabili ambiente
- endpoint online funzionanti

Quando recuperato, aggiungere qui:

RENDER_BACKEND_URL = inserire URL

---

## Stato GitHub

Repository noto:

poe-dashboard

Da verificare:

- remote origin
- branch attivo
- ultimo commit
- file effettivamente pushati

Comandi utili:

git remote -v
git branch
git status
git log --oneline -5

---

## Procedura terminali standard

Usare sempre questi nomi:

Terminale A = LIVE DATA

cd ~/Desktop/POE_MASTER/poe_progetto
python3 live_data.py

Terminale B = API

cd ~/Desktop/POE_MASTER/poe_progetto
uvicorn api:app --reload

Terminale C = DASHBOARD

cd ~/Desktop/POE_MASTER/poe_progetto
streamlit run dashboard.py

Terminale D = TEST

curl http://127.0.0.1:8000/kpi

---

## Regola anti-confusione

Non cambiare codice se prima non sono verificati:

1. cartella corretta
2. DB che cresce
3. API che legge lo stesso DB
4. dashboard che legge la stessa API

---

## Prossimo step tecnico corretto

1. Chiudere tutti i processi uvicorn/streamlit/live_data.
2. Avviare solo live_data.py.
3. Verificare che il DB cresca con:

python3 -c "from db import read_data; print(len(read_data()))"

4. Avviare solo api.py con uvicorn dalla cartella corretta.
5. Verificare che:

curl http://127.0.0.1:8000/kpi

mostri records uguale o vicino al numero letto direttamente dal DB.

6. Solo dopo aprire dashboard.py.

---

## Stato strategico

Priorità assoluta:
blindare flusso dati live_data.py → poe.db → api.py → dashboard.py.

Non migliorare grafica finché API e DB non sono allineati.


---

## FIX CRITICO 30 APRILE 2026 ORE 15:40

Problema risolto:
API mostrava records fermi a ~910 mentre il DB superava 2000 record.

Causa:
services.py usava pd.to_datetime senza format="mixed", quindi scartava molti timestamp validi.

Fix applicato:
pd.to_datetime(df["timestamp"], errors="coerce", format="mixed")

Stato verificato:
DB > 2080 record
API /kpi > 2090 record
Dashboard live sincronizzata.

Flusso backend locale stabile.


---

## RENDER BACKEND VERIFICATO 30 APRILE 2026 ORE 15:55

RENDER_BACKEND_URL = https://poe-backend-roqn.onrender.com

Servizio Render:
poe-backend

Repo collegata:
claudiodisalvo88-debug/poe-dashboard

Branch:
main

Commit deployato:
c6b0e6a Fix API DB sync and document PoE state

Endpoint online verificati:
- /health
- /
- /live
- /history
- /kpi
- /ranking

Nota:
Render risponde con version 1.1.0 anche se il codice locale è 1.2.0.
Probabile variabile ambiente POE_APP_VERSION=1.1.0 su Render.
Non blocca il funzionamento.


---

## DEMO CLOUD COMPLETA VERIFICATA 30 APRILE 2026 ORE 16:05

Flusso cloud verificato:

multi_node_sender.py → Render backend → dashboard Streamlit

Comando sender verso Render:

POE_API_URL=https://poe-backend-roqn.onrender.com python3 multi_node_sender.py

Comando dashboard collegata a Render:

POE_API_URL=https://poe-backend-roqn.onrender.com streamlit run dashboard.py

Esito:
Dashboard aggiornata correttamente con dati provenienti dal backend Render.

Stato:
Demo cloud PoE funzionante.


--------------------------------------------------
AGGIORNAMENTO 30 APRILE 2026 ORE 16:50
--------------------------------------------------

STATO MVP CLOUD VERIFICATO:

1. Backend FastAPI online su Render funzionante:
https://poe-backend-roqn.onrender.com

Endpoint verificati:
- /health
- /live
- /history
- /kpi
- /ranking
- /ingest

2. Dashboard pubblica Streamlit Cloud funzionante:
https://poe-dashboard.streamlit.app

Fix eseguiti:
- compatibilità Python/Streamlit cloud
- rimossi tutti i parametri width="stretch"
- sostituiti con use_container_width=True

3. Dashboard ora legge correttamente backend Render.

4. Numeri KPI/ranking crescono SOLO se è attivo localmente:

POE_API_URL=https://poe-backend-roqn.onrender.com python3 multi_node_sender.py

Questo significa:

ATTUALE ARCHITETTURA = SENDER ANCORA LOCALE

Mac locale --> Render backend --> Streamlit cloud

5. PROSSIMO STEP CRITICO:
portare anche il generatore dati in cloud h24
per rendere PoE completamente autonomo senza terminali accesi.

NOTE OPERATIVE:
ogni futura sessione tecnica deve iniziare SEMPRE leggendo POE_STATE.md
prima di toccare codice o terminali.

---

## AGGIORNAMENTO 30 APRILE 2026 ORE 18:40

STATO CLOUD AUTONOMO MVP:

Problema iniziale:
il generatore dati era ancora locale tramite:

POE_API_URL=https://poe-backend-roqn.onrender.com python3 multi_node_sender.py

Questo rendeva la demo dipendente dal Mac acceso.

Tentativo scartato:
Render Background Worker.

Motivo:
il Worker risultava a pagamento nella dashboard Render, quindi non è stato usato.

Soluzione applicata:
aggiunto generatore dati interno al backend FastAPI.

File creato:
- internal_generator.py

File modificato:
- api.py

Logica:
api.py avvia FastAPI e, tramite startup event, chiama:

start_internal_generator()

Il generatore interno:
- parte solo se POE_ENABLE_INTERNAL_GENERATOR=true
- genera NODE_01, NODE_02, NODE_03
- scrive nel database usando la stessa funzione di /ingest:
  ingest_node_data(payload)
- intervallo controllato da:
  POE_INTERNAL_SEND_INTERVAL_SECONDS

Variabili ambiente Render backend:
- POE_ENABLE_INTERNAL_GENERATOR=true
- POE_INTERNAL_SEND_INTERVAL_SECONDS=5

Test locale verificato:
curl http://127.0.0.1:8000/kpi

records cresciuti da:
1039

a:
1045

Conclusione:
internal_generator.py funziona localmente.

Commit GitHub pushato:
8990091 Add internal data generator for backend demo

Stato Git:
working tree clean

Stato Render:
variabili ambiente inserite su servizio poe-backend.
Deploy eseguito.
Verifica utente: tutto ok.

ARCHITETTURA ATTUALE AGGIORNATA:

Render backend FastAPI
    ├── API endpoints
    ├── internal_generator.py
    ├── poe.db
    ↓
Streamlit Cloud dashboard

Non serve più tenere acceso il Mac per generare dati demo.

ATTENZIONE:
Render free instance può andare in sleep per inattività.
Al primo accesso può avere ritardo di circa 50 secondi o più.
Questo non blocca la demo, ma va ricordato in presentazione.

PROSSIMO STEP CONSIGLIATO:
verificare domani dashboard pubblica e KPI dopo backend sleep/wake.
Poi aggiornare documentazione demo e preparare versione pitch/bando.


---

## AGGIORNAMENTO 30 APRILE 2026 ORE 18:40

STATO CLOUD AUTONOMO MVP:

Problema iniziale:
il generatore dati era ancora locale tramite:

POE_API_URL=https://poe-backend-roqn.onrender.com python3 multi_node_sender.py

Questo rendeva la demo dipendente dal Mac acceso.

Tentativo scartato:
Render Background Worker.

Motivo:
il Worker risultava a pagamento nella dashboard Render, quindi non è stato usato.

Soluzione applicata:
aggiunto generatore dati interno al backend FastAPI.

File creato:
- internal_generator.py

File modificato:
- api.py

Logica:
api.py avvia FastAPI e, tramite startup event, chiama:

start_internal_generator()

Il generatore interno:
- parte solo se POE_ENABLE_INTERNAL_GENERATOR=true
- genera NODE_01, NODE_02, NODE_03
- scrive nel database usando la stessa funzione di /ingest:
  ingest_node_data(payload)
- intervallo controllato da:
  POE_INTERNAL_SEND_INTERVAL_SECONDS

Variabili ambiente Render backend:
- POE_ENABLE_INTERNAL_GENERATOR=true
- POE_INTERNAL_SEND_INTERVAL_SECONDS=5

Test locale verificato:
curl http://127.0.0.1:8000/kpi

records cresciuti da:
1039

a:
1045

Conclusione:
internal_generator.py funziona localmente.

Commit GitHub pushato:
8990091 Add internal data generator for backend demo

Stato Git:
working tree clean

Stato Render:
variabili ambiente inserite su servizio poe-backend.
Deploy eseguito.
Verifica utente: tutto ok.

ARCHITETTURA ATTUALE AGGIORNATA:

Render backend FastAPI
    ├── API endpoints
    ├── internal_generator.py
    ├── poe.db
    ↓
Streamlit Cloud dashboard

Non serve più tenere acceso il Mac per generare dati demo.

ATTENZIONE:
Render free instance può andare in sleep per inattività.
Al primo accesso può avere ritardo di circa 50 secondi o più.
Questo non blocca la demo, ma va ricordato in presentazione.

PROSSIMO STEP CONSIGLIATO:
verificare domani dashboard pubblica e KPI dopo backend sleep/wake.
Poi aggiornare documentazione demo e preparare versione pitch/bando.

---

## AGGIORNAMENTO 2 MAGGIO 2026

STATO BACKEND CLOUD DOPO VERIFICA:

Backend Render attivo:

https://poe-backend-roqn.onrender.com

Dashboard pubblica attiva:

https://poe-dashboard.streamlit.app

Verifica effettuata:
- backend online
- internal_generator attivo su Render
- log Render mostrano `[INTERNAL OK]` per NODE_01, NODE_02, NODE_03
- `/kpi` cresce correttamente
- `/history?limit=5` restituisce correttamente solo 5 record
- database Render cresce senza Mac acceso

Problema riscontrato:
`/live` e `/history` inizialmente davano errore o restituivano storico troppo lungo/non leggibile.

Cause tecniche:
- `/history` restituiva tutto lo storico senza limite
- `/live` tentava confronti su timestamp con formati diversi
- il fix con parsing timestamp/timezone ha causato ancora errori su Render
- soluzione finale: evitare confronto timestamp e usare l’ordine naturale dei record letti dal DB

Fix finale applicato su `api.py`:
- rimossa logica `_parse_timestamp`
- rimossa logica `row_time`
- aggiunte funzioni:
  - `clean_value(value)`
  - `clean_row(row)`
- `/history` ora accetta:
  - `limit: int = 100`
- `/history?limit=5` verificato funzionante
- `/live` ora usa ultimo record disponibile per ogni nodo senza confrontare timestamp

Commit/fix logico:
stabilizzazione endpoint live/history senza ordinamento timestamp.

STATO ATTUALE BACKEND:

- `/health` = ok
- `/kpi` = ok e crescente
- `/history?limit=5` = ok
- `/ranking` = ok
- `/ingest` = ok
- `/live` = da verificare dopo ultimo deploy se restituisce 3 record NODE_01, NODE_02, NODE_03

ARCHITETTURA ATTUALE CONFERMATA:

Render backend FastAPI
    ├── internal_generator.py attivo
    ├── poe.db in crescita
    ├── /kpi funzionante
    ├── /history limitato funzionante
    └── /live stabilizzato lato codice

Streamlit Cloud dashboard
    ↓
https://poe-dashboard.streamlit.app

NOTA OPERATIVA:
Non serve più tenere acceso il Mac per generare dati demo.
Il generatore interno Render produce dati autonomamente.

ATTENZIONE:
Render free instance può andare in sleep.
Al primo accesso può servire attendere il risveglio backend.

PROSSIMO STEP:
1. Verificare definitivamente `/live?t=4001`.
2. Verificare dashboard pubblica dopo fix backend.
3. Se tutto è ok, passare alla documentazione demo.
4. Preparare materiale pitch/bando.
5. Non fare refactor o grafica finché il flusso demo non è marcato stabile.
---

## AGGIORNAMENTO 2 MAGGIO 2026 — VERIFICA DASHBOARD PUBBLICA

Dashboard pubblica verificata:

https://poe-dashboard.streamlit.app

Esito verifica:
- dashboard si apre correttamente
- nessun errore rosso visibile
- sidebar funzionante
- auto refresh attivo
- backend collegato a:
  https://poe-backend-roqn.onrender.com
- KPI visibili:
  - energia totale
  - potenza media
  - nodi attivi
  - ultimo update
- stato sistema visibile:
  - Health backend = HEALTHY
  - Qualità rete = STABILE
  - Top node visibile
  - record raccolti visibili
- grafici visibili:
  - andamento potenza nel tempo
  - energia per nodo
- sezioni operative visibili:
  - Trend rete
  - Ranking nodi
  - Dataset

STATO FINALE MVP CLOUD:

Proof of Energy MVP cloud verificato end-to-end.

Flusso confermato:

internal_generator.py su Render
    ↓
poe.db su backend Render
    ↓
API FastAPI Render
    ↓
Dashboard Streamlit Cloud pubblica

Conclusione:
Il Mac locale non è più necessario per generare dati demo.
La dashboard pubblica legge dati dal backend Render.
Il backend genera dati autonomamente tramite internal_generator.py.

STATO PROGETTO:
MVP cloud demo pronto per documentazione, pitch e bando.

PROSSIMO STEP:
preparare documentazione demo, executive summary e materiale bando.