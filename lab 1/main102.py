# Задание task_01_02.
#
# Выполнил: Гловели Д.К.
# Группа: ЦИБ-241


x = int(input("x="))
y = int(input("y="))
z = int(input("z="))

res = (((x**5 + 7)/(abs(-6)*y))**(1/3))/(7 - z % y)

print(round (res, 3))


# --------------
# Пример вывода:
#
# x=0
# y=1
# z=2
# 0.15
