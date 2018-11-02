#! /usr/bin/env python3

import pandas
import matplotlib
import matplotlib.pyplot as plt
import os
import sys

my_file = sys.argv[1]

# reading in initial data set:
data_frame = pandas.read_csv(my_file, sep = '\t', header = 'infer', low_memory = False)

df = pandas.read_csv(my_file, sep = '\t', header = 'infer', low_memory = False)

# Data cleaning

# Columns to drop:
to_drop = ['FTP Path', 'BioProject Accession', 'BioSample Accession', 'BioProject ID', 'Replicons', 'Assembly Accession']

df = df.drop(to_drop, axis = 1)

# there are '-' (NA) values in GC%
for x in df['GC%']:
    if x == '-':
        print(x)

for x in df['Genes']:
    if x == '-':
        print(x)

for x in df['Proteins']:
    if x == '-':
        print(x)

df[['GC%']].astype(float)

df.groupby('Group').describe()


# subsetting columns from the data set that has been read in:
#
# This subsets columns 1:4 and rows 1:2 :
subset = data_frame[data_frame.columns[1:4]][1:2]

# print out all the columns in the data:
data_frame.columns

# group by a certain column (e.g Group):
counts = data_frame.groupby('Group')['Group'].count()

print(counts)

# Plot the counts:
counts.plot.bar()

# Show the plot:
plt.show()

