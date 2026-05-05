# TASKS.md

## Ruolo
Lista operativa delle task PoE.
Questo file serve per sapere cosa fare, cosa è in corso e cosa è completato.

---

## PRIORITÀ ATTUALE

### TASK 1 — Verifica MVP cloud
Stato: COMPLETATA

Verificato il 5 maggio 2026:
- backend Render attivo
- dashboard Streamlit attiva
- internal generator attivo
- endpoint /health, /kpi, /live, /history?limit=5, /ranking funzionanti
- records backend: 46189 al momento della verifica

---

### TASK 2 — Creare memoria modulare PoE
Stato: IN CORSO

File da creare:
- TASKS.md
- DECISIONS.md
- ERRORS.md
- CHANGELOG.md
- ARCHITECTURE.md
- BANDO.md

Obiettivo:
ridurre POE_STATE.md a file indice/stato sintetico e spostare i dettagli nei file modulari.

---

### TASK 3 — Pulire POE_STATE.md
Stato: DA FARE

Azioni:
- rimuovere duplicati
- mantenere solo stato attuale
- collegare i file modulari
- non cancellare informazioni importanti senza prima spostarle nei moduli

---

### TASK 4 — Documentazione demo
Stato: DA FARE

Azioni:
- scrivere descrizione demo cloud
- spiegare architettura MVP
- preparare testo per bando/pitch
- indicare limite Render free sleep/wake

---

### TASK 5 — Installare strumenti AI locali
Stato: DA FARE

Ordine:
1. LM Studio
2. Ollama
3. OpenCode

Obiettivo:
costruire PoE Operating System con agenti locali e memoria operativa.


---

## Aggiornamento 5 maggio 2026 - strumenti AI locali

Stato strumenti AI locali su Mac Intel:

- LM Studio: scartato perché su macOS richiede Apple Silicon.
- Ollama: installato e funzionante.
- Modelli disponibili:
  - qwen2.5-coder:1.5b
  - llama3.2:1b
- Modello operativo principale:
  - qwen2.5-coder:1.5b
- OpenCode: scartato su Mac Intel.
  - script ufficiale installato ma fallisce con:
    zsh: illegal hardware instruction
  - installazione via npm completata, ma opencode --version fallisce con lo stesso errore.

Decisione operativa:
non perdere altro tempo su OpenCode nel Mac Intel.
Riprovare OpenCode solo su Dell/Linux dopo upgrade SSD.

Priorità successiva:
passare alla documentazione demo/bando senza modificare codice, deploy o dashboard.
