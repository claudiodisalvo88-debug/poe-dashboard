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
## Task — Shortlist fornitori tecnici PoE

Stato: aperta  
Priorità: alta  
Agente: FORNITORI AGENT

### Obiettivo
Creare una shortlist di fornitori competenti per ottenere preventivi tecnici reali per il bando PoE.

### Contesto
La linea operativa scelta è:

- fornitore competente > fornitore locale
- preventivo tecnico > preventivo generico
- fase 1 concreta > richiesta vaga per bando

Vanno scartati fornitori generici, agenzie WordPress, siti vetrina, landing page e preventivi vaghi.

### Azioni operative
1. Cercare fornitori con competenze in backend/API, IoT, smart meter, cloud, data platform, dashboard KPI ed energy monitoring.
2. Dividere i fornitori per categoria:
   - software/API/data platform
   - IoT/smart meter/nodo fisico
   - energy monitoring/consulenza tecnica
   - cloud/database/sicurezza
3. Verificare che ogni fornitore abbia competenze reali coerenti con PoE.
4. Preparare una tabella con fornitore, competenza, contatto, voce preventivo e stato.
5. Preparare email mirate per ciascuna categoria.
6. Aggiornare PREVENTIVI_DA_RICHIEDERE_POE.md.

### File coinvolti
- AGENTS.md
- TASKS.md
- BANDO.md
- PREVENTIVI_DA_RICHIEDERE_POE.md
- PIANO_SPESE_POE.md

### Output atteso
Tabella con almeno 8 fornitori seri divisi per categoria.

### Criterio di completamento
Almeno 6 fornitori validi selezionati e almeno 3 email tecniche pronte da inviare.
## Task — Richiesta preventivo software/API PoE

Stato: aperta  
Priorità: alta  
Agente: FORNITORI AGENT

### Obiettivo
Ottenere un preventivo tecnico per l’evoluzione software del MVP Proof of Energy.

### Contesto
PoE ha già un MVP funzionante con backend FastAPI, dashboard Streamlit, database e dati energetici simulati/generati. Il preventivo deve riguardare una Fase 1 concreta, non una richiesta generica per bando.

### Azioni operative
1. Selezionare fornitori con competenze in Python, FastAPI, API, database, dashboard e cloud.
2. Inviare email mirata per proposta tecnica/economica.
3. Richiedere descrizione attività, tempi, importo imponibile, IVA, totale, validità offerta e condizioni.
4. Evitare fornitori che propongono solo sito web, landing page o sviluppo WordPress.
5. Valutare il preventivo ricevuto e mapparlo nel piano spese.

### File coinvolti
- PREVENTIVI_DA_RICHIEDERE_POE.md
- PIANO_SPESE_POE.md
- BANDO.md
- ALLEGATO_3_SCHEMA_COMPILAZIONE_POE.md

### Output atteso
Preventivo software/API per evoluzione backend, database, dashboard KPI e documentazione tecnica.

### Budget indicativo
5.000 – 10.000 € + IVA

### Criterio di completamento
Almeno un preventivo software/API credibile ricevuto o una proposta tecnica/economica utilizzabile per Allegato 3.
## Task — Richiesta preventivo IoT / smart meter PoE

Stato: aperta  
Priorità: molto alta  
Agente: FORNITORI AGENT

### Obiettivo
Ottenere un preventivo tecnico per realizzare il primo nodo fisico PoE.

### Contesto
Il punto debole attuale del progetto è il passaggio da dati simulati/generati a dati raccolti da un nodo fisico reale. Il preventivo IoT/smart meter serve a rendere PoE più concreto e finanziabile.

### Azioni operative
1. Cercare fornitori con competenze in IoT, smart meter, gateway, sensori energetici e raccolta dati elettrici.
2. Richiedere proposta per:
   - scelta sensore/smart meter
   - acquisizione parametri elettrici base
   - gateway o dispositivo IoT
   - invio dati verso API cloud
   - test su primo nodo fisico
   - documentazione tecnica finale
3. Specificare se hardware incluso o escluso.
4. Richiedere tempi, importo, IVA, totale, validità e condizioni.
5. Valutare se il preventivo è compatibile con il piano spese PoE.

### File coinvolti
- PREVENTIVI_DA_RICHIEDERE_POE.md
- PIANO_SPESE_POE.md
- BANDO.md
- ALLEGATO_3_SCHEMA_COMPILAZIONE_POE.md

### Output atteso
Preventivo per prototipo nodo energetico IoT collegabile al backend PoE.

### Budget indicativo
3.000 – 8.000 € + IVA

### Criterio di completamento
Almeno un preventivo IoT/smart meter credibile ricevuto.
## Task — Richiesta preventivo consulenza energetica PoE

Stato: aperta  
Priorità: alta  
Agente: FORNITORI AGENT

### Obiettivo
Ottenere un preventivo per validazione tecnica energetica del progetto PoE.

### Contesto
PoE deve essere presentato come piattaforma software/IoT per monitoraggio energetico e calcolo di indicatori di performance, stabilità e reputazione energetica. Serve una validazione tecnica esterna per rafforzare la candidatura.

