# DECISIONS.md

## Ruolo
Registro delle decisioni tecniche e strategiche PoE.

---

## Decisioni principali

### 1. SQLite come sorgente live MVP
Decisione:
PoE non usa più CSV come fonte live principale.

Stato:
Confermata.

Motivo:
SQLite è più stabile per API, dashboard e storico dati.

---

### 2. CSV solo archivio legacy
Decisione:
poe_data.csv resta solo come archivio storico/vecchio.

Stato:
Confermata.

---

### 3. Backend cloud su Render
Decisione:
Il backend FastAPI è pubblicato su Render.

URL:
https://poe-backend-roqn.onrender.com

Stato:
Confermato e verificato.

---

### 4. Dashboard cloud su Streamlit
Decisione:
La dashboard pubblica è pubblicata su Streamlit Cloud.

URL:
https://poe-dashboard.streamlit.app

Stato:
Confermato e verificato.

---

### 5. Generatore interno nel backend
Decisione:
Usare internal_generator.py dentro FastAPI invece di tenere multi_node_sender.py acceso sul Mac.

Stato:
Confermata.

Motivo:
la demo non deve dipendere dal Mac acceso.

---

### 6. Render Background Worker scartato
Decisione:
Non usare Render Background Worker.

Motivo:
risultava a pagamento.

---

### 7. POE_STATE.md deve diventare indice sintetico
Decisione:
POE_STATE.md non deve crescere all'infinito.

Nuova struttura:
- POE_STATE.md = stato attuale + indice
- TASKS.md = task operative
- DECISIONS.md = decisioni
- ERRORS.md = errori
- CHANGELOG.md = cronologia modifiche
- ARCHITECTURE.md = architettura tecnica
- BANDO.md = parte documentale/bando
