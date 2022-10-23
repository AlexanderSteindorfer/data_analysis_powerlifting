import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# OpenPowerlifting data analysis 1.2
# Development of the numbers of male and female participants through time (relative).
# Data source: https://www.openpowerlifting.org/

df = pd.read_csv("data//openpowerlifting-2022-09-01//openpowerlifting.csv")

# In order to drop duplicates here, I need to first read in the whole DataFrame and apply it,
# since I will use the columns year and sex, where every row will have duplicates!
df = df.drop_duplicates()

df = df.sort_values("Date", ascending=True)
df["Year"] = df["Date"].map(lambda date: date.split("-")[0]).astype("int")

df = df[["Year", "Sex"]]
df = df[(df["Year"] > 2003) & (df["Sex"] != "Mx")]

df = df.dropna()

df_grouped = (df.reset_index().groupby(["Year", "Sex"], as_index=False).count()
                .rename(columns={"index":"Count"}))

# Now I create a new column, which will hold the percentage of male and female participants
# per year. I will then plot this column.
# First, I create a new DataFrame containing the total participants per year.
# Note: value_counts returns the Year column as index and renames it to "index" too.
# To revert this, I use rename_axis and then reset_index to get a standard index back.
df_participants = (df["Year"].value_counts(sort=False).rename_axis("Year")
                             .reset_index(name="Count"))

# The above returns one row per year. However, the grouped DataFrame contains two rows per year
# (male/female). Therefore, I duplicate all rows of the above result to have the exact same number
# of rows in both DataFrames, which will allow for a mathematical operation between them.
# Cast as DataFrame, otherwise it will return a NumPy array.
df_participants = pd.DataFrame(np.repeat(df_participants.values, 2, axis=0), 
                               columns=df_participants.columns)

# Creating the percentage column.
df_grouped["Percentage"] = round(df_grouped["Count"] / df_participants["Count"] * 100, 2)

# I can now print the whole DataFrame to see the relative numbers.
print(df_grouped)

# Plotting the relative values.
fig, ax = plt.subplots(dpi=150, figsize=(10,6))

for key, data in df_grouped.groupby("Sex"):
    data.plot(x="Year", y="Percentage", ax=ax, label=key, xlabel="Year", ylabel="Participants",
              grid=True)

ax.set_xlim(2004,2022)
plt.legend(bbox_to_anchor=(1.11,1))
ax.set_title("Participants in Powerlifting competitions 2004-2022 (relative)")
# plt.savefig("visualisation//1.2_sex_rel.png")