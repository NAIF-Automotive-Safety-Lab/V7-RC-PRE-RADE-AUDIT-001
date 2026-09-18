# V7 CANONICAL DATUM AND COORDINATE BASELINE

## Gate
**Project-wide canonical coordinate frame: CONFLICTED — NOT DECLARED.**

The Master Audit preserves multiple coordinate conventions and identifies C-001 as a direct contradiction. No transform is declared here. No source wins by convenience.

## Coordinate records

| Parameter | Reference | Current value | Normalized status | Source | Gap | Conflict |
|---|---|---|---|---|---|---|
| V5/R0 coordinate convention | SYSTEM | X=lateral; Y=longitudinal (front = negative Y); Z=vertical | CONFLICTED | V5_PARAMS / V7_R0_PACKAGE | Conflicts with current reconstruction and V7 R4 model frame. | C-001 |
| Current reconstruction coordinate convention | SYSTEM | X=longitudinal; Y=lateral; Z=up | CONFLICTED | V7_RECON_SCRIPT | Conflicts with legacy V5/R0 convention; source-to-model transforms are not authoritative. | C-001 |
| R4 model coordinate convention | SYSTEM | X=longitudinal carriage travel; Y=lateral vehicle-right; Z=up | CONFLICTED | V7_R4_MODEL | Not established as physical vehicle datum; inherits unresolved source mapping. | C-001 |
| vehicle datum | SYSTEM |  | OEM_REQUIRED | V7_R5_VEHICLE + V6/V7 disclosure | Authoritative vehicle-specific datum, package, hardpoints or anchor data are absent. |  |
| primary datum | 100–210/J |  | MISSING | V7_PMI_GDT + current engineering definitions | No released production drawing/PMI/GD&T package. |  |
| secondary datum | 100–210/J |  | MISSING | V7_PMI_GDT + current engineering definitions | No released production drawing/PMI/GD&T package. |  |
| tertiary datum | 100–210/J |  | MISSING | V7_PMI_GDT + current engineering definitions | No released production drawing/PMI/GD&T package. |  |
| H-point | SYSTEM |  | CONFLICTED | V7_R5_VEHICLE + V6/V7 disclosure | Authoritative vehicle-specific datum, package, hardpoints or anchor data are absent. | C-002 |
| R-point/SgRP | SYSTEM |  | OEM_REQUIRED | V7_R5_VEHICLE + V6/V7 disclosure | Authoritative vehicle-specific datum, package, hardpoints or anchor data are absent. |  |
| left/right hardpoint coordinates | 110L/110R |  | OEM_REQUIRED | V7_R5_VEHICLE + V6/V7 disclosure | Authoritative vehicle-specific datum, package, hardpoints or anchor data are absent. |  |
| restraint anchor coordinates | 190 |  | OEM_REQUIRED | V7_R5_VEHICLE + V6/V7 disclosure | Authoritative vehicle-specific datum, package, hardpoints or anchor data are absent. |  |

## Canonical declaration rule

A single project frame is not declared until the conflicting V5/R0 and current reconstruction/R4 conventions are reconciled by controlled evidence. No coordinate transform, H/R-point transform, rail datum, or BIW mapping is invented in this baseline.

## Vehicle frame

Vehicle datum, H-point/R-point, seat hardpoints, restraint anchor coordinates, and BIW interface coordinates remain **OEM_REQUIRED**.

## Local seat/joint frames

The current R4 model contains model-level axis semantics, including a seatback rotation axis and rail translation coordinate, but these remain **MODEL_ONLY** or **MISSING** until physical joint/datums are released.

## Engineering use

No numeric coordinate from a conflicted frame may be promoted to canonical engineering fact. All dependent dimensions, packaging checks, kinematic transforms, and hardpoint compatibility checks remain gated by datum reconciliation.
