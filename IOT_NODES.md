# IOT_NODES.md

## Ruolo del file

Questo file contiene la memoria operativa dei nodi energetici reali e futuri del progetto Proof of Energy.

Fonte principale:
POE_STATE.md

Regola:
non modificare codice IoT o collector senza prima aggiornare questo file quando cambia lo stato dei nodi.

---

## Stato generale nodi IoT

Fase attuale:
preparazione primo nodo reale.

Priorità:
REAL_NODE_01

---

## REAL_NODE_01

### Stato

In preparazione.

### Dispositivo scelto

Shelly Pro EM-50 con 2 pinze CT da 50A incluse.

### Tipo nodo

Nodo energetico reale AC monofase.

### Installazione

Da eseguire con elettricista.

Contatto operativo:
Enzo.

### Obiettivo

Misurare un circuito/carico reale e inviare i dati energetici al backend Proof of Energy.

### Schema logico

Shelly Pro EM-50
→ PoE Edge Collector
→ Backend API
→ Database
→ KPI / Energy Reputation
→ Dashboard

### Protocolli utili

- HTTP
- MQTT
- WebSocket
- Modbus TCP

### Dati attesi

- timestamp
- node_id
- voltage
- ampere
- watt
- energy_wh
- source
- quality_flag

### Node ID previsto

REAL_NODE_01

### Stato integrazione software

Non iniziata.

Motivo:
attendere acquisto, installazione e configurazione Shelly.

### Prossimi step

1. Acquistare Shelly Pro EM-50.
2. Avvisare Enzo.
3. Installare dispositivo.
4. Collegare Shelly alla rete.
5. Recuperare IP locale Shelly.
6. Verificare lettura dati da browser/API locale.
7. Creare PoE Edge Collector.
8. Inviare dati a `/ingest`.
9. Verificare dashboard e ranking.

---

## SOLAR_NODE_01

### Stato

Futuro / non prioritario.

### Dispositivo disponibile

Pannello fotovoltaico REC AE-Series Demo 20W DC.

### Dati pannello

- Pmax: 20 W ±5%
- Vmp: 2.8 V
- Imp: 7.1 A
- Voc: 3.6 V
- Isc: 7.8 A
- Uscita: DC

### Nota tecnica

Il pannello non è adatto a essere collegato direttamente a smart meter AC tipo Shelly Pro EM-50.

Per usarlo come nodo futuro servirà una soluzione DC dedicata:

- sensore tensione DC
- sensore corrente DC
- carico/regolatore adeguato
- microcontrollore o collector dedicato

### Decisione

Non usare SOLAR_NODE_01 nella fase 1.

---

## Regola operativa

Prima stabilizzare REAL_NODE_01.
Solo dopo valutare SOLAR_NODE_01.
