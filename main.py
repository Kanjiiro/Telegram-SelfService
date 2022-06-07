#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import telepot
import time
import os
from datetime import datetime as dnow
from datetime import date
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telepot.namedtuple import ReplyKeyboardRemove

now = None
allowed = ["INSERT IDS"]
global ID =
global TOKEN = ''


months = {1: 'Gennaio',
          2: 'Febbraio',
          3: 'Marzo',
          4: 'Aprile',
          5: 'Maggio',
          6: 'Giugno',
          7: 'Luglio',
          8: 'Agosto',
          9: 'Settembre',
          10: 'Ottobre',
          11: 'Novembre',
          12: 'Dicembre'}
days = {'Monday': 'Lunedi',
        'Tuesday': 'Martedi',
        'Wednesday': 'Mercoledi',
        'Thursday': 'Giovedi',
        'Friday': 'Venerdi',
        'Saturday': 'Sabato',
        'Sunday': 'Domenica'}


def mesi(msg):
    str(months[int(msg['text'].split(' ')[1])])


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id, msg['text'])

    if msg['text'] == '/start':
        if chat_id in allowed:
            bot.sendMessage(chat_id, text="Hey BOOOOY " +
                            str(dnow.now().strftime('%H:%M')))
        else:
            bot.sendMessage(
                chat_id, text="Non sei autorizzato ad usare questo bot!")

    elif msg['text'] == "1":
        bot.sendMessage(ID, 'Deleting keyboard',
                        reply_markup=ReplyKeyboardRemove())
        f = open('Pasti.txt', 'a')
        f.write(str(date.today().strftime("%A/%d/%m")) +
                '/'+msg['text'] + " \n")
        f.close()

    elif msg['text'] == "2":
        bot.sendMessage(ID, 'Deleting keyboard',
                        reply_markup=ReplyKeyboardRemove())
        f = open('Pasti.txt', 'a')
        f.write(str(date.today().strftime("%A/%d/%m")) +
                '/'+msg['text'] + " \n")
        f.close()

    elif msg['text'] == "None":
        bot.sendMessage(ID, 'Deleting keyboard',
                        reply_markup=ReplyKeyboardRemove())
        f = open('Pasti.txt', 'a')
        f.write(str(date.today().strftime("%A/%d/%m")) + '/0' + " \n")
        f.close()

    elif msg['text'] == "/pasti":
        if chat_id in allowed:
            bot.sendMessage(chat_id, "Sto inviando i pasti")
            bot.sendDocument(chat_id, open('Pasti.txt', 'rb'))

    elif msg['text'].split(' ')[0] == "/totale":
        if chat_id in allowed:
            with open('Pasti.txt', 'r') as f:
                content = f.read().splitlines()
                mese = msg['text'].split(' ')[1]
                pasti = []
                content = [x.split('/') for x in content]
                try:
                    for x in content:
                        if x[-2] == str(mese):
                            print(pasti)
                            pasti.append(int(x[-1]))
                            f = open(str(mesi(msg))+'.txt', 'a')
                            f.write(days[x[0]] + ' ' + x[1] +
                                    ' ha preso ' + str(x[-1])+' menu \n')
                            f.close()
                except:
                    IndexError()

                totale = "Pasti del mese di " + months[int(msg['text'].split(' ')[1])] + "\n" + "Totale: " + str(
                    sum(pasti)*6) + "€" + "\n" + "Numero pasti: " + str(sum(pasti))
                try:
                    print(os.path.getsize('Pasti.txt'))
                    if os.path.getsize('Pasti.txt') != 0:
                        bot.sendMessage(chat_id, totale)
                        bot.sendDocument(chat_id, open(str(mesi(msg)+'.txt')))
                    os.system(
                        'rm ' + str(mesi(msg)+'.txt'))
                except:
                    FileNotFoundError()
                    bot.sendMessage(chat_id, 'Mese inesistente nel database')
    elif msg['text'] == "/menu":
        keyboard()
    else:
        bot.sendMessage(chat_id, "Non sei autorizzato a usare questo Bot")

    time.sleep(5)


def keyboard():
    markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='1')],
        [KeyboardButton(text='2')],
        [KeyboardButton(text='None')]
    ])
    bot.sendMessage(ID, "Quanti menù?", reply_markup=markup)


bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

while 1:
    if dnow.now().strftime('%A %H:%M:%S') == 'Monday 12:10:00':
        keyboard()
    elif dnow.now().strftime('%A %H:%M:%S') == 'Sunday 12:10:00':
        f = open('Pasti.txt', 'a')
        f.write(str(date.today().strftime("%A/%d/%m")) + '/0' + " \n")
        f.close()
    elif dnow.now().strftime('%H:%M:%S') == '12:10:00' and dnow.now().strftime('%A') != 'Monday' and 'Sunday':
        keyboard()
    time.sleep(1)
