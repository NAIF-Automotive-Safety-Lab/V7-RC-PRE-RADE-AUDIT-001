# V7 RADE STAGE-0 DELIVERABLE SCHEMA

**CLASSIFICATION:** **CONFIDENTIAL — LIMITED PURPOSE ENGINEERING ASSESSMENT**  
**NDA:** REQUIRED

Rade shall return the following twelve deliverables as the Stage-0 assessment result:

1. `01_STAGE0_ENGINEERING_ASSESSMENT.md`
2. `02_PACKAGING_AND_OCCUPANT_ASSESSMENT.md`
3. `03_CLEARANCE_AND_KINEMATICS_REGISTER.csv`
4. `04_HARDPOINT_BIW_INTERFACE_ASSESSMENT.md`
5. `05_DFM_DFA_ASSESSMENT.md`
6. `06_ENGINEERING_DATA_GAP_REGISTER.csv`
7. `07_PROPOSED_CHANGE_REGISTER.csv`
8. `08_PROPOSED_CAD_CHANGE_PACKAGE/`
9. `09_BEFORE_AFTER_CHANGE_TRACEABILITY.md`
10. `10_STAGE0_FINAL_FINDINGS.md`
11. `11_STAGE0_ASSUMPTIONS_AND_LIMITATIONS.md`
12. `12_STAGE0_DELIVERABLE_MANIFEST.json`

## Required content by deliverable

### 01_STAGE0_ENGINEERING_ASSESSMENT.md
Address all ST0-01 through ST0-20. For every finding identify evidence basis, state classification, consequence, and required next action.

### 02_PACKAGING_AND_OCCUPANT_ASSESSMENT.md
Separate geometry-observable findings from H/R-point, occupant-envelope, restraint, and vehicle-dependent conclusions.

### 03_CLEARANCE_AND_KINEMATICS_REGISTER.csv
Required columns: `ID,AREA,ENTITY_OR_INTERFACE,LOCATION_OR_REFERENCE,EVIDENCE_STATE,TYPE,MODEL_LEVEL_FINDING,STATIC_IMPLICATION,DYNAMIC_KINEMATIC_IMPLICATION,INPUT_REQUIRED,STATUS,TRACE`

### 04_HARDPOINT_BIW_INTERFACE_ASSESSMENT.md
Identify what can be assessed from supplied V7 geometry and what requires authoritative vehicle/BIW/hardpoint data.

### 05_DFM_DFA_ASSESSMENT.md
Record manufacturability/assembly observations only; do not claim manufacturing release.

### 06_ENGINEERING_DATA_GAP_REGISTER.csv
Required columns: `GAP_ID,DATA_ITEM,STATE,WHY_REQUIRED,DEPENDENT_ASSESSMENT,OWNER_OR_SOURCE_REQUIRED,EVIDENCE_REQUIRED,STATUS`

### 07_PROPOSED_CHANGE_REGISTER.csv
Required columns: `PROPOSED_CHANGE_ID,SOURCE_FILE,SOURCE_SHA256,MODIFIED_FILE,MODIFIED_SHA256,PART_ID,CHANGE_DESCRIPTION,ENGINEERING_REASON,INTERFACE_IMPACT,PACKAGING_IMPACT,KINEMATIC_IMPACT,DFM_DFA_IMPACT,ASSUMPTIONS,EVIDENCE,STATUS`

### 08_PROPOSED_CAD_CHANGE_PACKAGE/
Each proposed CAD change must be independently traceable by before/after SHA-256 and tied to one register entry.

### 09_BEFORE_AFTER_CHANGE_TRACEABILITY.md
Provide an exact source-to-modified mapping and explain what changed and what did not.

### 10_STAGE0_FINAL_FINDINGS.md
Summarize accepted observations, unresolved blockers, conditional findings, and required next inputs without upgrading evidence state.

### 11_STAGE0_ASSUMPTIONS_AND_LIMITATIONS.md
List every assumption explicitly and distinguish it from controlled reference data and measured/validated evidence.

### 12_STAGE0_DELIVERABLE_MANIFEST.json
List all returned Stage-0 result files, their SHA-256 hashes, status, and any proposed-change package membership.
