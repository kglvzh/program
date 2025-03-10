
# Задание task_02_12.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241



a = int(input("a = "))
b = int(input("b = "))

for i in range(a, b+1) or range(b, a+1):
    print(i, end=' ')
else:
    print()
    if a < b:
        i1 = list(range(a, b+1))
        i1_1 = sorted(i1, reverse=True)
        for n in i1_1:
            print(n)
    else:
        i2 = list(range(b, a+1))
        i2_2 = sorted(i2, reverse=True)
        for n in i2_2:
            print(n)


# --------------
# Пример вывода:
#
# a = 1
# b = 5
# 1 2 3 4 5
# 5
# 4
# 3
# 2
# 1
