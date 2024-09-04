from collections import namedtuple
import typing
from typing import NamedTuple
import json
import dataclasses
from dataclasses import dataclass

""" Unicode Text Versus Bytes """


s = 'café'
len(s)
# >>> 4

b = s.encode('utf8')
# >>> b'caf\xc3\xa9'
len(b)
# >>> 5
# bytes b has five bytes (the code point for “é” is encoded as two bytes in UTF-8).
b.decode()
# >>> 'café'



cafe = bytes('café', encoding='utf_8')
# >>> b'caf\xc3\xa9'
cafe[0]
# >>> 99
cafe[1:]
# >>> b'c'
# The fact that my_bytes[0] retrieves an int but my_bytes[:1]
# returns a bytes sequence of length 1 is only surprising because we
# are used to Python’s str type, where s[0] == s[:1]. For all other
# sequence types in Python, 1 item is not the same as a slice of
# length 1.


cafe_arr = bytearray(cafe)
# >>> bytearray(b'caf\xc3\xa9')
cafe_arr[-1:]
# >>> bytearray(b'\xa9')


# encoders/decoders

# for codec in ['latin_1', 'utf_8', 'utf_16']:
#     print(codec, 'El Niño'.encode(codec), sep='\t')

# latin_1 b'El Ni\xf1o'
# utf_8   b'El Ni\xc3\xb1o'
# utf_16  b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'



# Coping with UnicodeEncodeError

# >>> city = 'São Paulo'
# >>> city.encode('utf_8')
# b'S\xc3\xa3o Paulo'
# >>> city.encode('utf_16')
# b'\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00'
# >>> city.encode('iso8859_1')
# b'S\xe3o Paulo'
# >>> city.encode('cp437')
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "/.../lib/python3.4/encodings/cp437.py", line 12, in encode
#  return codecs.charmap_encode(input,errors,encoding_map)
# UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in
# position 1: character maps to <undefined>
# >>> city.encode('cp437', errors='ignore')
# b'So Paulo'
# >>> city.encode('cp437', errors='replace')
# b'S?o Paulo'
# >>> city.encode('cp437', errors='xmlcharrefreplace')
# b'S&#227;o Paulo'


"""How do you find the encoding of a byte sequence? Short answer: you can’t. You must be told."""


# ASCII (American Standard Code for Information Interchange), which encodes 128 specified characters into seven-bit integers.

# Unicode, which provides a unique number for every character, no matter the platform, program, or language, and is capable of representing all the characters used in the world's writing systems.

# UTF-8, a variable-width character encoding capable of encoding all 1,107,616 valid character code points in Unicode using one to four one-byte (8-bit) units.



from unicodedata import name


# >>> name('a')
# 'LATIN SMALL LETTER A'
# >>> name('ā')
# 'LATIN SMALL LETTER A WITH MACRON'
# >>> name('ж')
# 'CYRILLIC SMALL LETTER ZHE'
# >>>



""" DATA CLASS BUILDERS"""


""" collections.namedtuple """

from collections import namedtuple


coordinate = namedtuple('Coordinate', 'lat lon')
coordinate = namedtuple('Coordinate', ['lat', 'lon'])
# >>> issublass(Coordinate, tuple)
# >>> True

moscow = coordinate(55.756, 37.617)
# >>> moscow
# >>> Coordinate(lat=55.756, lon=37.617)

# >>> moscow == coordinate(lat=55.756, lon=37.617)
# >>> True

City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

# >>> tokyo.population
# 36.933
# >>> tokyo.coordinates
# (35.689722, 139.691667)


# Named tuple attributes and methods:

# City._fields
# ('name', 'country', 'population', 'location')

Coordinate = namedtuple('Coordinate', 'lat lon')
delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))

delhi = City._make(delhi_data)
# same as:
delhi = City(*delhi_data) 

delhi_dict = delhi._asdict()
# >>> {'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': Coordinate(lat=28.613889, lon=77.208889)}

json.dumps(delhi._asdict())
# >>> '{"name": "Delhi NCR", "country": "IN", "population": 21.935, "location": [28.613889, 77.208889]}'

Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])
Coordinate(0, 0)
# >>> Coordinate(lat=0, lon=0, reference='WGS84')
# >>> {'reference': 'WGS84'}


# collections.namedtuple cannot add methods but there is a HACK:

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamond clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
        
    def __getitem__(self, position):
        return self._cards[position]
    
suit_values = dict(spades=3, hearts=2, diamond=1, clubs=0)

# Here is a function that ranks cards / method
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# Attach the function to the Card class as a method named overall_rank.
Card.overall_rank = spades_high
lowest_card = Card('2', 'clubs')
highest_card = Card('A', 'spades')
lowest_card.overall_rank()
# >>> 0
highest_card.overall_rank()
# >>> 51




