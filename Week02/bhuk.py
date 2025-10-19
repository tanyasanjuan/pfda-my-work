# This program use the next Url and it will print this JSON data:
# https://www.gov.uk/bank-holidays.json
# Author: Tanya San Juan

import requests
url = 'https://www.gov.uk/bank-holidays.json'
response = requests.get(url)
data = response.json()
print(data)
# this print a dictionary object with nested dictionaries and lists

# modifying the program to print the 1st holiday in northern ireland
print(data['northern-ireland']['events'][0])

# modifying the program to print the holidays that happen in northern ireland
for holiday in data['northern-ireland']['events']:
    print(f"{holiday['title']} falls on {holiday['date']}")

# modifying the program to print only the holidays in 2024 in northern ireland
for holiday in data['northern-ireland']['events']:
    if holiday['date'].startswith('2024'):
        print(f"{holiday['title']} falls on {holiday['date']}")

# modifying the program to print only the holidays in nothern ireland and not in england, wales and scotland
ni_holidays = data['northern-ireland']['events']
for holiday in ni_holidays:
    if holiday not in data['england-and-wales']['events'] and holiday not in data['scotland']['events']:
        print(f"{holiday['title']} falls on {holiday['date']}")