import telebot
from pyowm import OWM

owm = OWM('a464f9ec8c423ca4231d871fa1820406')
mgr = owm.weather_manager()

bot = telebot.TeleBot("2036184441:AAEkRHkFlLg5MTiD1-VaL4XwXzqUYBUVy3g")

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, я бот, знающий погоду во всем мире. Вводи город, чтобы тоже все узнать.')

@bot.message_handler(content_types=['text'])
def send_weather(message):
    try:

        observation = mgr.weather_at_place(message.text)
        w = observation.weather

        t = w.temperature('celsius')['temp']

        humi = w.humidity

        time = w.reference_time('iso')

        answer = message.text+': '+w.detailed_status+' now.\nTemperature is '+str(t)+' celsius.\nHumidity: '+str(humi)+'%\nUpdated:'+time

        bot.send_message(message.chat.id, answer)

    except:
        answer = 'Please, enter the correct value.'
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)
