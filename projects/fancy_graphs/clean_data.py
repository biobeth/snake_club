#! /usr/bin/env python3
#
# This is just a file with the code that I used to get used to pandas and
# data cleaning in Python.
# There should be nothing significantly important/awesome here.
#
# I guess my main goal is to generate a whole bunch of cleaned data for
# different purposes, so it can be used later for the "interactive website".
#
# Riku

import pandas
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import sys

my_file = 'prokaryotes.txt'

df = pandas.read_csv(my_file, sep = '\t', header = 'infer', low_memory = False)

# Data cleaning

# Convert '-' into NAs:
df = df.replace('-', np.nan)

for x in df.columns:
    df[x][0:5]

df = df.astype({"#Organism/Name": str, "TaxID": str, "BioProject Accession": str, "BioProject ID": str, "Group": str, "SubGroup": str, "Size (Mb)": float, "GC%": float, "Replicons": str, "WGS": str, "Scaffolds": float, "Genes": float, "Proteins": float, "Status": str, "Center": str, "BioSample Accession": str, "Assembly Accession": str, "Reference": str, "FTP Path": str, "Strain": str })

for column in df.columns:
    if df[column].dtype == 'float':
        df.boxplot(column, by = 'Group', rot = 90, fontsize = 8)
        plt.show()

df.groupby('Group').describe()

