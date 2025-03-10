
# Задание task_02_34.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241



# 1. Заполнение списка

# Используйте данный список для собственных тестов,
# чтобы избежать постоянного ввода значений
# Перед автоматической проверкой удалите его
# и используйте ввод с клавиатуры
# deposits = [
#    {"name": "Банк_1", "initial_sum": 50000, "rate": 5.2},
#    {"name": "Банк_2", "initial_sum": 20000, "rate": 3.7},
#    {"name": "Банк_3", "initial_sum": 45000, "rate": 6.8},
# ]

n = int(input('Количество банков = '))

deposits = []
for _ in range(n):
    data = input().split()
    deposit = {}
    deposit["name"] = data[0]
    data[1] = int(data[1])
    deposit["initial_sum"] = data[1]
    data[2] = float(data[2])
    deposit["rate"] = data[2]
    deposits.append(deposit)

# 2. Самый доступный банк (с наименьшей первоначальной суммой)
sorted_deposits = sorted(deposits, key=lambda x: x["initial_sum"])
deposit_min = sorted_deposits[0]
print(f'Самый доступный банк: {sorted_deposits[0]["name"]}, первоначальная сумма: {sorted_deposits[0]["initial_sum"]} руб.')

# Удалите комментарий и допишите код

# 3. Самый выгодный банк
#    прибыль = сумма * процент / 100

sorted_deposits_profit = sorted(deposits, key=lambda x: x["initial_sum"] * x["rate"] / 100)
sorted_deposits_profit_max = sorted_deposits_profit[-1]
print(f'Самый выгодный банк: {sorted_deposits_profit[-1]["name"]}, прибыль: {round(sorted_deposits_profit[-1]["initial_sum"] * sorted_deposits_profit[-1]["rate"] / 100, 2)} руб.')

# --------------
# Пример вывода:
#
# Количество банков = 3
# Банк_1 50000 5.2
# Банк_2 20000 3.7
# Банк_3 45000 6.8
# Самый доступный банк: Банк_2, первоначальная сумма: 20000.00 руб.
# Самый выгодный банк: Банк_3, прибыль: 3060.00 руб.