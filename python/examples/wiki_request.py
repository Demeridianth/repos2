import requests

# Define the Wikipedia API endpoint
WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

# Define the parameters for the API request
params = {
    "action": "query",
    "format": "json",
    "titles": "Python (programming language)",  # Page title
    "prop": "extracts",
    "exintro": True,  # Get the intro only
    "explaintext": True  # Get plain text, not HTML
}

# Make the request to the Wikipedia API
response = requests.get(WIKI_API_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract the page information | takes first paragraph: summary in wiki
    page = next(iter(data['query']['pages'].values()))
    
    # Check if the page exists
    if 'extract' in page:
        # Store the data in an object (a dictionary in this case)
        wiki_data = {
            "title": page['title'],
            "summary": page['extract']
        }
        
        # Print the extracted data
        print(wiki_data)
    else:
        print("No extract available for this page.")
else:
    print(f"Failed to retrieve data: {response.status_code}")



# Explanation:
# WIKI_API_URL: The URL of the Wikipedia API endpoint.
# params: The parameters sent with the request:
# action: The action to perform. "query" is used to fetch information about a page.
# format: The format of the output. "json" is used for JSON output.
# titles: The title of the Wikipedia page you want to fetch.
# prop: The property to get. "extracts" is used to get the content of the page.
# exintro: Limits the content to just the introduction.
# explaintext: Returns plain text instead of HTML.
# response.json(): Converts the response to a JSON object.
# page['extract']: The text content extracted from the Wikipedia page.



""" getting history saction """

# Define the Wikipedia API endpoint
WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

# Define the parameters for the API request
params = {
    "action": "parse",
    "format": "json",
    "page": "Python (programming language)",  # Page title
    "prop": "sections|text",  # Get the sections and full text
    "section": 0,  # Get the full page (we'll parse the section we need later)
    "formatversion": 2,
    "utf8": 1
}

# Make the request to the Wikipedia API
response = requests.get(WIKI_API_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract all sections
    sections = data.get('parse', {}).get('sections', [])
    
    # Find the "History" section
    history_section = None
    for section in sections:
        if section['line'].lower() == 'history':
            history_section = section
            break
    
    if history_section:
        # Now make another request to get the specific section content
        history_section_number = history_section['index']
        
        # Update parameters to fetch only the "History" section
        params['section'] = history_section_number
        response = requests.get(WIKI_API_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract and print the "History" section text
            history_text = data.get('parse', {}).get('text', "")
            wiki_data = {
                "title": "Python (programming language) - History",
                "history": history_text
            }
            print(wiki_data)
        else:
            print(f"Failed to retrieve History section: {response.status_code}")
    else:
        print("History section not found.")
else:
    print(f"Failed to retrieve data: {response.status_code}")

# Explanation:
# Request Parameters:

# "action": "parse": Uses the parse action to fetch the content of a page.
# "prop": "sections|text": Retrieves both sections and the full text.
# "page": "Python (programming language)": The title of the Wikipedia page.
# "section": 0: Initially fetches the entire page content to locate sections.
# Locating the "History" Section:

# The script first retrieves all sections to find the one labeled "History".
# Once identified, it retrieves the specific section content by making a subsequent request with the correct section parameter.
# Fetching and Parsing the Section:

# The history_section_number is used to fetch only the "History" section text.
# The result is stored in a dictionary called wiki_data and printed