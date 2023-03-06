per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада: '))
tkb = round(money * per_cent.get('ТКБ') / 100)
skb = round(money * per_cent.get('СКБ') / 100)
vtb = round(money * per_cent.get('ВТБ') / 100)
sber = round(money * per_cent.get('СБЕР') / 100)
deposit = [tkb, skb, vtb, sber]
max_deposit = max(deposit)
print('Накопленные средства за год вклада.')
print(f' Транскапиталбанк - {tkb}. \n СКБ-Банк = {skb}. \n Банк ВТБ - {vtb}. \n Сбербанк - {sber}.')
print(f"Максимальная сумма, которую вы можете заработать — {max_deposit}.")