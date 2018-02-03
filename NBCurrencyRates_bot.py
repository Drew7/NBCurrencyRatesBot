# -*- coding: utf-8 -*-
from urllib.request import Request, urlopen
import json
import telebot
import os


def get_quote(url):
    return urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})).read().decode(encoding='UTF-8')

bot = telebot.TeleBot(os.environ['TELEGRAM_KEY'])

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! " + message.from_user.first_name + " I am your CryptoBalance bot. How can i help you?")
        
    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")
        
    elif message.text == "Balance":
        
        btc_in = 5967.53979
        eth_in = 1465.396
        ltc_in = 660.8455728
        
        sum_uah = 8420 
        all_json = get_quote('https://btc-trade.com.ua/api/ticker')
        dictionary_all = json.loads(all_json)
        btc_uah = 0.0121499220 * float(dictionary_all['btc_uah']['sell'])
        btc_diff = btc_uah - btc_in
        eth_uah = 0.0610054820 * float(dictionary_all['eth_uah']['sell'])
        eth_diff = eth_uah - eth_in
        ltc_uah = 0.0818380605 * float(dictionary_all['ltc_uah']['sell'])
        ltc_diff = ltc_uah - ltc_in
        krb_uah = 0.0047016455 * float(dictionary_all['krb_uah']['sell'])
        
        sum_dif = btc_uah + eth_uah + ltc_uah + krb_uah + 0.0004066435 - sum_uah
        
        bot.send_message(message.from_user.id, "Bitcoin:   " + str(btc_diff) + " uah.")
        bot.send_message(message.from_user.id, "Ethereum : " + str(eth_diff) + " uah.")
        bot.send_message(message.from_user.id, "Litecoin:  " + str(ltc_diff) + " uah.")
        
        message_input_uah = "Input  : " + str(sum_uah) + " uah." 
        message_output = "Balance: " + str(sum_dif) + " uah"
        bot.send_message(message.from_user.id, message_input_uah)
        bot.send_message(message.from_user.id, message_output)
        
    else:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*[telebot.types.KeyboardButton(name) for name in ['Hi', 'How are you?', 'Balance']])
        bot.send_message(message.chat.id, "Choose one option:", reply_markup=markup)

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.from_user.id, "Help yourself.")

 # Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    bot.send_message(message.from_user.id, "What?")

bot.polling(none_stop=True, interval=0)