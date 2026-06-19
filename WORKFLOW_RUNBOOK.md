# WORKFLOW_RUNBOOK.md

## Purpose
Formalizzare un workflow agentico operativo basato su repository, così che task, output, review e prossime azioni restino tracciati senza dipendere dalla memoria chat.

## Source of truth
`POE_STATE.md` è sempre il primo file da leggere.
`POE_STATE.md` resta la fonte di verità sullo stato operativo del progetto.

## Operating principle
Gli agenti non si passano stato tramite conversazione.
Gli agenti lavorano leggendo e aggiornando file Markdown del repository.
Nessun agente può dichiarare stato verificato senza fonte repository, terminale o output reale.

## Standard workflow
1. Leggere `POE_STATE.md`.
2. Il PM definisce o valida il task.
3. Il task viene registrato in `AGENT_QUEUE.md`.
4. L'agente specializzato produce output sintetico in `AGENT_OUTPUTS.md`.
5. Il PM o verifier registra la decisione in `PM_REVIEW.md`.
6. Codex modifica solo i file autorizzati dal PM.
7. QA / Verifier controlla diff, vincoli e staging.
8. Se il task è valido, si eseguono commit e push.
9. `POE_STATE.md` viene aggiornato con la next action.

## Role boundaries
- ChatGPT PM non è dev diretto.
- Codex modifica file solo dopo validazione PM.
- Innovator Agent propone o valida ipotesi, ma non modifica file.
- QA / Verifier verifica prima del commit o subito dopo output Codex.
- Memory Agent mantiene `POE_STATE.md` sintetico e sposta il dettaglio nei file modulari.

## File responsibilities
- `POE_STATE.md`: stato sintetico, milestone, blocchi, next action.
- `AGENT_QUEUE.md`: coda task attivi, pending, blocked, completed.
- `AGENT_OUTPUTS.md`: output sintetici degli agenti, non conversazioni complete.
- `PM_REVIEW.md`: approvazioni, rifiuti, limiti e autorizzazioni per Codex.
- `AGENTS.md`: ruoli, regole e workflow ufficiale.
- `WORKFLOW_RUNBOOK.md`: regole operative trasversali.

## Terminal safety rules
- Verificare sempre `git status` prima di modificare file.
- Usare output reali di terminale per confermare stato e vincoli.
- Non dichiarare deploy, errori o fix non verificati.
- Non trattare la chat come fonte di verità operativa.

## Commit safety rules
- Non usare `git add .`.
- Non usare `git add -A`.
- `poe.db` non va staged o committato salvo decisione esplicita futura.
- Commit piccoli, leggibili e documentali quando il task è documentale.
- Ogni commit deve riflettere solo i file autorizzati dal PM review.

## When to use Innovator Agent
- Quando serve stressare una regola protocollo.
- Quando serve distinguere tra ipotesi, evidenza e criterio di validazione.
- Quando serve un test minimo prima di aprire nuova ricerca o decisione.

## When to use Codex
- Quando esiste una review PM che autorizza modifiche precise.
- Quando il task richiede aggiornamento ordinato di file Markdown.
- Quando serve applicare cambi documentali senza decidere il protocollo.

## When to use QA / Verifier
- Prima del commit.
- Dopo l'output di Codex.
- Quando bisogna controllare che non siano stati toccati file proibiti.
- Quando bisogna confermare che le claim restino coerenti con repository e terminale.

## When to update POE_STATE.md
- Quando cambia la next action.
- Quando cambia uno stato sintetico già verificato.
- Alla chiusura di un task che sposta la priorità operativa.
- Dopo commit o review che modifica il percorso di lavoro.

## Forbidden actions
- Aprire o chiudere ricerche senza traccia repository.
- Modificare codice, API, database o logica applicativa dentro task documentali.
- Inventare stato tecnico, output o validazioni.
- Usare memoria chat come sistema di handoff operativo.
- Fare staging massivo non verificato.
