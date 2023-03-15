money_list = []
tickets_amount = int(input('Введите количество билетов: '))
for i in range(1, tickets_amount + 1):
    age = int(input(f'Введите возраст {i}-го посетителя: '))
    if 0 < age < 18:
        money_list.append(0)
    elif 18 <= age < 25:
        money_list.append(990)
    elif 100 >= age >= 25:
        money_list.append(1390)
    else:
        print('Вводите корректный возраст!')
        exit()

sum_list = sum(money_list)
if len(money_list) >= 3 and sum(money_list) >= 990:
    sum_list = sum_list - (sum_list * 0.10)
    print(f'Сумма к оплате с учетом 10% скидки - {round(sum_list)}р.')
    exit()

print(f'Сумма к оплате - {sum_list}р.')