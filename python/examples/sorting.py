fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
# >>> ['apple', 'banana', 'grape', 'raspberry']
fruits
# >>> ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits, reverse=True)
# >>> ['raspberry', 'grape', 'banana', 'apple']
sorted(fruits, key=len)
# >>> ['grape', 'apple', 'banana', 'raspberry']
sorted(fruits, key=len, reverse=True)
# >>> ['raspberry', 'banana', 'grape', 'apple']
fruits
# >>> ['grape', 'raspberry', 'apple', 'banana']

# built-in function sorted creates a new list and returns it.


fruits.sort()
fruits
# >>>  ['apple', 'banana', 'grape', 'raspberry'] 

# The list.sort method sorts a list in place—that is, without making a copy. It returns None



# to sort a list of dicts:

l = [{'Name': 'Alice', 'Age': 40, 'Point': 80},
     {'Name': 'Bob', 'Age': 20},
     {'Name': 'Charlie', 'Age': 30, 'Point': 70}]

sorted(l)
# TypeError: '<' not supported between instances of 'dict' and 'dict'

sorted(l, key=lambda x: x['Age'])
# [{'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80}]



# Use the reverse argument to specify whether the sorting should be in descending or ascending order.

sorted(l, key=lambda x: x['Age'], reverse=True)
# [{'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 20, 'Name': 'Bob'}]