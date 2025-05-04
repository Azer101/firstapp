import telebot
import wikipedia
import re

bot = telebot.TeleBot('7526980231:AAGli0onQtYkwFO5xPZCjb5Jw0gMxo2jZfc')

wikipedia.set_lang('ru')

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        witext = ny.content[:1000]
        wimas = witext.split('.')
        wimas = wimas[:-1]
        witext2 = ''

        for i in wimas:
            if not('==' in i):
                if(len((i.strip()))>3):
                    witext2=witext2+i+''
            else:
                break 
        witext2=re.sub('\([^()]*\)', '', witext2)
        witext2=re.sub('\([^()]*\)', '', witext2)
        witext2=re.sub('\{[^\{\}]*\}', '', witext2)
        return witext2
    except Exception as e:
        return 'Нет такой информации'

@bot.message_handler(commnads=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Напиши мне что-то')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(non_stop=True, interval=0)













#@bot.message_handler(commands=['start'])
#def start(message):
#    bot.send_message(message.chat.id, 'Напиши мне что-то')

#@bot.message_handler(content_types=['text'])
#def handle_text(message):
#    bot.send_message(message.chat.id, "Ты написал " + message.text)
#bot.polling(non_stop=True, interval=0)