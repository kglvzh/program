
# Задание task_02_05.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241



x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))

if x > 0 and y > 0:
    print("1-я четверть")
elif x < 0 and y > 0:
    print("2-я четверть")
elif x < 0 and y < 0:
    print("3-я четверть")
else:
    print("4-я четверть")

# Удалите комментарий и допишите код

# --------------
# Пример вывода:
#
# Введите координату x: 5
# Введите координату y: 7
# 1-я четверть
