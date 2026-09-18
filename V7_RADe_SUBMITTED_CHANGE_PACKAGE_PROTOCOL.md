# V7 RADe SUBMITTED CHANGE PACKAGE PROTOCOL

**TASK_ID:** `V7-RADE-DISCLOSURE-HARDENING-GATE-005`  
**V7 AUTHORITY:** `V7-RC-003` remains immutable.  
**CONFIDENTIALITY:** **CONFIDENTIAL — LIMITED PURPOSE ENGINEERING ASSESSMENT**  
**NDA:** REQUIRED BEFORE TRANSFER

## Purpose
This protocol governs any modification proposed by Rade after receipt of the external Stage-0 package. It protects the authoritative V7 baseline while allowing controlled engineering proposals.

## Authority separation
- `CANONICAL_V7_R3/` = read-only V7-R3 CAD authority.
- `V7_RADE_WORKING_COPY/` = only permitted Rade modification area.
- Working-copy changes are **NON-AUTHORITATIVE** until separately reviewed and promoted.
- Rade may create proposals.
- Rade may **not** rewrite, delete, or edit the official project change register.

## Required proposed-change submission fields
Every proposed change must be delivered as a separate package containing these exact fields:

```text
PROPOSED_CHANGE_ID = <unique identifier>
ORIGINAL_FILE_HASH = <SHA-256 of unmodified source file>
MODIFIED_FILE_HASH = <SHA-256 of proposed file>
CHANGED_PART = <part / V7 reference>
CHANGED_GEOMETRY = <precise geometry delta; do not use “improved” or other non-traceable wording>
REASON = <engineering reason for the proposed change>
INTERFACE_IMPACT = <interfaces/joints affected or NONE with basis>
KINEMATIC_IMPACT = <DOF/stroke/angle/state impact or NONE with basis>
PACKAGING_IMPACT = <clearance/envelope/H-R-point/vehicle-interface impact or UNKNOWN>
DFM_IMPACT = <manufacturing/process/inspection impact or UNKNOWN>
ASSUMPTIONS = <explicit assumptions; no silent values>
EVIDENCE = <drawings, measurements, test records, analyses, or other traceable evidence>
STATUS = PROPOSED
```

## Non-negotiable rules
1. Do not overwrite a canonical R3 file.
2. Do not delete or rewrite the official project change register.
3. Do not promote a working-copy file to V7 authority by filename, visual fit, or existence.
4. Do not silently resolve `C-001` or any dimensional/coordinate conflict.
5. Do not infer vehicle datum, H/R points, BIW/hardpoints, restraint anchors, materials, fasteners, tolerances, mass properties, absorber law, lock behavior, rebound behavior, or physical performance.
6. Do not treat geometric touching/overlap as physical load-path proof.
7. Do not treat model motion as physical validation.

## Review status vocabulary
`PROPOSED` = submitted by Rade and not yet authoritative.  
`UNDER_REVIEW` = under project-authority engineering review.  
`ACCEPTED_FOR_TEST` = approved for a specified validation activity only.  
`REJECTED` = not accepted.  
`PROMOTED` = separately incorporated by project authority with its own controlled revision/change record.

## Evidence firewall
A proposed change does not establish CAE validation, crash performance, occupant protection, regulatory compliance, or manufacturing readiness. Those claims require their own authorized evidence gates.

## Confidentiality
**CONFIDENTIAL — LIMITED PURPOSE ENGINEERING ASSESSMENT**. NDA required before transfer. No public upload. No portfolio use. No third-party disclosure. No subcontracting. No onward transfer. No external AI upload. No training use.

## Commercial boundary
**ONE fixed-price Stage-0 result.** Hours are not the purchased output. No open-ended hourly expansion.
