# After Finishing all the worK
# Combining the code here:
import pandas as pd
import sqlite3
import requests
import numpy as np
import matplotlib.pyplot as plt

PARAMETERS = ["names.common","borders","currencies","area,population","region","languages","economy","area","coordinates"]

API_key = f"https://api.restcountries.com/countries/v5?response_fields={",".join(PARAMETERS)}&limit=100"

headers = {
    "Authorization": f"Bearer rc_live_c3badbed198e4610b8cc7f0abc9f7401"
}

response = requests.get(API_key, headers=headers)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code} - {response.text}")
    
df = pd.DataFrame(data['data']['objects'])  

print(df.columns)

# Sitting names ---> Common name only
df['Name'] = df['names'].str['common'].astype(str)

# Sitting Currency ---> The first one in the list of used currencies
df['Currency'] = df['currencies'].str[0].str['name'].astype(str)

# sitting Area ---> Kilometers only
df['Area'] = df['area'].str['kilometers'].astype(int)

# Sitting Borders ---> Destructing the list
df['Borders'] = df['borders'].str.join(', ').astype(str) # Turn the list into Comma Separated Values (as one string)
df['Borders'] = df['Borders'].replace('', 'ISLAND') # Any empty string indicates an ISLAND

# Dealing with the languages column
df['Language'] = df['languages'].str[0].str['bcp47']
df['Language'] = df['Language'].fillna('en') # Removing Null values: Default language is mainly English

# Sorting the DF by: Region & population
df = df.sort_values(by=['region', 'population'], ascending=[True, False])

# Resetting the names of some columns
df['Region'] = df['region']
df['Population'] = df['population']
df['Economy'] = df['economy']
df['Coordinates'] = df['coordinates']

# Setting Area ---> Kilometers only
df['Area'] = df['area'].str['kilometers'].astype(float)

# Dropping old columns, keeping the new formatted
df = df[['Name', 'Currency', 'Borders','Area', 'Language', 'Region', 'Population', 'Area', 'Economy', 'Coordinates']]

# Resetting the indeces
df = df.reset_index(drop=True)

print(df.head(5))

df.to_csv("Cleaned_Data.csv")