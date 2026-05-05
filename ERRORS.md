# ERRORS.md

## Ruolo
Registro errori, cause e soluzioni PoE.

---

## Errore 1 — API ferma a records ~910

Sintomo:
API /kpi mostrava records fermi a circa 910 mentre il database SQLite cresceva oltre 1600/2000 record.

Cause possibili iniziali:
- uvicorn vecchio ancora attivo
- porta 8000 sporca
- API lanciata da cartella sbagliata
- parsing timestamp non corretto

Causa effettiva trovata:
services.py usava pd.to_datetime senza format="mixed", scartando timestamp validi.

Fix:
pd.to_datetime(df["timestamp"], errors="coerce", format="mixed")

Stato:
Risolto.

---

## Errore 2 — Dashboard statica

Sintomo:
Dashboard Streamlit sembrava non aggiornarsi.

Causa:
La dashboard leggeva correttamente l'API, ma l'API non leggeva tutti i record aggiornati dal DB.

Fix:
Risolto allineamento API ↔ DB.

Stato:
Risolto.

---

## Errore 3 — /history troppo lungo

Sintomo:
Endpoint /history restituiva troppo storico, poco leggibile e pesante.

Fix:
Aggiunto parametro limit con default 100.

Esempio:
https://poe-backend-roqn.onrender.com/history?limit=5

Stato:
Risolto.

---

## Errore 4 — /live con timestamp problematici

Sintomo:
Endpoint /live dava errore o problemi con confronto timestamp.

Causa:
Parsing/confronto timestamp con formati diversi e timezone.

Fix:
Eliminato confronto timestamp.
Usato ordine naturale dei record DB e ultimo record disponibile per ogni nodo.

Stato:
Risolto.

---

## Errore 5 — File .docx corrotti

Sintomo:
Documenti Word pesavano circa 14B e davano errore:
BadZipFile: File is not a zip file

Causa:
File creati non erano veri documenti .docx validi.

Fix:
Installato python-docx e rigenerati i documenti.

Stato:
Risolto.


---

## Errore 5 maggio 2026 - OpenCode illegal hardware instruction su Mac Intel

Contesto:
Mac Intel x86_64.

Errore:
zsh: illegal hardware instruction

Quando avviene:
- dopo installazione script ufficiale OpenCode
- dopo installazione npm install -g opencode-ai
- al comando opencode --version

Causa probabile:
incompatibilità del binario/runtime con Mac Intel.

Fix applicato:
nessun fix operativo conveniente.

Decisione:
scartare OpenCode su Mac Intel.
Non bloccare PoE per questo errore.
Rimandare eventuale test a Dell/Linux dopo SSD.
