import requests
from bs4 import BeautifulSoup


def get_horoscope(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    data = soup.find('div', {'class': 'articleParagraph articleParagraph_dropCap'}).text
    return data
