# V7 RADE STAGE-0 INPUT MANIFEST

**CLASSIFICATION:** **CONFIDENTIAL — LIMITED PURPOSE ENGINEERING ASSESSMENT**  
**NDA:** REQUIRED

## Controlled inputs

| ID | Input | State | Stage-0 use |
|---|---|---|---|
| IN-01 | V7-R3 / V7-RC-003 geometry, 18 STEP artifacts | CONTROLLED_REFERENCE | Primary CAD inspection source |
| IN-02 | V7 architecture references 100–210 + J | CONTROLLED_REFERENCE | Functional decomposition and traceability |
| IN-03 | Current model has 2 generalized coordinates | MODEL_LEVEL | Kinematic review only |
| IN-04 | q1 model range 0 to 180 mm | MODEL_LEVEL | Translation/stroke implications only |
| IN-05 | q2 model range -10 to +25 deg | MODEL_LEVEL | Seatback-motion implications only |
| IN-06 | Nominal seatback angle reference 25 deg | CONCEPT_LEVEL | Packaging context only |
| IN-07 | Rail spacing reference 420 mm | CONCEPT_LEVEL | Integration context; not vehicle hardpoint data |
| IN-08 | Interface definitions for rails, absorbers, pelvic control, seatback links/frame, lock, rebound, restraint, occupant guidance, sensor and hinge references | CONTROLLED_REFERENCE / MODEL_LEVEL | Interface and kinematic assessment |
| IN-09 | Vehicle datum and vehicle-specific hardpoint package | INPUT_REQUIRED | Required to complete seat-to-body/BIW integration |
| IN-10 | Authoritative H-point / R-point and seating reference | INPUT_REQUIRED | Required for occupant packaging and seating geometry |
| IN-11 | Vehicle restraint anchor coordinates and related package | INPUT_REQUIRED | Required for restraint-interface assessment |
| IN-12 | Occupant envelope / anthropometric package applicable to the assessment | INPUT_REQUIRED | Required for meaningful occupant clearance conclusions |
| IN-13 | Released manufacturing dimensions, tolerances, PMI/GD&T where relevant | INPUT_REQUIRED | Required for DFM/DFA and release-level dimensional conclusions |
| IN-14 | Controlled materials, joints, fasteners, absorber, lock, rebound and mass-property data | NOT_ESTABLISHED / INPUT_REQUIRED | Required for later load, dynamics and physical-performance stages |
| IN-15 | Authorized CAE model and execution evidence | NOT_ESTABLISHED | Not part of Stage-0 proof unless separately supplied |
| IN-16 | Physical test evidence | NOT_ESTABLISHED | Not part of Stage-0 proof unless separately supplied |

## Evidence discipline
No estimated mass, estimated CG, estimated inertia, assumed H/R point, assumed vehicle hardpoint, assumed BIW coordinate, assumed material, assumed fastener preload, assumed absorber law, assumed lock behavior, or assumed rebound law is to be treated as verified fact.

## Assessment boundary
Stage-0 conclusions shall be conditional where the vehicle/OEM input set is incomplete. Lack of an input is a finding, not permission to infer it.
