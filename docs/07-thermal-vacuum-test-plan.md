# 07 — Thermal Vacuum Test Plan

Before flight, the Spartan Sat thermal model and component selections must be correlated against hardware data under representative vacuum and temperature conditions. This document lays out the planned test campaign for the thermal subsystem.

## Purpose

The test campaign has three objectives:

1. **Verify operating range.** Confirm each thermal-critical component (battery, Jetson compute, Iridium comms, solar panels, sensors) survives and operates across its specified temperature range in vacuum.
2. **Correlate the thermal model.** Adjust Rev 5 model parameters (coating α/ε, contact conductances, internal dissipation) until predicted and measured temperatures agree within a defined tolerance.
3. **Verify the control strategy.** Exercise the battery survival heater and any active thermal-control loops to confirm they hold the battery within its 0–40 °C operational band during cold-soak and hot-dwell.

## Test Articles

| Article | Test type | Rationale |
|---------|-----------|-----------|
| **Battery (Cannon BP955) assembly** | Component TVAC | Binding hot-side constraint; verifies capacity retention at operational temperature extremes |
| **Jetson TX2 compute module** | Component TVAC, thermal cycling | High heat dissipation; verify boot / throttle behavior across operational range |
| **Iridium 9603 SBD transceiver** | Component TVAC | Verify RF link performance and IC derating behavior at temperature extremes |
| **Primary sensor payload** (IMU, temperature sensors, camera module) | Component TVAC | Verify bias drift, dark current, and operational continuity |
| **Integrated 2U flat-sat** | System-level TVAC | End-to-end model correlation under combined hot / cold orbital profiles |

## Facility Requirements

| Parameter | Value |
|-----------|-------|
| Chamber vacuum level | ≤ 1 × 10⁻⁵ Torr |
| LN₂-cooled shroud | Yes (deep-space cold sink simulation, target ≤ 100 K) |
| IR-lamp solar simulation (for system test) | Yes, calibrated to ~1419 W/m² for hot case |
| Thermocouple channels | ≥ 32 (component, structure, shroud) |
| Data acquisition rate | ≥ 1 Hz |
| Vacuum-compatible heater plates | For component-level hot dwells |

Target facility: SJSU / university small-satellite lab, or partner facility with an existing 1 m-class TVAC chamber. Chamber selection is part of Rev 6 planning.

## Test Matrix

### Component-Level TVAC (per component)

| Phase | Temperature | Duration | Purpose |
|-------|-------------|----------|---------|
| 1. Pre-test ambient characterization | +20 °C, 1 atm | 30 min | Baseline functional check |
| 2. Pump-down | +20 °C, vacuum | 60 min | Outgassing verification |
| 3. Cold survival soak | Survival min | 4 h | Survive-only, no power-on |
| 4. Cold operational | Op min | 2 h | Full functional cycle at cold op limit |
| 5. Hot operational | Op max | 2 h | Full functional cycle at hot op limit |
| 6. Hot survival soak | Survival max | 4 h | Survive-only |
| 7. Return to ambient | +20 °C | 30 min | Post-test functional check |

Cold/hot limits per component come from [`docs/02-thermal-requirements.md`](02-thermal-requirements.md).

### System-Level TVAC (integrated 2U)

A single orbital-cycle simulation with the IR lamp gated on/off per the hot and cold case heat-flux profiles in [`data/orbital-heat-flux/`](../data/orbital-heat-flux/). Two full orbit cycles per case, with the instrumented +Z panel and internal components logged at 1 Hz.

## Instrumentation

- Type-T thermocouples on: battery case, Jetson TX2 heat spreader, Iridium can, each solar panel, four locations on each external face, each internal structural bracket. Target ~32 channels.
- Strain-relieved wiring via vacuum feedthrough; bonded using Kapton tape (no adhesives that outgas).
- Separate calibration pass on all TCs before the test pump-down.

## Pass / Fail Criteria

| Criterion | Pass threshold |
|-----------|----------------|
| Component survival | No permanent degradation after survival soaks; functional after return to ambient |
| Component operation | Full operational functionality maintained within op range |
| Model correlation (per node) | Measured vs. predicted within **±5 °C** for at least 90% of instrumented nodes |
| Battery heater duty cycle | Holds battery > 5 °C during cold-soak, with ≥ 20% duty-cycle margin |

A test that fails to meet the correlation band triggers a Rev 6 model update (adjust coating α/ε, contact conductance, or internal dissipation) and a re-run of the simulation before any hardware re-test.

## Schedule

This is a forward-looking plan. Test readiness is gated on: (a) completion of the Rev 6 design iteration with the coating patch on the +Z panel, (b) flight-like battery and Jetson TX2 units being available, and (c) chamber time being allocated. Estimated earliest start: late 2026.

## References

1. NASA GSFC, *General Environmental Verification Standard (GEVS)*, GSFC-STD-7000.
2. NASA Ames, *Small Spacecraft Thermal Modeling Guide* (see `docs/03-methodology.md` references).
3. ECSS-E-ST-10-03C, *Space engineering — Testing*, European Cooperation for Space Standardization, 2012.
