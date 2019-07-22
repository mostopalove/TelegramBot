import telebot
import MessageModule as M

bot = telebot.TeleBot('758885135:AAHqZgGeYa41JeMVWMLcg63YGaXe06ShS7w')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text == '/start':
        bot.send_message(message.from_user.id, M._welcomeMessage)
    else:
        bot.send_message(message.from_user.id, 'Я пока умею только отвечать на "Привет"')

bot.polling(none_stop=True, interval=0)