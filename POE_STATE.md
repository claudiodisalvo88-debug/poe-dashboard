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


---

## Aggiornamento operativo — 6 maggio 2026

### Stato tecnico

MVP cloud verificato il 6 maggio 2026.

Verifiche effettuate:

- git status: repository pulito e allineato a origin/main
- backend Render /health: ok
- backend Render /kpi: ok

Risultato backend:

- status: healthy
- service: Proof of Energy API
- version: 1.1.0
- nodes: 3
- records verificati: 1033

Nota:
il valore records è diverso dal precedente 46189. Interpretazione operativa: possibile reset/nuova persistenza SQLite su Render free. Non è bloccante per demo, ma conferma che SQLite su Render free non va presentato come storage persistente definitivo.

### Stato fornitori

Primo giro fornitori avviato.

Email inviate: 4

Fornitori contattati:

- Nexeta
- Codebaker
- Astrorei
- Higeco Energy

Stato:

- almeno un ticket / presa in carico ricevuta
- in attesa di risposte tecniche o commerciali
- preventivi reali non ancora ricevuti

Regola confermata:

- fornitore competente > fornitore locale
- preventivo tecnico > preventivo generico
- fase 1 concreta > richiesta vaga per bando

### Documenti bando aggiornati

Aggiornati file operativi in:

`/Users/franco/Desktop/POE_MASTER/documenti_bando/agent_readable`

File aggiornati o creati:

- PREVENTIVI_DA_RICHIEDERE_POE.md
- ALLEGATO_3_SCHEMA_COMPILAZIONE_POE.md
- ALLEGATO_10_COMPILAZIONE_CAMPI_POE.md
- ALLEGATO_5_SCHEMA_DNSH_POE.md
- PIANO_SPESE_POE.md
- PREVISIONI_ECONOMICHE_3_ANNI_POE.md
- DATI_SOCIETA_DA_COSTITUIRE_POE.md
- CHECKLIST_CANDIDATURA_SOCIETA_DA_COSTITUIRE.md

### Allegato 10

Allegato 10 rafforzato.

Sezioni rafforzate:

- RIS3 Molise
- sviluppo sperimentale
- industrializzazione risultati
- soluzioni tecniche innovative
- ampliamento target utenza
- prodotto-servizio innovativo
- bisogni sociali/ambientali
- economia digitale
- criteri definizione costi
- indicatori di risultato

Obiettivo raggiunto:
testi più concreti, collegati a MVP online, transizione energetica, software/cloud/API/dashboard, industrializzazione e indicatori misurabili.

### Piano spese

Piano spese PoE rivisto.

Totale investimento: 90.000 euro.

Ripartizione aggiornata:

- a) Attrezzature tecnologiche: 10.000 euro
- b) Componenti hardware e software: 28.000 euro
- c) Certificazioni / brevetti / know-how: 5.000 euro
- d) Consulenze specialistiche: 19.000 euro
- e) Altri costi di esercizio: 8.000 euro
- f) Personale: 15.000 euro
- g) Costi indiretti: 5.000 euro

Controlli interni:

- base a+b+c: 43.000 euro
- limite consulenze 50%: 21.500 euro
- consulenze previste: 19.000 euro
- limite altri costi 20%: 8.600 euro
- altri costi previsti: 8.000 euro
- costi indiretti previsti: 5.000 euro

Decisione:
aumentato il peso software/hardware e ridotta la voce personale rispetto alla bozza precedente.

### Previsioni economiche

Creato file:

`PREVISIONI_ECONOMICHE_3_ANNI_POE.md`

Sintesi:

- Anno 1: ricavi stimati 7.000 euro, costi stimati 63.000 euro, risultato -56.000 euro
- Anno 2: ricavi stimati 37.000 euro, costi stimati 40.000 euro, risultato -3.000 euro
- Anno 3: ricavi stimati 87.000 euro, costi stimati 56.000 euro, risultato +31.000 euro

Logica:
anno 1 sviluppo/validazione, anno 2 primi clienti, anno 3 scalabilità e margine operativo positivo.

### Dati società da costituire

Creato e aggiornato file:

`DATI_SOCIETA_DA_COSTITUIRE_POE.md`

Ipotesi operative non sensibili:

- società da costituire con Claudio Di Salvo come fondatore/proponente principale
- quota ipotizzata: 100% Claudio Di Salvo, salvo ingresso successivo di soci tecnici/finanziari
- amministratore ipotizzato: Claudio Di Salvo
- capitale sociale ipotizzato: 10.000 euro, da verificare con commercialista/notaio
- sede operativa in Molise: indirizzo da definire
- cofinanziamento: mezzi propri, capitale sociale e/o finanziamento soci da documentare

Restano da compilare offline:

- dati anagrafici
- codice fiscale
- documento identità
- residenza
- PEC
- indirizzo sede
- fonte copertura finanziaria documentabile

### DNSH / Allegato 5

Stato:
Allegato 5 DNSH pronto nella parte descrittiva, ma resta aperto un punto formale.

Bloccante:
numero scheda DNSH ufficiale da indicare nel modulo.

Decisione:
non inserire alcun numero finché non viene trovato il documento ufficiale `Verifica-DNSH_Allegato-Rapporto-Ambientale_PR_21-27` o fonte certa relativa all’Azione 1.1.3.

### Checklist candidatura

Checklist candidatura società da costituire trasformata in checklist operativa con stati:

- FATTO
- PARZIALE
- IN ATTESA
- DA FARE
- BLOCCANTE
- DOPO AMMISSIONE

Bloccanti attuali:

1. numero scheda DNSH ufficiale
2. preventivi reali fornitori
3. PEC da usare
4. sede operativa Molise
5. fonte documentabile del cofinanziamento
6. dati personali/documenti da compilare offline

### BANDO.md

BANDO.md aggiornato e pushato più volte con sintesi di:

- stato fornitori
- criteri valutazione preventivi
- schema Allegato 3
- rafforzamento Allegato 10
- piano spese
- DNSH
- dati società
- previsioni economiche
- checklist finale candidatura

### Prossime priorità

1. Monitorare risposte fornitori.
2. Valutare preventivi reali con schema A/B/C/D.
3. Trovare numero scheda DNSH ufficiale.
4. Definire PEC, sede Molise e fonte cofinanziamento.
5. Rilettura finale Allegato 10.
6. Compilare Allegato 3 con preventivi reali.
7. Preparare zip finale solo dopo controllo completo.

### Regola operativa aggiornata

Per la fase bando, ogni ripresa deve partire da:

1. POE_STATE.md
2. BANDO.md
3. CHECKLIST_CANDIDATURA_SOCIETA_DA_COSTITUIRE.md
4. file operativo specifico della task

Non creare nuovi file se esiste già un file operativo adatto.
Non modificare codice tecnico finché MVP cloud resta stabile.
