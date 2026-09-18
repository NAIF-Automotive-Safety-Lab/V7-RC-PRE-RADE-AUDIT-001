# V7 RADE STAGE-0 CHANGE CONTROL PROTOCOL

**CLASSIFICATION:** **CONFIDENTIAL — LIMITED PURPOSE ENGINEERING ASSESSMENT**  
**NDA:** REQUIRED

## Authority model
`01_CAD_AUTHORITY/V7_R3_CANONICAL/` is READ-ONLY and remains the sole V7 CAD authority.

`02_CAD_WORKING_COPY/` is the only modifiable CAD workspace provided for Stage-0 assessment.

A working-copy modification does not modify V7-R3 and does not acquire V7 master status automatically.

## Proposed change package
Rade may create proposed changes. Each change must be delivered under a unique `PROPOSED_CHANGE_ID` and contain:

- `PROPOSED_CHANGE_ID`
- `SOURCE_FILE`
- `SOURCE_SHA256`
- `MODIFIED_FILE`
- `MODIFIED_SHA256`
- `PART_ID`
- `CHANGE_DESCRIPTION`
- `ENGINEERING_REASON`
- `INTERFACE_IMPACT`
- `PACKAGING_IMPACT`
- `KINEMATIC_IMPACT`
- `DFM_DFA_IMPACT`
- `ASSUMPTIONS`
- `EVIDENCE`
- `STATUS`

New proposals start at `PROPOSED` unless changed by controlled project review.

## Change-register protection
Rade may create proposed-change records but may not rewrite, delete, or otherwise alter the official project change register.

## Before/after rule
Every modified CAD artifact must preserve the original source hash, provide the modified hash, identify the changed part/geometry, and state whether interfaces, packaging, kinematics, and DFM/DFA are affected.

## No silent resolution
Conflicting or missing engineering inputs remain explicitly unresolved until controlled evidence resolves them. A proposal must not silently convert an unresolved value into a final design fact.

## No automatic promotion
No Rade proposal becomes authoritative V7 geometry, manufacturing definition, or validated engineering performance merely because a modified STEP file exists.
