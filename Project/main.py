import pandas as pd
import sqlite3
import requests
import numpy

API_key = 'https://api.restcountries.com/countries/v5?q=palestine'

headers = {
    "Authorization": f"Bearer rc_live_c3badbed198e4610b8cc7f0abc9f7401"
}

response = requests.get(API_key, headers=headers)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code} - {response.text}")
    
df = pd.DataFrame(data)

print(df)