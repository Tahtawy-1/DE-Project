import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df.boxplot(
    column='population',
    figsize=(8, 5)
)

plt.title('Population Outliers')
plt.ylabel('Population')
plt.show()