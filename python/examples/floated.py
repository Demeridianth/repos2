from array import array
from random import random

list_flt = list(array('d', range(100)))

radnom_flt = array('d', (random() for i in range(100)))

array_flt = array('d', (i for i in range(100)))

float_lst = [float(i) for i in range(100)]

print(float_lst)

