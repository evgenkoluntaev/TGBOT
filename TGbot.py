import telebot
from pyowm import OWM

owm = OWM('Token')
mgr = owm.weather_manager()

bot = telebot.TeleBot("Token")

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
