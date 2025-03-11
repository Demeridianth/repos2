import numpy as np
import pandas as pd


nums = [1, 2, 3, 4]
series = pd.Series(nums, name = 'Numbers')
print(series)
# 0    1
# 1    2
# 2    3
# 3    4
# Name: Numbers, dtype: int64

series = pd.Series(np.arange(5), name='my Array')
print(series)
# 0    1
# 1    2
# 2    3
# 3    4
# Name: Numbers, dtype: int64

series.index