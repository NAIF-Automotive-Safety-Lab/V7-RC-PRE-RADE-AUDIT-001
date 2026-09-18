# V7 CANONICAL STATE MACHINE BASELINE

## Canonical vocabulary — frozen for this baseline

| ID | Canonical state | Meaning at controlled vocabulary layer |
|---|---|---|
| S0 | **Normal** | Normal/resting operating state. |
| S1 | **Armed/Capture** | Event preparation / capture state. |
| S2 | **Pelvis Lock/Capture** | Explicit pelvic capture/lock state. |
| S3 | **Ride-Down** | Controlled longitudinal ride-down state. |
| S4 | **Rotation/Rebound** | Controlled seatback rotation and rebound-management state. |
| S5 | **Secure/Post-event** | Post-event secure state. |

## Evidence-layer separation

**DISCLOSED STATE:** The project disclosure and P0-controlled terminology establish the six-label vocabulary above. Older V6 disclosure and older P0/model artifacts use different labels; those differences are preserved as conflicts C-011 and C-012.

**MODEL STATE:** The current R4 implementation/model contains a different operational label set and does not explicitly implement the six canonical labels as a physical state machine. Model-state semantics therefore remain **CONFLICTED / MODEL_ONLY** and are not silently mapped.

**PHYSICAL STATE:** No physical validation evidence establishes that the six canonical states occur in hardware with the required triggers, timing, engagement, release, reset, fault behavior, or fail-safe behavior.

**VALIDATED STATE:** No S0–S5 state transition sequence is validated as a T-OCS physical crash result.

## Required evidence to move beyond terminology control

1. Controlled implementation mapping from each canonical state to actual 170/140/130/150/180 mechanisms.
2. Trigger thresholds and transition timing from authorized dynamic testing.
3. Lock engagement/disengagement/reset/fault testing.
4. Rebound behavior and reset testing.
5. End-stop and rail overtravel evidence.

## Prohibition

No alternate S0–S5 terminology may be introduced into the canonical baseline. No model label is to be represented as a validated physical state.
