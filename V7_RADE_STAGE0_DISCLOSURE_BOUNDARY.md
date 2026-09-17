# V7 RADE STAGE-0 DISCLOSURE BOUNDARY

## MAY BE DISCLOSED / REVIEWED
- Stable V7 reference numerals and functional decomposition.
- V6/V7 temporal state model and disclosed mechanical relationships.
- Claim-to-validation mapping and proposed observables.
- Current engineering-definition and gap status.
- Explicit model-only results with their model status labels.
- Source identities, revisions, evidence provenance and current blocker statements.

## MUST NOT BE PROMOTED TO PROJECT FACT
- Vehicle-specific datum, seat hardpoints, H-point/R-point, restraint anchor coordinates and BIW mounting details — `OEM_INPUT_REQUIRED` — Not currently evidenced; must not be inferred.
- Unreleased exact manufacturing dimensions/tolerances/GD&T not present in authoritative released drawings — `SOURCE_REQUIRED` — No release evidence; prevents false precision.
- Supplier-confirmed material/fastener allocations not backed by direct controlled evidence — `SOURCE_REQUIRED` — Current supplier confirmation remains zero.
- Physical absorber, lock, rebound and joint characterization results not actually performed — `TEST_REQUIRED` — No physical evidence exists.
- Mass/CG/inertia as project facts where not measured/controlled — `SOURCE_REQUIRED / TEST_REQUIRED` — Current values unresolved.
- Vehicle crash pulse, initial crash conditions, validated restraint inputs and structural load cases — `OEM_INPUT_REQUIRED` — External inputs remain unresolved.
- CAE outputs, injury metrics, safety factors or correlation claims not supported by authorized execution and acceptance criteria — `BLOCKED` — CAE is not validated/executed for release use.
- Manufacturing-release artifacts, production supplier data, PPAP/APQP, tooling/SOP evidence — `BLOCKED / NOT_EVIDENCED` — Production release is not established.

## PASS FIREWALL
1. Any PASS on H-point/R-point without authoritative vehicle/package reference and traceable coordinate definition.
2. Any PASS on occupant packaging without vehicle-specific envelope, seating reference and clearance verification.
3. Any PASS on backrest angle/range/end-stops that treats model reference range or concept geometry as physical capability.
4. Any PASS on clearance/interference without adequate intended-contact classification and authoritative geometry/motion verification.
5. Any PASS on rail/hardpoint/BIW integration without controlled vehicle mounting geometry and relevant load-interface evidence.
6. Any PASS on materials without controlled material identity/grade/density/certification mapped to the intended V7 part.
7. Any PASS on PMI/GD&T/tolerances without released authoritative drawings/PMI and configuration control.
8. Any PASS on fasteners/preload without exact hardware identity plus controlled installation/preload data.
9. Any PASS on 130/170/180/joint behavior without actual required component characterization and traceable raw results.
10. Any PASS on critical load-path capacity based only on topology, geometric touching, or model motion.
11. Any PASS on CAE validation while critical inputs remain unresolved or the required solver/model execution evidence is absent.
12. Any PASS on crash/occupant safety, injury reduction, regulatory compliance, OEM approval, or manufacturing readiness without their corresponding evidence gates.
13. Any overall PASS that suppresses a known blocker or silently converts an assumption/reference/target into a confirmed fact.

## FAIL-CLOSED RULE
Rade Stage-0 must remain a disclosure/review stage. When a required fact is missing, the correct output is `SOURCE_REQUIRED`, `OEM_INPUT_REQUIRED`, `TEST_REQUIRED`, `BLOCKED`, or another explicitly bounded status—not an inferred PASS.