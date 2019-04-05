from route import Route, ChooseMethods
from telebot import util
import telebot


TOKEN = '816290774:AAEhjJPl_ceOjPzqpWBNM-vLv3WEMvj3ZCc'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'NumericalBot can perform  of some calculations numerical methods')


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, '''
    List of available methods and their input:
        -Bisection methods(interval and function): bisection -10 0 x*3+2
        -Euler method(function, x, y, h, begin, end): 
            euler (2/3)*x*y+2*x 2 1 0.25 4 5.5
        -Runge-Kutta method(function, x, y, h, begin, end): 
            rungekutta (2/3)*x*y+2*x 2 1 0.1 4 4.5
    ''')


@bot.message_handler(func=lambda message: True)
def send_answer(message):
    method = ChooseMethods(message.text)
    Route(method.kwargs)
    large_text = open('data.txt', 'rb').read()
    splitted_text = util.split_string(large_text, 3000)
    for text in splitted_text:
        bot.send_message(message.chat.id, text)
    file = open('data.txt', 'rb')
    bot.send_document(message.chat.id, file)
    file.close()


bot.polling()





