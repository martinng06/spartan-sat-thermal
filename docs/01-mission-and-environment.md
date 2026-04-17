# 01 — Mission and Thermal Environment

## Mission

**Spartan Sat** is a 2U CubeSat developed by the San Jose State University CubeSat program. The reference mission profile used for thermal sizing begins with ISS deployment into low Earth orbit (~400 km) and considers a follow-on lunar flyby phase.

For thermal analysis, the dominant phase is LEO: an ~95-minute orbit split roughly into 60 minutes of sunlight and 35 minutes of eclipse. This is the case that drives the hot / cold design points.

## Thermal Environment at 400 km LEO

| Source | Value | Notes |
|--------|-------|-------|
| Solar flux | ~1361 W/m² (±3%) | Kopp & Lean 2011 |
| Earth albedo | 0.14–0.19 → ~185–270 W/m² | NASA SSSRI |
| Earth IR (OLR) | ~218–228 W/m² | NASA SSSRI |
| Lunar IR | ~0 | Included for flyby phase only |
| Background | Earth + deep space (~3 K) | |

Solar, albedo, and Earth IR are used for thermal sizing. Solar flare / CME heating is milliwatt-scale on CubeSat-class surface areas and is treated as negligible; the real solar-storm risks for LEO CubeSats are drag from thermospheric density surges and communications blackout, both tracked in the environment doc but out of scope for the thermal model.

## Design Orbit Cases

Two bounding steady-orbit cases are carried forward into the Rev 5 transient analysis:

| Case | Beta angle | Solar flux | Earth albedo | Notes |
|------|-----------|-----------|--------------|-------|
| Hot | 60° | 1419 W/m² | 0.55 | Summer solstice, high-β sunlit arc |
| Cold | 0° | 1317 W/m² | 0.18 | Winter solstice, long eclipse |

Solar-flux values above are total incident; the **absorbed** fluxes applied as boundary conditions (after multiplying by surface absorptivity α ≈ 0.25 for bare Al 6061) are contained in `data/orbital-heat-flux/`.

## References

1. NASA SSSRI, *Preliminary Thermal Analysis of Small Satellites*, 2018.
2. NASA, *Solar Constant and Solar Variability*, Lessons Learned #693, 2015.
3. NASA, *Small Spacecraft Technology State of the Art (2024)* — thermal chapter.
