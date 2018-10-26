#! /usr/bin/env python3

import pandas
import matplotlib
import matplotlib.pyplot as plt
import os

summary = sys.argv[1]
locs = sys.argv[2]

# reading in initial data sets:
data_frame = pandas.read_csv(summary, sep = '\t', header = 'infer', low_memory = False)
lat_lon = pandas.read.csv(locs, sep='\t',header='none')

#add latitude and longitude for submitters
lat_lon.columns=['Center','lat','lon']
df = pandas.merge(data_frame, lat_lon, on='Center')

#convert release data column data type to datetime

df['Release Date'] = pandas.to_datetime(df['Release Date'])

#set index
df.index= data_frame['Release Date']

#count number of submissions at the end of each calendar year
df.resample('A').count()
