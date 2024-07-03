import requests
from bs4 import BeautifulSoup
import schedule
import time

# URL of the webpage to monitor
URL = "https://www.gesobau.de/mieten/wohnungssuche/"

# Global variable to store previously found items
previous_items = set()


def fetch_items():
    """Fetch and parse the webpage content, returning the relevant div items."""
    response = requests.get(URL)
    response.raise_for_status()  # Check for request errors
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all(
        'div', class_="teaserList__item results-entry wohnungssuche")
    return set(item.find('a')['href'] for item in items)


if __name__ == '__main__':
    print(fetch_items())
