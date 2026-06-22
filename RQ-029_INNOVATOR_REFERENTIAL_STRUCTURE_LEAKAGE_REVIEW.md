# RQ-029 Innovator referential structure leakage review

Status:
ACCEPT_WITH_CONSTRAINTS

Scope:
Innovator / PM stress-test only

Reviewed file:
`RQ-029_A_ONLY_REFERENTIAL_STRUCTURE_RESEARCH_FRAMING.md`

Core finding:
`RQ-029` can remain useful and safe only if referential structure is treated as existence of a referential relation in research-framing, not as proof that a reference is good, resolvable, unique or operationally usable.

Stress-test outcome by question:

## 1. Does referential structure inevitably imply a registry?

Finding:
No, not inevitably.
Risk appears only if referential structure is reinterpreted as needing a canonical lookup source.

Constraint:
Referential structure must not imply existence of any canonical registry, node directory, identity table or entity catalog.

## 2. Can domain entity be used safely without becoming a whitelist?

Finding:
Yes, but only if domain entity remains a research placeholder and not an allowed-class list.

Constraint:
Domain entity must not become a bounded list of approved entity classes, allowed namespaces or protocol-approved entity types.

## 3. Can referential structure be discussed without requiring disambiguation?

Finding:
Yes, but only at the level of possible relation existence.
Leakage starts when the question shifts from whether a relation can exist to which exact entity is meant.

Constraint:
`RQ-029` must not require entity disambiguation, canonical identity resolution or uniqueness of referent.

## 4. Can existence of reference be separated from correctness or validity of reference?

Finding:
Yes.
This is the main safe core of `RQ-029`.
The research can ask whether an evidence unit can structurally point toward a domain entity without asking whether that pointing is correct.

Constraint:
Existence of reference must remain fully separable from correctness, validity, authenticity or factual match.

## 5. Does this boundary accidentally create an admissibility rule?

Finding:
Potentially yes, if referential structure is later read as required for admissibility beyond `RQ-029`.

Constraint:
`RQ-029` must not imply that lacking referential structure makes an evidence unit inadmissible, invalid or excluded elsewhere in protocol logic.

## 6. Does this boundary accidentally create a validation rule?

Finding:
Potentially yes, if any later task turns referential structure into a must-pass evidence check.

Constraint:
Referential structure must remain research-framing only, not a validation condition, not a pass/fail rule and not a verification step.

## 7. Does this boundary accidentally imply implementation fields, IDs, schemas, database tables, API contracts or node registries?

Finding:
Yes, this is a real leakage vector.
The terms reference, domain entity and structure can drift quickly toward field names, identifiers and storage contracts.

Constraint:
`RQ-029` must not imply required IDs, schemas, columns, tables, contracts, endpoints, payload shapes or registries.

## 8. Does RQ-029 remain useful if it cannot verify correctness, validity, uniqueness or disambiguation?

Finding:
Yes.
Its residual usefulness is exactly to test whether referentiality can be discussed as a structural research object before operational and validating machinery exists.

Main leakage risks found:

* drift from domain entity to approved entity list
* drift from reference existence to reference correctness
* drift from reference relation to disambiguation requirement
* drift from research property to admissibility rule
* drift from research property to validation rule
* drift from abstract referential structure to IDs, schemas, tables or registries

Boundary constraints required:

* treat domain entity as research placeholder only
* treat referential structure as possible relation existence only
* separate existence from correctness, validity, authenticity and uniqueness
* prohibit disambiguation requirement
* prohibit admissibility spillover
* prohibit validation-rule spillover
* prohibit implementation-shaped artifacts such as IDs, schemas, tables, contracts and registries

Status interpretation:

* `RQ-029` remains OPEN / RESEARCH-FRAMING
* `RQ-029` Decision remains `NONE`
* `RQ-029` is not answered
* `RQ-029` is not validated
* `RQ-029` is not closed
* `PD-029` is not created
* `RQ-026`, `RQ-027` and `RQ-028` remain OPEN / RESEARCH-FRAMING with Decision `NONE`

Next required PM action:
Open a PM refinement task for `RQ-029` wording so the accepted research boundary explicitly blocks whitelist drift, admissibility spillover, validation-rule spillover and implementation-shaped leakage.
