import collections
from random import choice
import math


"""PYTHON DATA MODEL"""


Card = collections.namedtuple('Card', ['rank', 'suit'])
# We use namedtuple to build classes of objects that
# are just bundles of attributes with no custom methods, like a database record.
# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamond clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
        
    def __getitem__(self, position):
        return self._cards[position]
        
deck = FrenchDeck()
some_card = Card(8, 'clubs')

# from random import choice
random_card = choice(deck)

# slice   Lst[ Initial : End : IndexJump ]
top_3_cards = deck[:3]

# will take all Acec, will take card 12 and skip the next 13 cards
take_12_skip_13 = deck[12::13]

# Just by implementing the __getitem__ special method, our deck is also iterable:
# for card in deck:
#     print(card)

# for card in reversed(deck):
#     print(card)



suit_values = dict(spades=3, hearts=2, diamond=1, clubs=0)

# Here is a function that ranks cards
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    ...
#     print(card)

# Card(rank='2', suit='clubs')
# Card(rank='2', suit='diamonds')
# Card(rank='2', suit='hearts')
# ... (46 cards omitted)
# Card(rank='A', suit='diamonds')
# Card(rank='A', suit='hearts')
# Card(rank='A', suit='spades')



# import math
# A simple two-dimensional vector class; through the use of the special methods __repr__, __abs__, __add__, and __mul__.


class Vector:
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})'
        # repr uses !r to get the standard representation of the attributes to be displayed
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
        # The math.hypot() method returns the Euclidean norm. The Euclidian norm is the distance from the origin to the coordinates given.
        # in this case between vectors
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __bool__(self):
        return bool(self.x or self.y)
    

# addition:   
v1 = Vector(2, 4)
v2 = Vector(2, 1)
v_sum = v1 + v2
# >>> Vector(4, 5)

# absolute value
v = Vector(3, 4)
abs_value = abs(v)
# >>> 5.0

# scalar multiplication
scal = v * 3
# >>> Vector(9, 12)
abs_scal = abs(v * 3)
# >>> 15.0