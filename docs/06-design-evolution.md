# 06 — Iterative Design

The 2U thermal model was built up over five revisions. Each revision was a scoped iteration driven by a flaw found in the previous one.

## Timeline

| Rev             | Focus                               | Change from prior                                                                                                                                                                                      |
| --------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1U Test**     | First-principles checkout           | 1U geometry, three simplified models (hot / eclipse / intermediary) in ANSYS Mechanical. Used to verify hand-calc absorbed powers and sanity-check boundary conditions.                                |
| **2U Baseline** | Initial 2U cold case                | Moved to 2U geometry; bare Al 6061 + Type III black anodize; ANSYS Mechanical steady-state.                                                                                                            |
| **Rev 3**       | Migration to Thermal Desktop        | Re-imported geometry into Thermal Desktop.                                                                                                                                                             |
| **Rev 4**       | Internal components                 | Added battery, Jetson TX2, Iridium 9603, camera, SDR as thermal nodes with per-case dissipation. First comparison against component operational limits.                                                |
| **Rev 5**       | Finer mesh + consistent power model | 8×16 nodes per face (~70 nodes on +Z alone), unified hot / cold load cases, 5,000-ray RadCAD sweep.                                                                                                    |

## What Changed and Why

**1U → 2U.** Doubling the volume changes the surface-to-mass ratio and the internal component layout; the 1U results were never going to transfer directly, but the 1U runs were cheap and quickly caught mistakes in how absorbed-flux boundary conditions were being applied in the solver.

**ANSYS → Thermal Desktop.** ANSYS Mechanical handles conduction and surface-to-ambient radiation well but does not natively model orbital mechanics and orbital heat fluxes or surface-to-surface radiative exchange with view factors.

**Coarser → finer mesh.** Rev 2 used ~8 nodes per face, Rev 5 uses ~128 nodes per face (~70 on +Z after geometry simplification). The finer mesh resolves temperature gradients across the sun-facing panel that the coarser model was averaging away.

**Consistent hot / cold definition.** Early revisions mixed beta / solar-flux / albedo values between runs. Seperating the two cases allowed for a more accurate solution to analyze.
