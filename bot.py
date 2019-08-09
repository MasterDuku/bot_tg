 # -*- coding: utf-8 -*-
import  
import random
 
import telebot
from telebot.types import Message 
 
 
TOKEN = "895271748:AAF8q8iGZ9argSZW8JfvOtDGHM-cc3hBdvQ"
 
tbot = telebot.TeleBot(TOKEN)
 
 
@tbot.message_handler(commands=['start', 'help'])
    def command_handler(message: Message):
        tbot.reply_to(message, 'There is no answer =(')
 
 
@tbot.message_handler(content_types=['text'])
    def echo_digits(message: Message):
        tbot.reply_to(message, str(random.random()))
 
 
tbot.polling(timeout=60)