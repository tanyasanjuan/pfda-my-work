# Representing data
# Author: Tanya San Juan
# This program creates a CSV file called data.csv.

import csv
import pandas as pd

filename = 'data.csv'
datadir = '/Users/tanya/OneDrive/Documentos/ATU/Dev/pands/pfda-my-work/Week02/'

with open (datadir + filename, 'rt') as fp:
    reader = csv.reader(fp, delimiter=',')
    for line in reader:
        print(line)
# this will print each line as a list

# modifiying the program to deal with the header line separately
with open (datadir + filename, 'rt') as fp:
    reader = csv.reader(fp, delimiter=',')
    linecount = 0
    for line in reader:
        if not linecount: # first row ie header row
            print(f"{line}\n-------------------")
        else:
            print(line)
        linecount += 1

# Program modified to calculate the average age of the people in the CSV file
with open (datadir + filename, 'rt') as fp:
    reader = csv.reader(fp, delimiter=',')
    linecount = 0
    total_age = 0
    for line in reader:
        if not linecount: # first row ie header row
            pass
        else: # all other rows
            total_age += int(line[1]) # the age is in the second column (index 1)
        linecount += 1
    print(f"\nAverage Age is: {total_age/(linecount-1)}") # linecount-1 to exclude header row



# we will use the quoted parameter to read in the numbers as floats
with open (datadir + filename, 'rt') as fp:
    reader = csv.reader(fp, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total_age = 0
    for line in reader:
        if not linecount: # first row ie header row
            pass
        else: # all other rows
            total_age += line[1] # the age is in the second column (index 1)
        linecount += 1
    print(f"\nAverage Age is: {total_age/(linecount-1)}") # linecount-1 to exclude header row


# read the file as a dictionary object
with open (datadir + filename, 'rt') as fp:
    reader = csv.DictReader(fp, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total_age = 0
    for line in reader:
        total_age += line['age'] # the age is in the column with header 'age'
        linecount += 1
    print(f"\nAverage Age is: {total_age/linecount}") # there's no the -1 here as DictReader skips the header row

df = pd.read_csv(datadir + filename)
df.info()