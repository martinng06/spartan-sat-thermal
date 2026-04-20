# Orbital Heat Flux Boundary Conditions

Time-history heat flux profiles applied as boundary conditions to the Spartan Sat 2U CubeSat thermal model during transient simulation runs.

## Files

| File                             | Description                                               |
| -------------------------------- | --------------------------------------------------------- |
| `sun_face_loads.csv` / `.xlsx`   | Absorbed solar flux on the sun-facing panel               |
| `earth_face_loads.csv` / `.xlsx` | Absorbed Earth-albedo + IR flux on the nadir-facing panel |

## Columns

- `time_s` — seconds from start of simulation
- `q_sun_W_per_m2` / `q_albedo_W_per_m2` — absorbed heat flux (W/m²)

## Profile shape

Each file is a step-function approximation of a LEO thermal environment:

- **Sunlit (~60 min):** flux is at its peak value
- **Eclipse (~35 min):** flux drops to 0
- Pattern repeats across ~12 orbits (~19 hours of simulated time)

## Source values

| Quantity                    | Value                  | Source           |
| --------------------------- | ---------------------- | ---------------- |
| Solar constant              | 1361 W/m²              | Kopp & Lean 2011 |
| Earth albedo                | 0.14–0.19 (LEO 400 km) | NASA SSSRI 2018  |
| Earth IR                    | 218–228 W/m²           | NASA SSSRI 2018  |
| Sun-face absorptivity (α)   | 0.25 (bare Al 6061)    | —                |
| Peak absorbed solar (q_sun) | 340.25 W/m²            | 1361 × α         |
