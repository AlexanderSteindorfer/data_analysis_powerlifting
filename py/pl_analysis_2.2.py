import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# OpenPowerlifting data analysis 2.2
# Correlation of the age of participants with the total weight lifted in Powerlifting competitions.
# Data source: https://www.openpowerlifting.org/

df = pd.read_csv("data//openpowerlifting-2022-09-01//openpowerlifting.csv")

df = df.drop_duplicates()

df = df[["Sex", "Age", "AgeClass", "TotalKg"]]
df = df.sort_values(["Age", "TotalKg"])

df = df.dropna()

df["Age"] = df["Age"].apply(np.floor)
df = df[(df["Age"] > 4) & (df["Sex"] != "Mx")]


# Since the plot in the end immediately shows that there are outliers with impossible values
# for competitors of young age, I examine the DataFrame more closely.
print(df.head())

# Correcting these mistakes in the database is difficult and can only be done based on 
# estimations, dropping unrealistic extremes. As a guide, I am looking at the average value
# for the total of competitors with an age of 12 (150 kg), although this includes the wrong
# values too. I researched that one 9 year old athlete indeed achieved a total of 250 kg.
print(df[df["Age"] == 12].mean())

df = df.drop(df[(df["Age"] >= 10) & (df["Age"] < 12) & (df["TotalKg"] > 350)].index)
df = df.drop(df[(df["Age"] < 10) & (df["TotalKg"] > 280)].index)

# The correlation of age with the total is -0.106361, a slightly negative correlation.
# The following plot will clearify why this is the case.
print(df.corr())

# Plotting the correlation of age with total weight lifted in competitions
plt.figure(dpi=150,figsize=(10,6))
(sns.scatterplot(data=df.sample(frac=0.01), x="Age", y="TotalKg", hue="Sex", s=15,
                 palette="PuRd", alpha=0.8)
    .set(title="Correlation of age with total weight lifted in Powerlifting competitions"))
    
plt.legend(bbox_to_anchor=(1.11,1))
# plt.savefig("visualisation//2.2_corr_age-total.png")