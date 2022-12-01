import telebot
from downlod_horoscope_from_website import get_horoscope
bot = telebot.TeleBot('5798771779:AAHSFF0CQgEHFm4rK_ss1-SmdrkjQzLni6M')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)  # наша клавиатура
    key_aries = telebot.types.KeyboardButton(text='Овен')
    key_taurus = telebot.types.KeyboardButton(text='Телец')
    key_gemini = telebot.types.KeyboardButton(text='Близнецы')
    key_cancer = telebot.types.KeyboardButton(text='Рак')
    key_leo = telebot.types.KeyboardButton(text='Лев')
    key_virgo = telebot.types.KeyboardButton(text='Дева')
    key_libra = telebot.types.KeyboardButton(text='Весы')
    key_scorpio = telebot.types.KeyboardButton(text='Скорпион')
    key_sagittariu = telebot.types.KeyboardButton(text='Стрелец')
    key_capricorn = telebot.types.KeyboardButton(text='Козерог')
    key_aquarius = telebot.types.KeyboardButton(text='Водолей')
    key_pisces = telebot.types.KeyboardButton(text='Рыбы')
    keyboard.add(key_taurus, key_aries, key_gemini, key_cancer, key_leo, key_virgo, key_libra, key_scorpio,
                 key_sagittariu, key_capricorn, key_aquarius, key_pisces)
    bot.send_message(message.chat.id, text='Привет! Выбери знак зодиака', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Овен":
        bot.send_message(message.chat.id, text=get_horoscope('https://www.elle.ru/astro/aries/day/'))
    elif message.text == "Телец":
        bot.send_message(message.chat.id, text=get_horoscope('https://www.elle.ru/astro/taurus/day/'))
    elif message.text == "Близнецы":
        bot.send_message(message.chat.id, text=get_horoscope('https://www.elle.ru/astro/gemini/day/'))
    elif message.text == "Рак":
        bot.send_message(message.chat.id, text=get_horoscope('https://www.elle.ru/astro/cancer/day/'))
    elif message.text == "Лев":
        bot.send_message(message.chat.id, text=get_horoscope('https://www.elle.ru/astro/leo/day/'))
    elif message.text == "Дева":
        bot.send_message(message.chat.id, text=get_horoscope('https://www.elle.ru/astro/virgo/day/'))
    elif message.text == "Весы":
        bot.send_message(message.chat.id, text=get_horoscope('https://www.elle.ru/astro/libra/day/'))
    elif message.text == "Скорпион":
        bot.send_message(message.chat.id, text=get_horoscope('https://www.elle.ru/astro/scorpio/day/'))
    elif message.text == "Стрелец":
        bot.send_message(message.chat.id, text=get_horoscope('https://www.elle.ru/astro/sagittarius/day/'))
    elif message.text == "Козерог":
        bot.send_message(message.chat.id, text=get_horoscope('https://www.elle.ru/astro/capricorn/day/'))
    elif message.text == "Водолей":
        bot.send_message(message.chat.id, text=get_horoscope('https://www.elle.ru/astro/aquarius/day/'))
    elif message.text == "Рыбы":
        bot.send_message(message.chat.id, text=get_horoscope('https://www.elle.ru/astro/pisces/day/'))


bot.polling(none_stop=True)
