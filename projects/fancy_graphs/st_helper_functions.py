import numpy as np
import pandas

def remove_small_values(df, small, large): 
	"""

	Returns a pandas dataframe (df) with values between 'small' and 'large' counted into a new column (small values), and removed from the dataset.  
	Note that the columns of the input dataframe must be the grouping we care about. 
	Unsure how to force this.  
	Requires numpy and pandas. Also unsure how to force this. 
	BUG: this removes some small value too. 
	https://stackoverflow.com/questions/42916989/replace-missing-values-in-all-columns-except-one-in-pandas-dataframe

	"""

	i = [x for x in range(small, large)]

	#sum all entries with small values
	df['small values'] = df.isin(i).sum(1)

	df.iloc[:, 0:-1] = df.iloc[:, 0:-1].replace(i, np.NaN)


	#replace all small values with NaN 
	#df.replace(i, np.NaN, inplace=True)

	#drop columns where all rows are NaN 
	df.dropna(axis=1, how = 'all', inplace=True)

	return df 


def group_df_by(data_frame, grouping, time_interval = "M"): 

	"""
	Groups data_frame by the grouping value. 
	grouping must be a column name of data_frame. 
	You can also specify the time interval- default is month. 
	(Look, I used an assert statement!)
	"""


	#count number of submissions every month
	assert grouping in data_frame.columns
	#selecting only one column speeds up function by 20-40s. Will still take 2mins
	data_frame = data_frame.loc[:, [grouping]].groupby(grouping).resample(time_interval).count()
	data_frame = data_frame[grouping].unstack(grouping)
	return data_frame


