import telebot

bot = telebot.TeleBot('5798771779:AAHSFF0CQgEHFm4rK_ss1-SmdrkjQzLni6M')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Привет! Выбери знак зодиака')


bot.polling(none_stop=True)
