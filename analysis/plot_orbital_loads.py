"""Plot absorbed orbital heat fluxes (sun + earth) vs. time.

Reads data/orbital-heat-flux/*.csv and writes figures/orbital-heat-flux.png.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "orbital-heat-flux"
OUT = ROOT / "figures" / "orbital-heat-flux.png"

sun = pd.read_csv(DATA / "sun_face_loads.csv")
earth = pd.read_csv(DATA / "earth_face_loads.csv")

t_hr_sun = sun["time_s"] / 3600.0
t_hr_earth = earth["time_s"] / 3600.0

fig, ax = plt.subplots(figsize=(10, 4.5))
ax.step(t_hr_sun, sun["q_sun_W_per_m2"], where="post", label="Sun face (absorbed solar)", color="#d9642c", linewidth=1.8)
ax.step(t_hr_earth, earth["q_albedo_W_per_m2"], where="post", label="Earth face (absorbed albedo)", color="#2b6cb0", linewidth=1.8)

ax.set_xlabel("Time (hours)")
ax.set_ylabel("Absorbed heat flux (W/m²)")
ax.set_title("Spartan Sat 2U — Orbital Heat Flux Boundary Conditions (LEO 400 km)")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper right")
ax.set_xlim(0, max(t_hr_sun.max(), t_hr_earth.max()))

fig.tight_layout()
OUT.parent.mkdir(exist_ok=True, parents=True)
fig.savefig(OUT, dpi=150)
print(f"wrote {OUT}")
