import numpy as np
from console_logging import console


nums = np.array([1, 2, 3, 4, 5])
# print(nums)
# [1 2 3 4 5]

d = {1: 'A', 2: 'B'}

nums_mul = np.array([[[1, d, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1]],
                    [[1, 1, 1, 1], [1, '1', 1, 1], [1, 1, 1, 1]]])

# print(nums_mul[0])
# print(nums_mul[0, 1])
# [1 2 3]
# 2

print(nums_mul.shape)
# (2, 3, 3)
# 2 lists with three list elements with 3 elements

print(nums_mul.ndim)
# 3
# three levels in depth

print(nums_mul.size)
# 24
# number of all elements

print(nums_mul.dtype)



# datatypes #

print(type(nums_mul[0][0][0]))
print(repr(nums_mul[0][0][1]))
# <class 'numpy.str_'>
# changing one element to a string changes everything to a string

mul = np.array([[1,2,3],
                [4, 5, 6],
                [7, 8, 9]], dtype='<U7')
# dtype changed array elements into strings
#  BECAUSE NUMPY IS WRITTEN IN C

print(mul.dtype)
# <U7
print(repr(mul[1][0]))
# np.str_('4')



# full #
# fill numpy array with one value

fl = np.full((2, 3, 4), 9)
print(fl)
# [[[9 9 9 9]
#   [9 9 9 9]
#   [9 9 9 9]]

#  [[9 9 9 9]
#   [9 9 9 9]
#   [9 9 9 9]]]
# 2 lists of 3 list elemnts with 4 elements in them

zr = np.zeros((2, 3, 2))
print(zr)
# [[[0. 0.]
#   [0. 0.]
#   [0. 0.]]

#  [[0. 0.]
#   [0. 0.]
#   [0. 0.]]]

one = np.ones((2, 2, 2))
print(one)
# [[[1. 1.]
#   [1. 1.]]

#  [[1. 1.]
#   [1. 1.]]]



# arange #
# (start, end, step)

x_values = np.arange(0, 100, 5) 
print(x_values)
# [ 0  5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]


# linspace #
# (start, end, how many values do u want to generate)

ln = np.linspace(0, 100, 8)
print(ln)
# [  0.          14.28571429  28.57142857  42.85714286  57.14285714
#   71.42857143  85.71428571 100.        ]



# nan | inf #
# not a number | infinity #

print(np.isnan(np.sqrt(-1)))
# check if the square root of -1 is not a number
# >>> Ture

print(np.isinf(np.array([10]) / 0))
# devide 10 by zero
# >>> [ True]
 

print(np.sqrt(-1))
# check if the square root of -1 is not a number
# >>> nan

print((np.array([10]) / 0))
# devide 10 by zero
# >>> [inf]



# math operations

# def python list
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

# numpy array
a1 = np.array(l1)
a2 = np.array(l2)

print(l1 * 5)
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(a1 * 5)
# [ 5 10 15 20 25]

print(l1 + l2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(a1 / a2)
# [ 7  9 11 13  5]


b1 = np.array([1,2,3])
b2 = np.array([[1],
               [2]])

print(b1 + b2)
# [[2 3 4]
#  [3 4 5]]
# 1 + 1, 2 + 1, 3 + 1
# 1 + 2, 2 + 2, 3 + 2


# sqrt #
# returns the square root
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.sqrt(a))
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
print(np.arctan(a))
# ETC.


# array functions

a = np.array([1, 2, 3])

a = np.append(a, [7, 8, 9])
# need to use = for a change to happen

a = np.insert(a, 3, [4, 5, 6])
# (array, position, what to insert)

print(a)


# DELETE #
# doesnt work as u might think !!!
rows = np.array([[1, 2, 3],
                 [4, 5, 6]])

print(np.delete(rows, 1, 1))
# (array, index, axis)
# axis 0 = delete row
# axis 1 = delete column


# STRUCTURING #

sc = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])
# shape (4, 5) - 4 lists (rows) with 5 elements

print(sc.shape)
print(sc.reshape((5, 4)))
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]]
print(sc.reshape((20,)))
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
print(sc.reshape((20, 1)))
# [[ 1]
#  [ 2]
#  .
#  .
#  .
#  [20]]

print(sc.reshape((2, 2, 5)))
# [[[ 1  2  3  4  5]
#   [ 6  7  8  9 10]]

#  [[11 12 13 14 15]
#   [16 17 18 19 20]]]
# 2 collections, 2 lists (rows), 5 elements


