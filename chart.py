import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
sns.set_context("talk")

# ---- Synthetic data ----
np.random.seed(42)
departments = ["Technical Support", "Customer Care", "Billing"]
data = []

for dept in departments:
    if dept == "Technical Support":
        times = np.random.normal(18, 5, 200)
    elif dept == "Customer Care":
        times = np.random.normal(25, 7, 200)
    else:
        times = np.random.normal(35, 6, 200)

    for t in times:
        data.append([dept, abs(t)])

df = pd.DataFrame(data, columns=["Department", "Resolution_Time"])

# ---- Force exact 512×512 canvas ----
fig = plt.figure(figsize=(8, 8), dpi=64)  # 8 in * 64 dpi = 512 px
ax = fig.add_subplot(111)

sns.violinplot(
    data=df,
    x="Department",
    y="Resolution_Time",
    palette="viridis",
    cut=0,
    ax=ax
)

ax.set_title("Resolution Time Distribution by Department", fontsize=18)
ax.set_xlabel("Department", fontsize=14)
ax.set_ylabel("Resolution Time (minutes)", fontsize=14)

# ---- REMOVE ALL PADDING / MARGINS ----
fig.subplots_adjust(left=0.08, right=0.98, top=0.92, bottom=0.12)
plt.margins(0)

# Important: NO tight layout, NO bbox_inches
fig.savefig("chart.png", dpi=64, pad_inches=0)

plt.close()
print("Saved EXACT 512x512 chart.png")
