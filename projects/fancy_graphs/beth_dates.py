#! /usr/bin/env python3

import pandas
import matplotlib
import matplotlib.pyplot as plt
import os

my_file = sys.argv[1]

# reading in initial data set:
data_frame = pandas.read_csv(my_file, sep = '\t', header = 'infer', low_memory = False)

#convert release data column data type to datetime

data_frame['Release Date'] = pandas.to_datetime(data_frame['Release Date'])

#set index
data_frame.index= data_frame['Release Date']

#count number of submissions at the end of each calendar year
data_frame.resample('A').count()
