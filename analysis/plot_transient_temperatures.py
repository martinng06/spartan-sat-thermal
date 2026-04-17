"""Plot transient temperature history for the Rev 5 hot and cold cases.

Reads data/raw-simulation/2ucubesat-rev5-transient-temperatures.xlsx and writes
figures/node-temperature-map.png.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "data" / "raw-simulation" / "2ucubesat-rev5-transient-temperatures.xlsx"
OUT = ROOT / "figures" / "node-temperature-map.png"

sheets = {"hotcase": "Hot case (β=60°, 1419 W/m²)", "coldcase": "Cold case (β=0°, 1317 W/m²)"}

fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=True)

for ax, (sheet, title) in zip(axes, sheets.items()):
    df = pd.read_excel(XLSX, sheet_name=sheet)
    t_hr = df["Times"] / 3600.0
    node_cols = [c for c in df.columns if str(c).startswith("POSZCUBESAT")]
    # Each node trace in light gray
    for c in node_cols:
        ax.plot(t_hr, df[c] - 273.15, color="#b0c4d9", linewidth=0.6, alpha=0.5)
    # Average in bold
    if "avg" in df.columns:
        ax.plot(t_hr, df["avg"] - 273.15, color="#1a3a5c", linewidth=2.2, label="Panel average")
    # Battery op limits (10°C to 40°C)
    ax.axhline(10, color="#2b8a3e", linestyle="--", linewidth=1.2, label="Battery op 10°C")
    ax.axhline(40, color="#c92a2a", linestyle="--", linewidth=1.2, label="Battery op 40°C")

    ax.set_xlabel("Time (hours)")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, t_hr.max())
    if ax is axes[0]:
        ax.set_ylabel("Temperature (°C)")
    ax.legend(loc="lower right", fontsize=8)

fig.suptitle("Spartan Sat Rev 5 — +Z panel transient temperature (71 nodes)", fontsize=12)
fig.tight_layout()
OUT.parent.mkdir(exist_ok=True, parents=True)
fig.savefig(OUT, dpi=150)
print(f"wrote {OUT}")
