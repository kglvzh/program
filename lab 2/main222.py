# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_02_22.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241
# E-mail: dzhajmg@gmail.com


n = int(input('n = '))

max = 0
min = 0

count = 0
for i in range(n):
    count += 1
    f = float(input(f'{count}-е число: '))
    if i == 0:
        min = f
        max = f
    elif f < min:
        min = f
    elif f > max:
        max = f

print("Максимум: {:.2f}".format(max))
print("Минимум: {:.2f}".format(min))

# --------------
# Пример вывода:
#
# n = 4
# 1-е число = 6.2
# 2-е число = 3.8
# 3-е число = 1.1
# 4-е число = 9.66
# Максимум: 9.66
# Минимум: 1.10
