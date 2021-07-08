import re
import requests
from fake_useragent import UserAgent
from http import HTTPStatus
from bs4 import BeautifulSoup

UA = UserAgent()

BASE_URL = 'https://housinganywhere.com'
REGEX_DIGITS = re.compile(r'(\d+)')


def _get_page_content(page: int):
    source = f'{BASE_URL}/s/Berlin--Germany'
    params = {
        'page': page,
    }
    headers = {
        'User-Agent': UA.random,
    }
    response = requests.get(source, params=params, headers=headers)

    if response.status_code == HTTPStatus.OK:
        return response.text

    return None


def _get_property_details(link):
    headers = {
        'User-Agent': UA.random,
    }
    response = requests.get(BASE_URL + link, headers=headers)

    if response.status_code == HTTPStatus.OK:
        return response.text

    return None


def _get_property_links(html_doc: str):
    result = set()
    soup = BeautifulSoup(html_doc, 'html.parser')

    links = soup.find_all('a', attrs={'data-test-locator': 'Listing Card'})
    for link in links:
        result.add(link['href'])

    return result


def _normalize_property_details(html_doc: str):
    result = {}
    soup = BeautifulSoup(html_doc, 'html.parser')
    area = soup.select_one('p:-soup-contains("Property")')

    if area:
        area = REGEX_DIGITS.search(area.text.strip()).group()
        result['area'] = area
    else:
        print('No Area TODO')

    return result



def main():
    page = 78
    while True:
        print(f'Page: {page}')

        page += 1
        raw_content = _get_page_content(page)
        links = _get_property_links(raw_content)

        if not links:
            break

        for link in links:
            property_details = _get_property_details(link)
            print(link)
            property_data = _normalize_property_details(property_details)
            print(property_data)

main()
