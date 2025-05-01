import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the file
df = pd.read_csv("s_OSD-476.txt", sep=r'\s+')

# Set plot style
sns.set(style="whitegrid")

# Create a single boxplot for all RNAContamination values
plt.figure(figsize=(6, 6))
sns.boxplot(y=df["RNAContamination"], color="skyblue")

# Set labels and title
plt.title("Overall RNA Contamination")
plt.ylabel("RNA Contamination")
plt.xlabel("")

# Show the plot
plt.tight_layout()
plt.show()
