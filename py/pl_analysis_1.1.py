import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

# OpenPowerlifting data analysis 1.1
# Development of the numbers of male and female participants through time (absolute).
# Data source: https://www.openpowerlifting.org/

# Creating a DataFrame from the entire data set:
df = pd.read_csv("data//openpowerlifting-2022-09-01//openpowerlifting.csv")

# looking at general info about the DataFrame
print(df.info())
print(df.head())

# Calculating the percentage of missing data for each column.
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print("{} - {}%".format(col, np.round(pct_missing, 2)))

# Counting and dropping duplicates.
print(df.duplicated().sum())
df = df.drop_duplicates()

# The following shows that the data set includes entries from 1964-09-05 to 2022-08-28.
print(df["Date"].min())
print(df["Date"].max())

# Sorting by Date and creating a new column, which only contains the year.
df = df.sort_values("Date", ascending=True)
df["Year"] = df["Date"].map(lambda date: date.split("-")[0]).astype("int")

# Counting the number of competitors per year.
print(df["Year"].value_counts(sort=False))

# Selecting the columns to visualise.
df = df[["Year","Sex"]]

# I select only male and female, since "Mx" is too small to be visualised
# in context (about 0.0015%).
# I want to look specifically at the years 2004-2022, since these are the most dynamic
# in both absolute and relative numbers, as exploring the grouped DataFrame below revealed.
df = df[(df["Year"] > 2003) & (df["Sex"] != "Mx")]

# Dropping rows with missing values.
# I am not applying this to the whole DataFrame, since this will remove a lot of data
# based on missing values in columns I don't intend to use.
df = df.dropna()

# I group the DataFrame to get male and female participants per year.
df_grouped = (df.reset_index().groupby(["Year","Sex"], as_index=False).count()
                .rename(columns={"index":"Count"}))

print(df_grouped)

# Plotting the absolute values.
fig, ax = plt.subplots(dpi=150, figsize=(10,6))

# Note: Pandas DataFrames and Series are structured like dictionaries.
# Therefore, I can plot the data using a loop.
for key, data in df_grouped.groupby("Sex"):
    data.plot(x="Year", y="Count", ax=ax, label=key, xlabel="Year", ylabel="Participants",
              grid=True)

ax.set_xlim(2004,2022)
plt.legend(bbox_to_anchor=(1.11,1))
ax.set_title("Participants in Powerlifting competitions 2004-2022 (absolute)")
# plt.savefig("visualisation//1.1_sex_abs.png")