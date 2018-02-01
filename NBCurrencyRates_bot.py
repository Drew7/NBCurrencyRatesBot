# -*- coding: utf-8 -*-
from urllib.request import Request, urlopen
import json
import telebot


def get_quote(url):
    return urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})).read().decode(encoding='UTF-8')

bot = telebot.TeleBot('508133554:AAER-3E_kcMTrnQWtL7wF_MBaOndTXhl2KU')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! " + message.from_user.first_name + " I am CurrencyRates bot. How can i help you?")
        
    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")
        
    elif message.text == "Balance":
        sum_uah = 5420 
        all_json = get_quote('https://btc-trade.com.ua/api/ticker')
        dictionary_all = json.loads(all_json)
        btc_uah = 0.01015 * float(dictionary_all['btc_uah']['sell'])
        eth_uah = 0.0179550180 * float(dictionary_all['eth_uah']['sell'])
        krb_uah = 0.0047016455 * float(dictionary_all['krb_uah']['sell'])
        sum_dif = btc_uah + eth_uah + krb_uah + 0.2859790000 - sum_uah
        
        message_for_client = "Input  : " + sum_uah + " uah. " + "Balance: " + sum_dif + " uah"
        bot.send_message(message.from_user.id, message_for_client)
        
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