import requests

# print(requests.get('http://127.0.0.1:8000/transactions/8').json())        # by store_number
# print(requests.get('http://127.0.0.1:8000/transactions/by_date?date=2013-07-12').json())        # by date
print(requests.get('http://127.0.0.1:8000/transactions/search?date=2013-07-12&store_number=44').json())        # by date
