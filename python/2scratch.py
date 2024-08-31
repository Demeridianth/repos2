import requests
import pprint

data ={'key': 'value'}
response = requests.post('https://www.whatismybrowser.com/detect/what-is-my-user-agent/', data=data)
print(response.text)

