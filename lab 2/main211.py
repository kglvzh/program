
# Задание task_02_11.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241



start = int(input("start = "))
k = int(input("k = "))
s = int(input("s = "))
n_count = 0 # кол-во уже выведенных чисел

n = start # первоначальное число
while (n_count < 10):
    if n % 10 == k and n % s == 0:
        print(n, end=' ')
        n_count += 1

    n = n + 1
print()

# --------------
# Пример вывода:
#
# start = 100
# k = 7
# s = 9
# 117 207 297 387 477 567 657 747 837 927
