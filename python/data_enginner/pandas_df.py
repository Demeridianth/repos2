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
dt['id']                # get column
dt[['id', 'name']]      # get 2 columns


# iloc STOP POINT NOT INCLUSIVE !!!
dt.iloc[:5, :1]         # first axis is rows, second is column, works with numerical indexes
dt.iloc[:, -1]          # will grab data_series
dt.iloc[:, [-1]]          # will grab data_frame


# loc STOP POINT IS INCLUSIVE !!!
dt.loc[:, 'id']             # works with named values
dt.loc[:, 'id': 'name']     # get slice
dt.loc[:, ['id', 'name']]   # get all data from columns

oil = pd.read_csv('oil.csv')
oil.columns = ['data', 'price']     # rename columns
oil['euro price'] = oil['price'] * 1.1      # create new column
print(oil.head())


# drop
oil.drop('price', axis=1)                           # will not change/save dataframe
oil.euro = oil.drop('price', axis=1)                # will create a var with a new data frame
oil.drop('price', axis=1, inplace=True)             # WILL  change/save dataframe
oil = pd.concat([oil, oil.iloc[[-1]]], ignore_index=True)       # duplicates the last row


# duplicates
oil.duplicated()        # return True on duplicates
oil.duplicated(subset='price').sum()        # count duplicates
oil.drop_duplicates(subset=['price'], keep='last', ignore_index=True)       # delete duplicates, subset=keep last duplicate, ingonre_index = removes gaps


# NaN
oil.isna().sum()        # count Null values
oil.fillna(0)           # fill missing values with 0
oil.fillna({'price':0}) # fill missing values in a column 'price'
oil['price'].fillna(0)
oil.dropna()            # drop missing values


# filtering
oil.loc[oil['price'] > 100]

oil['benchmark'] = 100      # creating new column
oil.loc[oil['price'] > oil['benchmark']]        # use it for filtering

oil.loc[oil['date'].str[:4] == '2013']      # slice off year using str() and use it as a filter

mask = ([oil['price'] > oil['benchmark']])

mask = (oil['dcoilwtico'] > oil['benchmark']) & (oil['date'].str[:4] == '2013')     # multiple conditions filter
oil[mask]


# filtering with QUARY()
oil = pd.read_csv('oil.csv', parse_dates=['date'])      # parse_dates will make dates datetime64 dtype
oil.query('dcoilwtico > benchmark and date.dt.year == 2013')
smokers_southeast = dt.query('smoker == "yes" and region == "southeast"')       # column names dont have "", values DO
# transactions.query("store_nbr in [25, 31] and date.str[6] in ['5', '6'] and transactions < 2000").sum().iloc[2]


# sorting
oil.sort_index(ascending=False)         #from highest to lowest
oil.sort_index(axis=1)         # axis 1 will sort column name

oil.sort_values(['month', 'dcoilwtico'], ascending=[True, False])       # date by 2 columns, and giving them different ascending values