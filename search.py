import requests
from bs4 import BeautifulSoup

def search_resources(query):
    """
    Searches for resources related to a specific query using Google search.

    Args:
    - query (str): Search query.

    Returns:
    - list of dict: List of relevant websites with title, URL, and snippet.
    """
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('div', class_='g')
    relevant_websites = []
    for result in search_results:
        title = result.find('h3').text
        url = result.find('a')['href']
        snippet = result.find('div', class_='s').text
        relevant_websites.append({'title': title, 'url': url, 'snippet': snippet})
    return relevant_websites
