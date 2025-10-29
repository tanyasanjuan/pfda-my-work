# Program to read a CSV file from a URL and display its contents using pandas
# Author: Tanya San Juan

import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=wind_speed_10m,rain&past_days=3&forecast_days=1&format=csv"
df = pd.read_csv(url)
print(df.head())  # Display the first few rows of the DataFrame