import requests
import pprint

""" get """

# response = requests.get("http://httpbin.org/get")

params = {
    'name': 'Mike',
    'age': 25
}

# response = requests.get("http://httpbin.org/get", params=params)
# print(response.url)

# print(response.status_code)
# >>> 200 = OK
# >>> 404 = HTTP 404 Not Found

# print(response.text)
# >>> origin adress

# show as json dict
# res_json = response.json()
# del res_json('origin') # show withou IP
# print(res_json)
# >>> {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-66c8865a-767744e5766ebeb904065202'}, 'origin': '77.93.31.48', 'url': 'http://httpbin.org/get'}


""" post """

payload = {
    'name': 'Mike',
    'age': 25
}

# response = requests.post("http://httpbin.org/post", data=payload)
# print(response.url)

# res_json = response.json()
# del res_json('origin') # show withou IP
# print(res_json)


""" status codes"""

# response = requests.get("http://httpbin.org/status/500")

# if response.status_code == requests.codes.not_found:
#     print('Not Found')
# else: 
#     print(response.status_code)


""" user agent """

# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
#     'Accept': 'image/png'
# }

# # get image
# response = requests.get("http://httpbin.org/image", headers=headers)

# print(response.text)

# with open('myimage.png', 'wb') as f:
#     f.write(response.content)


""" timeout """

# for example to see if proxy works
# for _ in [1, 2, 3]:
#     try:
#         response = requests.get("http://httpbin.org/delay/5", timeout=3)
#     except:
#         continue


# res_json = response.json()
# print(res_json)



""" proxy server"""

proxies = {
    'http': '47.252.29.28:11222',
    'htttp': '47.252.29.28:11222'
}

# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0"
# }
# response = requests.get("http://httpbin.org/get", headers=headers, proxies=proxies, timeout=20, verify=False)


# print(response.text)


# Testing Proxy with curl (optional):
# To further verify if the proxy is working as expected, you can test it using curl from the command line:

# sh
# Copy code
# curl -x 20.47.108.204:8888 http://httpbin.org/get



""" get """
response = requests.get('http://google.com')
# >>> print(response.status_code)

# returns True if response code < 400
if response.ok:
    print('Do something...')

# server response in unicode
# >>> print(response.text)

# if the response is a file: there is a point to use .content
# >>> print(response.content)


""" json """
# if the response is in json
response_git = requests.get('http://api.github.com')
# response_json = response_git.json()

# pprint will return response as python dict
# pprint.pprint(response_json)
# print(type(response_json))

# # u can get values now by keys
# >>> print(response_json['repository_search_url'])


""" headers """
# headers = exta information that client and server exchange

# info about server | response headears
# print(response_git.json())

#info about client | request headers
# print(response_git.request.headers)

# user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0'}
# response= requests.get('http://api.github.com', headers=user_agent)
# print(response.request.headers)


""" params """
# params | how many python repositories on github and info bout them
params = {'q': 'python'}
response= requests.get('http://api.github.com/search/repositories', params=params)
response_json = response.json()
# pprint.pprint(response_json)
# print(response_json['total_count'])


""" cookie """
# cookies are info that server sends to browser for saving | like that user is already logged in
cookies = {'session_token': '12345678'}
response = requests.get('http://httpbin.org/cookies', cookies=cookies)
# print(response.text)


""" session """
# session keeps condition between requests

# set up cookies in one requests and get them in the other
with requests.Session() as session:
    session.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    response = session.get('http://httpbin.org/cookies')
    # print(response.text)


""" post """
# used to send data to server

data = {'key': 'value'}
response = requests.post('http://httpbin.org/post', json=data)
print(response.text)


""" download an image """

img_url = 'https://i0.wp.com/junilearning.com/wp-content/uploads/2020/06/python-programming-language.webp?fit=1920%2C1920&ssl=1'

response = requests.get(img_url)

with open('image.png', 'wb') as file:
    file.write(response.content)



"""check status programm"""

import requests 
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict


def check_status(url: str) -> None:
    try:
        response = requests.get(url)

        # Information
        status_code = response.status_code
        headers = response.headers
        content_type = headers.get('Content-Type', 'Unknown')
        server = headers.get('Server', 'Unknown')
        response_time = response.elapsed.total_seconds()

        print(f' {url}')
        print(f'Status Code: {status_code}')
        print(f'Content Type: {content_type}')
        print(f'Server: {server}')
        print(f'Response Time: {response_time:.2f} seconds')
    except RequestException as e:
        print(f'Error: {e}')
              

def main() -> None:
    url_to_check = 'http://www.apple.com'
    check_status(url=url_to_check)


if __name__ == '__main__':
    main()



