
# Задание task_02_27.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241



n = int(input('n = '))

count = 0
i = 2
while count < n:
    prostoe = True
    for j in range (2, i):
        if i % j == 0:
            prostoe = False
            break
    if prostoe:
        count += 1
        print(i, end=' ')
    i += 1

# --------------
# Пример вывода:
#
# n = 10
# 2 3 5 7 11 13 17 19 23 29