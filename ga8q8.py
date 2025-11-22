
# analysis/retention_analysis.py
# Python 3.8+ recommended
import os
import math
import matplotlib.pyplot as plt

# --- Data (quarterly retention rates for 2024) ---
quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
retention = [65.02, 71.48, 72.37, 75.86]

# --- Calculations ---
avg_retention = sum(retention) / len(retention)
avg_retention_rounded = round(avg_retention, 2)

# Print summary
print("Quarterly retention rates:", list(zip(quarters, retention)))
print("Computed average retention:", avg_retention_rounded)

# --- Visualization ---
plt.figure(figsize=(8,5))
plt.plot(quarters, retention, marker='o', linewidth=2)
plt.axhline(85, linestyle='--', linewidth=1.5)   # industry benchmark
plt.text(0.1, 85 + 0.7, "Industry target = 85", fontsize=9, va='bottom')
plt.ylim(min(retention) - 5, max(85, max(retention)) + 5)
plt.title("Customer Retention Rate — 2024 Quarterly Trend")
plt.xlabel("Quarter")
plt.ylabel("Retention Rate (%)")
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save plot
out_dir = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(out_dir, exist_ok=True)
plot_path = os.path.join(out_dir, "retention_plot.png")
plt.savefig(plot_path, dpi=150)
print("Saved chart to:", plot_path)
plt.close()

# --- Additional simple metric: gap to target ---
industry_target = 85
gap = industry_target - avg_retention
print(f"Average retention: {avg_retention_rounded} (target gap: {gap:.2f} percentage points)")

# Optional: Save summary to a small text file for including in PR
summary_path = os.path.join(out_dir, "summary.txt")
with open(summary_path, "w") as f:
    f.write(f"Average retention (2024): {avg_retention_rounded}\n")
    f.write(f"Industry target: {industry_target}\n")
    f.write(f"Gap to target: {gap:.2f}\n")
print("Saved summary to:", summary_path)
