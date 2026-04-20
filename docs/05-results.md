# 05 — Results

## Headline Numbers — Transient Simulation

Both cases run for ~6 orbits starting from a 293.15 K (20 °C) initial condition. The 2U geometry uses bare Type III gray anodized aluminum (α ≈ 0.61, ε ≈ 0.86) on all exterior surfaces.

### Hot Case (β = 60°, solar = 1419 W/m², albedo = 0.55)

| Metric                     |       Value |
| -------------------------- | ----------: |
| Final panel average        | **47.0 °C** |
| Final panel max            |     48.2 °C |
| Final panel min            |     46.1 °C |
| Time to quasi-steady cycle |   ~4 orbits |

### Cold Case (β = 0°, solar = 1317 W/m², albedo = 0.18)

| Metric                     |       Value |
| -------------------------- | ----------: |
| Final panel average        | **12.0 °C** |
| Final panel max            |     12.9 °C |
| Final panel min            |     11.4 °C |
| Time to quasi-steady cycle |   ~4 orbits |

![Sun-face transient](../figures/node-temperature-map.png)

## Comparison Against Component Limits — Hot Case

Each component runs at a different temperature depending on its power dissipation and thermal coupling to the structure. The Jetson TX2 runs hottest because of its 15 W draw; the battery sits closer to the panel average because of its low self-heating.

| Component              |  Power | Op ceiling | Sim temp |           Margin |
| ---------------------- | -----: | ---------: | -------: | ---------------: |
| Battery (Cannon BP955) | 0.17 W |     +40 °C |   +44 °C | **−4 °C (FAIL)** |
| Jetson TX2             |   15 W |     +80 °C |   +62 °C |       **+18 °C** |
| Iridium 9603           |  0.8 W |     +70 °C |   +49 °C |       **+21 °C** |
| Solar panel            |      — |     +85 °C |   +55 °C |       **+30 °C** |

## Comparison Against Component Limits — Cold Case

| Component              |  Power | Op floor | Sim temp |     Margin |
| ---------------------- | -----: | -------: | -------: | ---------: |
| Battery (Cannon BP955) | 0.17 W |     0 °C |    +8 °C |  **+8 °C** |
| Jetson TX2             |   12 W |   −25 °C |   +19 °C | **+44 °C** |
| Iridium 9603           |  0.8 W |   −30 °C |   +10 °C | **+40 °C** |
| Solar panel            |      — |   −40 °C |    +3 °C | **+43 °C** |

## Key Findings

The Type III gray anodize design keeps 3 of 4 binding components inside their temperature range. The Jetson TX2, Iridium 9603, and solar panels all pass with ≥18 °C of margin on the hot side and ≥40 °C on the cold side.

The battery is the one component that does not meet its operational limit as it reaches +44 °C in the hot case, exceeding its +40 °C ceiling by 4 °C. This is expected as the battery has the strictest thermal requirements.

Although the battery did not pass in this configuration, this was a great learning experience and our mistakes pave the path for more succesful design terations to come.
