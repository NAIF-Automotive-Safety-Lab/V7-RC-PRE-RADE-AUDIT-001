# V7 RADE STAGE-0 DISCLOSURE BOUNDARY

**CLASSIFICATION:** **CONFIDENTIAL — LIMITED PURPOSE ENGINEERING ASSESSMENT**  
**NDA:** REQUIRED

## Permitted
The external assessment may use V7 technical architecture, supplied V7-R3 STEP geometry, relevant model-level dimensions and motion ranges, model-level interface definitions, engineering data gaps, limitations, assessment requirements, proposed-change procedure, deliverable requirements, acceptance criteria, and confidentiality controls necessary for the Stage-0 assessment.

## Required classification of numerical information
Each numerical item shall be explicitly labeled as one of:

`CONTROLLED_REFERENCE` · `MODEL_LEVEL` · `CONCEPT_LEVEL` · `INPUT_REQUIRED` · `NOT_ESTABLISHED` · `PROPOSED` · `TEST_REQUIRED`

No value may be upgraded by wording alone.

## Fail-closed boundaries
- Vehicle datum: `INPUT_REQUIRED` where absent.
- H-point / R-point: `INPUT_REQUIRED` where authoritative data are absent.
- Vehicle seat hardpoints: `INPUT_REQUIRED` where absent.
- Restraint anchor coordinates: `INPUT_REQUIRED` where absent.
- BIW geometry and attachment coordinates: `INPUT_REQUIRED` where absent.
- Physical joint axes, stops, compliance, lock/rebound behavior: `NOT_ESTABLISHED` / `TEST_REQUIRED` unless supported by evidence.
- Mass, CG and inertia: `NOT_ESTABLISHED` unless controlled evidence exists.
- Materials, fasteners, tolerances and GD&T: `INPUT_REQUIRED` / `NOT_ESTABLISHED` unless controlled evidence exists.
- CAE results: not claimed without executed and accepted CAE evidence.
- Crash/occupant safety validation: not claimed without validated test/CAE evidence.
- Manufacturing release: not claimed from STEP inspection alone.

## V7-only rule
This disclosure is written exclusively as a V7 technical assessment package. It does not rely on unrelated project history or external-project comparisons.

## Confidentiality
No public upload, portfolio use, third-party disclosure, subcontracting, external AI upload, model training, publication, or reuse for other clients.
