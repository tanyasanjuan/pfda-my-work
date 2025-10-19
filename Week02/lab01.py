# Representing data
# Author: Tanya San Juan
# This program creates a CSV file called data.csv.

import csv

filename = 'data.csv'
datadir = 'where did you put it'

with open(datadir + filename, 'rt') as fp:
    reader = csv.reader(fp, delimiter=)
    for line in reader:
        print(line)