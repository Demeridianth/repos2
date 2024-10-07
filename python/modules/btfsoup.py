import requests
from bs4 import BeautifulSoup

# Function to scrape the text of a Wikipedia page
def scrape_wikipedia_text(url):
    # Send a GET request to the Wikipedia page
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve page with status code {response.status_code}")
    
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the main content div
    content_div = soup.find('div', {'class': 'mw-parser-output'})
    
    # Extract the text from all paragraph tags within the content div
    paragraphs = content_div.find_all('p')
    
    # Combine the text from all paragraphs
    article_text = "\n".join([p.get_text() for p in paragraphs])
    
    return article_text


# Example usage
url = 'https://en.wikipedia.org/wiki/Web_scraping'  # Replace with the Wikipedia page URL of your choice
article_text = scrape_wikipedia_text(url)

# Print the first 500 characters of the text
# print(article_text[:500])


# Explanation:
# requests.get(url): Sends a request to the Wikipedia page.
# BeautifulSoup(response.text, 'html.parser'): Parses the HTML content of the page.
# soup.find('div', {'class': 'mw-parser-output'}): Identifies the main content area of the Wikipedia article.
# content_div.find_all('p'): Extracts all paragraphs within the main content area.
# article_text: Joins the text from all paragraphs into a single string.





# https://en.wikipedia.org/wiki/Book
page = requests.get('https://en.wikipedia.org/wiki/Book')
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify)

#mw-content-text > div.mw-content-ltr.mw-parser-output > p:nth-child(8)

# paragraphs without attrs

# Find all <p> tags without any attributes
# elements_without_attributes = soup.find_all(lambda tag: tag.name == 'p' and not tag.attrs)

# # Print the results
# for element in elements_without_attributes:
#     print(element)


# second paragraph

# Find all paragraphs in the main content of the article
paragraphs = soup.find_all('p')

# Print the second paragraph (index 1 since it's zero-based)
if len(paragraphs) > 1:
    print(paragraphs[1].get_text())
else:
    print("Second paragraph not found.")