import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service




#SELENIUM#
# chrome_path 

options = webdriver.ChromeOptions()
driver_path = "C:/Users/sergi/AppData/Local/Google/Chrome/UserData/chromedriver.exe"
service = Service(executable_path=driver_path)
# service = Service()
driver = webdriver.Chrome(service=service)
driver.get('https://oxylabs.io/blog')

blog_titles = driver.find_elements(By.CSS_SELECTOR, 'a.e1dscegp1')
for title in blog_titles:
    print(title.text)
driver.quit()  # closing the browser



#BEAUTIFULL SOUP
# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(id='ResultsContainer')
# print(results.prettify())
# job_elements = results.find_all('div', class_='card-content')
# for job in job_elements:a
#     print(job, end='\n'*2)
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()


# python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())

# python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]

# for job_element in python_job_elements:
#     link_url = job_element.find_all('a')[1]['href']
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()
#     print(f'Apply here: {link_url}\n')
    
    # links = job_element.find_all('a', string=lambda text: 'Apply' in text)
    # for link in links:
    #     link_url = link['href']
    #     print(f'Apply here: {link_url}\n')



    ###############################



# form_data = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post('https://oxylabs.io/', data=form_data)
# print(response.text)

# url = 'https://oxylabs.io/'
# proxies={'http': 'http://user:password@pr.oxylabs.io:7777'}
# response = requests.get('https://ip.oxylabs.io/', proxies=proxies)
# soup = BeautifulSoup(response.text, 'html.parser')
# blog_titles = soup.select('a.e1dscegp1')
# for title in blog_titles:
#     # print(title.text)




