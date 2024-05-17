"""Dictionaries and sets"""



"""dict comprehension"""


dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

country_dial = {country: code for code, country in dial_codes}
# {'Bangladesh': 880, 'Brazil': 55, 'China': 86, 'India': 91, 'Indonesia': 62,
# 'Japan': 81, 'Nigeria': 234, 'Pakistan': 92, 'Russia': 7, 'United States': 1}

dial_sorted = {code: country.upper() for country, code in sorted(country_dial.items()) if code < 70}
# Sorting country_dial by name, reversing the pairs again, uppercasing values,
# and filtering items with code < 70.
# dial_sorted = {}
# for country, code in sorted(country_dial.items()):
#     if code < 70:
#         dial_sorted[code] = country.upper()
# {55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA', 1: 'UNITED STATES'}



"""Unpacking Mappings"""


def dump(**kwargs):
    return kwargs

dump(**{'x': 1}, y=2, **{'z': 3})
# {'x': 1, 'y': 2, 'z': 3}
# we can apply ** to more than one argument in a function call. This works when
# keys are all strings and unique across all arguments (because duplicate keyword argu‐
# ments are forbidden)

{'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}
# {'a': 0, 'x': 4, 'y': 2, 'z': 3}
# duplicate keys are allowed. Later occurrences overwrite previous ones—
# see the value mapped to x in the example.



""" Merging mappins with | """


d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d1 | d2
# {'a': 2, 'b': 4, 'c': 6}


# we apply merge (|) and update (|=) to dicts
dict1 = {"a": 0, "b": 1, "c": 2}
dict2 = {"c": 20, "d": 30}

# Merge, | 
dict1 | dict2
{"a": 0, "b": 1, "c": 20, "d": 30}
# >>> d1 
# {"a": 0, "b": 1, "c": 2}
# dict1 UNCHANGED!!!

# Update, |=
d1 |= d2
# >>> d1 
# {"a": 0, "b": 1, "c": 20, "d": 30}
# dict1 REASSIGNED!!!



"""Pattern Matching with Mappings"""


def get_creators(record: dict) -> list:
 match record:
    case {'type': 'book', 'api': 2, 'authors': [*names]}:
        return names
    case {'type': 'book', 'api': 1, 'author': name}:
        return [name]
    case {'type': 'book'}:
        raise ValueError(f"Invalid 'book' record: {record!r}")
    case {'type': 'movie', 'director': name}:
        return [name]
    case _:
        raise ValueError(f'Invalid record: {record!r}')
     

book1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Godel, Esher, Bach')
# >>> get_creators(book1)
# >>> ['Douglas Hofstadter']

from collections import OrderedDict
book2 = OrderedDict(api=2, type='book', title='Python in a Nutshell', authors='Martelli Ravenscroft Holden'.split())
# >>> ['Martelli', 'Ravenscroft', 'Holden']

# mapping patterns succeed on partial matches. In the doctests, the b1 and b2 subjects include a 'title' key that does not appear in any
# 'book' pattern, yet they match.



# There is no need to use **extra to match extra key-value pairs, but if you want to capture them as a dict, you can prefix one variable with **. It must be the last in the pattern, and **_ is forbidden because it would be redundant. A simple example:

food = dict(category='ice cream', flavor='vanilla', cost=199)
match food:
    case {'category': 'ice cream', **details}:
        print(f'Ice cream details: {details}')

# >>> Ice cream details: {'flavor': 'vanilla', 'cost': 199}



""" Inserting or Updating Mutable Values """


# fetch and update a list of word occurrences from the index i a text file

import re
import sys

WORD_RE = re.compile(r'\w+')

# index = {}
# with open(sys.argv[1], encoding='utf-8') as fp:
#     # sys.argv[] takes a text file as an argument in command line: "python3 1scratch.py zen.txt"
#     for line_no, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)
#             # this is ugly; coded like this to make a point
#             occurrences = index.get(word, [])
#             occurrences.append(location)
#             index[word] = occurrences 

# for word in sorted(index, key=str.upper):
#     print(word, index[word])


#better version with dict.setdefault()

# index = {}
# with open(sys.argv[1], encoding='utf-8') as fp:
#  for line_no, line in enumerate(fp, 1):
#     for match in WORD_RE.finditer(line):
#         word = match.group()
#         column_no = match.start() + 1
#         location = (line_no, column_no)
#         index.setdefault(word, []).append(location)


# display in alphabetical order
# for word in sorted(index, key=str.upper):
#     print(word, index[word])



# my_dict.setdefault(key, []).append(new_value)

# is the same as:

# if key not in my_dict:
#   my_dict[key] = []
#   my_dict[key].append(new_value)



""" defaultdict: Another Take on Missing Keys """
import collections

# index = collections.defaultdict(list)
# with open(sys.argv[1], encoding='utf-8') as fp:
#  for line_no, line in enumerate(fp, 1):
#     for match in WORD_RE.finditer(line):
#         word = match.group()
#         column_no = match.start() + 1
#         location = (line_no, column_no)
#         index[word].append(location)


# display in alphabetical order
# for word in sorted(index, key=str.upper):
#     print(word, index[word])



""" The __missing__ Method """

# When searching for a nonstring key, StrKeyDict0 converts it to str when it is not found
class StrKeyDict0(dict):
   
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
       try:
          return self[key]
       except KeyError:
          return default
       
    def __contains__(self, key):
       return key in self.keys() or str(key) in self.keys()
    


d = StrKeyDict0([('2', 'two'), ('4', 'four')])

# >>> d['2']
# 'two'
# >>> d[4]
# 'four'
# >>> d[1] 
   


""" collections.ChainMap """ 


d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)
from collections import ChainMap
chain = ChainMap(d1, d2)
# >>> chain['a']
# 1
# >>> chain['c']
# 6

# Updates or insertions to a ChainMap only affect the first input mapping. Con‐
# tinuing from the previous example:

chain['c'] = -1
# >>> d1
# {'a': 1, 'b': 3, 'c': -1}
# >>> d2
# {'a': 2, 'b': 4, 'c': 6}



"""collections.Counter"""


ct = collections.Counter('abracadabra')
ct
# >>> Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.update('aaaaazzz')
ct
# Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
# >>> ct.most_common(3)
# [('a', 10), ('z', 3), ('b', 2)]



""" immutable dict """


from types import MappingProxyType


d = {1: 'A'}
d_proxy = MappingProxyType(d)
d_proxy
# >>> mappingproxy({1: 'A'})
d_proxy[1]
#  >>> 'A'
# >>> d_proxy[2]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 2

d[2] = 'B'
d_proxy
# >>> mappingproxy({1: 'A', 2: 'B'})
d_proxy[2]
# >>> 'B'



""" Dictionary Views """


d = dict(a=10, b=20, c=30)
values = d.values()
values
# >>> dict_values([10, 20, 30])
len(values)
# >>> 3
list(values)
# >>> [10, 20, 30]
reversed(values)
# >>> <dict_reversevalueiterator object at 0x10e9e7310>
values[0]
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'dict_values' object is not subscriptable


# 133


      


