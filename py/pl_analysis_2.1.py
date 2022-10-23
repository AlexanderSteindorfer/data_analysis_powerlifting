import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# OpenPowerlifting data analysis 2.1
# Analysis of age (and sex) of the participants
# Data source: https://www.openpowerlifting.org/

df = pd.read_csv("data//openpowerlifting-2022-09-01//openpowerlifting.csv")

df = df.drop_duplicates()

df = df[["Sex", "Age", "AgeClass"]]
df = df.sort_values("Age")

df = df.dropna()

# I already see that there are entries where the age is not correctly entered, or where the TotalKg
# is impossible for the respective age (class).
print(df.head())

# I look for the youngest age class to remove all rows with an age below it, since these are
# not allowed to participate in competitions and must therefore have an incorrect age.
print(df["AgeClass"].unique())

# Rounding down decimals and removing rows where age is null or below 5 years, which is the
# lowest possible age. Again, "Mx" is simply too small to be visualised in context.
df["Age"] = df["Age"].apply(np.floor)
df = df[(df["Age"] > 4) & (df["Sex"] != "Mx")]


print(df["Age"].min())
print(df["Age"].max())
print(round(df["Age"].mean()))

# Counting the number of participants per age class.
print(df["AgeClass"].value_counts(sort=False))

# Adding a 0 in front of the age class 5-12 for proper sorting.
df["AgeClass"] = df["AgeClass"].map(lambda x: x.zfill(5))

# Grouping the DataFrame
df_grouped = (df.reset_index().groupby(["AgeClass","Sex"], as_index=False).count()
                  .rename(columns={"index":"Count"}))

# Creating a percentage column to show the percentage of males and females per age class.
df_participants = (df["AgeClass"].value_counts(sort=False).rename_axis("AgeClass")
                                 .reset_index(name="Count"))

df_participants = pd.DataFrame(np.repeat(df_participants.values, 2, axis=0), 
                               columns=df_participants.columns)

# The .astype() method is necessary to perform the math operation, as otherwise the two
# Count columns have different data types.
df_participants["Count"] = df_participants["Count"].astype("int")
df_grouped["Percentage"] = round(df_grouped["Count"] / df_participants["Count"] * 100, 2)

# Histogram plot of the number of participants per age class.
# Notes on the plot: 
# The plot clearly shows that Powerlifting competitions are most popular in the age class
# 24 to 34 years, for both men and women. 
# It also shows that below 16 years, the relative number of females in competitions is higher
# than in any age class above 15 years. For the class 5-12 years, it is even about 50%, which
# the numbers above show better than the plot in this case.
# Conversely, the older the age class, the lower the relative amount of females in competitions.
# This is a great addition to our previous analysis of the sex of competitors, as it shows
# that we are likely to see an increased number of female competitors in the future.
plt.figure(dpi=150,figsize=(12,6))

(sns.histplot(data=df, x="AgeClass", hue="Sex", hue_order=["F","M"],
              palette="RdBu", edgecolor="white", linewidth=0.3, zorder=3)
    .set(title="Distribution of age classes in Powerlifting competitions (1964-2022)"))

# Note: adding the labels ("MF") to the legend allows to move the legend outside of
# the hist- or displot, which is usually problematic.
# And for some reason, the order MF needs to be the opposite of the hue_order argument in the
# plot to get the legend colours right.
plt.legend("MF", bbox_to_anchor=(1.11,1))
plt.grid(axis="y", alpha=0.4, zorder=0)
# plt.savefig("visualisation//2.1_age_classes.png")