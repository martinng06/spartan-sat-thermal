# Raw Simulation Output — Rev 5 Transient Temperatures

`2ucubesat-rev5-transient-temperatures.xlsx` — direct export of transient nodal temperature history from the final Rev 5 thermal simulation of the Spartan Sat 2U CubeSat.

| Sheet      | Load case                                                | Beta angle | Solar flux | Albedo |
| ---------- | -------------------------------------------------------- | ---------- | ---------- | ------ |
| `hotcase`  | Worst-case hot (high beta, high albedo, summer solstice) | 60°        | 1419 W/m²  | 0.55   |
| `coldcase` | Worst-case cold (beta 0, low albedo, winter solstice)    | 0°         | 1317 W/m²  | 0.18   |

## Structure

Each sheet is ~100 rows × 75 columns:

- **Column A (`Times`):** simulation time in seconds (0 → ~22,000 s, ~6 orbits)
- **Columns B–BV:** instantaneous nodal temperature in Kelvin for each of the 71 surface nodes on the +Z (sun-facing) panel.
- **Last three columns:** per-timestep `avg`, plus the battery operational limits (283 K / 10 °C and 313 K / 40 °C) as horizontal reference lines for plotting.
