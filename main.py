
import telebot
from telebot import types
#2104196344:AAEz8QHE6bDDScjnOe9DJTJ3LMGnzFch0NM
bot = telebot.TeleBot("2104196344:AAEz8QHE6bDDScjnOe9DJTJ3LMGnzFch0NM")

name = ''
suname = ''
age = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Доброе утро че сказать, для регистрации введи /reg")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'привет раб':
        bot.reply_to(message, 'здаравствуйте господин')
    elif message.text == 'ты лох':
        bot.reply_to(message, 'да((')
    elif message.text == '/reg':
        bot.send_message(message.from_user.id,'как тебя зовут то?')
        bot.register_next_step_handler(message,reg_name)
	#bot.reply_to(message, message.text)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'фамилия какая?')
    bot.register_next_step_handler(message,reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'укажи возраст')
    bot.register_next_step_handler(message,reg_age)


def reg_age(message):
        global age
        # age = message.text
        while age == 0:
           try:
               age = int(message.text)
           except Exception:
               bot.send_message(message.from_user.id, "вводи цифрами ")
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton('Конечно', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton('Нет', callback_data='yes')
        keyboard.add(key_no)
        question = 'Тебе ' + str(age) + ' лет? И тебя зовут ' + name + ' ? А также твоя фамилия ' + surname + ' ?'
        bot.send_message(message.from_user.id,  text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.from_user.id, 'Ну и дурацкое у тебя имя')
    elif call.data == 'no':
            bot.send_message(call.message.from_user.id, 'Пиши новые данные')
            bot.send_message(call.message.from_user.id, 'как тебя зовут то?')
            bot.register_next_step_handler(call.message, reg_name)

bot.polling()

