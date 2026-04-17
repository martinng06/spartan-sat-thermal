"""Scatter plot of candidate surface materials on an alpha vs. epsilon chart.

Reads data/materials-properties.csv and writes figures/materials-tradeoff.png.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "data" / "materials-properties.csv"
OUT = ROOT / "figures" / "materials-tradeoff.png"

df = pd.read_csv(CSV)
palette = {"film": "#2b6cb0", "paint": "#c92a2a", "anodize": "#d9842c", "bare": "#495057"}

fig, ax = plt.subplots(figsize=(10, 7))

for cat, color in palette.items():
    sub = df[df["category"] == cat]
    ax.scatter(sub["alpha_BOL"], sub["epsilon_BOL"],
               color=color, s=80, label=cat, edgecolor="black", linewidth=0.6)
    for _, r in sub.iterrows():
        ax.annotate(r["material"], (r["alpha_BOL"], r["epsilon_BOL"]),
                    xytext=(6, 4), textcoords="offset points", fontsize=7.5, alpha=0.85)

# α/ε = 1 reference line
x = np.linspace(0, 1, 50)
ax.plot(x, x, color="gray", linestyle="--", alpha=0.5, label="α / ε = 1")

ax.set_xlabel("Solar absorptivity α (BOL)")
ax.set_ylabel("IR emissivity ε (BOL)")
ax.set_title("Spartan Sat Surface Material Trade Study — α vs. ε")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right")

# Shade "radiator-friendly" quadrant (low α, high ε)
ax.axhspan(0.6, 1.0, xmin=0, xmax=0.3, color="#2b8a3e", alpha=0.06)
ax.text(0.02, 0.97, "radiator-friendly\n(low α, high ε)", fontsize=8, color="#2b8a3e",
        verticalalignment="top", alpha=0.8)

fig.tight_layout()
OUT.parent.mkdir(exist_ok=True, parents=True)
fig.savefig(OUT, dpi=150)
print(f"wrote {OUT}")
