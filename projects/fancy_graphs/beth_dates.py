#! /usr/bin/env python3

import pandas
import matplotlib
import matplotlib.pyplot as plt
import os
import bokeh
from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import CARTODBPOSITRON

output_file("tile.html")

# range bounds supplied in web mercator coordinates
p = figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000),
           x_axis_type="mercator", y_axis_type="mercator")
p.add_tile(CARTODBPOSITRON)

show(p)


summary = sys.argv[1]
locs = sys.argv[2]

# reading in initial data sets:
data_frame = pandas.read_csv(summary, sep = '\t', header = 'infer', low_memory = False)
lat_lon = pandas.read_csv(locs, sep='\t')

#add latitude and longitude for submitters
lat_lon.columns=['Center','lat','lon']
df = pandas.merge(data_frame, lat_lon, on='Center')

#convert release data column data type to datetime

df['Release Date'] = pandas.to_datetime(df['Release Date'])
df['Year']=df['Release Date'].dt.year
df['Month']=df['Release Date'].dt.month

#set index
df.index= data_frame['Release Date']

#count number of submissions at the end of each calendar year
df.resample('A').count()