""" typing.NamedTuple"""

import typing
from typing import NamedTuple


Coordinate = typing.NamedTuple('Coordinate',[('lat', float), ('lon', float)])
# >>> issubclass(Coordinate, tuple)
# True
# >>> typing.get_type_hints(Coordinate)
# {'lat': <class 'float'>, 'lon': <class 'float'>}

Coordinate = typing.NamedTuple('Coordinate', lat=float, lon=float)


# In the __init__ method generated by typing.NamedTuple, the fields appear as
# parameters in the same order they appear in the class statement.


class Coords(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
    
coords = Coords(26.5, 67.5)

typing.get_type_hints(coords)
# >>> {'lat': <class 'float'>, 'lon': <class 'float'>}




class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'

Coordinate = NamedTuple('Coordinate', lat=float, lon=float)


# there is no type checking on runtime in type.NamedTuple
trash = Coordinate('NL!', None )

# both types are not float as in class instance fields
# >>> Coordinate(lat='NL!', lon=None)


class DemoNamedTuple(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'

# >>> DemoNamedTuple.__annotations__
# {'a': <class 'int'>, 'b': <class 'float'>}

# >>> DemoNamedTuple.a
# _tuplegetter(0, 'Alias for field number 0')
# >>> DemoNamedTuple.b
# _tuplegetter(1, 'Alias for field number 1')
# >>> DemoNamedTuple.c
# 'spam'

# >>> DemoNamedTuple.__doc__
# 'DemoNamedTuple(a, b)'

demo = DemoNamedTuple(8)
# DemoNamedTuple(a=8, b=1.1)


demo_named_tuple = NamedTuple('Demo', a=int, b=float, c='spam')

# in_line_demo = demo_named_tuple(5)
# >>> TypeError: Demo.__new__() missing 2 required positional arguments: 'b' and 'c'
#  !!! CANNOT assing values to isinstance field using this syntax !!!



""" @dataclass class builder """


@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'

# >>> DemoDataClass.__annotations__
# {'a': <class 'int'>, 'b': <class 'float'>}
# >>> DemoDataClass.__doc__
# 'DemoDataClass(a: int, b: float = 1.1)'
# >>> DemoDataClass.a
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: type object 'DemoDataClass' has no attribute 'a'
# >>> DemoDataClass.b
# 1.1
# >>> DemoDataClass.c
# 'spam'

dc = DemoDataClass(9)
# >>> dc.a
# 9
# >>> dc.b
# 1.1
# >>> dc.c
# 'spam'

# >>> dc.a = 10
# >>> dc.a
# 10
# >>> dc.b = 1
# >>> dc.b
# 1
# >>> dc.c = 'more spam'
# >>> dc.c
# 'more spam'

# !!! @dataclass builder makes the object mutable !!!

# keyword arguments
# @dataclass(init=True, repr=True, eq=True, order=False,
#  unsafe_hash=False, frozen=False)


# frozen makes obj immutable
@dataclass(frozen=True)
class DemoClass():
    a: int = 1
    b: str = 'a'

fruit = DemoClass(1, 'orange')

# __eq__ set to True by default
# >>> a == b
# >>> True

# in simple class that would take:

class Fruit:
    def __init__(self, quantity=int, color=str) -> None:
        self.quantity = quantity
        self.color = color

    def __eq__(self, other):
        return self.quantity == other.quantity and self.color == other.color


apple = Fruit(1, 'orange')
pear = Fruit(1, 'orange')

# >>> apple == pear
# >>> True



# cannot set mutable value as default 
@dataclass
class ClubMember:
 name: str
 guests: list = []

#  >>> ValueError: mutable default <class 'list'> for field guests is not allowed:
# use default_factory

from typing import ClassVar
# unless
from dataclasses import dataclass, field
@dataclass
class ClubMember:
 name: str
 guests: list = field(default_factory=list)
 athlete: bool = field(default=False, repr=False)

 
@dataclass
class HackerClubMember(ClubMember):
    # annotation like this will make both typechecker and @dataclass "happy"
    all_handles: ClassVar[set[str]] = set()
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)



# init-only variables

from dataclasses import dataclass, InitVar, field
from re import Pattern
import re


# @dataclass
# class C:
#     i: int
#     j: int = None
#     database: InitVar[DatabaseType] = None
 
#     def __post_init__(self, database):
#         if self.j is None and database is not None:
#             self.j = database.lookup('j')
#         c = C(10, database=my_database)
      

@dataclass
class Condition:
    prop1: str
    prop2: str
    prop3: str
    pattern_str: InitVar[str]
    pattern: Pattern = field(init=False)

    def __post_init__(self, pattern_str):
        self.pattern = re.compile(pattern_str)


c = Condition("p1", "p2", "p3", "[a-z]+")

#217