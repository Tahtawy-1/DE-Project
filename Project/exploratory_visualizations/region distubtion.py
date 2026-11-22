import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter

df = pd.read_csv("Cleaned_Data.csv")

ax = df.groupby('Region')['Population'].sum().plot(
    kind='barh',
    figsize=(10, 5),
)

# Option C: millions → 200M, 400M, ... 1,600M
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1e6:,.0f}M'))

plt.title('Total Population by Region')
plt.ylabel('Region')
plt.xlabel('Population')
plt.tight_layout()
plt.show()