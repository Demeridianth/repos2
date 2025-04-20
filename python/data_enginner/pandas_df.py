import pandas as pd
import numpy as np


""" DATAFRAMES """

# base python into dataframe, rarely used

dt = pd.DataFrame(
    {
        'item_id': [1, 2],
        'item_name': ['item_1', 'item_2'],

    }
)

dt.shape
dt.index
dt.columns
dt.columns = ['id', 'name']     # changed name of the columns
dt.axes         # number of lines and names of columns
dt.head()       # firts five lines
dt.tail()       # last five lines
dt.sample()     # random sample
dt.info()
dt.info(show_counts=True)       # if more then 1.7 min lines, u need this to display the NaN values
dt.describe()       # will, show mean, max, min etc.
dt.describe(include='all').round()       # even MORE info !

dt.isna().sum()         # count NaN

