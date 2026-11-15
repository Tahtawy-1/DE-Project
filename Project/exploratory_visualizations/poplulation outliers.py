import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Cleaned_Data.csv")

df.boxplot(
    column='Population',
    figsize=(8, 5)
)

plt.title('Population Outliers')
plt.ylabel('Population')
plt.show()