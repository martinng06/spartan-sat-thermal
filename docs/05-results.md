# 05 — Results

## Headline Numbers — Rev 5 Transient Simulation

Both cases run for ~6 orbits starting from a 293.15 K (20 °C) initial condition. All temperatures below are for the instrumented +Z (sun-facing) panel.

### Hot Case (β = 60°, solar = 1419 W/m², albedo = 0.55)

| Metric | Value |
|--------|------:|
| Final panel average | **73.8 °C** |
| Final panel max | 74.0 °C |
| Final panel min | 73.4 °C |
| Time to quasi-steady cycle | ~4 orbits |

### Cold Case (β = 0°, solar = 1317 W/m², albedo = 0.18)

| Metric | Value |
|--------|------:|
| Final panel average | **46.2 °C** |
| Final panel max | 46.3 °C |
| Final panel min | 46.0 °C |
| Time to quasi-steady cycle | ~4 orbits |

![Sun-face transient](../figures/node-temperature-map.png)

Data source: `data/raw-simulation/2ucubesat-rev5-transient-temperatures.xlsx` (71 nodes × 102 timesteps, both cases).

## Comparison Against Component Limits

The sun-facing panel is the hottest exterior surface. Interior components are thermally coupled to this panel through the structure, so panel temperature is the binding constraint for the battery.

| Component | Op ceiling | Rev 5 panel result (hot) | Margin |
|-----------|-----------:|-------------------------:|-------:|
| Battery (operational) | +40 °C | +73.8 °C | **−34 °C (FAIL)** |
| Jetson TX2 (operational) | +80 °C | +73.8 °C | +6 °C |
| Iridium 9603 (operational) | +70 °C | +73.8 °C | **−4 °C (FAIL)** |
| Solar panel (operational) | +85 °C | +73.8 °C | +11 °C |

See `figures/hot-cold-case-bar.png` for the visual.

## Key Finding

The Rev 5 bare-anodize design **fails the hot case on the battery and Iridium comms module** by a meaningful margin. This is exactly the result the simulation is designed to produce: it tells the design team that a passive-only bare-aluminum exterior is not sufficient and **active or coating-based thermal control is required**.

The planned next step is a design revision adding a low-α / high-ε coating patch (NZOT white paint or silvered FEP film — see `docs/04`) on the +Z panel to knock down absorbed solar on the sun-view face, with the battery thermally strapped to a cold interior panel.

## Earlier Revisions

For the 2U Baseline Rev 2 case (bare Type III anodize, less detailed mesh, simpler internal power model) the spread of node temperatures was:

| Case | Min | Max |
|------|-----:|-----:|
| Hot | +42 °C | +82 °C |
| Cold | +17 °C | +57 °C |

These results confirmed the directional finding (hot-case too hot for battery), drove the Rev 3–5 mesh refinement and coating trade-study work, and established the regression dataset that Rev 5 was checked against. See `docs/06-design-evolution.md`.

## How to Reproduce the Figures

```bash
cd analysis
pip install -r requirements.txt
python plot_orbital_loads.py
python hot_cold_case_summary.py
```

Both scripts read the CSV / XLSX files in `data/` and write PNGs into `figures/`.
