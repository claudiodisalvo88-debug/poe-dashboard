# PROTOCOL_DECISIONS.md

## PD-000

PoE misura il contributo energetico verificabile.

STATUS: VALIDATED

## PD-001

Gerarchia PoE:
INEFFICIENZA
RIDUZIONE
CONTRIBUTO
VALORE
REPUTAZIONE
INCENTIVO

STATUS: VALIDATED

## PD-002

Un contributo energetico e un comportamento osservabile e verificabile che produce un miglioramento misurabile del sistema energetico.

STATUS: VALIDATED

## PD-003

Il valore nel protocollo PoE e la riduzione verificabile di una inefficienza del sistema energetico.

STATUS: VALIDATED

## PD-004

La reputazione PoE e dinamica e aggiornata continuamente in base al valore sistemico verificato generato dal nodo.

STATUS: VALIDATED

## PD-005

La reputazione PoE misura la capacita dimostrata di un soggetto di generare valore sistemico nel tempo.

STATUS: VALIDATED

## PD-006

Proof of Energy identifica inefficienze energetiche, misura il contributo dei partecipanti alla loro riduzione e trasforma tale contributo in valore verificabile.

STATUS: VALIDATED

## PD-007

Le inefficienze primitive del protocollo PoE V1 sono:

IE-002 Consumo evitabile
IE-003 Punte di carico
IE-005 Mancanza di flessibilita

Le seguenti inefficienze sono classificate come derivate:

IE-001 Energia sprecata
IE-004 Energia rinnovabile non utilizzata
IE-006 Instabilita locale

STATUS: VALIDATED

## PD-008

CONTRIBUTO, RIDUZIONE e VALORE sono oggetti protocollari distinti.

RIDUZIONE:
delta osservabile e verificabile di una inefficienza catalogata rispetto a baseline, finestra temporale e contesto validati.

CONTRIBUTO:
comportamento osservabile, verificabile e attribuibile a un nodo o soggetto che partecipa causalmente alla riduzione.

VALORE:
proprieta protocollare derivata da una riduzione verificata, attribuita e sistemicamente rilevante di una inefficienza catalogata.

VALORE non e identico alla RIDUZIONE grezza.
VALORE e RIDUZIONE qualificata dal protocollo tramite verifica, attribuzione, rilevanza sistemica e controllo contro manipolazioni.

STATUS: VALIDATED

## PD-009

For each primitive inefficiency, PoE V1 metrics must separate:

1. observable behavior;
2. candidate contribution;
3. measured reduction;
4. reduction verification;
5. attribution to contribution;
6. recognized value.

IE-002, IE-003 and IE-005 must each define:

* metric target;
* observable inputs;
* baseline requirement;
* valid reduction;
* invalid reduction;
* attribution rule;
* value condition;
* attack vectors;
* minimum verification rule.

RQ-008 validates the conceptual metric structure only.
It does not validate final quantitative formulas, thresholds, scoring rules, tokens, or incentives.

STATUS: VALIDATED
