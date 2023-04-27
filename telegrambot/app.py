from extensions import ExtensionException,Extensions
from config import token, keys
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
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) > 3:
            raise ExtensionException("Слишком много параметров!")

        quote, base, amount = values
        total_base = Extensions.get_price(quote, base, amount)
    except ExtensionException as e:
        bot.reply_to(message, f"Ошбика пользователя!\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        text = f"Цена {amount} {quote} в {base} = {total_base}."
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)