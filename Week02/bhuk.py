# This program use the next Url and it will print this JSON data:
# https://www.gov.uk/bank-holidays.json
# Author: Tanya San Juan

import requests
url = 'https://www.gov.uk/bank-holidays.json'
response = requests.get(url)
data = response.json()
print(data)