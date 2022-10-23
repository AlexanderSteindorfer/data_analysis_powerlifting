import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# OpenPowerlifting data analysis 3.1
# Analysis of correlation of bodyweight with total weight lifted in competitions.
# Data source: https://www.openpowerlifting.org/

df = pd.read_csv("data//openpowerlifting-2022-09-01//openpowerlifting.csv")

df = df.drop_duplicates()

df = df[["Sex", "BodyweightKg", "TotalKg", "Best3SquatKg", "Best3BenchKg", "Best3DeadliftKg"]]
df = df[df["Sex"] != "Mx"]
df = df.sort_values(["BodyweightKg", "TotalKg"])

df = df.dropna()

# There are definitely entries where the wrong bodyweight has been entered.
print(df.head(20))

# Again, this is difficult to clean and can only be done based on an estimation.
# I use the following condition to drop rows: bodyweight below 30 kg
# and total weight lifted above 200 kg.
df = df.drop(df[(df["BodyweightKg"] < 30) & (df["TotalKg"] > 200)].index)

# Renaming some columns for the plot.
df = df.rename(columns={"TotalKg":"Total", "BodyweightKg":"Bodyweight"})

print(df.corr())

# Scatter plot of the correlation of bodyweight with total weight lifted in competitions.
plt.figure(dpi=150,figsize=(10,6)) 
(sns.scatterplot(data=df.sample(frac=0.005), x="Bodyweight", y="Total", hue="Sex", 
                 hue_order=["M","F"], s=15, palette="magma", alpha=0.8)
    .set(title="Correlation of bodyweight with total weight lifted in Powerlifting competitions"))

plt.legend(bbox_to_anchor=(1.11,1))
# plt.savefig("visualisation//3.1_corr_weight-total.png")