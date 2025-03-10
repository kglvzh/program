
# Задание task_02_20.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241



n = int(input('n = '))

for i in range(100, 1000):
    i_sum = 0

    i_sum += i % 10
    i_sum += i // 100
    i_sum += i // 10 % 10

    if i_sum == n:
        print(i, end=' ')
    else:
        continue

# --------------
# Пример вывода:
#
# n = 3
# 102 111 120 201 210 300
