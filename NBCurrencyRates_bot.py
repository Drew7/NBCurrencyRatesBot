# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot('508133554:AAER-3E_kcMTrnQWtL7wF_MBaOndTXhl2KU')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! " + message.from_user.first_name + " I am CurrencyRates bot. How can i help you?")
        
    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")
    
    else:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*[telebot.types.KeyboardButton(name) for name in ['Hi', 'How are you?', 'How are u?', '/start', '/help']])
        #markup.row('Hi', 'How are you?')
        #markup.row('How are u?', '/start', '/help')
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