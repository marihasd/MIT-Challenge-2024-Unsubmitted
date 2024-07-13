import requests
from bs4 import BeautifulSoup

def extract_resource_info(url):
    """
    Extracts detailed information about a resource from a given URL.

    Args:
    - url (str): URL of the resource.

    Returns:
    - dict: Extracted information about the resource.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        resource_name = soup.find('h1').text.strip()
        services_offered = [li.text for li in soup.find_all('ul')[0].find_all('li')]
        eligibility_criteria = soup.find('p', text='Eligibility Criteria').find_next('p').text
        contact_info = soup.find('p', text='Contact Information').find_next('p').text
        location = soup.find('p', text='Location').find_next('p').text
        specializations = [li.text for li in soup.find('p', text='Specializations').find_next('ul').find_all('li')]

        return {
            'resource_name': resource_name,
            'services_offered': services_offered,
            'eligibility_criteria': eligibility_criteria,
            'contact_info': contact_info,
            'location': location,
            'specializations': specializations
        }

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url}, {e}")
        return None
    except AttributeError as e:
        print(f"Error parsing HTML attributes for URL: {url}, {e}")
        return None
    except Exception as e:
        print(f"Error parsing HTML for URL: {url}, {e}")
        return None
