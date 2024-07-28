from array import array
import os
from random import random
import numpy as np
from collections import deque



"""An Array of Sequences"""
# array - (RU)массив


# Every Python object in memory has a header with metadata. The
# simplest Python object, a float, has a value field and two metadata
# fields:
# • ob_refcnt: the object’s reference count
# • ob_type: a pointer to the object’s type
# • ob_fval: a C double holding the value of the float
# On a 64-bit Python build, each of those fields takes 8 bytes. That’s
# why an array of floats is much more compact than a tuple of floats:
# the array is a single object holding the raw values of the floats,
# while the tuple consists of several objects—the tuple itself and each

#  TYPECODE	C TYPE	            PYTHON TYPE	      SIZE
# 'b'	    signed char	        int	                1
# 'B'	    unsigned char	    int	                1
# 'u'	    wchar_t	            Unicode character	2
# 'h'	    signed short	    int	                2
# 'H'	    unsigned short	    int	                2
# 'i'	    signed int	        int	                2
# 'I'	    unsigned int	    int	                2
# 'l'	    signed long	        int	                4
# 'L'	    unsigned long	    int	                4
# 'q'	    signed long long	int	                8
# 'Q'	    unsigned long long	int	                8
# 'f'	    float	            float	            4
# 'd'	    double	            float	            8

# Container sequences
# Can hold items of different types, including nested containers. Some examples:
# list, tuple, and collections.deque.

# Flat sequences
# Hold items of one simple type. Some examples: str, bytes, and array.array.



"""List Comprehensions and Readability"""


# 1 Build a list of Unicode code points from a string
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

# 2  Build a list of Unicode code points from a string, using a listcomp
symbols = '$¢£¥€¤'
codes_comp = [ord(symbol) for symbol in symbols]


# Local Scope Within Comprehensions and Generator Expressions
# variables assigned with the “Walrus operator” := remain accessible after
# those comprehensions or expressions return, unlike local variables in a function.
x = 'ABC'
codes = [ord(x) for x in x]

codes_walrus = [last := ord(c) for c in x]
# x was not clobbered: it’s still bound to 'ABC'.
# last remains.
# c is gone; it existed only inside the listcomp.



# listcomp vs map and filter
symbols = '$¢£¥€¤'
more_codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]

codes_filter_map = list(filter(lambda c: c > 127, map(ord, symbols)))



"""Cartesian Products"""


# (RU) декартовым произведением множеств А и В называется упорядоченное множество пар (a, b), первый элемент которых принадлежит A, а второй - В; Обозначается A x B. Если элементами A и B являются все действительные числа, то A x B представляет собой декартову плоскость


#  list of T-shirts available in two colors
# and three sizes.
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# sizes = list('sml'.upper())
tshirts = [(color, size) for size in sizes for color in colors]
# >>> [('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'), ('black', 'L'), ('white', 'L')]

# for size in sizes:
#     for color in colors:
#         print((color, size))
# ('black', 'S')
# ('white', 'S')
# ('black', 'M')
# ('white', 'M')
# ('black', 'L')
# ('white', 'L')

tshirts_color_first = [(color, size) for color in colors 
                                        for size in sizes]
# >>> [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]



"""Generator Expressions"""


symbols = '$¢£¥€¤'

tuple_genexp = tuple(ord(symbol) for symbol in symbols)

array_genexp = array('I', (ord(symbol) for symbol in symbols))

colors = ['black', 'white']
sizes = list('SML')
# for tshirt in (f'{color} {size}' for color in colors for size in sizes):
#     print(tshirt)



"""Tuples Are Not Just Immutable Lists"""


