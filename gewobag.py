import requests
from bs4 import BeautifulSoup
import schedule
import time

# URL of the webpage to monitor
URL = "https://www.gewobag.de/fuer-mieter-und-mietinteressenten/mietangebote/?objekttyp%5B%5D=wohnung&gesamtmiete_von=&gesamtmiete_bis=&gesamtflaeche_von=&gesamtflaeche_bis=&zimmer_von=&zimmer_bis=&sort-by="

# Global variable to store previously found items
previous_items = set()


def fetch_items():
    """Fetch and parse the webpage content, returning the relevant div items."""
    response = requests.get(URL)
    response.raise_for_status()  # Check for request errors
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_="angebot-footer")
    return set(item.find('a')['href'] for item in items)


if __name__ == '__main__':
    print(fetch_items())
