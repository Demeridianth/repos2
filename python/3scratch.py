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

sales_series[1:5]       # slicing
# bananas      5
# tea        155
# coconut      0
# sugar      518


""" iloc | handles actual indexes"""

# iloc
sales_series.iloc[2]        # grabs by index even if index is text based
# 155

sales_series.iloc[[1, 3]]       #  by passing a list - grabs indexes and values
# bananas    5
# coconut    0


""" loc | handles index values """

sales_series.index = ['coffee', 'bananas', 'tea', 'coconut', 'sugar']
# coffee       0
# bananas      5
# tea        155
# coconut      0
# sugar      518

sales_series.loc['tea']         # preffered way to grab values by their CUSTOM index
# 155

sales_series.loc['coffee': 'coconut']       # .loc slice WILL INCLUDE last 'index'
# coffee       0
# bananas      5
# tea        155
# coconut      0

sales_series[0:3]           # simple slice WILL NOT INCLUDE last 'index'
# coffee       0
# bananas      5
# tea        155


""" reset index"""

reseted_series =  sales_series.reset_index()          # returns default indexes with index values BUT doesnt change the series
reseted_series
# 0	    0	0
# 1	    2	1
# 2	    3	2
# 3	    100	3
# 4	    5	4


sales_series.reset_index(drop=True)         # resets indexes to default numbers
# 0      0
# 1      5
# 2    155
# 3      0
# 4    518


""" .isin()  ~.isin()  (in, not in) """

sales_series.index.isin(['coffee'])
# array([ True, False, False, False, False])

~sales_series.index.isin(['coffee'])
# array([False,  True,  True,  True,  True])        # tilde inverts


""" sorting """

sales_series.sort_values()
# coffee       0
# coconut      0
# bananas      5
# tea        155
# sugar      518
# Name: Sales, dtype: int64

sales_series.sort_values(ascending=False)
# sugar      518
# tea        155
# bananas      5
# coffee       0
# coconut      0
# Name: Sales, dtype: int64


sales_series.sort_index()
# coconut      0
# coffee       0
# coffee       5
# sugar      518
# tea        155

sales_series.sort_index(ascending=False)        # alphabetically by index name
# tea        155
# sugar      518
# coffee       0
# coffee       5
# coconut      0


sales_series.sort_index(ascending=False, inplace=True)      # will save the changes to the series


""" math operations """

monday_sales = pd.Series([0, 5, 155, 0, 518])
monday_sales
# 0      0
# 1      5
# 2    155
# 3      0
# 4    518
# dtype: int64

'$' + monday_sales.astype('float').astype('string')
# 0      $0.0
# 1      $5.0
# 2    $155.0
# 3      $0.0
# 4    $518.0
# dtype: string

my_series = pd.Series([1, np.NaN, 2, 3, 4], index = ['day_0', 'day_1', 'day_2', 'day_3', 'day_4'])
my_series
# day_0    1.0
# day_1    NaN
# day_2    2.0
# day_3    3.0
# day_4    4.0
# dtype: float64

my_series.add(1, fill_value=0)      # if 'fill_value' sees a missing value it will make it ZERO !!!
# day_0    2.0
# day_1    1.0
# day_2    3.0
# day_3    4.0
# day_4    5.0
# dtype: float64


""" string methods """

string_series = pd.Series(my_series.index)
# 0    day_0
# 1    day_1
# 2    day_2
# 3    day_3
# 4    day_4
# dtype: object

string_series.str.contains('3')
# 0    False
# 1    False
# 2    False
# 3     True
# 4    False
# dtype: bool

string_series.str[1:3]
# 0    ay
# 1    ay
# 2    ay
# 3    ay
# 4    ay
# dtype: object


# 0    Adult 25
# 1    Child 12
# 2    Adult 64
# 3     Teen 17
# 4    Adult 45
string_series.str.split(' ', expand=True)       # will split 'Adult' and '25
string_series[1].astype('int')      # will convert 25 to int
string_series
# 	    0	1
# 0	Adult	25
# 1	Child	12
# 2	Adult	64
# 3	Teen	17
# 4	Adult	45