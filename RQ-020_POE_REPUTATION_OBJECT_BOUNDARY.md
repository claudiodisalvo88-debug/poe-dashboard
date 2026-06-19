# RQ-020_POE_REPUTATION_OBJECT_BOUNDARY

## Title
PoE Reputation object boundary

## Question
When can reputation-ready evidence contribute to defining a PoE Reputation object without becoming final formula, ranking, incentive logic, token issuance or economic scoring?

## Scope
- Define the protocol boundary within which reputation-ready evidence can contribute to a PoE Reputation object.
- Define minimal object components and bounded descriptive contents.
- Define separation rules, comparability rule, conflict representation, partial/capped/conditional representation and staleness representation.
- Preserve reputation-ready evidence != PoE Reputation object != formula != ranking != incentive.

## Non-scope
- No final reputation formula.
- No weights, scalar score, ranking or leaderboard.
- No incentives, reward, token, payout or economic allocation.
- No economic scoring.
- No API, database, dashboard logic or implementation.

## Definition
PoE Reputation object = oggetto protocollare non economico, multidimensionale e non ordinante che rappresenta per un nodo le capacita sistemiche dimostrate tramite bounded reputation-ready evidence separate per IE primitive, node boundary, time window, evidence type, readiness status, conflict state, staleness state e source references, senza diventare formula, score, ranking, incentivo, token, payout o allocazione economica.

## Validated decision
PD-020 - VALIDATED

The PoE Reputation object is a non-economic, multidimensional and non-ordering protocol object that represents demonstrated systemic capacities of a node through bounded reputation-ready evidence separated by IE primitive, node boundary, time window, evidence type, readiness status, conflict state, staleness state and source references.

The PoE Reputation object may contain readiness statuses, evidence summaries, conflict flags, staleness flags, capped markers, conditional markers, manipulation-risk markers, boundary integrity notes and source references.

The PoE Reputation object must not contain or imply weights, formula, scalar score, ranking, leaderboard, incentive, reward, token, payout, economic allocation, economic right, API, database, dashboard logic or implementation.

Reputation objects may be described but not ordinally compared before a separate future protocol decision on reputation formula or ranking.

## Minimal object components
Il PoE Reputation object puo contenere solo componenti descrittivi e bounded:

1. Node boundary:
   nodo, asset, sito o aggregatore a cui l'oggetto si riferisce.

2. IE primitive dimension:
   IE-002, IE-003, IE-005 separate.

3. Readiness status:
   ready, partial, capped, conditional, historical, conflict-marked, not-ready.

4. Evidence summary:
   descrizione sintetica, non punteggio.

5. Time window:
   periodo coperto dall'evidenza.

6. Evidence type:
   ordinaria, ricorrente, eccezionale, storica, capped, condizionata.

7. Conflict flags:
   conflitti intra-IE o cross-IE esposti, non compensati.

8. Staleness flags:
   evidenza current, recent, historical, stale, expired-for-readiness, continuity-missing.

9. Capped / conditional markers:
   limiti concettuali dell'evidenza.

10. Manipulation-risk marker:
    rischio assente, residuo, non risolto.

11. Source references:
    collegamento alle evidenze che supportano lo stato.

12. Boundary integrity note:
    avviso se il boundary e cambiato o incompleto.

Il PoE Reputation object non puo contenere:

- peso
- totale
- coefficiente
- score finale
- posizione
- payout
- token entitlement
- rank
- leaderboard
- diritto economico

## Separation rules
IE primitive:
Obbligatorio. Un oggetto puo contenere piu dimensioni IE, ma deve tenerle separate.

Time window:
Obbligatorio. Evidenza recente e storica non devono fondersi.

Node boundary:
Obbligatorio. Non mischiare nodo, sito, asset e aggregatore senza boundary esplicito.

Evidence type:
Obbligatorio. Evidenza ordinaria, eccezionale, capped e storica devono restare distinguibili.

Readiness status:
Obbligatorio. Partial-ready non deve apparire come full-ready.

## Comparability rule
Prima di una futura decisione esplicita su formula o ranking, i PoE Reputation objects non devono essere comparati in senso ordinale.

Confronti vietati:

- Nodo A ha reputazione maggiore di Nodo B.
- Nodo A e top ranked.
- Nodo A merita piu reward.
- Nodo A ha score superiore.
- IE-002 + IE-003 = reputazione totale.
- Questo oggetto abilita accesso, premio, token o payout.

Confronti ammessi solo descrittivi:

- Nodo A ha readiness IE-002; Nodo B no.
- Nodo A ha evidenza storica; Nodo B ha evidenza recente.
- Nodo A e conflict-marked su IE-003.
- Nodo A ha capped readiness per evento eccezionale.
- Nodo A ha conditional readiness entro uno specifico boundary.

## Conflict representation
Il conflitto non deve essere compensato.

