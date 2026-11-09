import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Cleaned_Data.csv")

# Currencies Bar Chart
currencies = df['Currency'].value_counts()[:10]

other_currencies = len(df['Currency'].value_counts())-10

currencies["Other"] = other_currencies

currencies.plot(kind='barh', x=range(0,60,2))

plt.gca().invert_yaxis()
plt.xticks(range(0,61,4))
# Add titles and labels
plt.title("Currencies Used Around the World")
plt.xlabel("Number of Countries")
plt.ylabel("Countries")

# Display the plot
plt.show()