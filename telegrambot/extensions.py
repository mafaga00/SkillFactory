from config import currencies
import requests
import json

class APIException(Exception):
    pass

class BotExtensions:
    @staticmethod
    def get_price(values):
        if len(values) != 3:
            raise APIException("Неверное количество параметров")
        quote, base, amount = values
        if quote == base:
            raise APIException(f"Вы ввели одинаковые валюты: {base}")
        try:
            quote_formated = currencies[quote]
        except KeyError:
            raise APIException(f"Такая валюта не поддерживается: {quote}")
        try:
            base_formated = currencies[base]
        except KeyError:
            raise APIException(f"Такая валюта не поддерживается: {base}")
        try:
            amount = abs(float(amount.replace(',', '.')))
        except ValueError:
            raise APIException(f"Не корректно введено количество валюты: {amount}")

        html = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_formated}&tsyms={base_formated}')
        result = (json.loads(html.content)[base_formated])
        return result * amount