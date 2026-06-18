# RQ-007 — Formal distinction between CONTRIBUTO, RIDUZIONE, VALORE

Status: VALIDATED / CLOSED
Decision: PD-008

## Question

Determinare se CONTRIBUTO, RIDUZIONE e VALORE sono tre oggetti distinti oppure oggetti parzialmente coincidenti nel protocollo PoE.

## Repository basis

- PD-000: PoE misura il contributo energetico verificabile.
- PD-001: gerarchia PoE: INEFFICIENZA -> RIDUZIONE -> CONTRIBUTO -> VALORE -> REPUTAZIONE -> INCENTIVO.
- PD-002: un contributo energetico e un comportamento osservabile e verificabile che produce un miglioramento misurabile del sistema energetico.
- PD-003: il valore nel protocollo PoE e la riduzione verificabile di una inefficienza del sistema energetico.
- PD-007: inefficienze primitive PoE V1: IE-002 Consumo evitabile, IE-003 Punte di carico, IE-005 Mancanza di flessibilita.

## Verdict

CONTRIBUTO, RIDUZIONE e VALORE sono oggetti distinti.

La distinzione minima e:

- RIDUZIONE = delta osservabile e verificabile di una inefficienza catalogata rispetto a baseline, finestra temporale e contesto validati.
- CONTRIBUTO = comportamento osservabile, verificabile e attribuibile a un nodo/soggetto che partecipa causalmente alla riduzione.
- VALORE = proprieta protocollare derivata da una riduzione verificata, attribuita e sistemicamente rilevante di una inefficienza catalogata.

VALORE non e identico alla RIDUZIONE grezza. VALORE e RIDUZIONE qualificata dal protocollo tramite verifica, attribuzione, rilevanza sistemica e controllo contro manipolazioni.

## Object definitions

### RIDUZIONE

Definizione:
Riduzione e la diminuzione osservabile di una inefficienza energetica catalogata, misurata rispetto a una baseline e dentro una finestra temporale definita.

Input osservabili:
- serie temporali di consumo, produzione o storage;
- baseline validata;
- finestra temporale;
- contesto operativo;
- identificazione dell'inefficienza target.

Output osservabili:
- delta numerico dell'inefficienza;
- durata del delta;
- intensita del delta;
- eventuali effetti collaterali.

Condizioni necessarie:
- inefficienza target definita;
- baseline disponibile;
- dato misurabile;
- confronto verificabile.

Condizioni sufficienti:
- delta positivo rispetto a baseline validata;
- finestra temporale coerente;
- dato non contraddetto da effetti collaterali immediati.

Verifica:
- confronto prima/dopo o contro baseline equivalente;
- controllo su dati osservabili;
- controllo contro spostamento artificiale dell'inefficienza.

Attribuzione:
Non necessaria per affermare che una riduzione aggregata e avvenuta. Necessaria per trasformarla in contributo o valore PoE assegnabile.

### CONTRIBUTO

Definizione:
Contributo e un comportamento osservabile, verificabile e attribuibile che partecipa causalmente alla riduzione di una inefficienza energetica.

Input osservabili:
- identita del nodo/soggetto;
- comportamento energetico osservato;
- timestamp;
- misura prima/dopo;
- inefficienza target;
- condizioni del sistema.

Output osservabili:
- azione o comportamento attribuito;
- quota di riduzione attribuibile;
- evidenza causale minima;
- stato: candidate contribution oppure valid contribution.

Condizioni necessarie:
- comportamento osservabile;
- verificabilita del dato;
- attribuzione a nodo/soggetto;
- relazione causale con una riduzione.

Condizioni sufficienti:
- comportamento misurato;
- riduzione verificata;
- nesso causale plausibile e non contraddetto;
- assenza di manipolazione evidente.

Verifica:
- audit del comportamento;
- confronto con condizioni equivalenti;
- controllo baseline;
- controllo che il comportamento non crei inefficienza altrove.

Attribuzione:
Essenziale. Senza attribuzione non esiste contributo PoE assegnabile.

### VALORE

Definizione:
Valore e l'effetto protocollare riconosciuto quando una riduzione verificata di una inefficienza catalogata e attribuita a un contributo e produce miglioramento sistemico netto.

Input osservabili:
- riduzione verificata;
- contributo attribuito;
- inefficienza target;
- baseline;
- finestra temporale;
- controlli contro manipolazioni;
- eventuali effetti collaterali.

Output osservabili:
- valore sistemico riconosciuto;
- quantita o qualita del miglioramento;
- base per reputazione futura;
- ragione di validita o rigetto.

Condizioni necessarie:
- inefficienza catalogata;
- riduzione verificata;
- attribuzione valida;
- rilevanza sistemica;
- effetto netto non negativo.

Condizioni sufficienti:
- riduzione verificata;
- attribuzione al contributo;
- miglioramento sistemico netto;
- nessuna evidenza di baseline gaming, double counting o shifting.

Verifica:
- verifica della riduzione;
- verifica dell'attribuzione;
- verifica della rilevanza sistemica;
- verifica di non trasferimento dell'inefficienza.

