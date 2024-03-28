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