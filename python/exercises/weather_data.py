import json
weather_data = [
    {'country': 'Russia', 'city': 'Moscow', 'date': '2022-01-01', 'temperature': -30},
    {'country': 'Russia', 'city': 'Moscow', 'date': '2022-01-02', 'temperature': -23},
    {'country': 'Russia', 'city': 'Moscow', 'date': '2022-01-03', 'temperature': -27},
    {'country': 'Russia', 'city': 'Saint Petersburg', 'date': '2022-01-01', 'temperature': -34},
    {'country': 'Russia', 'city': 'Saint Petersburg', 'date': '2022-01-02', 'temperature': -26},
    {'country': 'Russia', 'city': 'Saint Petersburg', 'date': '2022-01-03', 'temperature': -12},

    {'country': 'Latvia', 'city': 'Riga', 'date': '2022-01-01', 'temperature': -5},
    {'country': 'Latvia', 'city': 'Riga', 'date': '2022-01-02', 'temperature': -9},
    {'country': 'Latvia', 'city': 'Riga', 'date': '2022-01-03', 'temperature': -4},
    {'country': 'Latvia', 'city': 'Daugavpils', 'date': '2022-01-01', 'temperature': -3},
    {'country': 'Latvia', 'city': 'Daugavpils', 'date': '2022-01-02', 'temperature': -8},
    {'country': 'Latvia', 'city': 'Daugavpils', 'date': '2022-01-03', 'temperature': -2},

    {'country': 'Spain', 'city': 'Barcelona', 'date': '2022-01-01', 'temperature': 0},
    {'country': 'Spain', 'city': 'Barcelona', 'date': '2022-01-02', 'temperature': 6},
    {'country': 'Spain', 'city': 'Barcelona', 'date': '2022-01-03', 'temperature': 9},
    {'country': 'Spain', 'city': 'Madird', 'date': '2022-01-01', 'temperature': -2},
    {'country': 'Spain', 'city': 'Madird', 'date': '2022-01-02', 'temperature': 5},
    {'country': 'Spain', 'city': 'Madird', 'date': '2022-01-03', 'temperature': 11},
]

# results['Russia']['Saint Petersburg']['2022-01-01']

'''
{'Latvia': {'Riga': {'2022-01-01': 5}}}

'''

full_info = {}

for data in weather_data:
    country_name = data['country']
    city_name = data['city']
    date = data['date']
    temperature = data['temperature']
    if country_name not in full_info:
        full_info[country_name] = {}

    if city_name not in full_info[country_name]:
        full_info[country_name][city_name] = {}

    if date not in full_info[country_name][city_name]:
        full_info[country_name][city_name][date] = temperature


weather = open('weather_results.json', 'w')
generate_json = json.dumps(full_info)
weather.write(generate_json)
weather.close()


for country in full_info:
    print(country)

    for city in full_info[country]:
        print(f'  {city}')

        for exact_date in full_info[country][city]:
            print(f'   {exact_date}:   {full_info[country][city][exact_date]}')


        