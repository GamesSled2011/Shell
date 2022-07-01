from email import message
from tkinter import Image
import telebot
from telebot import types
import requests
Help = "Команды бота : start, links, Hello, id, photo, plus, bot, premium, username "

#API
bot = telebot.TeleBot('')

#Самая первая команда
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='')

@bot.message_handler(commands=["Help","help"])
def help(message):
    bot.send_message(message.chat.id, Help, parse_mode="html")


#Кнопка
@bot.message_handler(commands=['links'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Поддержите автора', url='https://www.donationalerts.com/r/syirezz'))
    markup.add(types.InlineKeyboardButton('Проект автора', url='https://discord.gg/BZaYstsMer'))
    markup.add(types.InlineKeyboardButton('Исходный код', url='https://boosty.to/shellbot'))
    bot.send_message(message.chat.id, "Вот тебе ссылки!", reply_markup=markup)
#Попытка №2
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):  
    bot.send_message(message.chat.id, 'Вау крутая картинка занесу ка я её в базу данных')

@bot.message_handler(commands=['Hello'])
def get_user_text(message):
    bot.send_message(message.chat.id, '<b>И тебе привет</b>', parse_mode='html')


@bot.message_handler(commands=['id'])
def get_user_text(message):
    bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode="html")



@bot.message_handler(commands=['photo'])
def get_user_text(message):
    photo = open('d:\Проекты\TelegramBot/Image.png', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['bot'])
def get_user_text(message):
    bot.send_message(message.chat.id, f"Робот : {message.from_user.is_bot}", parse_mode="html")


@bot.message_handler(commands=['premium'])
def get_user_text(message):
    bot.send_message(message.chat.id, f"Премиюм статуст Телеграмм : {message.from_user.is_premium}", parse_mode="html")

@bot.message_handler(commands=['username'])
def get_user_text(message):
    bot.send_message(message.chat.id, f"Твой никнейм : {message.from_user.username}", parse_mode="html")
    
# @bot.message_handler()
# def get_user_text(message):
#     bot.send_message(message.chat.id, message, parse_mode="html")


# #Плисование
# storage = {}
# @bot.message_handler(commands=['plus'])
# def init_storage(user_id):
#   storage[user_id] = dict(first_number=None, second_number=None)
# def store_number(user_id, key, value):
#   storage[user_id][key] = dict(value=value)
# def get_number(user_id, key):
#   return storage[user_id][key].get('value')
# @bot.message_handler(func=lambda m: True)
# def plus(message):
#   init_storage(message.from_user.id)
#   bot.reply_to(message, "Введите + чтобы прибавить два числа ")
#   bot.register_next_step_handler(message, plus)
# def plus(message):
#       if message.text == "+":
#          bot.reply_to(message,"Введите номер 1: ")
#          bot.register_next_step_handler(message, plus_one)
#       else:
#          bot.reply_to(message, "Введите + чтобы прибавить два числа ")
#          bot.register_next_step_handler(message, plus)
# def plus_one(message):
#         first_number = message.text
#         if not first_number.isdigit():
#             msg = bot.reply_to(message, 'Вводите только цифры!')
#             bot.register_next_step_handler(message, plus_one)
#             return
#         store_number(message.from_user.id, "first_number", first_number)
#         bot.reply_to(message, "Введите номер 2: ")
#         bot.register_next_step_handler(message, plus_two)
# def plus_two(message):
#        second_number = message.text

#        if not second_number.isdigit():
#             msg = bot.reply_to(message, 'Вводите только цифры!')
#             bot.register_next_step_handler(message, plus_two)
#             return
#        store_number(message.from_user.id, "second_number", second_number)
#        number_1 = get_number(message.from_user.id, "first_number")
#        number_2 = get_number(message.from_user.id, "second_number")
#        result_plus = int(number_1) + int(number_2)
#        bot.reply_to(message, f"Ответ: {result_plus}")   






bot.polling(non_stop=True)

#Не удачный код