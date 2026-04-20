# 04 — Materials and Coatings Trade Study

This trade study explores surface coatings, films, and anodizations against availability, cost, and BOL performance.

## Background

- **Absorptivity (α)** — fraction of incident solar energy absorbed (0–1). Low α → cooler in sun.
- **Emissivity (ε)** — effectiveness at radiating in the IR (0–1). High ε → cools faster to space.
- **α / ε < 1:** surface runs cooler in sunlight
- **α / ε > 1:** surface runs hotter in sunlight

**BOL vs. EOL**. UV, atomic oxygen, and particle flux degrade α and ε over the mission lifetime. All flight-surface selections must include end-of-life margin.

## Candidate Trade Space

### Films

| Material                       |   α (BOL) |   ε (BOL) | Supplier          | Notes                               |
| ------------------------------ | --------: | --------: | ----------------- | ----------------------------------- |
| Silvered FEP                   | 0.05–0.10 |   0.6–0.8 | Dunmore, Sheldahl | Gold-standard passive radiator film |
| ITO-coated Ag-FEP              | 0.05–0.10 |   0.6–0.8 | Dunmore           | Conductive variant (ESD control)    |
| Aluminized Kapton (VDA Kapton) |   0.3–0.4 |   0.1–0.2 | Dunmore, Sheldahl | Low-ε insulator; poor radiator face |
| Acktar White film              |     < 0.4 |     > 0.7 | Acktar / Edmund   | Flexible high-ε white skin          |
| Acktar Metal Velvet (black)    | very high | very high | Acktar / Edmund   | Internals/shade; runs hot in sun    |

### Surface Coatings

| Coating        | Type               | α / ε (BOL)      | Supplier | Notes                                     |
| -------------- | ------------------ | ---------------- | -------- | ----------------------------------------- |
| S13GP:6N/LO-1  | White (ZnO)        | 0.18 / 0.85–0.90 | HII AMCL | Easy cure; plan EOL darkening             |
| NZOT / DNZOT   | White (ZOT)        | 0.09–0.12 / 0.90 | HII AMCL | Strong candidate for 2U sun-view radiator |
| YB-71P         | White ZOT/silicate | 0.10–0.15 / 0.90 | HII AMCL | Heritage flight-qualified radiator paint  |
| D21:6N/LO      | Black siloxane     | 0.96 / 0.90+     | HII AMCL | Interior / shade; avoid sunlit exteriors  |
| Aeroglaze Z306 | Polyurethane black | 0.95 / 0.88      | Socomore | Flight-heritage black paint               |

### Aluminum Anodization

| Treatment                     | α / ε             | Cost | Notes                            |
| ----------------------------- | ----------------- | ---- | -------------------------------- |
| Clear anodize (Type II)       | 0.3–0.5 / 0.8     | $    | Neutral exterior; AO-resistant   |
| Black anodize (Type III dyed) | ~0.9 / ~0.8       | $    | Hot in sun; good for internals   |
| Chromate conversion (Alodine) | 0.2–0.3 / 0.1–0.2 | $    | Conductive, low-ε, retains heat  |
| Polished / bare aluminum      | 0.1 / 0.05–0.1    | $    | Oxidizes in LEO unless protected |

## Working Selection

The current baseline uses **Type III gray anodized aluminum** for the full external structure (α ≈ 0.61, ε ≈ 0.85).

- Passes cold-case & hot-case simulations

## References

Values drawn from NASA SoA Small Spacecraft Technology Report (2024), NASA MISSE program results, supplier datasheets, and Adibekyan et al. 2017 (IJT, high-accuracy emissivity data on Nextel 811-21, Aeroglaze Z306, and Acktar Fractal Black).
