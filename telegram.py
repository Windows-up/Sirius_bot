import telebot

from config import decode_trigger, TO_SECURE_MESSAGE, DE_SECURE_MESSAGE, START_MESSAGE
from secure import deSecure, toSecure


def analitics(msg):
    if decode_trigger in msg:
        return DE_SECURE_MESSAGE, deSecure(msg[:-1])
    else:
        return TO_SECURE_MESSAGE, toSecure(msg) + decode_trigger


token = '1899440343:AAGiZ9Kz2ycsWSCE5Xtaek904IlVPxs_gSg'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, START_MESSAGE)


@bot.message_handler(content_types='text')
def message_reply(message):
    msg, text = analitics(message.text)
    bot.send_message(message.chat.id, msg)
    bot.send_message(message.chat.id, text)


bot.infinity_polling()
