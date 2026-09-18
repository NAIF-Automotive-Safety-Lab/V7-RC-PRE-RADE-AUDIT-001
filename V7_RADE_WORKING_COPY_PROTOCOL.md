# V7 RADE WORKING COPY PROTOCOL

**Authority:** V7-R3 remains immutable. The working copy is non-authoritative.

**Modification right:** Rade may modify only `V7_RADE_WORKING_COPY/`. Canonical/reference snapshots are view-only.

**PROPOSED_CHANGE rule:** Every modified CAD artifact must be identified as `PROPOSED_CHANGE` and recorded in `V7_RADE_PROPOSED_CHANGE_REGISTER.csv`. Such modifications have no authoritative V7 status.

**CAD representation:** The approved geometry is V7-R3 STEP. No native CATIA V5 master is available in the controlled payload. STEP is therefore a geometry exchange/assessment representation, not native master CAD.

**Coordinate rule:** Do not resolve C-001. Model coordinates may be used for internal assessment only. Do not convert them into vehicle coordinates or infer vehicle H/R points, hardpoints or BIW geometry without authorized OEM datum evidence.

**Conflict rule:** Conflicting values must remain conflicting until controlled evidence resolves them.

**Fail-closed data:** H/R points, BIW, vehicle hardpoints, materials, mass/CG/inertia, fasteners, joint compliance, absorber law, lock behavior, rebound behavior, production tolerances, CAE inputs and crash pulse remain unresolved controls.

**Stage-0 use:** Identify packaging problems, hardpoint dependencies, kinematic conflicts, DFM/DFA issues and justified proposed engineering solutions. Do not certify V7.

**Provenance:** `SOURCE_PROJECT_COMMIT_SHA=f562a8cfe00835f1919ab3683bf17b3ae407100b`; `AUDIT_REPOSITORY_COMMIT_SHA=NOT_ESTABLISHED_IN_AVAILABLE_RECORDS`.