Attribuzione:
Necessaria per valore PoE assegnabile. Un miglioramento aggregato non attribuito puo esistere come effetto di sistema, ma non genera valore reputazionale assegnabile.

## Answers

### A. Puo esistere un contributo senza valore?

Risposta: dipende dal significato di contributo.

- Contributo PoE valido: no. Per PD-002, il contributo valido produce miglioramento misurabile.
- Candidate contribution: si. Un comportamento puo essere osservabile e attribuibile ma non produrre valore se non riduce una inefficienza, se agisce fuori finestra utile, se sposta l'inefficienza altrove o se non supera la verifica.

Esempi:
- un nodo riduce consumo quando non esiste consumo evitabile rilevante;
- un carico viene spostato fuori da un picco ma crea un nuovo picco;
- una risposta flessibile arriva troppo tardi rispetto alla condizione di sistema.

### B. Puo esistere una riduzione senza contributo?

Risposta: si.

Esempi:
- calo dei consumi per meteo favorevole;
- riduzione causata da blackout o guasto;
- riduzione dovuta a chiusura casuale di un carico;
- miglioramento aggregato non attribuibile a un nodo specifico.

In questi casi la riduzione puo essere reale, ma non diventa contributo PoE se manca comportamento attribuibile e verificabile.

### C. Puo esistere valore senza attribuzione?

Risposta: no, per valore PoE assegnabile.

Puo esistere miglioramento aggregato non attribuito, ma non puo generare reputazione PoE per un nodo. La reputazione misura capacita dimostrata di generare valore sistemico nel tempo; senza attribuzione non c'e capacita dimostrata assegnabile.

### D. Qual e la definizione minima di VALORE?

VALORE = riduzione verificata, attribuita e sistemicamente rilevante di una inefficienza energetica catalogata, con effetto netto positivo o non negativo e senza evidenza di manipolazione.

### E. VALORE e identico a RIDUZIONE?

No.

RIDUZIONE e il delta misurato di una inefficienza.
VALORE e la proprieta protocollare derivata dalla riduzione quando il delta e verificato, attribuito, sistemicamente rilevante e non manipolato.

PD-003 resta valida solo se interpretata come formula compressa: valore = riduzione verificabile qualificata dal protocollo, non semplice delta grezzo.

### F. Attacchi se gli oggetti non sono distinti

1. Baseline gaming: aumentare artificialmente il consumo iniziale per mostrare riduzione.
2. Peak fabrication: creare o amplificare picchi per poi ridurli.
3. Attribution theft: reclamare riduzioni prodotte da meteo, guasti, altri nodi o eventi esterni.
4. Double counting: assegnare la stessa riduzione a piu nodi o piu categorie.
5. Value laundering: contare una riduzione grezza come valore anche se non migliora il sistema.
6. Temporal shifting: ridurre in una finestra e ricreare l'inefficienza in un'altra.
7. Flexibility simulation: simulare flessibilita in condizioni non rilevanti.
8. Derived-inefficiency inflation: gonfiare inefficienze derivate per duplicare valore gia contato nelle primitive.
9. Negative externality masking: produrre riduzione locale creando instabilita, picchi o sprechi altrove.

## G. Causal validation

RQ-007 introduce una correzione importante: la catena PD-001 non deve essere letta come ordine causale rigido.

PD-001 resta valida come gerarchia protocollare, ma il nesso causale minimo e:

INEFFICIENZA VALIDATA
-> METRICA DELL'INEFFICIENZA
-> BASELINE / CONDIZIONE DI CONFRONTO
-> COMPORTAMENTO OSSERVABILE
-> CONTRIBUTO CANDIDATO
-> RIDUZIONE MISURATA
-> VERIFICA DELLA RIDUZIONE
-> ATTRIBUZIONE AL CONTRIBUTO
-> VALORE
-> REPUTAZIONE

Questa struttura evita il rischio di osservare una riduzione e poi cercare retroattivamente un contributo a cui assegnarla.

## H. Candidate contribution rule

Un comportamento energetico osservato non e automaticamente contributo valido.

Stati minimi:

1. comportamento osservato;
2. contributo candidato;
3. contributo verificato;
4. contributo attribuito;
5. valore protocollare riconosciuto.

Il passaggio da candidato a valido richiede riduzione verificata, attribuzione e rilevanza rispetto a una inefficienza primitiva o a un percorso derivato autorizzato.

## I. Final decision

RQ-007: VALIDATED / CLOSED

Decisione prodotta: PD-008

Conseguenza protocollare:
PoE deve trattare CONTRIBUTO, RIDUZIONE e VALORE come oggetti separati nella fase di ricerca, documentazione e futura modellazione dati. La reputazione non deve derivare da riduzioni grezze, ma da valore protocollare riconosciuto.

Conseguenza aggiuntiva:
Le prossime metriche per IE-002, IE-003 e IE-005 devono misurare separatamente:

- comportamento osservabile;
- riduzione misurata;
- verifica della riduzione;
- attribuzione al contributo;
- valore riconosciuto.
