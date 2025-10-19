# Representing data
# Author: Tanya San Juan
# This program creates a CSV file called data.csv.

import csv

filename = 'data.csv'
datadir = '/Users/tanya/OneDrive/Documentos/ATU/Dev/pands/pfda-my-work/Week02/'
"""
with open (datadir + filename, 'rt') as fp:
    reader = csv.reader(fp, delimiter=',')
    for line in reader:
        print(line)
# this will print each line as a list
"""
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
