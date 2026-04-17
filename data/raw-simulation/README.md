# Raw Simulation Output — Rev 5 Transient Temperatures

`2ucubesat-rev5-transient-temperatures.xlsx` — direct export of transient nodal temperature history from the final Rev 5 thermal simulation of the Spartan Sat 2U CubeSat.

## What's inside

Two worksheets, one per load case:

| Sheet | Load case | Beta angle | Solar flux | Albedo |
|-------|-----------|-----------|------------|--------|
| `hotcase` | Worst-case hot (high beta, high albedo, summer solstice) | 60° | 1419 W/m² | 0.55 |
| `coldcase` | Worst-case cold (beta 0, low albedo, winter solstice) | 0° | 1317 W/m² | 0.18 |

## Structure

Each sheet is ~100 rows × 75 columns:

- **Column A (`Times`):** simulation time in seconds (0 → ~22,000 s, ~6 orbits)
- **Columns B–BV:** instantaneous nodal temperature in Kelvin for each of the 71 surface nodes on the +Z (sun-facing) panel. Node IDs are `POSZCUBESAT.xxx`, matching the Thermal Desktop mesh.
- **Last three columns:** per-timestep `avg`, plus the battery operational limits (283 K / 10 °C and 313 K / 40 °C) as horizontal reference lines for plotting.

## How to read it

Initial condition: all nodes at 293.15 K (20 °C). The model is then subjected to the orbital heat flux profile in `data/orbital-heat-flux/` and the internal component dissipation listed in `data/component-thermal-budget.csv`.

Typical end-of-run nodal averages:

- Hot case: ~347 K (≈ 74 °C) — above the battery operational ceiling, driving the need for coatings or radiator area.
- Cold case: ~319 K (≈ 46 °C) — above ambient because internal dissipation dominates during the sunlit arc.

## What this file is, and isn't

This is raw solver output — not a cleaned-up results summary. Column headers are the Thermal Desktop submodel node IDs, temperatures are in Kelvin, and time starts at zero. Anyone with Excel, Python (pandas + openpyxl), or Libreoffice can open it and verify the numbers.

It's included here as proof that the simulation actually ran to completion on 71 nodes across a full orbital transient. Native Thermal Desktop binaries (`.hra`, `.rck`, `.rco`) are excluded from the repo because they are tool-specific and not useful without the software.
