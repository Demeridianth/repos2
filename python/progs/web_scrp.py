import requests
from bs4 import BeautifulSoup


URL = 'https://pythonjobs.github.io/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='main')

job_elements = results.find_all('div', class_='job')
for job in job_elements:
    link_url = job.find('a', class_='go_button')['href']
    title = job.find('h1')
    location = job.find('span', class_='info')
    date = job.find_all('span')[1]
    print(location.text.strip())
    print(title.text)
    print(date.text.strip())
    print(f'More info: https://pythonjobs.github.io/{link_url}')
    print()

    
