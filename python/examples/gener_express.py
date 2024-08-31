"""Generator Expressions"""
import array


symbols = '$¢£¥€¤'

tuple_genexp = tuple(ord(symbol) for symbol in symbols)

array_genexp = array('I', (ord(symbol) for symbol in symbols))

colors = ['black', 'white']
sizes = list('SML')
# for tshirt in (f'{color} {size}' for color in colors for size in sizes):
#     print(tshirt)