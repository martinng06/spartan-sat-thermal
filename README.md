# Spartan Sat — Thermal Engineering

**Thermal analysis and control design for the Spartan Sat 2U CubeSat, SJSU CubeSat program.**

![Transient temperature — Rev 5 hot and cold cases](figures/node-temperature-map.png)

- **Mission:** 2U CubeSat, ISS deployment to Low Earth Orbit (~400 km)
- **Technology stack:** Thermal Desktop + Sinda, SolidWorks, Python
- **Headline finding:** The bare Type III gray anodize 2U design reaches **~47 °C panel average in the hot case** — 3 of 4 binding components pass their operational limits with healthy margin. The battery exceeds its 40 °C ceiling by 4 °C, identifying it as the design driver. Coating trades on the +Z panel are being evaluated to close the gap, and design iterations are continuing from this baseline.

## Contents

| Folder                 | What's in it                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| [`docs/`](docs/)       | technical documents: mission, requirements, methodology, materials, results, iteration history, TVAC testing |
| [`figures/`](figures/) | plots and simulation renders                                                                                 |
| [`data/`](data/)       | boundary conditions, component thermal budget, materials properties, raw simulation output                   |

## Mission and Environment

Spartan Sat is designed for a LEO orbit at ~400 km. The thermal environment is bounded by:

| Source       | Value                     |
| ------------ | ------------------------- |
| Solar flux   | ~1361 W/m²                |
| Earth albedo | 0.14–0.19 → ~185–270 W/m² |
| Earth IR     | ~218–228 W/m²             |

Two design cases are carried through the analysis: a hot case (β = 60°, solar = 1419 W/m², albedo = 0.55) and a cold case (β = 0°, solar = 1317 W/m², albedo = 0.18).

## Component Thermal Requirements

Key flight components and their operational temperature limits:

| Component              |    Power | Op range      |
| ---------------------- | -------: | ------------- |
| Battery (Cannon BP955) |   0.17 W | 0 to +40 °C   |
| Jetson TX2             |     15 W | −25 to +80 °C |
| Iridium 9603           |    0.8 W | −30 to +70 °C |
| Solar panels           | -------- | −40 to +85 °C |

The battery drives the hot-side design as its 40 °C operational ceiling is the temperature constraint.

## Methodology

- **Geometry:** 2U CubeSat (0.1 × 0.1 × 0.2 m), SolidWorks → Thermal Desktop
- **Mesh:** ~70 nodes on the +Z face (8×16 per large face)
- **Radiative exchange:** RadCAD Monte Carlo, 5,000 rays per node
- **Analysis:** Transient, initialize nodes at 293.15 K
- **Verification:** Excel radiation-balance hand calculations

## Key Results

### Bare Type III Gray Anodized Aluminum

| Metric              |    Hot case |   Cold case |
| ------------------- | ----------: | ----------: |
| Final panel average | **47.0 °C** | **12.0 °C** |

![Panel temperature vs. component limits](figures/hot-cold-case-bar.png)

| Component              | Sim temp (hot) | Op limit |           Margin |
| ---------------------- | -------------: | -------: | ---------------: |
| Battery (Cannon BP955) |         +44 °C |   +40 °C | **−4 °C (FAIL)** |
| Jetson TX2             |         +62 °C |   +80 °C |       **+18 °C** |
| Iridium 9603           |         +49 °C |   +70 °C |       **+21 °C** |
| Solar panel            |         +55 °C |   +85 °C |       **+30 °C** |

Three of four components stay inside their temperature range. The battery exceeds its +40 °C ceiling by 4 °C in the hot case, which was expected given the small temperature range. Design iterations are continuing from this baseline, and the work done here provides a strong foundation to build from.

## Materials Trade Study

16 candidate surface treatments catalogued across films, paints, and anodizations, with BOL α / ε, supplier, and cost.

![Materials trade study](figures/materials-tradeoff.png)

## Iterative Processes

Five design revisions were carried out and each revision was addressed a flaw in the previous one.

<p align="center">
  <img src="figures/cubesat_rev1.png" width="48%" />
  <img src="figures/cubesat_rev4.png" width="48%" />
</p>

Left: early Rev 1 temperature field — coarse mesh, narrow range, used to verify radiative boundary conditions. Right: Rev 4 temperature field — fine mesh across the full 2U assembly with internal components included, showing the full thermal gradient from sun-lit to shaded surfaces.

## Thermal Vacuum Testing

Preliminary component-level thermal-vacuum tests were performed on a benchtop vacuum chamber to verify that key electronics survive and operate in vacuum and to spot-check thermal model assumptions (surface emissivity, outgassing, thermocouple attachment) before scaling to a full system-level test

<p align="center">
  <img src="figures/tvac_1.jpg" width="50%" />
  <img src="figures/tvac_2.png" width="30%" />
</p>

Left: electronics test article instrumented with type-T thermocouples on the baseplate inside the chamber. Right: bell-jar vacuum chamber pulled down to rough vacuum for the test run.

## Contact

Martin Nguyen — [LinkedIn](https://www.linkedin.com/in/martinnguyen0/) · marngu06@gmail.com
