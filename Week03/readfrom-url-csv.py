# Program to read a CSV file from a URL and display its contents using pandas
# Author: Tanya San Juan

import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=wind_speed_10m,rain&past_days=3&forecast_days=1&format=csv"
df = pd.read_csv(url)
print(df.head())  # Display the first few rows of the DataFrame

# For different protocol, (we need to pip install S3Fs)
url = "s3://noaa-gsod-pds/2020/72278023183.csv"
df_s3 = pd.read_csv(url)
print(df_s3.head())  # Display the first few rows of the DataFrame from S3

# Write it out to an Excel file
excel_filename = 'weather_data.xlsx'
df.to_excel(excel_filename, index=False)

# Using Json will display the data in a different format
url_json = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=wind_speed_10m,rain&past_days=3&forecast_days=1&format=json"
df_json = pd.read_json(url_json)
print(df_json.head())  # Display the first few rows of the DataFrame from JSON
# results are in a list format.