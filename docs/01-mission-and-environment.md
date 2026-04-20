# 01 — Mission and Thermal Environment

## Mission

**Spartan Sat** is a 2U CubeSat developed by the San Jose State University CubeSat program. The reference mission profile used for thermal sizing begins with ISS deployment into LEO (~400km)

## Thermal Environment at 400 km LEO

| Source         | Value                     | Notes                         |
| -------------- | ------------------------- | ----------------------------- |
| Solar flux     | ~1361 W/m² (±3%)          | Kopp & Lean 2011              |
| Earth albedo   | 0.14–0.19 → ~185–270 W/m² | NASA SSSRI                    |
| Earth IR (OLR) | ~218–228 W/m²             | NASA SSSRI                    |
| Lunar IR       | ~0                        | Included for flyby phase only |
| Background     | Earth + deep space (~3 K) |                               |

Solar, albedo, and Earth IR are used for thermal sizing. Solar flare / CME heating is milliwatt-scale on CubeSat-class surface areas and is treated as negligible as of 2026; the real solar-storm risks for LEO CubeSats are drag from thermospheric density surges and communications blackout, both tracked in the environment doc but out of scope for the thermal model.

## Design Orbit Cases

Two bounding steady-orbit cases are carried forward

| Case | Beta angle | Solar flux | Earth albedo |
| ---- | ---------- | ---------- | ------------ |
| Hot  | 60°        | 1419 W/m²  | 0.55         |
| Cold | 0°         | 1317 W/m²  | 0.18         |

## References

1. NASA SSSRI, _Preliminary Thermal Analysis of Small Satellites_, 2018.
2. NASA, _Solar Constant and Solar Variability_, Lessons Learned #693, 2015.
3. NASA, _Small Spacecraft Technology State of the Art (2024)_ — thermal chapter.
