import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Cleaned_Data.csv")

grouped = df.groupby('Language').aggregate({"Language":"count"})

grouped[grouped['Language'] > 1].plot(
    kind='barh',
    figsize=(10, 5)
)

plt.title('Total Number of countries that speak a Language')
plt.xlabel('Number of Countries')
plt.ylabel('Language')
plt.tight_layout()
plt.show()