### Azioni operative
1. Cercare ingegneri energetici, società di consulenza energetica, ESCo o consulenti IoT/energia.
2. Richiedere proposta per:
   - analisi modello dati energetici
   - scelta parametri tecnici da monitorare
   - definizione metriche di stabilità/performance
   - supporto test nodo fisico
   - relazione tecnica sintetica finale
3. Richiedere importo, IVA, totale, tempi, validità e condizioni.
4. Verificare che la proposta non sia una consulenza generica scollegata da PoE.
5. Mappare il preventivo nel piano spese.

### File coinvolti
- PREVENTIVI_DA_RICHIEDERE_POE.md
- PIANO_SPESE_POE.md
- BANDO.md
- ALLEGATO_3_SCHEMA_COMPILAZIONE_POE.md

### Output atteso
Preventivo per consulenza energetica e validazione tecnica del modello PoE.

### Budget indicativo
2.000 – 5.000 € + IVA

### Criterio di completamento
Almeno un preventivo tecnico-energetico credibile ricevuto.
## Task — Richiesta preventivo cloud/database/sicurezza PoE

Stato: aperta  
Priorità: media  
Agente: FORNITORI AGENT

### Obiettivo
Ottenere un preventivo per infrastruttura cloud, database persistente, backup e sicurezza base della piattaforma PoE.

### Contesto
L’MVP è già online, ma per una fase professionale serve stabilizzare backend, database, monitoraggio, backup e sicurezza API.

### Azioni operative
1. Cercare consulenti cloud, DevOps o fornitori infrastruttura con competenze API/database.
2. Richiedere proposta per:
   - revisione architettura cloud
   - backend production-ready
   - database persistente
   - backup
   - monitoraggio uptime
   - sicurezza minima API
   - documentazione tecnica
3. Richiedere importo, IVA, totale, tempi, validità e condizioni.
4. Valutare compatibilità con piano spese e Allegato 3.

### File coinvolti
- PREVENTIVI_DA_RICHIEDERE_POE.md
- PIANO_SPESE_POE.md
- BANDO.md
- ALLEGATO_3_SCHEMA_COMPILAZIONE_POE.md

### Output atteso
Preventivo per infrastruttura cloud e database PoE.

### Budget indicativo
1.500 – 4.000 € + IVA

### Criterio di completamento
Almeno un preventivo cloud/database credibile ricevuto oppure incluso dentro preventivo software/API.
## Task — Valutazione preventivi ricevuti

Stato: aperta  
Priorità: alta  
Agente: QA AGENT + BANDO AGENT

### Obiettivo
Valutare i preventivi ricevuti e decidere quali sono utilizzabili per il bando PoE.

### Contesto
Non tutti i preventivi sono automaticamente validi. Ogni preventivo deve essere controllato per coerenza tecnica, completezza formale e compatibilità con il piano spese.

### Azioni operative
1. Controllare intestazione fornitore, P.IVA, data, descrizione attività, imponibile, IVA, totale, validità offerta e condizioni.
2. Verificare che la descrizione sia coerente con PoE.
3. Scartare preventivi generici o troppo vaghi.
4. Mappare ogni preventivo alla voce corretta del piano spese.
5. Aggiornare Allegato 3 e PIANO_SPESE_POE.md.
6. Segnalare eventuali correzioni da chiedere al fornitore.

### File coinvolti
- BANDO.md
- ALLEGATO_3_SCHEMA_COMPILAZIONE_POE.md
- PIANO_SPESE_POE.md
- PREVENTIVI_DA_RICHIEDERE_POE.md

### Output atteso
Tabella preventivi con stato:
- valido
- da correggere
- non adatto

### Criterio di completamento
Almeno 3 preventivi credibili classificati e inseribili nella documentazione bando.
## Task — Shortlist fornitori seri per preventivi PoE

Stato: aperta  
Priorità: alta  
Agente: FORNITORI AGENT

### Obiettivo
Ottenere preventivi tecnici reali per la Fase 1 di Proof of Energy, evitando fornitori generici e richieste vaghe da bando.

### Regola operativa
- Fornitore competente > fornitore locale
- Preventivo tecnico > preventivo generico
- Fase 1 concreta > richiesta vaga per bando

### Fornitori primo giro
1. CodeBaker — software/API/IoT — info@codebaker.it
2. NEXETA — IoT/energy monitoring — info@nexeta.com
3. Electrex — energy monitoring/API/MQTT — info@electrex.it
4. Energy Wave — monitoring/consulenza — monitoring@energywave.it / consulting@energywave.it
5. Eurek — hardware/gateway/nodo fisico — info@eurek.it
6. Holonix — IoT/data platform — info@holonix.it / commerciale@holonix.it

### Azioni operative
1. Inviare email mirate ai primi 6 fornitori.
2. Tracciare risposte ricevute.
3. Classificare ogni risposta come: valida, da correggere, non adatta.
4. Mappare ogni preventivo ricevuto su voce spesa bando.
5. Aggiornare PREVENTIVI_DA_RICHIEDERE_POE.md e PIANO_SPESE_POE.md.

### Output atteso
Almeno 3 preventivi credibili:
- 1 software/API;
- 1 IoT/smart meter;
- 1 consulenza energy monitoring/cloud.

### Criterio di completamento
Task completata quando almeno 3 preventivi tecnici reali sono disponibili e mappati nel piano spese PoE.
