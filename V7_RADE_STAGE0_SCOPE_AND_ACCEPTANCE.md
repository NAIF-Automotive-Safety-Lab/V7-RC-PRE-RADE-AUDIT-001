# V7 RADE STAGE-0 SCOPE AND ACCEPTANCE

**CLASSIFICATION:** **CONFIDENTIAL — LIMITED PURPOSE ENGINEERING ASSESSMENT**  
**NDA:** REQUIRED

## Stage-0 scope
The assessment shall examine the current V7 engineering definition, using the supplied V7-R3 STEP geometry and controlled Stage-0 references, and shall distinguish evidence from assumptions and inputs required from the vehicle/OEM context.

## Controlled V7 architecture
- `100` — Primary/base reference
- `110L / 110R` — Dual-rail reference
- `120` — Carriage / translation reference
- `130L / 130R` — Ride-down absorber references
- `140` — Pelvic-control reference
- `150L / 150R` — Seatback rotation-link references
- `160` — Seatback structural frame reference
- `170` — Lock reference
- `180` — Rebound-management reference
- `190` — Restraint-interface reference
- `200` — Occupant-guidance reference
- `210` — Sensor-interface reference
- `J` — Hinge/pivot reference

## Controlled model-level numerical references
The following values may be used only with the stated evidence state:

| Item | Value | Unit | Evidence state | Use boundary |
|---|---:|---|---|---|
| Generalized-coordinate count | 2 | coordinates | MODEL_LEVEL | Model-level kinematic assessment only |
| Translation coordinate q1 range | 0 to 180 | mm | MODEL_LEVEL | Model-level stroke discussion only; not physical capability |
| Seatback rotation coordinate q2 minimum | -10 | deg | MODEL_LEVEL | Model-level range only; not physical stop capability |
| Seatback rotation coordinate q2 maximum | +25 | deg | MODEL_LEVEL | Model-level range only; not physical stop capability |
| Nominal seatback angle reference | 25 | deg | CONCEPT_LEVEL | Packaging reference only |
| Rail spacing reference | 420 | mm | CONCEPT_LEVEL | Not an OEM hardpoint spacing; requires vehicle datum confirmation |

Any other numerical value used by the assessor must be classified as `CONTROLLED_REFERENCE`, `MODEL_LEVEL`, `CONCEPT_LEVEL`, `INPUT_REQUIRED`, `NOT_ESTABLISHED`, `PROPOSED`, or `TEST_REQUIRED`.

## Twenty assessment areas

| ID | Assessment area | Minimum assessment question | Required evidence status |
|---|---|---|---|
| ST0-01 | H-point / R-point dependency | What seat/occupant results depend on authoritative H/R-point definition? | INPUT_REQUIRED where absent |
| ST0-02 | Occupant package | Is the supplied geometry compatible with the required occupant envelope? | INPUT_REQUIRED for vehicle/occupant reference |
| ST0-03 | Torso/backrest geometry | What does the seatback geometry imply for torso support and package space? | Geometry + explicit assumptions |
| ST0-04 | Backrest angle and motion | What are the packaging implications of model-level q2 motion? | MODEL_LEVEL; physical limits not established |
| ST0-05 | Occupant clearance envelope | Where are likely clearance checks required? | INPUT_REQUIRED for occupant envelope |
| ST0-06 | Static interference | Which supplied geometries require static interference review? | Geometry-traceable |
| ST0-07 | Dynamic/kinematic clearance implications | Which clearances depend on q1/q2 motion? | MODEL_LEVEL; no dynamic validation claim |
| ST0-08 | Rail integration | Are rail/runner interfaces sufficiently defined for assessment and integration? | Partial/model-level; vehicle interface input required |
| ST0-09 | Seat-to-body hardpoint integration | Are mounting locations traceable to vehicle geometry? | INPUT_REQUIRED where absent |
| ST0-10 | BIW interface logic | What vehicle-body information is required to complete interface assessment? | INPUT_REQUIRED |
| ST0-11 | Load-path/interface observations | Are the defined model interfaces coherent enough for Stage-0 review? | Model-level only; capacity not established |
| ST0-12 | Kinematic conflicts | Are q1/q2, links, hinge, lock, and rebound semantics internally coherent? | Model-level; physical semantics require evidence |
| ST0-13 | Packaging feasibility | What can be accepted now and what is conditional on vehicle inputs? | Conditional only; no visual-fit PASS |
| ST0-14 | Manufacturing feasibility observations | What manufacturability risks are visible from current geometry? | Observation only |
| ST0-15 | DFM/DFA observations | What part count, access, assembly, feature, and joining issues should be reviewed? | Observation only; no manufacturing release |
| ST0-16 | Missing dimensional data | Which dimensions are missing or require controlled clarification? | Explicit gap register |
| ST0-17 | Missing mass-property data | What mass/CG/inertia inputs are missing? | NOT_ESTABLISHED unless controlled evidence exists |
| ST0-18 | Missing material/fastener data | What material, joint, and fastener information is missing? | INPUT_REQUIRED / NOT_ESTABLISHED |
| ST0-19 | Missing validation data | What testing/CAE evidence is needed for later stages? | TEST_REQUIRED / NOT_CLAIMED |
| ST0-20 | Proposed engineering corrections | What changes are justified, why, and how would they be controlled? | PROPOSED; traceable; no automatic promotion |

## Acceptance criteria
The Stage-0 deliverable is acceptable only when all twenty areas are addressed; findings are traceable to supplied geometry/data; missing inputs are explicit; assumptions are separated from evidence; H/R-point and vehicle hardpoint limits are explicit; static and dynamic clearance are distinguished; kinematic conflicts are documented; DFM/DFA observations are documented; proposed changes are separate from the existing V7 definition; and no unsupported validation or manufacturing/safety claim is made.

## Automatic failure conditions
The Stage-0 deliverable fails if it invents H/R points, vehicle hardpoints, BIW coordinates, materials, masses, CG/inertia, absorber laws, lock/rebound characteristics; silently resolves a known dimensional/coordinate conflict; converts model dimensions to manufacturing facts; overwrites canonical V7; submits untraceable geometry; or claims crash, CAE, safety, regulatory, or manufacturing validation without corresponding evidence.
