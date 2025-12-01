import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Professional seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# ---- Synthetic Business Data: Support Efficiency Analysis ----
np.random.seed(42)

departments = ["Technical Support", "Customer Care", "Billing"]
data = []

for dept in departments:
    if dept == "Technical Support":
        times = np.random.normal(loc=18, scale=5, size=200)   # faster resolution
    elif dept == "Customer Care":
        times = np.random.normal(loc=25, scale=7, size=200)
    else:
        times = np.random.normal(loc=35, scale=6, size=200)   # slower resolution
    
    for t in times:
        data.append([dept, abs(t)])   # abs() avoids negative synthetic values

df = pd.DataFrame(data, columns=["Department", "Resolution_Time"])

# ---- Create Violin Plot ----
plt.figure(figsize=(8, 8))  # 512x512 pixels when dpi=64

sns.violinplot(
    data=df,
    x="Department",
    y="Resolution_Time",
    palette="viridis",
    cut=0
)

plt.title("Resolution Time Distribution by Department", fontsize=18)
plt.xlabel("Department", fontsize=14)
plt.ylabel("Resolution Time (minutes)", fontsize=14)

# ---- Export exact 512x512 PNG ----
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

print("chart.png generated successfully.")
