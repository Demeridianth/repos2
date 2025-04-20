import numpy as np
from numpy.random import default_rng


nums = [1, 2, 12, 15, 12313, 1413414]

arr_nums = np.array(nums)
# array([      1,       2,      12,   12313, 1413414])

arr_nums.ndim  # number of dimensions
arr_nums.size   
arr_nums.shape  
arr_nums.dtype  

arr_nums.reshape(2, 3)  # (rows, columns)


""" array creation """

np.zeros((2, 5), dtype=int)     # rows, colums, dtype  fills with zeros
np.ones((2, 5), dtype=int)      # rows, colums, dtype   fils with ones
np.arange(1, 10)                # start, stop, step
np.linspace(1, 10, 5)           # start, stop, n  (floats)
np.arange(1, 11).reshape(2, 5)  # create an array from 1 to 10 and give it 2 rows and 5 columns (int)


""" random """

# random
rng = default_rng(12345)
random_array = rng.random(10)  # 10 numbers between 0 and 1  with a 'seed'(name) of '12345' = will always generate the same 'random' number
rng = np.random.default_rng(616)
rng.random(10)
# array([0.392595  , 0.65460534, 0.33051526, 0.45009373, 0.6001609 ,
#        0.77769883, 0.96428968, 0.56511439, 0.50409848, 0.6566927 ])

# normal
rng.normal(5, 1, 10) # middle number, deviation, n  and will return float

# integers
rand_int = rng.integers(0, 10, 100)  # start, end, n   random int

# choice
a = np.array([1, 2, 3, 4, 5, 6])
half = rng.choice(a, size=len(a)//2, replace=False)  # Randomly select half the elements



numbers = np.random.random(6)
# will generate random floats from 0 to 1

numbers = np.random.randint(100, size=(2, 3, 4))    # or  low, high, size=() IF MORE 1 dimention

arr = np.random.uniform(low=10, high=20, size=5)  # 5 random floats between 10 and 20


""" indexing and slicing """

products = ['tea', 'milk', 'beef', 'fruit', 'coffee', 'vegetables']
products2d = np.array(products).reshape(2, 3)
# array([['tea', 'milk', 'beef'],
#        ['fruit', 'coffee', 'vegetables']], dtype='<U10')

# indexing in 2d
products2d[1, 1]        # will get 'coffee' - it is on row index[1] AND on that row it is on index[1]

# slicing in 2d
products2d[1:, 1]       # will get 'coffee' - first "argument" is rows, second is columns


""" math operations """

sales = [[0, 1, 12, 1231, 12414], [1, 5, 4354, 1241, 1241334]]
sales_arr = np.array(sales)
# array([[      0,       1,      12,    1231,   12414],
#        [      1,       5,    4354,    1241, 1241334]])

sales_arr + 2     # will add 2 to each element
sales_arr * 3     # will multiply each elements by 3

quantity = sales_arr[0, :]   # the first row
prices = sales_arr[1, :]     # multiplied by second row

quantity * prices
# array([          0,           5,       52248,     1527671, 15409920276])

# round
rand_nums = rng.random(19)
rand_nums = rand_nums.round(2)      # round up to 2 numbers after dot = 0.nn


""" filtering """

sales = [0, 1, 21, 12, 0,  23, 0]
sales_arr = np.array(sales)

sales_arr != 0
# array([False,  True,  True,  True, False,  True,  True, False])
sales_arr[sales_arr != 0]
# array([     1,   2321, 124124,  12312,    565])

sales_arr % 2 == 0

# AND ,  OR
sales_arr[(sales_arr == 565) | (sales_arr > 2000)]       #  '|' = OR

mask =  sales_arr[(sales_arr > 2000) & (sales_arr < 12000)]       #  '&' = AND
sales_arr[mask]   # store conditions in a variable


sales = [0, 1, 21, 12, 0]
sales_arr = np.array(sales)

products = ['meat', 'milk', 'eggs', 'coffee', 'sweets']
products = np.array(products)

products[sales_arr != 0]     # filter by other array of numbers
# array(['milk', 'eggs', 'coffee'], dtype='<U6')   


""" where() """
#
np.where('logical_test', 'value_if_true', 'value_if_false')
#

arr = np.arange(20)
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
#        17, 18, 19])

np.where(arr % 2 ==0)
# (array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18], dtype=int64)

np.where(arr & 2 == 0, 'even', 'odd')
# array(['even', 'even', 'odd', 'odd', 'even', 'even', 'odd', 'odd', 'even',
#        'even', 'odd', 'odd', 'even', 'even', 'odd', 'odd', 'even', 'even',
#        'odd', 'odd'], dtype='<U4')

np.where(arr % 2 == 0, 'even', np.where(arr == 9, arr, 'odd'))    # does a double test and look if the value is nine and pulls it
# array(['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even',
#        '9', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd',
#        'even', 'odd'], dtype='<U11')


a = np.array(['dog', 'dog', 'cat', 'dog', 'cat'])
b = np.where(a == 'cat')
# [2, 4]
# WHERE WILL RETURN INDEX OF MATCHED STRINGS


""" sum, mean, max"""

arr.sum()           # returns sum
arr.sum(axis=0)     # sum columns
# arr.sum(axis=1)     # sum rows

arr.mean()          # returns avarage
arr.max()           # returns max value
arr.min()           # returns min value

arr = np.arange(20).reshape(2, 10)
# array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]])


rng = np.random.default_rng(616)

price = (rng.random(10) * 10).round(2)

inventory = rng.integers(0, 100, 10)

(price * inventory).sum()
(price * inventory).mean()


""" functions"""

np.median(arr)      # the number in the middle (not avarage)

np.unique(arr)      # returns unique values

np.sqrt(arr)        # returns square root of every value

np.percentile(arr, 50)      # 50 % of all numbers of the array are below the returned number
ten = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
np.percentile(ten, 75)
# np.float64(7.75)      # 75 % of all number in an array 'ten' are below 7.75


""" sort """

arr = np.random.uniform(1, 1000, 10).reshape(2, 5).round(2)
# array([[ 46.23,  49.71, 383.99, 409.06, 999.18],
#        [235.28, 435.51, 652.72, 897.78, 974.21]])

arr.sort()      # by default will sort 1 axis (rows)
# array([[ 46.23,  49.71, 383.99, 409.06, 999.18],
#        [235.28, 435.51, 652.72, 897.78, 974.21]])

arr.sort(0)     # will sort by 0 axis (rows)
# array([[ 46.23,  49.71, 383.99, 409.06, 974.21],
#        [235.28, 435.51, 652.72, 897.78, 999.18]])

np.sort(arr)       # wont change array
arr.sort()         # will change array



