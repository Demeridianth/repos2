import typing

class City(typing.NamedTuple):
    continent: str
    country: str
    city: str

cities = [
 City('Asia', 'Tokyo', 'JP'),
 City('Asia', 'Delhi', 'IN'),
 City('North America', 'Mexico City', 'MX'),
 City('North America', 'New York', 'US'),
 City('South America', 'São Paulo', 'BR'),
]

def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia', country=cc):
                results.append(city)
    print(results)
    
match_asian_cities()
