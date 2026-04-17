# 02 — Component Thermal Requirements

Each onboard component must stay within its operational temperature range during nominal operation and within its survival range at all times (including eclipse cold-soak and safe mode). These requirements define the targets the thermal control design must meet.

## Component Heat Output and Temperature Limits

| Component | Nominal power | Operational range | Survival range | Driver |
|-----------|--------------:|-------------------|-----------------|--------|
| Battery (Cannon BP955) | ~0.17 W | **0 to +40 °C** | −20 to +60 °C | Charge/discharge efficiency, cell life |
| Jetson TX2 (compute) | ~15 W | −25 to +80 °C | −40 to +85 °C | Silicon junction temp |
| Iridium 9603 (comms) | ~0.8 W | −30 to +70 °C | −40 to +85 °C | IC derating |
| Solar panels (external) | — (generator) | −40 to +85 °C | −65 to +100 °C | Cell efficiency vs. temp |

The **battery dominates the hot-side design**: its 40 °C operational ceiling is ~35 °C lower than the other electronics, so coating and radiator choices are sized against the battery, not the compute.

## Internal Power Dissipation (per case)

Powers vary with mission mode. The values applied in the Rev 5 transient run:

| Component | Hot-case draw | Cold-case draw |
|-----------|--------------:|---------------:|
| Battery | ~0.17 W | ~0.17 W |
| Jetson TX2 | ~15 W | ~12 W |
| Iridium 9603 | ~0.8 W | ~0.8 W |
| Camera | 1.5 W | 0 W |
| SDR | 3.5 W | 1 W |
| **Total internal** | **~21 W** | **~14 W** |

## Derived Design Margins

To ensure the flight design has margin against model uncertainty, the thermal design budget is set ~5 °C inside each operational limit. For the battery this gives a working target of **+5 to +35 °C** inside the battery compartment.

See `data/component-thermal-budget.csv` for the machine-readable version.
