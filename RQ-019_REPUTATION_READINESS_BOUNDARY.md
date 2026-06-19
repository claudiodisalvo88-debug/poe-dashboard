# RQ-019_REPUTATION_READINESS_BOUNDARY

## Title
Reputation readiness boundary

## Question
When can aggregated reputation evidence become ready to inform future PoE reputation without becoming final reputation, ranking, incentive logic, token issuance or economic scoring?

## Scope
- Define the protocol boundary within which aggregated reputation evidence can become reputation-ready evidence.
- Define readiness gates for sufficiency, consistency, freshness, conflict status, manipulation risk and boundary integrity.
- Define separation rules, partial/conditional/capped readiness, conflict handling, staleness/expiry handling and failure outcomes.
- Preserve aggregated reputation evidence != reputation-ready evidence != final reputation != incentive.

## Non-scope
- No final reputation formula.
- No weights, score, ranking or leaderboard.
- No incentives, reward, token, payout or economic allocation.
- No economic scoring.
- No API, database, dashboard logic or implementation.

## Definition
Reputation-ready evidence = stato protocollare non economico in cui aggregated reputation evidence e abbastanza matura, coerente, non conflittuale e delimitata da boundary espliciti per informare una futura reputazione PoE senza diventare reputazione finale, ranking, score, incentivo, token, payout o diritto economico.

## Validated decision
PD-019 - VALIDATED

Aggregated reputation evidence puo diventare reputation-ready solo come maturita informativa non economica e non finale, entro vincoli espliciti di IE primitive, node boundary, time window, evidence type, sufficiency, consistency, freshness, conflict status, manipulation risk e boundary integrity.

Reputation-ready evidence deve preservare separazione da final reputation, ranking, score, incentive, token, payout, economic allocation, economic right, API, database, dashboard e implementation logic.

Readiness puo essere partial-ready, conditional-ready, capped-ready, postponed, not-ready, rejected o reputation-ready, in base a sufficiency, consistency, persistence/freshness, conflict status, manipulation risk e boundary integrity.

Cross-IE readiness deve restare separata salvo futura decisione protocollare esplicita che validi una interpretazione cross-IE non economica, non ordinante e non reputazionale finale.

## Readiness gates
Aggregated reputation evidence puo diventare reputation-ready solo se:

1. L'aggregazione e gia valida secondo PD-018.
2. Il node boundary e identico o attribuitivamente compatibile.
3. La IE primitive e dichiarata.
4. La time window e dichiarata.
5. L'evidenza e sufficiente per descrivere capacita nel tempo.
6. Esiste coerenza interna tra evidence item aggregati.
7. Non esiste conflitto cross-IE non risolto.
8. Nessun peggioramento sistemico e nascosto dietro evidenza positiva.
9. L'evidenza non e stale oppure e marcata come storica/capped.
10. Evidenza ordinaria ed evidenza eccezionale restano separate.
11. Il rischio manipolativo residuo e escluso, delimitato o trattato come capped/postponed.
12. Nessuna formula implicita viene prodotta.
13. Nessun ranking implicito viene prodotto.
14. Nessun uso economico implicito viene prodotto.

## Separation rules
IE primitive:
Readiness resta separata per IE-002, IE-003 e IE-005. Non esiste readiness unica cross-IE senza decisione separata.

Time window:
Readiness deve indicare la finestra temporale coperta. Evidenza vecchia e recente non vanno fuse senza dichiarare recenza e continuita.

Node boundary:
Readiness resta agganciata al nodo, asset, sito o boundary attribuito. Se il boundary cambia, readiness va separated o postponed.

Evidence type:
Evidenza ricorrente, episodica, eccezionale, capped, sospetta o storica deve restare distinguibile.

Ordinary vs exceptional:
L'evidenza eccezionale non puo simulare persistenza ordinaria.

## Partial / conditional readiness
partial-ready:
Un nodo puo essere ready per una IE e not-ready per un'altra. Esempio: ready per IE-002, not-ready per IE-003.

conditional-ready:
L'evidenza e pronta solo entro condizioni esplicite, come stessa classe asset, stessa finestra, stesso boundary, assenza di rebound, assenza di peggioramento cross-IE.

