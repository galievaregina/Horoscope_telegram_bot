import unittest
from downlod_horoscope_from_website import get_horoscope, send_horoscope
import time


class TestBot(unittest.TestCase):

    def test_check_data_downloading(self):
        url_list = ['https://www.elle.ru/astro/aries/day/', 'https://www.elle.ru/astro/taurus/day/',
                    'https://www.elle.ru/astro/gemini/day/', 'https://www.elle.ru/astro/cancer/day/',
                    'https://www.elle.ru/astro/leo/day/', 'https://www.elle.ru/astro/virgo/day/',
                    'https://www.elle.ru/astro/libra/day/', 'https://www.elle.ru/astro/scorpio/day/',
                    'https://www.elle.ru/astro/sagittarius/day/', 'https://www.elle.ru/astro/capricorn/day/',
                    'https://www.elle.ru/astro/aquarius/day/', 'https://www.elle.ru/astro/pisces/day/']
        for url in url_list:
            data = get_horoscope(url)
            self.assertIsNotNone(data)
            time.sleep(5)

    def test_message_sending(self):
        correct_message = "Чтобы получить гороскоп, нажми на кнопку с необходимым знаком зодиака"
        message_1 = send_horoscope('лев')
        self.assertEquals(message_1, correct_message)
        message_2 = send_horoscope('Привет')
        self.assertEquals(message_2, correct_message)
        message_3 = send_horoscope('Lion')
        self.assertEquals(message_3, correct_message)
        url_list = ['https://www.elle.ru/astro/aries/day/', 'https://www.elle.ru/astro/taurus/day/',
                    'https://www.elle.ru/astro/gemini/day/', 'https://www.elle.ru/astro/cancer/day/',
                    'https://www.elle.ru/astro/leo/day/', 'https://www.elle.ru/astro/virgo/day/',
                    'https://www.elle.ru/astro/libra/day/', 'https://www.elle.ru/astro/scorpio/day/',
                    'https://www.elle.ru/astro/sagittarius/day/', 'https://www.elle.ru/astro/capricorn/day/',
                    'https://www.elle.ru/astro/aquarius/day/', 'https://www.elle.ru/astro/pisces/day/']
        sign_list = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог',
                     'Водолей', 'Рыбы']
        i = 0
        while i < 12:
            self.assertEquals(get_horoscope(url_list[i]), send_horoscope(sign_list[i]))
            i = i + 1
            time.sleep(5)


if __name__ == '__main__':
    unittest.main()