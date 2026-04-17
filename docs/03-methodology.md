# 03 — Methodology

## Tool Stack

| Purpose | Tool |
|---------|------|
| CAD geometry | SolidWorks (2U assembly, internal components) |
| Thermal solver (primary) | **C&R Technologies Thermal Desktop + RadCAD** |
| Thermal solver (secondary / verification) | ANSYS Workbench Mechanical — Steady-State and Transient Thermal |
| Post-processing & plots | Python (pandas, numpy, matplotlib) |
| Hand-calc sanity check | Excel (radiation-balance workbook) |

Thermal Desktop is the primary tool because it is the industry standard for spacecraft thermal modeling: it handles orbital heat fluxes (solar, albedo, Earth IR), radiative exchange via Monte Carlo ray tracing (RadCAD), and transient node solutions in one integrated workflow. ANSYS runs were used as independent verification on simplified cases.

## Model Setup

**Geometry.** 2U CubeSat (0.1 × 0.1 × 0.2 m) imported from SolidWorks. External wall modeled as a 1 mm thin shell; internal components (battery, Jetson TX2, Iridium 9603, camera, SDR, solar panels) represented as thermal masses with specified dissipation.

**Material.** Aluminum 6060 structure (ρ = 2700 kg/m³, c_p = 900 J/kg·K, k = 170 W/m·K). Surface finish swept through the design iterations — bare Al 6061, Type III gray anodize, black anodize — to study α / ε effects.

**Mesh.** Surface discretized into **~70 surface nodes on the +Z face** (target: 8×16 nodes per large face). Total model size scales linearly with the active panel count.

**Radiative exchange.** RadCAD Monte Carlo ray tracing with **5,000 rays per node** computes view factors between every surface pair (and to space and to Earth). Output is a full radiation-conductor matrix consumed by the transient solver.

**Analysis type.** Transient. Each run simulates ~6 orbits (~22,000 s) starting from a 293.15 K (20 °C) initial condition, until the temperature field reaches a quasi-steady orbital cycle.

## Load Cases

Two bounding cases are simulated per design revision (see `docs/01`):

- **Hot case:** β = 60°, solar = 1419 W/m², albedo = 0.55, full internal dissipation
- **Cold case:** β = 0°, solar = 1317 W/m², albedo = 0.18, reduced dissipation (survival-mode)

## Boundary Conditions

- External radiation to deep space (ε_space_equivalent = 1.0, T = 3 K)
- Solar heat flux applied as a time-varying profile to the sun-facing panel (see `data/orbital-heat-flux/sun_face_loads.csv`)
- Earth IR + albedo applied to the nadir-facing panel (see `data/orbital-heat-flux/earth_face_loads.csv`)
- Vacuum — no convection
- Internal component dissipation as discrete node heat sources

## Verification

1. **Hand calculation.** A simple radiation-balance spreadsheet solves σT⁴ for a single-node representation of each face. Used to bound the expected steady-state temperature before running the full transient.
2. **Case sweep.** Five design revisions (Rev 1 → Rev 5) progressively refined mesh, material properties, and internal power allocations. Temperature history convergence was checked between revisions.
3. **Orbit replay.** Applied boundary-condition profiles replicate expected duty cycle (sunlit arc / eclipse) and were sanity-checked against NASA reference values for LEO at 400 km.
