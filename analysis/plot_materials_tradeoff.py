"""Scatter plot of candidate surface materials on an alpha vs. epsilon chart.

Uses numbered markers on the scatter and a legend table beside it so the
names never overlap. Reads data/materials-properties.csv and writes
figures/materials-tradeoff.png.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "data" / "materials-properties.csv"
OUT = ROOT / "figures" / "materials-tradeoff.png"

df = pd.read_csv(CSV).reset_index(drop=True)
palette = {"film": "#2b6cb0", "paint": "#c92a2a", "anodize": "#d9842c", "bare": "#495057"}

fig = plt.figure(figsize=(13, 7))
gs = fig.add_gridspec(1, 2, width_ratios=[1.5, 1.0], wspace=0.05)
ax = fig.add_subplot(gs[0, 0])
legend_ax = fig.add_subplot(gs[0, 1])
legend_ax.axis("off")

# Plot markers with numeric labels
for i, row in df.iterrows():
    color = palette.get(row["category"], "#333")
    ax.scatter(row["alpha_BOL"], row["epsilon_BOL"], s=150, color=color,
               edgecolor="black", linewidth=0.8, zorder=3)
    ax.annotate(str(i + 1), (row["alpha_BOL"], row["epsilon_BOL"]),
                ha="center", va="center", fontsize=8, fontweight="bold",
                color="white", zorder=4)

# alpha/epsilon = 1 reference line
x = np.linspace(0, 1, 50)
ax.plot(x, x, color="gray", linestyle="--", alpha=0.6, label="α / ε = 1")

ax.set_xlabel("Solar absorptivity α (BOL)", fontsize=11)
ax.set_ylabel("IR emissivity ε (BOL)", fontsize=11)
ax.set_title("Surface Material Trade Study — α vs. ε", fontsize=12)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.grid(True, alpha=0.3)

# Radiator-friendly quadrant shading
ax.axhspan(0.6, 1.0, xmin=0, xmax=0.3, color="#2b8a3e", alpha=0.06)
ax.text(0.02, 0.97, "radiator-friendly\n(low α, high ε)", fontsize=9, color="#2b8a3e",
        verticalalignment="top", alpha=0.9)

# Category color legend (top-right of plot)
for j, (cat, color) in enumerate(palette.items()):
    ax.scatter([], [], color=color, s=80, edgecolor="black",
               linewidth=0.5, label=cat)
ax.legend(loc="lower right", fontsize=9)

# Numbered legend table on the right
legend_ax.text(0.0, 1.0, "Material Index", fontsize=12, fontweight="bold",
               transform=legend_ax.transAxes)
for i, row in df.iterrows():
    color = palette.get(row["category"], "#333")
    y_pos = 0.96 - (i + 1) * 0.055
    legend_ax.text(0.0, y_pos, f"{i + 1}.", fontsize=9, fontweight="bold",
                   color=color, transform=legend_ax.transAxes,
                   family="monospace")
    legend_ax.text(0.06, y_pos, row["material"], fontsize=9,
                   transform=legend_ax.transAxes)

fig.tight_layout()
OUT.parent.mkdir(exist_ok=True, parents=True)
fig.savefig(OUT, dpi=150, bbox_inches="tight")
print(f"wrote {OUT}")
