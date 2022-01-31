# -*- coding: utf-8 -*-
import telebot
import os
import sys
import datetime
import json
import emoji
sys.path.append('/home/mberezovskiy/project/DB')
import dblogic
from time import sleep
import random


filecreds = open('/home/mberezovskiy/Creds/CredentialsBot.json')
CredsBot = json.loads(filecreds.read())
bot = telebot.TeleBot(CredsBot["SecretBotKey"])

date= datetime.datetime.today()



##Методы 


def GetChallenge(IdChat):
    i=0
    for line in challenges:
        if line.GetId()==IdChat:
            return i
        i+=1
    return 0
          
def CreateChallenge(IdChat, IdPerson, NamePerson):
    return dblogic.AddChallenge(dblogic.ConnectDB("db_Pidor"), IdChat, IdPerson, str(NamePerson))

    
    



@bot.message_handler(commands=['start'])
def start_message(message):
    test=CreateChallenge(message.chat.id, message.from_user.id, message.from_user.username)
    if test==1:
        bot.send_message(message.chat.id, "От создателей таких шедевров как \"Купель у Миксельбурга\" и \"Ну в этом году уж точно поедем за УАЗиком \"  ")
        bot.send_message(message.chat.id, "ПИДОР-БОТ!!!!")
    else: 
        bot.send_message(message.chat.id, "АЗАЗАЗА")

@bot.message_handler(commands=['register'])
def register_message(message):
    test = dblogic.AddChallenger(dblogic.ConnectDB("db_Pidor"), message.chat.id, message.from_user.id, str(message.from_user.username))
    if test ==1:
        bot.send_message(message.chat.id, "Милости прошу к нашему шалашу")
    else: bot.send_message(message.chat.id, "Так ты уже около параши")

@bot.message_handler(commands=['champions'])
def spisok_message(message):
    text=''
    spisok = dblogic.GetResult(dblogic.ConnectDB("db_Pidor"), message.chat.id)[0]
    if spisok == 0 : bot.send_message(message.chat.id, "Не спеши, петушок")
    else:
        spisok = sorted(spisok, key = lambda pidor: pidor[1], reverse=True)
        for each in spisok:
            text+=str(each[0])
            text+=': '
            text+=str(each[1])
            text+=' \n'
        bot.send_message(message.chat.id, text)
   
def poll():
     try:  bot.polling()
     except :
         sleep(5)
         poll()

@bot.message_handler(commands=['pidor'])
def pidor_message(message):
    spisok = dblogic.GetResult(dblogic.ConnectDB("db_Pidor"), message.chat.id)
    if spisok==0: bot.send_message(message.chat.id, "Не спеши, петушок")
    else:
        pidor = random.randint(0, len(spisok)-1)
        result = dblogic.PushScore(dblogic.ConnectDB("db_Pidor"), message.chat.id, spisok[pidor][2])
        val=(str(spisok[pidor][0]), str(spisok[pidor][2]))
        text = "А петушок у нас сегодня [%s](tg://user?id=%s)" + " \xF0\x9F\x90\xB6"
        if result == 1: 
            bot.send_message(message.chat.id, text % val, parse_mode='Markdown')
            bot.send_message(message.chat.id, "Таков путь")
        else: bot.send_message(message.chat.id, "Кажется, сегодня у нас уже есть пидарок"+ " \xF0\x9F\x9A\x80")

@bot.message_handler(commands=['test'])
def pidor_message(message):
    val=("you", "119385217")
    text = "А петушок у нас сегодня [%s](tg://user?id=%s)" + " \xF0\x9F\x90\xB6"
    bot.send_message(message.chat.id, text % val, parse_mode='Markdown')
    print('azazaza')

#@bot.message_handler()
#def echo_message(message):
#    print(message.text)
#    print('ты пЁс')




#test

poll()
