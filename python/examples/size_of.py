from array import array
import sys


lst = [1.0, 2.0, 3.0]
arr = array('f', [1.0, 2.0, 3.0])

a  = sys.getsizeof(lst)
b  = sys.getsizeof(arr)