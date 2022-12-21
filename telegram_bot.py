import telebot

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Привет! Выбери знак зодиака')


bot.polling(none_stop=True)