capped-ready:
L'evidenza e valida ma limitata perche vecchia, eccezionale, residualmente incerta o non pienamente ripetuta.

postponed:
Readiness sospesa quando mancano dati su conflitto, staleness, boundary, manipolazione o continuita.

## Conflict rules
Cross-IE conflict:
Il conflitto cross-IE blocca readiness globale.

No hidden harm:
Evidenza positiva in IE-005 non puo nascondere peggioramento IE-002.
Evidenza positiva in IE-003 non puo compensare automaticamente peggioramento IE-002.

No cross-IE netting:
Il netting cross-IE e formula implicita e resta vietato.

Esiti ammessi per conflitto:

- separated: readiness solo nella IE non conflittuale
- conditional-ready: ready solo se il conflitto e delimitato e non sistemico
- postponed: conflitto non ancora valutato
- rejected: conflitto invalida il valore sistemico

## Staleness / expiry
Readiness puo scadere concettualmente senza definire decay formula.

Evidenza vecchia senza continuita recente non deve dimostrare capacita attuale.

Evidenza storica puo restare informativa ma deve essere marcata come storica, capped o not-ready.

Regola minima:
readiness richiede attualita sufficiente o continuita osservata.

Non definire mesi, pesi o curva di decadimento in RQ-019.

## Failure outcomes
rejected:
Evidenza esclusa dalla readiness perche invalida, manipolata, conflittuale in modo grave, non attribuibile o economicamente contaminata.

not-ready:
Evidenza valida ma insufficiente per informare reputazione futura.

capped-ready:
Evidenza pronta solo come segnale limitato, non pieno.

conditional-ready:
Evidenza pronta solo entro condizioni esplicite.

partial-ready:
Evidenza pronta per una IE, boundary o finestra, ma non per reputazione generale.

postponed:
Readiness sospesa per insufficienza dati o conflitto non risolto.

reputation-ready:
Evidenza ammessa a informare futura reputazione, senza essere reputazione finale.

## Anti-reputation leakage rule
Reputation-ready evidence e solo uno stato di maturita informativa non economica.

Non costituisce:

- reputazione finale
- score
- ranking
- leaderboard
- token
- incentivo
- reward
- payout
- allocazione economica
- diritto economico
- implementazione

Qualsiasi trasformazione da readiness a reputazione richiede decisione protocollare successiva e separata.

Qualsiasi trasformazione da reputazione a incentivo richiede decisione protocollare successiva e separata.

## Test cases
Case A - Strong same-IE history:
Repeated aggregation-eligible evidence in IE-002 across multiple windows with no conflict.
Esito: reputation-ready per IE-002.
Boundary: non diventa score, ranking o reputazione finale.

Case B - Strong but old evidence:
Strong aggregated evidence six months ago but no recent continuity.
Esito: capped-ready storico oppure not-ready.
Vietato trattarla come capacita attuale piena.

Case C - Cross-IE mixed evidence:
Separate aggregated evidence in IE-002 and IE-003.
Esito: partial-ready separated.
Non fondere in readiness unica cross-IE.

Case D - Partial readiness:
Ready per IE-002, not-ready per IE-003.
Esito: partial-ready.
Questo preserva granularita e impedisce ranking sintetico prematuro.

Case E - Conflict:
Positive aggregated evidence in flexibility but negative evidence in avoidable consumption.
Esito: conditional-ready, postponed o rejected.
Mai compensazione automatica.

Case F - Exceptional emergency event:
One rare capped exceptional event with high systemic relevance.
Esito: capped-ready, non full-ready.
Puo dimostrare capacita eccezionale, non persistenza ordinaria.

Case G - Manipulation risk reduced but not eliminated:
Evidence passes aggregation gates but has residual uncertainty.
Esito: capped-ready o postponed.
Se manipolazione confermata: rejected.

Case H - Hidden ranking risk:
Readiness labels allow comparison between nodes.
Esito: rejected se abilita ordinamento tra nodi.
Readiness puo classificare stato protocollare dell'evidenza, non valore relativo tra soggetti.

## Final status
RQ-019 VALIDATED / CLOSED
