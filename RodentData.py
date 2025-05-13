import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the file
df = pd.read_csv("s_OSD-770.txt", sep=r'\s+')

# Check Columns
print(df.columns)

# Extract regolith type from Source
# df["RegolithType"] = df["Source"].apply(lambda x: x.split(",")[2])


# Set plot style
sns.set(style="whitegrid")

# Define the categories to plot
categories = ["SpaceFlight", "GroundControl", "VivariumControl"]

# Create subplots (4 plots since there are 4 regolith types)
fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

# Plot each boxplot by regolith type
for ax, category in zip(axes, categories):
    sns.boxplot(
        data=df[df["FactorValue[Spaceflight]"] == category],
        y="RNAContamination",
        ax=ax,
    )
    ax.set_title(f"{category} RNA Contamination")
    ax.set_xlabel("")
    ax.set_ylabel("RNA Contamination")

# Adjust layout and display
plt.tight_layout()
plt.show()

