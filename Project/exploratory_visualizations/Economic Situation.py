import ast
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Cleaned_Data.csv")

country = input("Please Enter a Country Name: ").strip().capitalize()

try:
    economic_situation = df[df['Name'] == country]['Economy'].reset_index()['Economy'][0]
    economic_situation = ast.literal_eval(economic_situation)

    gini_coefficient = pd.Series(economic_situation['gini_coefficient'])

    sns.lineplot(gini_coefficient, marker = 'o')

    plt.title(f"Gini Coefficient Over Time for {country}")
    plt.xlabel("Year")
    plt.ylabel("Gini Coefficient")
    plt.show()
except KeyError:
    print("Sorry, this country's data isn't available :(")