from extensions import APIException, BotExtensions
from config import token, currencies
import telebot

bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Привет! Я Бот-Конвертер валют и я могу:\n- Показать список доступных валют через команду /values \
    \n- Вывести конвертацию валюты при вводе:\n<имя валюты> <в какую валюту перевести> <количество переводимой валюты>\n \
- Напомнить, что я могу через команду /help'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in currencies.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.lower().split()
    try:
        result = BotExtensions.get_price(values)
    except APIException as e:
        bot.reply_to(message, f'Ошбика пользователя!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'{values[2]} {currencies[values[0]]} = {result} {currencies[values[1]]}'
        bot.reply_to(message, text)


bot.polling()