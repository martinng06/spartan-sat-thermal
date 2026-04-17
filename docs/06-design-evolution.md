# 06 — Design Evolution (Rev 1 → Rev 5)

The 2U thermal model was built up over five revisions between September 2025 and March 2026. Each revision was a scoped iteration driven by a specific question or gap found in the previous one.

## Timeline

| Rev | Date | Focus | Change from prior |
|-----|------|-------|-------------------|
| **1U Test** | 2025-09-22 | First-principles checkout | 1U geometry, three simplified models (hot / eclipse / intermediary) in ANSYS Mechanical. Used to verify hand-calc absorbed powers and sanity-check boundary conditions. |
| **2U Baseline** | 2025-10-11 | Initial 2U cold case | Moved to 2U geometry; bare Al 6061 + Type III black anodize; ANSYS Mechanical steady-state. |
| **2U Baseline Rev 2** | 2025-10-17 | Mesh refinement + hot case | 8-node-per-face mesh; both hot and cold cases; produced first full-coverage temperature spread (hot: 42–82 °C, cold: 17–57 °C). |
| **Rev 3** | 2025-11 → 2025-12 | Migration to Thermal Desktop | Re-imported geometry into Thermal Desktop. Configured RadCAD radiative network. First run of the full transient with orbital heat-flux profiles from `data/orbital-heat-flux/`. |
| **Rev 4** | 2026-01 → 2026-02 | Internal components | Added battery, Jetson TX2, Iridium 9603, camera, SDR as thermal nodes with per-case dissipation. First comparison against component operational limits. |
| **Rev 5** | 2026-03 | Finer mesh + consistent power model | 8×16 nodes per face (~70 nodes on +Z alone), unified hot / cold load cases with the Tables in `docs/02-thermal-requirements.md`, 5,000-ray RadCAD sweep. Output is the transient file in `data/raw-simulation/`. |

## What Changed and Why

**1U → 2U.** Doubling the volume changes the surface-to-mass ratio and the internal component layout; the 1U results were never going to transfer directly, but the 1U runs were cheap and quickly caught mistakes in how absorbed-flux boundary conditions were being applied in the solver.

**ANSYS → Thermal Desktop.** ANSYS Mechanical handles conduction and surface-to-ambient radiation well but does not natively model orbital heat fluxes or surface-to-surface radiative exchange with view factors. Thermal Desktop is the industry standard for this. Rev 3 was the switch.

**Coarser → finer mesh.** Rev 2 used ~8 nodes per face, Rev 5 uses ~128 nodes per face (~70 on +Z after geometry simplification). The finer mesh resolves temperature gradients across the sun-facing panel that the coarser model was averaging away.

**Blank internals → per-component dissipation.** Rev 2 carried the structure only; Rev 4 introduced the component thermal budget (battery, Jetson, Iridium, camera, SDR) and solved the full internal + external heat balance. Most of the design-relevant insights (battery hot-case failure) come from Rev 4 onward.

**Consistent hot / cold definition.** Early revisions mixed beta / solar-flux / albedo values between runs. Rev 5 locks the two bounding cases (β = 60°, solar = 1419 W/m², albedo = 0.55 for hot; β = 0°, solar = 1317, albedo = 0.18 for cold) as the authoritative load cases for all downstream work.

## What's Next (Rev 6 Backlog)

1. Add a coating patch (NZOT white paint or silvered FEP) on the +Z panel, re-run hot case. Target: battery stays below +35 °C op limit with 5 °C margin.
2. Introduce a survival-heater on the battery for the cold case and size its duty cycle.
3. Add MLI blanketing on the side panels that don't need to be radiators.
4. Execute the thermal-vacuum test campaign in [`docs/07-thermal-vacuum-test-plan.md`](07-thermal-vacuum-test-plan.md) and correlate the model against the measured data (target ±5 °C on ≥ 90% of nodes).
