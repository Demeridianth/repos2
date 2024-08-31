import wikipedia

try:
    # Fetch the summary of the Wikipedia page
    summary_text = wikipedia.summary("Python (programming language)", sentences=3)

    # Store it in an object (a dictionary in this case)
    wiki_data = {
        "title": "Python (programming language)",
        "summary": summary_text,
    }

    print(wiki_data)

except wikipedia.exceptions.DisambiguationError as e:
    print(f"Disambiguation error: {e.options}")
except wikipedia.exceptions.PageError:
    print("Page does not exist.")\
    



import wikipediaapi

# Create a Wikipedia object
wiki_wiki = wikipediaapi.Wikipedia('en')

# Fetch a Wikipedia page
page = wiki_wiki.page("Python (programming language)")

# Check if the page exists
if page.exists():
    # Get the summary of the page
    summary_text = page.summary

    # Store it in an object (a dictionary in this case)
    wiki_data = {
        "title": page.title,
        "summary": summary_text,
        "full_text": page.text
    }

    print(wiki_data)
else:
    print("Page does not exist.")