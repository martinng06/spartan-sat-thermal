"""Compare Rev 5 hot-case panel temperature against component operational limits.

Reads data/component-thermal-budget.csv and the Rev 5 hot-case final panel
average temperature, and writes figures/hot-cold-case-bar.png.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
BUDGET = ROOT / "data" / "component-thermal-budget.csv"
XLSX = ROOT / "data" / "raw-simulation" / "2ucubesat-rev5-transient-temperatures.xlsx"
OUT = ROOT / "figures" / "hot-cold-case-bar.png"

budget = pd.read_csv(BUDGET)

# Extract Rev 5 end-of-run panel averages (hot + cold)
hot = pd.read_excel(XLSX, sheet_name="hotcase")
cold = pd.read_excel(XLSX, sheet_name="coldcase")
hot_final_avg_C = hot["avg"].iloc[-1] - 273.15
cold_final_avg_C = cold["avg"].iloc[-1] - 273.15

fig, ax = plt.subplots(figsize=(11, 5.5))
y = np.arange(len(budget))

# Operational range bars (gray)
for i, row in budget.iterrows():
    ax.barh(i, row["op_max_C"] - row["op_min_C"], left=row["op_min_C"],
            color="#c7d2d9", edgecolor="#6c757d", linewidth=0.8,
            label="Operational range" if i == 0 else None)

# Hot-case panel temp marker
ax.axvline(hot_final_avg_C, color="#c92a2a", linestyle="-", linewidth=2,
           label=f"Rev 5 hot-case panel avg ({hot_final_avg_C:.1f} °C)")
# Cold-case panel temp marker
ax.axvline(cold_final_avg_C, color="#2b6cb0", linestyle="-", linewidth=2,
           label=f"Rev 5 cold-case panel avg ({cold_final_avg_C:.1f} °C)")

ax.set_yticks(y)
ax.set_yticklabels(budget["component"])
ax.invert_yaxis()
ax.set_xlabel("Temperature (°C)")
ax.set_title("Spartan Sat Rev 5 — Panel Temperature vs. Component Operational Limits")
ax.axvline(0, color="black", linewidth=0.6, alpha=0.4)
ax.grid(True, axis="x", alpha=0.3)
ax.legend(loc="lower right")
ax.set_xlim(-50, 100)

fig.tight_layout()
OUT.parent.mkdir(exist_ok=True, parents=True)
fig.savefig(OUT, dpi=150)
print(f"wrote {OUT}")
print(f"hot final avg: {hot_final_avg_C:.2f} °C")
print(f"cold final avg: {cold_final_avg_C:.2f} °C")
