# 07 — Preliminary Thermal Vacuum Testing

Before committing to a full system-level test campaign, a set of preliminary thermal-vacuum (TVAC) tests were run on a benchtop vacuum chamber. The goal at this stage was **not** flight qualification — it was to shake out the test workflow, verify instrumentation, and check whether the thermal-model assumptions about emissivity and convection-loss behaved as expected in rough vacuum.

## Facility

Small benchtop bell-jar vacuum chamber in the SJSU lab. Rough vacuum only (mechanical pump, no turbo / cryo stages), so the achievable pressure was in the ~10⁻² Torr range — sufficient to kill convective heat transfer, which is what mattered for the model-correlation question. No LN₂ cold shroud.

<p align="center">
  <img src="../figures/tvac_2.png" width="40%" />
</p>

## Test Articles

Preliminary runs focused on individual electronics test articles rather than the full 2U stack:

- A small PCB assembly representative of the kind of thermal mass the flight electronics present.
- Standalone resistive heater elements on aluminum baseplates (used to simulate component dissipation).
- Temperature sensors (type-T thermocouples) both on the article and on the chamber baseplate as reference.

<p align="center">
  <img src="../figures/tvac_1.jpg" width="55%" />
</p>

Test article on the aluminum baseplate, instrumented with type-T thermocouples bonded to the component and routed out through the chamber feedthrough.

## Instrumentation

- **Type-T thermocouples** — 4 to 6 channels per run, bonded with Kapton tape on the article, the baseplate, and a chamber-wall reference point.
- **Handheld DAQ** logging at ~1 Hz during each run.
- **Vacuum gauge** on the chamber for pressure-vs-time logging during pump-down and dwell.

## What the Preliminary Runs Looked Like

Each run followed a simple three-phase profile — the full-campaign version of this will go in the Rev 6 test plan later.

1. **Ambient check.** Article at ambient pressure and room temperature. Turn on resistive heater. Log the steady-state component temperature to get a baseline with natural convection present.
2. **Pump-down and vacuum dwell.** Evacuate to working vacuum (~10⁻² Torr). Hold the same heater power for 15–30 min. The component runs hotter than ambient because the convection path is gone and radiation is the only remaining sink — a first-order check that matches the intent of the flight thermal model.
3. **Return to ambient.** Vent, let the article cool, verify nothing was damaged.

## What We Confirmed

- **Convection really does dominate at ambient** for these small electronics. Removing it pushed steady-state temperatures up by tens of degrees at the same heater power — qualitatively consistent with the radiation-only boundary condition used in the flight model.
- **Thermocouple + Kapton attachment survives pump-down and venting cleanly.** Bond quality is the biggest source of scatter in the readings; a lesson carried forward into the Rev 6 test plan.
- **The benchtop chamber is the right tool for model spot-checks, not for flight qualification.** Achievable vacuum level, shroud temperature, and IR simulation are all limited. Component qualification and system-level testing will need a proper TVAC facility with LN₂ shrouding — that's Rev 6 scope.

## Limitations

- Rough vacuum only (no high-vacuum stage).
- No cold shroud — the chamber walls were at room temperature, so "deep space" was not represented.
- No solar / IR simulation lamp.
- Small number of thermocouple channels (4–6); no high-channel-count correlation exercise.

## Next Step (Rev 6)

The preliminary data and workflow from these benchtop runs feed into the Rev 6 test plan, which covers a proper TVAC campaign: LN₂-shrouded chamber, calibrated IR lamp for solar simulation, ≥32 thermocouple channels, and a quantitative model-vs-measurement correlation band across the battery, Jetson TX2, Iridium 9603, and the integrated 2U flat-sat.

## References

1. NASA GSFC, *General Environmental Verification Standard (GEVS)*, GSFC-STD-7000 — background on flight TVAC practice.
2. NASA Ames, *Small Spacecraft Thermal Modeling Guide* — see [`docs/03-methodology.md`](03-methodology.md).
