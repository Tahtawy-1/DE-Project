import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Cleaned_Data.csv")

# Area distribution
discribtion = df.describe()

q1 = discribtion['Area']['25%']
q3 = discribtion['Area']['75%']

print(q1, q3)

IQR = q3 - q1
upper_bound = 1.5 * q3
lower_bound = 1.5 * q1

upper_outlier = df[df['Area'] > upper_bound][['Name','Area']]
lower_outlier = df[df['Area'] < lower_bound][['Name','Area']]

print(upper_outlier)
print("_"*50)
print(lower_outlier)

print(
    f"""
    The given Data is {(len(upper_outlier)+len(lower_outlier))/len(df)}% outliers.
    """
)
print(
    f"""
    The given Data is {(len(lower_outlier))/len(df)}% lower outliers.
    """
)
print(
    f"""
    The given Data is {(len(upper_outlier))/len(df)}% upper outliers.
    """
)

