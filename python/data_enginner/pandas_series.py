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
      # will convert 25 to int
string_series
# 	    0	1
# 0	Adult	25
# 1	Child	12
# 2	Adult	64
# 3	Teen	17
# 4	Adult	45


""" aggregation functions """

my_series.count()       # will deduct empty values (lines)
my_series.sum()

my_series.quantile(50)      # will deduct percentage of the series, what percentage of the numbers 
df = pd.DataFrame({
    'A': [10, 20, 30, 40, 50],
    'B': [5, 15, 25, 35, 45]
})
# Median (50th percentile) of each column
print(df.quantile(0.5))
# A    30.0
# B    25.0
# Name: 0.5, dtype: float64

my_series.quantile(0.5, interpolation='nearest')        # will grab an actual value instead of a percentage


my_series.nunique()         # number of unique values
my_series.unique()         # grab unique values

# 0    day_0
# 1    day_0
# 2    day_2
# 3    day_2
# 4    day_4
my_series.value_counts()        # show the number of all the same values
# day_0    2
# day_2    2
# day_4    1

my_series.value_counts(normalize=True)      # will grab percentage that each value takes in the series


""" missing data: NaN """
# will make any data type into a float, even if it is not

sales = pd.Series([0, 1, 2, pd.NA, 100], dtype='Int16')     # pandas method handling NaN

na_series = pd.Series(['COMPLETE', pd.NA, pd.NA, pd.NA, 'COMPLETE'])
# 0    COMPLETE
# 1        <NA>
# 2        <NA>
# 3        <NA>
# 4    COMPLETE
# dtype: object

na_series.isna()
# 0    False
# 1     True
# 2     True
# 3     True
# 4    False
# dtype: bool

na_series.isna().sum()      # will count missing values
3

na_series.value_counts(dropna=False)        # will count everything
# <NA>        3
# COMPLETE    2
# Name: count, dtype: int64

na_series.dropna()
# 0    COMPLETE
# 4    COMPLETE
# dtype: object

na_series.fillna('INCOMPLETE')
# 0      COMPLETE
# 1    INCOMPLETE
# 2    INCOMPLETE
# 3    INCOMPLETE
# 4      COMPLETE
# dtype: object


""" apply(), custom function """

na_series.apply(lambda x: x[-1])
# same as
na_series.str[-1]


def search(string, looking_for):
    if looking_for in string:
        print('found it')
    print('Nope')

na_series.apply(search, args=2)

# oil_series.apply(lambda x: 'buy' if x < oil_series.quantile(0.9) else 'wait')


def func(price, percentile):        # first argument will be the series automatic
    if price < percentile:
        return 'buy'
    return 'wait'

na_series.apply(func, args=(na_series.quantile(0.9),))



""" where """

# df.where(logical test, value IF FALSE, inplace=False)         # numpy WHERE IS BETTER, because VALUE IF TRUE

s_series = pd.Series(['day_0', 'day_1', 'day_2', 'day_3', 'day_4'])
# 0    day_0
# 1    day_1
# 2    day_2
# 3    day_3
# 4    day_4
# dtype: object

s_series.where(
    s_series.str.contains('2'), 'Nope').where(
    ~s_series.str.contains('2'), 'Found it')

# 0        Nope
# 1        Nope
# 2    Found it
# 3        Nope
# 4        Nope
# dtype: object

# WITH NUMPY
np.where(s_series.str.contains('2'), 'Found it', 'Nope')
# pd.Series(np.where(s_series.str.contains('2'), 'Found it', 'Nope'))       # convert into a Series

