# RQ-017_REPUTATION_ELIGIBILITY_AFTER_RECOGNIZED_VALUE

## Title
Reputation eligibility after recognized value

## Question
When can recognized value become reputation-eligible in PoE V1 without collapsing recognized value into reputation, incentive, token logic, economic scoring or final ranking?

## Scope
- Define when recognized value can become non-economic reputation evidence.
- Define the minimum eligibility gates between recognized value and future reputation logic.
- Define failure outcomes for recognized value that does not pass the reputation-eligibility gates.
- Preserve the distinction recognized value != reputation != incentive.

## Non-scope
- No final reputation formula.
- No ranking logic.
- No token logic.
- No reward, payout or economic allocation logic.
- No economic scoring.
- No implementation or code behavior.

## Validated decision
PD-017 - VALIDATED

Un recognized value puo diventare reputation-eligible solo come evidenza non economica della capacita sistemica dimostrata dal nodo, dopo aver superato gate separati di validita protocollare, attribuzione, non duplicazione, evidenza sufficiente, resistenza alla manipolazione, sicurezza cross-IE, boundary integrity e comparabilita intra-IE oppure rilevanza sistemica eccezionale.

Reputation eligibility non definisce formula reputazionale, ranking finale, incentivo, reward, token, payout, allocazione economica o diritto economico.

## Eligibility gates
Un recognized value diventa reputation-eligible solo se supera:

1. Protocol-valid recognized value
2. Attribution preserved
3. Boundary integrity
4. Evidence sufficiency
5. Non-duplication
6. Manipulation resistance
7. Cross-IE safety
8. Intra-IE comparability
9. Persistence or repeatability
10. Exceptional systemic relevance, only as capped exception
11. Non-economic interpretation
12. Separation from incentives

## Failure outcomes
Recognized value che non supera i gate deve essere classificato come:

- rejected
- zero
- capped
- postponed
- eligible

rejected:
Il recognized value non puo entrare nel percorso reputazionale.

zero:
Il recognized value resta valido come valore, ma non produce evidenza reputazionale utilizzabile.

capped:
Il recognized value puo essere considerato solo in modo limitato, senza formula numerica definita qui, tipicamente per eventi eccezionali o rischio residuo controllato.

postponed:
Il recognized value resta sospeso fino a evidenza sufficiente, comparabilita, anti-gaming o verifica cross-IE.

eligible:
Il recognized value puo essere considerato in una futura logica reputazionale, non definita da RQ-017.

## Anti-economic leakage rule
L'eligibilita reputazionale e solo ammissibilita informativa non economica.
Non costituisce incentivo, reward, token, credito, payout, diritto economico, ranking finale, allocazione o promessa di compenso.
Qualunque uso economico della reputazione richiede una decisione protocollare separata, successiva e non implicita.

## Test cases
1. Recognized value valido, attribuito, comparabile e ripetibile:
   outcome atteso -> eligible

2. Recognized value valido ma con attribuzione dubbia o doppio conteggio plausibile:
   outcome atteso -> postponed oppure rejected

3. Recognized value valido come valore ma non comparabile intra-IE e senza rilevanza sistemica eccezionale:
   outcome atteso -> postponed

4. Recognized value legato a evento eccezionale con forte rilevanza sistemica ma comparabilita debole:
   outcome atteso -> capped

5. Recognized value valido ma interpretabile come premio economico implicito:
   outcome atteso -> zero oppure rejected finche la lettura non economica non viene separata

## Final status
RQ-017 VALIDATED / CLOSED
