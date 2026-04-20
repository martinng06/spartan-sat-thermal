# 03 — Methodology

## Tool Stack

| Purpose                 | Tool                                          |
| ----------------------- | --------------------------------------------- |
| CAD                     | SolidWorks (2U assembly, internal components) |
| Thermal solver          | Thermal Desktop + Sinda                       |
| Post-processing & plots | Python (pandas, numpy, matplotlib)            |
| Hand-calc sanity check  | Excel                                         |

Thermal Desktop is the primary tool because it is the industry standard for spacecraft thermal modeling. It handles orbital heat fluxes (solar, albedo, Earth IR), radiative exchange via Monte Carlo ray tracing, and transient node solutions in one integrated workflow.

## Model Setup

**Geometry.** 2U CubeSat (0.1 × 0.1 × 0.2 m) imported from SolidWorks. Internal components (battery, Jetson TX2, Iridium 9603, camera, SDR, solar panels) represented as thermal masses with specified dissipation.

**Material.** Aluminum 6060 structure (ρ = 2700 kg/m³, c_p = 900 J/kg·K, k = 170 W/m·K). Surface finish swept through the design iterations starting from bare aluminum to grey type 3 annodized.

**Mesh.** Surface discretized into ~70 surface nodes on the +Z face (target: 8×16 nodes per large face). Total model size scales linearly with the active panel count.

**Radiative exchange.** RadCAD Monte Carlo ray tracing with 5,000 rays per node computes view factors between every surface pair (to space and to Earth).

**Analysis type.** Transient

## Load Cases

Two bounding cases are simulated per design revision

- **Hot case:** β = 60°, solar = 1419 W/m², albedo = 0.55, full internal dissipation
- **Cold case:** β = 0°, solar = 1317 W/m², albedo = 0.18, reduced dissipation

## Boundary Conditions

- External radiation to deep space (ε = 1.0, T = 3 K)
- Solar heat flux applied as a time-varying profile to the sun-facing panel
- Earth IR + albedo applied to the nadir-facing panel
- Vacuum — no convection
- Internal component dissipation as discrete node heat sources

## Verification

1. **Hand calculation.** A simple radiation-balance spreadsheet solves σT⁴ for a single-node representation of each face.
