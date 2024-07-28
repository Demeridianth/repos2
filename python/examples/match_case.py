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

# mapping patterns succeed on partial matches. In
# the doctests, the b1 and b2 subjects include a 'title' key that does not appear in any
# 'book' pattern, yet they match.



# There is no need to use **extra to match extra key-value pairs, but if you want to capture them as a dict, you can prefix one variable with **. It must be the last in the pattern, and **_ is forbidden because it would be redundant. A simple example:

food = dict(category='ice cream', flavor='vanilla', cost=199)
match food:
    case {'category': 'ice cream', **details}:
        print(f'Ice cream details: {details}')

# >>> Ice cream details: {'flavor': 'vanilla', 'cost': 199}



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


def main():
    print(f'{"":15} | {"lattitude":>9} | {"longtitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


for record in metro_areas:
    match record:
        case (name, _, _, (lat, lon)):
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')



# bind any part of a pattern with a variable using the as keyword
# match random:
#     case [name, _, _, (lat, lon) as coord]:

# Variable Set Value
# name 'Shanghai'
# lat 31.1
# lon 121.3
# coord (31.1, 121.3)


# check for type by make patterns more specific by adding type information
# case [str(name), _, _, (float(lat), float(lon))]:d




records = [{'id_number': '3', 'genre': 'novel', 'title': 'War and Peace', 'author': 'Tolstoy'}, 
           {'id_number': '2', 'genre': 'novel', 'title': 'Crime and Punishment', 'author': 'Dostoyevsky'}]

book = str(input('Your book name?: '))
for record in records:
    match record:
        case {'title': title} if title == book:
            print(f"title: {title} | {record}")