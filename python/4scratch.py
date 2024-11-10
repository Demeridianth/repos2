import requests
import json

country = input('country: ')
city = input('city: ')
response = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}%2C%20{country}?unitGroup=metric&key=BTQTHAA84DKENYU4NLH4AM4FM&contentType=json')
response_json = response.json()
# print(response_json)
timezone = response_json['resolvedAddress']
print(timezone)
days = response_json['days']
print(days[0].get('tempmax'))

# with open('weather.json', 'w') as file:
#     json_file = json.dumps(response_json)
#     file.write(json_file)