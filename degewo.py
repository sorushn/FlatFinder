import requests
from bs4 import BeautifulSoup
import schedule
import time

# URL of the webpage to monitor
URL = "https://immosuche.degewo.de/de/search?size=10&page=1&property_type_id=1&categories%5B%5D=1&lat=&lon=&area=&address%5Bstreet%5D=&address%5Bcity%5D=&address%5Bzipcode%5D=&address%5Bdistrict%5D=&address%5Braw%5D=&district=&property_number=&price_switch=true&price_radio=null&price_from=&price_to=&qm_radio=50&qm_from=&qm_to=&rooms_radio=custom&rooms_from=1&rooms_to=&wbs_required=&order=rent_total_without_vat_asc"

# Global variable to store previously found items
previous_items = set()


def fetch_items(URL):
    """Fetch and parse the webpage content, returning the relevant div items."""
    response = requests.get(URL)
    response.raise_for_status()  # Check for request errors
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all(
        'article', class_="article-list__item article-list__item--immosearch")
    return set(item.find('a')['href'] for item in items)


def get_max_pages(URL):
    response = requests.get(URL)
    response.raise_for_status()  # Check for request errors
    # print("pager__page-link" in response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    max_page = soup.find_all(string="Ende")
    print(max_page)
    # return set(item.find('a')['href'] for item in items)


if __name__ == '__main__':
    get_max_pages(URL)
    # print(fetch_items(URL))
