my_dict = {}
my_dict
{'some': 2, 46: 15, 'use_name': 'info'}

for key, value in my_dict.items():
    print(f'{key} : {value}')


#some : 2
#46 : 15
#use_name : info

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

