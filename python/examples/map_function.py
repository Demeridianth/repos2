import re
import math


""" map built in function """

# map(function, iterable[, iterable1, iterable2,..., iterableN])

# This first argument to map() is a transformation function. In other words, it’s the function that transforms each original item into a new (transformed) item. Even though the Python documentation calls this argument function, it can be any Python callable. This includes built-in functions, classes, methods, lambda functions, and user-defined functions.


# square numbers through a function
def square_number(number): # transforming function
    return number ** 2

numbers = [1, 2, 3, 4, 5]

squared = map(square_number, numbers)


# Note: In Python 2.x, map() returns a list. This behavior changed in Python 3.x. Now, map() returns a map object, which is an iterator that yields items on demand. That’s why you need to call list() to create the desired list object.


# strings to integers through int() built-in function
strings = ['1', '2', '3', '4', '5']

string_to_int = map(int, strings)



# with different built-in functions
numbers = [-2, -1, 0, 1, 2]

# absolute values
abs_values = map(abs, numbers)

# float
float_numbers = map(float, numbers)

# length of each word
words = ['this', 'is', 'Python']

words_len = map(len, words)



# multiple lists of iterables
# iteration stops at the end of the shortest iterable

first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]

# !!!pow(4, 3) = Return the value of 4 to the power of 3 (same as 4 * 4 * 4)

# list(map(pow, first_it, second_it))



# using methods of built-in STR class 
string_it = ['processing', ' strings ', 'with ', 'map ']

capitalize = map(str.capitalize, string_it)

upper = map(str.upper, string_it)

strip = map(str.strip, string_it)  # str.strip() takes an optional argument called .char. that defaults to removing whitespace



# removing punctuation
# module re

# in a word
def remove_punctuation(word):
    return re.sub(r'[!?.:;,"()-]', "", word)   # re.sub(pattern, repl, string, count=0, flags=0)

no_punct =  remove_punctuation('...Python!')


# in text
text = """Some people, when confontred with a problem, think "I know, I'll use regular expressions." Now they have two problems. Jamie Zawinski"""

words = text.split()    # each word into string

remove_punct = map(remove_punctuation, words)



# CEASER CIPHER
# each letter shifts by three, a = d, d = e etc.

# Original alphabet: abcdefghijklmnopqrstuvwxyz
# Alphabet rotated by three: defghijklmnopqrstuvwxyzabc

# ord() takes a Unicode character and returns an integer that represents the Unicode code point position

# chr() is the inverse of ord(). It takes an integer representing the Unicode code point of a Unicode character and returns the character at that position

def rotate_chr(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Keep punctuation and whitespace
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    # If the rotation is inside the alphabet
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotated_pos - len(alphabet))

message = ''.join(map(rotate_chr, 'my secret message goes here'))



# MATH OPERATIONS
def powers(x):
    return x ** 2, x ** 3

numbers = [1, 2, 3, 4]

square_cube =  (map(powers, numbers))
# >>> [(1, 1), (4, 8), (9, 27), (16, 64)]


# math module
numbers = [1, 2, 3, 4, 5, 6, 7]

factorial = map(math.factorial, numbers)
# >>> [1, 2, 6, 24, 120, 720, 5040]


# temperatures
def to_fahrenheit(c):
    return 9 / 5 * c + 32

def to_celsius(f):
    return (f - 32) * 5 / 9


celsius_temps = [100, 40, 80]
convert_to_f = list(map(to_fahrenheit, celsius_temps))

fahr_temps = [212, 104, 176]
conver_to_c = list(map(to_celsius, fahr_temps))