Se un nodo e ready per IE-003 ma ha evidenza negativa o non risolta in IE-002, l'oggetto puo esistere solo come conflict-marked-reputation-object.

Il conflitto deve essere esposto come stato separato:

- IE positiva interessata
- IE negativa o danneggiata
- finestra temporale del conflitto
- boundary coinvolto
- stato del conflitto: unresolved, bounded, rejected, postponed

Vietato netting cross-IE.
Una riduzione di picco non cancella automaticamente consumo evitabile aumentato.

## Partial / capped / conditional representation
Partial-ready:
Entra come dimensione limitata: ready solo per IE-002, non come reputazione generale.

Capped-ready:
Entra con marker esplicito: capacita dimostrata solo entro evento, finestra o contesto limitato.

Conditional-ready:
Entra con condizioni visibili: stesso boundary, stessa classe di asset, stessa finestra, assenza di rebound, assenza di conflitto cross-IE.

Exceptional readiness:
Puo entrare solo come capacita eccezionale, non come prova di capacita ordinaria continuativa.

Non deve esistere conversione automatica da capped/conditional a full reputation object.

## Staleness representation
Evidenza stale puo restare nell'oggetto solo come historical capacity.

Non deve implicare forza reputazionale attuale.

Non serve definire formula di decay.

Stati ammessi:

- current
- recent
- historical
- stale
- expired-for-readiness
- continuity-missing

Se non c'e continuita recente, l'oggetto puo essere partial, capped o historical, non full-ready.

## Failure outcomes
rejected:
L'oggetto non puo essere formato perche l'evidenza e invalida, manipolata, non attribuibile, economicamente contaminata o conflittuale in modo grave.

no-reputation-object:
Il nodo ha evidenza insufficiente o not-ready; esistono dati, ma non un oggetto reputazionale.

partial-reputation-object:
Esiste solo per una IE, finestra o boundary.

conditional-reputation-object:
Valido solo sotto condizioni esplicite.

capped-reputation-object:
Contiene evidenza valida ma limitata, eccezionale, stale o residualmente incerta.

conflict-marked-reputation-object:
Esiste ma espone conflitti non risolti; non puo essere sintetizzato.

reputation-object-ready:
L'oggetto e strutturalmente coerente e puo informare una futura formula reputazionale, senza essere formula.

## Anti-leakage rule
Il PoE Reputation object e una rappresentazione protocollare non economica e non ordinante di capacita sistemiche dimostrate.

Non puo produrre:

- formula
- punteggio
- score scalare
- ranking
- leaderboard
- incentivo
- reward
- token
- payout
- allocazione
- diritto economico
- API
- database
- dashboard
- implementazione

Qualunque uso numerico, comparativo, economico o decisionale richiede una futura decisione protocollare separata.

Qualunque oggetto che genera un valore scalare unico deve essere rifiutato come formula nascosta.

Qualunque oggetto che ordina nodi deve essere rifiutato come ranking nascosto.

Qualunque oggetto che abilita reward, token, payout o accesso economico deve essere rifiutato come incentive leakage.

## Test cases
Case A - Single-IE reputation:
Nodo con readiness solo IE-002.
Esito: partial-reputation-object.
Puo avere oggetto PoE Reputation parziale, non reputazione generale.

Case B - Multi-IE separated reputation:
Nodo con readiness per IE-002 e IE-003, senza cross-IE synthesis.
Esito: reputation-object-ready separated.
Puo rappresentare entrambe, ma senza score unico.

Case C - Conflict inside reputation:
Nodo ready per IE-003 ma con evidenza negativa o non risolta in IE-002.
Esito: conflict-marked-reputation-object.
L'oggetto puo esistere, ma deve esporre il conflitto e vietare sintesi positiva.

Case D - Capped readiness:
Nodo con capped-ready evidence da evento eccezionale.
Esito: capped-reputation-object.
L'evento eccezionale entra come capacita eccezionale, non ordinaria.

Case E - Historical evidence:
Nodo con vecchia readiness evidence ma senza continuita recente.
Esito: partial o capped historical object.
Deve indicare capacita storica, non forza attuale.

Case F - Hidden ranking risk:
Due nodi hanno reputation objects diversi.
Esito: rejected se il confronto produce ordine tra nodi.
Confronto descrittivo ammesso; confronto ordinale vietato.

Case G - Economic leakage:
Reputation object usato per allocare accesso, reward, token o payout.
Esito: fuori scope e rejected come uso del reputation object.

Case H - Object too weak:
Se l'oggetto e solo lista di evidenze, non aggiunge nulla.
Deve aggiungere struttura minima: IE dimensions, status, boundary, time window, flags, source references, conflict/staleness/capped markers.
Se non aggiunge questi boundary, va rigettato come layer inutile.

## Final status
RQ-020 VALIDATED / CLOSED
