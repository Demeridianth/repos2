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