#! /usr/bin/env python3

import pandas
import matplotlib
import matplotlib.pyplot as plt
import os
import sys
import numpy as np
from st_helper_functions import *

#my_file = sys.argv[1]

my_file = "prokaryotes.txt"

# reading in initial data set:
data_frame = pandas.read_csv(my_file, sep = '\t', header = 'infer', low_memory = False)

#stolen from Beth. Should make data imports etc into some functions. 
#How would we write tests for that? (so changes to the helper functions don't break other ppls code)


data_frame['Release Date'] = pandas.to_datetime(data_frame['Release Date'])

#set index
data_frame.index = data_frame['Release Date']

#Group by TaxID AND 
#count number of submissions at the end of each calendar year
data_frame_grouped = data_frame.groupby("TaxID").resample("M").count()

#What are the most popular strains? 

##groups the data frame by TaxID 
df = data_frame_grouped['Strain'].unstack("TaxID") 

##returns the rows (TaxIDs) with the largest number of entries, for each year
#needs to be done before grouping. 
top_per_year = df.idxmax(axis=1)
top_overall = df.sum().sort_values().iloc[-15:]

#we don't need this
top_overall_list = list(top_overall.index)

col_order = df.sum().sort_values(inplace=False).index
df[col_order]

#splits (ordered) dataframe into two parts- lowest, and highest 20 TaxIDs
df1=np.split(df[col_order], [-20], axis=1)

#Combines these dataframes, summing all small values to combine them
final_df = pandas.concat([df1[1], df1[0].sum(axis=1)], axis=1)

#Make the plot! 
final_df.plot.areas()
plt.show()

