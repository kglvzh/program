
# Задание task_02_10.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241
# E-mail: dzhajmg@gmail.com


n = int(input("n = "))

n_sum = 0
n_count = 0

while (n != 0):
    last  = n % 10
    n_sum += last

    n_count += 1

    n = n // 10

print(f"Сумма = {n_sum}")
print(f"Количество = {n_count}")

# --------------
# Пример вывода:
#
# n = 12345
# Сумма = 15
# Количество = 5
