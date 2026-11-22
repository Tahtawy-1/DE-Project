import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("Cleaned_Data.csv")

region = input("Please enter a continent: ").strip().capitalize()

cond = df["Region"] == region

fig, ax = plt.subplots()

ax.scatter(df[cond]["Longitude"], df[cond]["Latitude"])

ax.set_title(f"Approximate location for the countries in {region}")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.show()