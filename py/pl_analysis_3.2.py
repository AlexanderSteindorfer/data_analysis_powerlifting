import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# OpenPowerlifting data analysis 3.2
# Analysis of correlation of the three exercises with the total weight lifted in Powerlifting competitions.
# Data source: https://www.openpowerlifting.org/

df = pd.read_csv("data//openpowerlifting-2022-09-01//openpowerlifting.csv")

df = df.drop_duplicates()

df = df[["Sex", "TotalKg", "Best3SquatKg", "Best3BenchKg", "Best3DeadliftKg"]]
df = df[df["Sex"] != "Mx"]
df = df.sort_values(["TotalKg"])

df = df.dropna()

# Dropping outliers based on estimations.
df = df.drop(df[(df["TotalKg"] > 480) & (df["Best3DeadliftKg"] < 100)].index)
df = df.drop(df[(df["TotalKg"] > 500) & (df["Best3BenchKg"] < 50)].index)
df = df.drop(df[(df["TotalKg"] > 300) & (df["Best3SquatKg"] < 50)].index)
df = df.drop(df[(df["Best3SquatKg"] > 300) & (df["Best3DeadliftKg"] < 150)].index)
df = df.drop(df[(df["Best3SquatKg"] > 230) & (df["Best3DeadliftKg"] < 70)].index)
df = df.drop(df[(df["Best3BenchKg"] > 200) & (df["Best3SquatKg"] < 150)].index)
df = df.drop(df[(df["Best3BenchKg"] > 200) & (df["Best3DeadliftKg"] < 150)].index)

# Renaming some columns for the plots.
df = df.rename(columns={"TotalKg":"Total", "Best3SquatKg":"Best squat",
                        "Best3BenchKg":"Best bench press", "Best3DeadliftKg":"Best deadlift"})

# Visualising the correlation with a heat
corr = df.corr()
plt.figure(dpi=200)
sns.heatmap(data=corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True,
            cmap=sns.diverging_palette(220, 20, as_cmap=True), linewidth=0.3)
plt.title("Correlation Matrix: total, squat, bench press, deadlift")
# plt.savefig("visualisation//3.2_corr_matrix.png", bbox_inches="tight")

# Pair plot of the correlations between total, squat, bench press and deadlift.
(sns.pairplot(data=df.sample(frac=0.005), dropna=True, hue="Sex", hue_order=["M","F"],
              palette="magma"))
# plt.savefig("visualisation//3.2_corr_total-exercises.png")