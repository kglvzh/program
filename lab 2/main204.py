
# Задание task_02_04.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241



year_today = int(input('Введите текущий год: '))
month_today = int(input('Введите текущий месяц: '))

year = int(input('Введите год рождения: '))
month = int(input('Введите месяц рождения: '))

# Считается, введенные значения находятся в допустимых пределах,и
# что 'month_today' >= 'month' (проверять значения не нужно)
# Результат необходимо записать в переменную 'age'
age = year_today - year
if month_today <= month:
    age -= 1

print("Число полных лет: ", age)

# --------------
# Пример вывода:
#
# Введите текущий год: 2017
# Введите текущий месяц: 5
# Введите год рождения: 2000
# Введите месяц рождения: 1
# Число полных лет:  17
#
# Введите текущий год: 2015
# Введите текущий месяц: 6
# Введите год рождения: 2010
# Введите месяц рождения: 8
# Число полных лет:  4
#
# Введите текущий год: 2020
# Введите текущий месяц: 5
# Введите год рождения: 2000
# Введите месяц рождения: 5
# Число полных лет:  20
