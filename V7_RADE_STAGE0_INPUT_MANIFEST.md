# V7 RADE STAGE-0 INPUT MANIFEST

**Purpose:** controlled minimum disclosure set for Rade Stage-0. **Not** a manufacturing or safety validation package.

| ID | DATA | CLASS | STATUS | STAGE-0 USE |
|---|---|---|---|---|
| R0-IN-01 | V7 stable reference architecture 100, 110L/110R, 120, 130, 140, 150L/150R, 160, 170, 180, 190, 200, 210 and J | KNOWN / DISCLOSURE_DEFINED | AVAILABLE | Understand invention architecture and stable terminology. |
| R0-IN-02 | V7 core relationship: bilateral load paths + controlled ride-down + distinct seatback rotation path + event-state transitions + rebound + restraint availability | KNOWN / DISCLOSURE_DEFINED | AVAILABLE | Assess technical disclosure coherence; not proof of performance or novelty. |
| R0-IN-03 | V6/V7 temporal state model S0 Normal, S1 Armed/Capture, S2 Ride-down, S3 Rotation Control, S4 Rebound Control, S5 Secure | KNOWN / DISCLOSURE_DEFINED | AVAILABLE | Trace the temporal/mechanical sequence disclosed. |
| R0-IN-04 | V7 12-requirement audit P0-001..P0-012 and current statuses | KNOWN | AVAILABLE | Know exactly what is defined vs. unproven. |
| R0-IN-05 | Current model-only results: 2 generalized coordinates, 180 mm model travel, q2 reference range −10..+25 deg | MODEL_DERIVABLE | AVAILABLE_WITH_LABEL | Review as model evidence only. |
| R0-IN-06 | Current interface intent IF-R4-01..09 | DESIGN_DEFINED | AVAILABLE | Trace logical interfaces and identify evidence gaps. |
| R0-IN-07 | Current readiness/gap/evidence status and source map | KNOWN | AVAILABLE | Bound every Stage-0 statement. |
| R0-IN-08 | Prior-art warning and claim-to-validation mapping from V6/V7 | KNOWN / DISCLOSURE_DEFINED | AVAILABLE | Patent-preparation review context; not legal opinion. |
| R0-IN-09 | Source revisions, artifact identities and evidence provenance metadata | KNOWN | AVAILABLE | Traceability and disclosure integrity. |

## Mandatory scope boundary
- Rade receives stable architecture, disclosure logic, current engineering-definition status, model-vs-fact separation, and evidence provenance.
- Vehicle-specific and production-release data are not to be invented to fill disclosure gaps.
- Model-only values may be shown only with an explicit model/evidence label.
- No item with `SOURCE_REQUIRED`, `OEM_INPUT_REQUIRED`, or `TEST_REQUIRED` status becomes a project fact merely because it appears in the package.