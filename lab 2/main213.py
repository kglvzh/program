# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_02_13.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241
# E-mail: dzhajmg@gmail.com


a = int(input('a = '))
b = int(input('b = '))

n_sum = 0 # сумма
n_mult = 1 # произведение
count = 0 # кол-во нечётных чисел
nechet = 1 # произведение нечётных чисел

for n in range(a, b+1):
    n_sum += n
    n_mult *= n
    if n % 2 == 1:
        count += 1
        nechet *= n

n_avg = round(n_sum / (b-a+1), 2)
n_avg_geom = round(nechet ** (1 / count), 2)

print("Сумма =", n_sum)
print("Произведение =", n_mult)
print(f"Среднее арифметическое = {n_avg}")
print(f"Среднее геометрическое нечетных чисел = {n_avg_geom}")

# --------------
# Пример вывода:
#
# a = 1
# b = 5
# Сумма = 15
# Произведение = 120
# Среднее арифметическое = 3.00
# Среднее геометрическое нечетных чисел = 2.47
