# temperatures
def to_fahrenheit(c):
    return 9 / 5 * c + 32

def to_celsius(f):
    return (f - 32) * 5 / 9


celsius_temps = [100, 40, 80]
convert_to_f = list(map(to_fahrenheit, celsius_temps))

fahr_temps = [212, 104, 176]
conver_to_c = list(map(to_celsius, fahr_temps))