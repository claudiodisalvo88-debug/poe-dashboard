# RQ-018_REPUTATION_EVIDENCE_AGGREGATION_BOUNDARIES

## Title
Reputation evidence aggregation boundaries

## Question
When can multiple reputation-eligible recognized values be aggregated as reputation evidence without becoming final reputation formula, ranking, incentive logic, token issuance or economic scoring?

## Scope
- Define the protocol boundaries within which multiple reputation-eligible evidence items can be aggregated as non-economic reputation evidence.
- Define aggregation gates for node boundary, IE primitive, time window, evidence type, conflict handling and non-duplication.
- Define separation rules, conflict rules, duplication/correlation rules and failure outcomes for aggregated reputation evidence.
- Preserve recognized value != reputation eligibility != aggregated reputation evidence != final reputation != incentive.

## Non-scope
- No final reputation formula.
- No weights.
- No ranking or leaderboard.
- No incentives, reward, token, payout or economic allocation.
- No economic scoring.
- No API, database, dashboard logic or implementation.

## Definition
Aggregated reputation evidence = insieme non economico, non finale e non ordinante di piu evidenze reputation-eligible, raggruppate entro boundary espliciti per descrivere capacita sistemica dimostrata senza produrre reputazione finale, ranking, score, incentivo, token, payout o diritto economico.

## Validated decision
PD-018 - VALIDATED

Un insieme di reputation-eligible evidence puo essere aggregato solo come evidenza reputazionale non economica, non finale e non ordinante, entro boundary espliciti di nodo, IE primitive, finestra temporale, tipo di evidenza e non duplicazione.

L'aggregazione deve preservare separazione per IE primitive, impedire duplicazioni, identificare correlazioni, isolare evidenze eccezionali capped, esporre conflitti e vietare netting cross-IE automatico.

Aggregated reputation evidence non definisce final reputation, ranking, score, incentivo, reward, token, payout, allocazione economica, diritto economico, API, database, dashboard o implementation logic.

## Aggregation gates
Piu evidence item possono diventare aggregation-eligible solo se:

1. Ogni item e gia reputation-eligible.
2. Il node boundary e identico o attribuitivamente compatibile.
3. La time window e dichiarata.
4. La IE primitive e dichiarata.
5. La separazione tra IE-002, IE-003 e IE-005 e preservata.
6. I duplicati sono esclusi o merged.
7. Gli item correlati o dipendenti sono identificati.
8. I conflitti cross-IE sono esclusi, separati, capped o postponed.
9. Le evidenze eccezionali capped restano separate dalle evidenze ordinarie.
10. L'aggregato non produce score unico, classifica, ranking, diritto economico, token o incentivo.

## Separation rules
IE primitive:
Aggregazione primaria separata per IE. IE-002 con IE-002, IE-003 con IE-003, IE-005 con IE-005.

Cross-IE aggregation:
Ammessa solo come vista descrittiva separata, non come valore unico cumulato.

Time window:
Obbligatoria. L'aggregato deve dichiarare periodo, recenza e continuita osservata senza definire decay formula.

Node boundary:
Obbligatorio. Non aggregare evidenze di nodo, asset, sito, gruppo o aggregatore se l'attribuzione non distingue i livelli.

Evidence type:
Separare evidenza ricorrente, episodica, sospetta, corretta, capped, emergenziale.

Ordinary vs exceptional:
L'evento eccezionale puo affiancare la storia ordinaria, non sostituirla.

## Conflict rules
Cross-IE conflict:
Se una evidenza positiva in una IE peggiora un'altra IE, l'aggregazione positiva deve essere separated, capped o postponed finche il danno non e escluso o confinato.

Negative evidence:
Non va nascosta dentro un aggregato positivo. Deve restare visibile come contro-evidenza separata.

Boundary conflict:
Se evento, nodo, asset o finestra non coincidono, non aggregare. Esito: postponed o separated.

Netting vietato:
Non compensare automaticamente +IE-003 con -IE-002. Questo sarebbe formula cross-IE implicita.

## Duplication/correlation rules
Duplicate evidence:
Se due item derivano dallo stesso evento sottostante, non possono contare due volte.
Esito: merged se sono la stessa evidenza descritta due volte; rejected se la duplicazione e intenzionale o manipolativa.

Correlated evidence:
Se piu item non sono duplicati ma dipendono dallo stesso comportamento, stessa finestra o stessa baseline, non devono essere trattati come indipendenti.
Esito: capped o separated.

Dependent evidence:
Se IE-003 e IE-005 derivano dalla stessa risposta, serve prova che riducano due inefficienze distinte. Altrimenti full double counting e vietato.

## Failure outcomes
rejected:
L'evidenza non puo entrare nell'aggregazione perche invalida, manipolata, duplicata in modo fraudolento, fuori boundary o conflittuale in modo non risolto.

merged:
Due o piu evidenze descrivono lo stesso evento sottostante e devono diventare un solo item aggregabile.

capped:
Evidenza valida ma limitata perche eccezionale, episodica, correlata, dipendente o con incertezza residua.

separated:
Evidenza valida ma non aggregabile nello stesso bucket per IE, finestra, boundary, tipo o natura ordinaria/eccezionale.

postponed:
Servono dati aggiuntivi su attribuzione, boundary, correlazione, conflitto o non duplicazione.

aggregation-eligible:
Evidenza ammessa a essere raggruppata in un bucket descrittivo non economico e non finale.

## Anti-formula rule
L'aggregazione di evidenza reputazionale non puo produrre valore numerico unico, ordine tra nodi, ranking, leaderboard, formula reputazionale, score economico, incentivo, token, payout, allocazione o diritto economico.

Se un aggregato permette di dire "Nodo A > Nodo B" senza una decisione reputazionale successiva, l'aggregazione e diventata ranking nascosto.

Se un aggregato permette di calcolare premio, token o allocazione, l'aggregazione e diventata incentivo nascosto.

Se un aggregato comprime IE diverse in un solo valore, l'aggregazione e diventata formula cross-IE implicita.

## Test cases
Case A - Same IE repeated evidence:
Puo essere aggregation-eligible se stesso nodo, stessa IE, finestre dichiarate, non duplicazione, baseline non manipolato e boundary preservato.

Case B - Cross-IE mixed evidence:
IE-002 e IE-003 devono restare separated. Non creare bucket unico.

Case C - Conflicting evidence:
Il positivo IE-003 non puo nascondere peggioramento IE-002. Esito: postponed o rejected se il danno invalida il valore sistemico.

Case D - Duplicate evidence:
Stesso evento sottostante = merged. Duplicazione opportunistica = rejected.

Case E - Correlated evidence:
Non puo contare come indipendente. Esito: capped o separated.

Case F - Exceptional event:
Solo bucket separato capped. Non deve apparire come ricorrenza ordinaria.

Case G - Time decay:
Aggregazione puo descrivere evidenza storica e recenza senza definire decay formula. Evidenza vecchia senza continuita recente resta storica, non prova piena di capacita attuale.

Case H - Hidden scoring risk:
Se l'aggregato ordina nodi, produce classifica o abilita decisioni economiche, e rejected come aggregazione e rinviato a futura ricerca reputazionale/ranking esplicitamente autorizzata.

## Final status
RQ-018 VALIDATED / CLOSED
