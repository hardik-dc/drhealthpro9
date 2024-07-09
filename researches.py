import wikipediaapi

def get_disease_info(disease_name):
    # Specify a user agent as required by Wikipedia API policy
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent="MrHealthPro/1.0 (YourContactInformation)"
    )
    
    page = wiki_wiki.page(disease_name)
    
    if page.exists():
        summary = page.summary[:1000]  # Get a brief description (first 1000 characters)
        
        # Find the 'Prevention' or 'Precautions' section in the Wikipedia page
        precautions = ""
        for section in page.sections:
            if '' in section.title.lower() or '' in section.title.lower():
                precautions = section.text[:1000]  # Get precautions (first 1000 characters)
                break
        
        return summary, precautions
    else:
        return "Disease not found on Wikipedia", ""
