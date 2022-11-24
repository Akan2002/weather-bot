import telebot
from telebot import types
from config import TOKEN
from main import get_weather

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    text = 'Я бот погоды, отправь название города!'
    bot.send_message(message.chat.id, text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('London')
    item2 = types.KeyboardButton('Bishkek')
    item3 = types.KeyboardButton('Astana')
    item4 = types.KeyboardButton('Vatikan')

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,'Выбери кнопку', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':
        text = get_weather(message.text)
        bot.send_message(message.chat.id, text)
    
# @bot.message_handler(content_types=['text'])

bot.polling(non_stop = True)