# tuples used as records
lax_coordinates = (33.9424, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CR342567'), ('ESP', 'XDA205856')]

# for passport in sorted(traveler_ids):
#     print('%s/%s' % passport)
# BRA/CR342567
# ESP/XDA205856
# USA/31195855

# for country, _ in traveler_ids:
#     print(country)
# USA
# BRA
# ESP



"""Tuples as Immutable Lists"""


# tuple is immutable, but if one of the references points to a mutable object, like a list and that list is changed then the value of tuple is changed! 
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
a == b
# >>> True
b[-1].append(99)
a == b
# >>> False



# determine explicitly if a tuple (or any object) has a fixed value, use the hash built-in to create a fixed function like this:
def fixed(object):
    try:
        hash(object)
    except TypeError:
        return False
    return True

immute = fixed((10, 'alpha', (1, 2)))
mute = fixed((10, 'alpha', [1, 2]))



"""Unpacking Sequences and Iterables"""


# parrarel assignment ((RU) паралельное присваивание)
lax_coordinates = (33.3141, -12.123123)
latitude, longtitude = lax_coordinates
latitude
# >>> 33.3141
longtitude
# >>> -12.123123


# prefixing an argument with * when calling a function
divmod(20, 8)
# >>> (2, 4)

t = (20, 8)
divmod(*t)
# # >>> (2, 4)
# The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).

quontient, remainder = divmod(*t)
quontient, remainder 
# >>> (2, 4)


_, filename = os.path.split('/home/python/.ssh/id_rsa.pug')
filename
# >>> id_rsa.pug



"""Using * to Grab Excess Items"""


a, b, *rest = range(5)
a, b, *rest
# >>> (0, 1, [2, 3, 4])

a, b, *rest = range(3)
a, b, *rest
# >>> (0, 1, [2])

a, b, *rest = range(2)
a, b, *rest
# >>> (0, 1, [])

a, *body, c, d = range(5)
a, *body, c, d
# >>> (0, [1, 2], 3, 4) 

*head, b, c, d = range(5)
*head, b, c, d 
# >>> ([0, 1], 2, 3, 4)





"""Unpacking with * in Function Calls and Sequence Literals"""


def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

fun(*[1, 2], 3, *range(4, 7))
# >>> (1, 2, 3, 4, (5, 6))


# * can also be used when defining list, tuple, or set literals
*range(4), 4
# >>> (0, 1, 2, 3, 4)
[*range(4), 4]
# >>> [0, 1, 2, 3, 4]
{*range(4), 4, *(5, 6, 7)}
# >>> {0, 1, 2, 3, 4, 5, 6, 7}



""""Nested Unpacking"""


metro_areas = [
 ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]



# print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
# for name, _, _, (lat, lon) in metro_areas:
#     if lon <= 0:
#         print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')



"""Match/Case""" """Pattern Matching with Sequences"""


# imaginary robot
# def handle_command(self, message):
#  match message:
#     case ['BEEPER', frequency, times]:
#         self.beep(times, frequency)
#     case ['NECK', angle]:
#         self.rotate_neck(angle)
#     case ['LED', ident, intensity]:
#         self.leds[ident].set_brightness(ident, intensity)
#     case ['LED', ident, red, green, blue]:
#         self.leds[ident].set_color(ident, red, green, blue)
#     case _:
#         raise InvalidCommand(message)


# Destructuring nested tuples
metro_areas = [
 ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


# def main():
#     print(f'{"":15} | {"lattitude":>9} | {"longtitude":>9}')
#     for record in metro_areas:
#         match record:
#             case [name, _, _, (lat, lon)] if lon <= 0:
#                 print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


# for record in metro_areas:
#     match record:
#         case (name, _, _, (lat, lon)):
#             print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')



# bind any part of a pattern with a variable using the as keyword
# match random:
#     case [name, _, _, (lat, lon) as coord]:

# Variable Set Value
# name 'Shanghai'
# lat 31.1
# lon 121.3
# coord (31.1, 121.3)


# check for type by make patterns more specific by adding type information
# case [str(name), _, _, (float(lat), float(lon))]:


# HOW OFTEN MATCH/CASE IS USED?
# DOESNT WORK, SYNTAX ERROR



# Pattern Matching Sequences in an Interpreter

# Peter Norvig of Stanford University wrote lis.py: an interpreter for a subset of the
# Scheme dialect of the Lisp programming language in 132 lines of beautiful and readable Python code.


# pseudo code
def evaluate(exp, env):
    "Evaluate an expression in an environment."
    if isinstance(exp): # variable reference
        return env[exp]
 # ... lines omitted
    elif exp[0] == 'quote': # (quote exp)
        (_, x) = exp
        return x
    elif exp[0] == 'if': # (if test conseq alt)
        (_, test, consequence, alternative) = exp
        if evaluate(test, env):
            return evaluate(consequence, env)
        else:
            return evaluate(alternative, env)
    elif exp[0] == 'lambda': # (lambda (parm…) body…)
        (_, parms, *body) = exp
        # return Procedure(parms, body, env)
    elif exp[0] == 'define':
        (_, name, value_exp) = exp
        env[name] = evaluate(value_exp, env)
 # ... more lines omitted


#   Pattern matching with match/case


# def evaluate(exp, env):
#     match exp:
#         case ['quote', x]:
#             return x
#         case ['if', test, consequence, alterantive]:
#             if evaluate(test, env):
#                 return evaluate(consequence, env)
#             else:
#                 return evaluate(alterantive, env)
        # case ['lamda', [*parms], *body] if body:
        #     return Procedure(parms, body, env)
        # case ['define', Symbol() as name, value_exp]:
        #     env[name] = evaluate(value_exp, env)



""" SLICING """


lst = [10, 20, 30, 40, 50, 60]
lst[:2]
# >>> [10, 20]
lst[3:]
# >>> [40, 50, 60]

#  s[a:b:c] can be used to specify a stride or step c, causing the resulting slice to skip items.

string = 'bicycle'
string[::3]
# >>> 'bye'
string[::-1]
# >>> elcycib
string[::-2]
# >>> 'eccb'

# to evaluate the expression seq[start:stop:step], Python calls seq.__getitem__(slice(start, stop, step)). 


# slice objects

invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3     $52.50
1489  6mm Tactile Switch x20                $4.95     2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1     $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1     $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
# for item in line_items:
#     print(item[UNIT_PRICE], item[DESCRIPTION])


slice_list = [(1, 2, 3, 4, 5, 6), (7, 8, 9, 10), (11, 12, 13, 14, 15, 16)]

first_two = slice(0, 2)
last_two = slice(-2, -1)

# for tpl in slice_list:
#     print(tpl[-1], tpl[-2])


# Assigning to Slices

lst = list(range(11))
lst[2:5] = [20, 30]
# >>> [0, 1, 20, 30, 5, 6, 7, 8, 9, 10]

del lst[5:7]
# >>> [0, 1, 20, 30, 5, 7, 8, 9, 10]



"""Building List in List"""

board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
# board = []
# for i in range(3):
#     row = ['_'] * 3
#     board.append(row)


# A tempting, but WRONG, shortcut
weird_board = [['_'] * 3] * 3
weird_board[1][2] = '0'
# row = ['_'] * 3
# board = []
# for i in range(3):
#     board.append(row) 



# Augmented Assignment with Sequences

l = [1, 2, 3]
id(l)
# >>> 139740284457088
l *= 2
id(l)
# >>> 139740284457088

t = (1, 2, 3)
id(t)
# >>> 139740284455616
t *= 2
id(t)
# >>> 139740285914432

# • Avoid putting mutable items in tuples.
# • Augmented assignment is not an atomic operation—we just saw it throwing an
# exception after doing part of its job.
# • Inspecting Python bytecode is not too difficult, and can be helpful to see what is
# going on under the hood.



"""list.sort Versus the sorted Built-In"""


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



"""Arrays"""


#  TYPECODE	C TYPE	            PYTHON TYPE	      SIZE
# 'b'	    signed char	        int	                1
# 'B'	    unsigned char	    int	                1
# 'u'	    wchar_t	            Unicode character	2
# 'h'	    signed short	    int	                2
# 'H'	    unsigned short	    int	                2
# 'i'	    signed int	        int	                2
# 'I'	    unsigned int	    int	                2
# 'l'	    signed long	        int	                4
# 'L'	    unsigned long	    int	                4
# 'q'	    signed long long	int	                8
# 'Q'	    unsigned long long	int	                8
# 'f'	    float	            float	            4
# 'd'	    double	            float	            8

# an array of float values does not hold full-fledged float instances, but only the packed bytes representing their machine values

#  When creating an array, you provide a typecode, a letter to determine the underlying C
# type used to store each item in the array. For example, b is the typecode for what
# C calls a signed char, an integer ranging from –128 to 127.


# shows creating, saving, and loading an array of 10 million floatingpoint random numbers.
floats = array('d', (random() for i in range(10**2)))
floats[-1]
# >>> 0.915212492314622

# It is a common and routine task in Python; the act of writing binary data to a file when you need to save non-textual data such as images, audio files, or serialized objects.
file_binary = open('floats.bin', 'wb')
floats.tofile(file_binary)
file_binary.close()

floats2 = array('d')
file_binary = open('floats.bin', 'rb')
floats2.fromfile(file_binary, 10**2)
# Read 10 million numbers from the binary file
file_binary.close()
floats[-1]
# 0.8275676541565994
floats2[-1]
# 0.8275676541565994
floats == floats2
# >>> True

# it takes about 0.1 seconds for array.fromfile to load 10 million double-precision floats from a binary file created with array.tofile



""" Memoryview """
# The built-in memoryview class is a shared-memory sequence type that lets you handle slices of arrays without copying bytes.

octets = array('B', range(6))
m1 = memoryview(octets)
m1.tolist()
# >>> [0, 1, 2, 3, 4, 5]

m2 = m1.cast('B', [2, 3])
# Build new memoryview from that previous one, but with 2 rows and 3 columns.
m2.tolist()
# >>>  [[0, 1, 2], [3, 4, 5]]

m3 = m1.cast('B', [3, 2])
m3.tolist()
# >>> [[0, 1], [2, 3], [4, 5]]

m2[1, 1] = 22
# change 4 to 22
m3[1, 1] = 33
# change 3 to 33

# >>> octets
# >>> array('B', [0, 1, 2, 33, 22, 5])


numbers = array('h', [1])
memv = memoryview(numbers)
# memoryview from array of 5 16-bit signed integers (typecode 'h').

memv_oct = memv.cast('B')
# Create memv_oct by casting the elements of memv to bytes (typecode 'B').

mlist = memv_oct.tolist()
#  >>> [253, 255, 255, 255, 0, 0, 1, 0, 2, 0]

memv_oct[1] = 4

# >>> numbers
# >>> array('h', [-3, -1, 1024, 1, 2])



"""NumPy"""


a = np.arange(12)
# >>> a
# >>> array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

# type(a)
# >>> <class 'numpy.ndarray'>

# a.shape
# >>> (12,)    
# this is a one-dimensional, 12-element array

a.shape = 3, 4
# >>> a
# array([[ 0, 1, 2, 3],
#        [ 4, 5, 6, 7],
#        [ 8, 9, 10, 11]])

a[2]
# >>> array([ 8, 9, 10, 11])
a[2, 1]
# >>> 9

a[:, 1]
# >>> array([1, 5, 9])    
# Get column at index 1.

a.transpose()
# array([[ 0, 4, 8],
#        [ 1, 5, 9],
#        [ 2, 6, 10],
#        [ 3, 7, 11]])
# swapping columns with rows

# Load 10 million floating-point numbers from a text file
# floats = np.loadtxt('floats-10M-lines.txt')



"""Deques and Other Queues"""


dq = deque(range(10), maxlen=10)
# >>> deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

dq.rotate(3)
deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
# Rotating with n > 0 takes items from the right end and prepends them to the left; when n < 0 items are taken from left and appended to the right.

dq.rotate(-4)
# >>> deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)

dq.appendleft(-1) 
# >>> deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

dq.extend([11, 22, 33])
# >>> deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
# Adding three items to the right pushes out the leftmost -1, 1, and 2.

dq.extendleft([10, 20, 30, 40])
# >>> deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
# extendleft(iter) works by appending each successive item of the iter argument to the left of the deque, therefore the final position of the items is
# reversed.



# deque implements most of the list methods, and adds a few that are spe‐
# cific to its design, like popleft and rotate. But there is a hidden cost: removing
# items from the middle of a deque is not as fast. It is really optimized for appending
# and popping from the ends