# u need to assign it for changes to take place
sc = sc.reshape(5, 4)
print(sc)

# BUT if you use RESIZE, you dont need to assign it
sc.resize((10, 2))
print(sc)
# [[ 1  2]
#  [ 3  4]
#  [ 5  6]
#  [ 7  8]
#  [ 9 10]
#  [11 12]
#  [13 14]
#  [15 16]
#  [17 18]
#  [19 20]]


print(sc.flatten())
# will give one dimention
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
# WILL NOT MAKE A CHANGE TO THE ORIGINAL

print(sc.ravel())
# will give one dimention
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
# WILL CHANGE THE ORIGINAL

# a.flat
var_for = [v for v in sc.flat]
print(var_for)



#  TRANSPOSE # (SWAP ROWS AND COLUMNS)
arr_ = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])


print(arr_.transpose())
# [[ 1  6 11 16]
#  [ 2  7 12 17]
#  [ 3  8 13 18]
#  [ 4  9 14 19]
#  [ 5 10 15 20]]
# OR
print(arr_.T)
# [[ 1  6 11 16]
#  [ 2  7 12 17]
#  [ 3  8 13 18]
#  [ 4  9 14 19]
#  [ 5 10 15 20]]

# OR similar, where u can specify the axes
print(arr_.swapaxes(0, 1))



# JOIN AND SPLIT

arr1 = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10]])

arr2 = np.array([[11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])

# with CONCANTENATE you can choose axis to join
# arr = np.concatenate((arr1, arr2), axis=0)
# print(arr)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)
# [[ 1  2  3  4  5 11 12 13 14 15]
#  [ 6  7  8  9 10 16 17 18 19 20]]


# STACK
# add dimensions
arr = np.stack((arr1, arr2))
print(arr)
# [[[ 1  2  3  4  5]
#   [ 6  7  8  9 10]]

#  [[11 12 13 14 15]
#   [16 17 18 19 20]]]

arr = np.vstack((arr1, arr2))
# on axis 0, same as concantenate
print(arr)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]

arr = np.hstack((arr1, arr2))
# on axis 1
print(arr)
# [[ 1  2  3  4  5 11 12 13 14 15]
#  [ 6  7  8  9 10 16 17 18 19 20]]





# SPLIT

arr = np.array([[1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12], 
                [13, 14, 15, 16, 17, 18],
                [19, 20, 21, 22, 23, 24]])

print(np.split(arr, 2, axis=1))
# [array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10]]), 
# array([[11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20]])]


#  ARRAGATE FUNCTIONS

print(arr.min())
print(arr.max())
print(arr.mean()) # an avarage
print(arr.std())  # Compute the standard deviation along the specified axis
print(arr.sum())
print(np.median(arr))



# RANDOM #

numbers = np.random.randint(100, size=(2, 3, 4))
print(numbers)
# [[[98 57 71 75]
#   [20 64 30 84]
#   [28 50 50 66]]

#  [[36 72 17 91]
#   [60 20 48 68]
#   [21 80 53 78]]]

numbers = np.random.randint(2, size=(2, 3, 4))
print(numbers)
# [[[0 0 0 0]
#   [1 1 0 0]
#   [1 0 0 0]]

#  [[0 0 1 0]
#   [0 1 1 1]
#   [1 1 1 1]]]

numbers = np.random.randint(90, 100, size=(2, 3, 4))
# min - max, size
print(numbers)
# [[[92 97 98 98]
#   [99 93 93 98]
#   [95 91 96 99]]

#  [[94 92 93 99]
#   [90 97 95 94]
#   [90 92 98 99]]]

numbers = np.random.binomial(20, p=0.5, size=(1, 10))
# out of 10 tries, propability, size of the array
# LIKE A COIN FLIP
print(numbers)

numbers = np.random.normal(loc=170, scale=15, size=(1, 10))
# medium size, deviation, size of array
# LIKE SIZE OF STUDENTS IN CLASS
print(numbers)

numbers = np.random.choice([1, 2, 3, 4, 5], size=(5, 10))
# random number out of list


# EXPORT/IMPORT

# saving an npy file (it is binary)
np.save("myarray.npy", a)

# will load your array/np file
np.load("myarray.npy", a)



# saving a csv file
np.savetxt("myarray.csv", a, delimiter=",")

# loading csv
np.loadtxt('myarray.csv', delimiter=",")