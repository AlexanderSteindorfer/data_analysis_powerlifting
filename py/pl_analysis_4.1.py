import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# OpenPowerlifting data analysis 4.1
# Analysis of the development of the total weight lifted through time.
# Data source: https://www.openpowerlifting.org/

df = pd.read_csv("data//openpowerlifting-2022-09-01//openpowerlifting.csv")

df = df.drop_duplicates()

df = df[["Date", "Sex", "TotalKg", "Best3SquatKg", "Best3BenchKg", "Best3DeadliftKg"]]
df = df[df["Sex"] != "Mx"]
df = df.sort_values(["TotalKg"])

df = df.dropna()

df["Year"] = df["Date"].map(lambda date: date.split("-")[0]).astype("int")

# Max and min total for male and female.
print("M:")
print(df[df["Sex"] == "M"]["TotalKg"].min())
print(df[df["Sex"] == "M"]["TotalKg"].max())
print("F:")
print(df[df["Sex"] == "F"]["TotalKg"].min())
print(df[df["Sex"] == "F"]["TotalKg"].max())

# Average total for male and female.
print("\nM:")
print(np.round(df[df["Sex"] == "M"]["TotalKg"].mean(), 1))
print("F:")
print(np.round(df[df["Sex"] == "F"]["TotalKg"].mean(), 1))

# Grouping the DataFrame with aggregate mean.
df_grouped = (df.groupby(["Year","Sex"], as_index=False).mean())

# Printing the whole grouped DataFrame
pd.set_option('display.max_rows', None)
print(df_grouped)

# Plotting the grouped DataFrame
fig, ax = plt.subplots(dpi=150, figsize=(10,6))

for key, data in df_grouped.groupby("Sex"):
    data.plot(x="Year", y="TotalKg", ax=ax, label=key, xlabel="Year",
              ylabel="Total weight lifted", grid=True)

plt.legend(bbox_to_anchor=(1.11,1))
ax.set_title("Average total weight lifted in Powerlifting competitions 1964-2022")
# plt.savefig("visualisation//4.1_avg_total.png")