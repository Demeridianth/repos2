import numpy as np
import pandas as pd


nums = [1, 2, 3, 4]
series = pd.Series(nums, name = 'Numbers')
series
# 0    1
# 1    2
# 2    3
# 3    4
# Name: Numbers, dtype: int64

series = pd.Series(np.arange(5), name='my Array')
series
# 0    1
# 1    2
# 2    3
# 3    4
# Name: Numbers, dtype: int64


# RangeIndex(start=0, stop=5, step=1)
series.index = [10, 20, 30, 40 , 50]        # u can change index
series
# 10    0
# 20    1
# 30    2
# 40    3
# 50    4
# Name: my Array, dtype: int64

series.values
# [0 1 2 3 4]


""" data types """

series = pd.Series(np.arange(5), name='Array')
# 0    0
# 1    1
# 2    2
# 3    3
# 4    4
# Name: Array, dtype: int64

series.astype('float')      # you can change datatypes in Pandas
# 0    0.0
# 1    1.0
# 2    2.0
# 3    3.0
# 4    4.0
# Name: my Array, dtype: float64

series.astype('bool')
series.astype('object')
series.astype('string')


""" indexing """

# Custom index
sales = [0, 5, 155, 0, 518]
items = ['coffee', 'bananas', 'tea', 'coconut', 'sugar']        # replace indexes with items

sales_series = pd.Series(sales, index=items, name='Sales')
# OR
sales_series.index = ['coffee', 'bananas', 'tea', 'coconut', 'sugar']
# coffee       0
# bananas      5
# tea        155
# coconut      0
# sugar      518

sales_series['tea']
# 155

sales_series['bananas':'sugar']         # when slicing using string labels as indexes the last one WILL BE INCLUDED !
# bananas      5
# tea        155
# coconut      0
# sugar      518

# iloc
sales_series.iloc[2]        # grabs by index even if index is text based
# 155

sales_series.iloc[[1, 3]]       #  by passing a list - grabs indexes and values
# bananas    5
# coconut    0

sales_series[1:5]       # slicing
# bananas      5
# tea        155
# coconut      0
# sugar      518