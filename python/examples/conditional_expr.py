from typing import NamedTuple

# conditional expression
x = 1
a = '1' if x == 1 else False
print(a)
# >>> 1


a = 10 if 0 else 5

# same as:

if 0:
    a = 10
else:
    a = 5


class Coords(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
