import requests
from bs4 import BeautifulSoup


def get_horoscope(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    data = soup.find('div', {'class': 'articleParagraph articleParagraph_dropCap'}).text
    return data


def send_horoscope(message_in):
    if message_in == "Овен":
        message_out = get_horoscope('https://www.elle.ru/astro/aries/day/')
    elif message_in == "Телец":
        message_out = get_horoscope('https://www.elle.ru/astro/taurus/day/')
    elif message_in == "Близнецы":
        message_out = get_horoscope('https://www.elle.ru/astro/gemini/day/')
    elif message_in == "Рак":
        message_out = get_horoscope('https://www.elle.ru/astro/cancer/day/')
    elif message_in == "Лев":
        message_out = get_horoscope('https://www.elle.ru/astro/leo/day/')
    elif message_in == "Дева":
        message_out = get_horoscope('https://www.elle.ru/astro/virgo/day/')
    elif message_in == "Весы":
        message_out = get_horoscope('https://www.elle.ru/astro/libra/day/')
    elif message_in == "Скорпион":
        message_out = get_horoscope('https://www.elle.ru/astro/scorpio/day/')
    elif message_in == "Стрелец":
        message_out = get_horoscope('https://www.elle.ru/astro/sagittarius/day/')
    elif message_in == "Козерог":
        message_out = get_horoscope('https://www.elle.ru/astro/capricorn/day/')
    elif message_in == "Водолей":
        message_out = get_horoscope('https://www.elle.ru/astro/aquarius/day/')
    elif message_in == "Рыбы":
        message_out = get_horoscope('https://www.elle.ru/astro/pisces/day/')
    else:
        message_out = "Чтобы получить гороскоп, нажми на кнопку с необходимым знаком зодиака"
    return message_out
