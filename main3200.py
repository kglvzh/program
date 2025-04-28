# Задание task_03_02_01.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241


def foo(a):
    """
    Алгоритм: сортировка списка методом пузырька по возрастанию.

    Сложность: O(N^2).
    """
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a


a = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2, 2]
foo(a)



# Задание task_03_02_02.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241


def foo(i):
    """
    Алгоритм: преобразование целого числа в строку с остаточным делением на 10.

    Параметры:
        - i (int): число.

    Сложность: O(log(N)).
    """
    digits = "0123456789"
    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result = digits[i%10] + result
        i = i // 10
    return result



# Задание task_03_02_03.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241


def foo(s):
    """
    Алгоритм: суммирование всех чисел в строке.

    Параметры:
        - s (str): строка.

    Сложность: O(N).
    """
    val = 0
    for c in s:
        if c.isdigit():
            val += int(c)
    return val



# Задание task_03_02_04.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241


def foo(n):
    """
    Алгоритм: поиск простых чисел от 1 до n включительно.

    Параметры:
        - n (int): число.

    Сложность: O(N^2).
    """
    res = []
    for i in range(1, n + 1):
        divisors = 0
        j = 2
        while j < i and divisors == 0:
            if i % j == 0:
                divisors += 1
            j += 1

        if divisors == 0:
            res.append(i)

    return res



# Задание task_03_02_05.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241


def foo(nums):
    """
    Алгоритм: проверка на наличие четного числа в списке.

    Параметры:
        - nums (list): список.

    Сложность: O(N).
    """
    for x in nums:
        if x % 2 == 0:
            return True
    else:
        return False



# Задание task_03_02_06.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241


def foo(nums):
    """
    Алгоритм: сложение первого элемента списка с квадратом последнего элемента.

    Параметры:
        - nums (list): список.

    Сложность: O(1).
    """
    return (nums[0] + nums[-1] ** 2)



# Задание task_03_02_07.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241


def foo(low, high):
    """
    Алгоритм: реализация бинарного поиска для угадывания числа в диапазоне [low, high].

    Параметры:
        - low (int): нижняя граница;
        - high (int): верхняя граница.

    Сложность: O(log(N)).
    """
    guessing = True
    while guessing:
        guess = (low + high) // 2
        print("Загаданное число {0}?".format(guess))
        pointer = input(
            "Введите '+', если Ваше число меньше.\n"
            "Введите '-' если Ваше число больше.\n"
            "Введите '=', если я угадал.\n").lower()
        if pointer == "+":
            high = guess
        elif pointer == "-":
            low = guess
        elif pointer == "=":
            guessing = False
        else:
            print("Введите '+', '-' или '='.")

    return guess


# ЗАКОММЕНТИРУЙТЕ этот код перед запуском проверки
low, high = 0, 100
print("Пожалуйста, загадайте число от {0} до {1}!".format(low, high))
guess = foo(low, high)
print("Игра окончена, Вы загадали число: {0}.".format(guess))



# Задание task_03_02_08.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241


import random
import time


def timeit(func, *args, **kw):
    """Выполнить функицю 'func' с параметрами '*args', '**kw' и
    вернуть время выполнения в мс."""

    time_start = time.time()
    res = func(*args, **kw)
    time_end = time.time()

    return (time_end - time_start) * 1000.0, res


def maxmin1(data):
    """Вернуть минимум и максимум из 'data'.

    Алгоритм:
        Последовательный перебор всего массива.

    Сложность: 
        O(N).

    Параметры:
        - data (list of int): список целых чисел.

    Результат:
        tuple: мин. и макс. значения."""

    if not data:
        return (None, None)
    
    min_val = max_val = data[0]
    for num in data[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return (min_val, max_val)


def maxmin2(data):
    """Вернуть минимум и максимум из 'data'.

    Алгоритм:
        Сортировка списка, и возврат первого и последнего элементов.

    Сложность: 
        O(N log(N)).

    Параметры:
        - data (list of int): список целых чисел.

    Результат:
        tuple: мин. и макс. значения."""

    if not data:
        return (None, None)
    
    sorted_data = sorted(data)
    return (sorted_data[0], sorted_data[-1])


def maxmin3(data):
    """Вернуть минимум и максимум из 'data'.

    Алгоритм:
        Используя встроенные функции min() и max().

    Сложность: 
        O(N).

    Параметры:
        - data (list of int): список целых чисел.

    Результат:
        tuple: мин. и макс. значения."""

    if not data:
        return (None, None)
    
    return (min(data), max(data))


if __name__ == "__main__":
    GEN_LIMIT = 1000000
    dataset = []
    for i in range(4, 7):
        dataset.append(random.sample(range(-GEN_LIMIT, GEN_LIMIT), 10**i))

    res = [["i", "1 способ (мс.)", "2 способ (мс.)", "3 способ (мс.)"]]
    for data in dataset:
        res.append([len(data),
                   timeit(maxmin1, data)[0],
                   timeit(maxmin2, data)[0],
                   timeit(maxmin3, data)[0]])

    # Вывод
    print("{:>15} {:>15} {:>15} {:>15}".format(*res[0]))
    for r in res[1:]:
        print("{:>15} {:>15.2f} {:>15.2f} {:>15.2f}".format(*r))

# -------------
# Пример вывода:
#
#              i  1 способ (мс.)  2 способ (мс.)  3 способ (мс.)
#          10000            1.00            5.00            0.00
#            ...



# Задание task_03_02_09.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241


import random
import time


def timeit(func, *args, **kw):
    """Выполнить функицю 'func' с параметрами '*args', '**kw' и
    вернуть время выполнения в мс."""

    time_start = time.time()
    res = func(*args, **kw)
    time_end = time.time()

    return (time_end - time_start) * 1000.0, res


def is_ok_to_pass_1(db, passport_id):
    """Вернуть отметку о допуске из 'db' для паспорта с номером 'passport_id'.

    Если паспорт не найден в базе данных, возвращается отказ в допуске.

    Алгоритм:
        Последовательный перебор списка.

    Сложность: 
        O(N).

    Параметры:
        - db (list of dict): база данных;
        - passport_id (str): номер паспорта.

    Результат:
        bool: отметка о допуске."""
    for entry in db:
        if entry['id'] == passport_id:
            return entry['ok']
    return False


def is_ok_to_pass_2(db_opt, passport_id):
    """Вернуть отметку о допуске из 'db_opt' для паспорта с номером 'passport_id'.

    Если паспорт не найден в базе данных, возвращается отказ в допуске.

    Алгоритм:
        Поиск в хэш-таблице (словаре).

    Сложность: 
        O(1).

    Параметры:
        - db_opt (dict): оптимизированная база данных для поиска;
        - passport_id (str): номер паспорта.

    Результат:
        bool: отметка о допуске."""
    return db_opt.get(passport_id, False)


def ok_str(flag):
    return "Да" if flag else "Нет"


if __name__ == "__main__":
    print("Загрузка базы данных... ")

    GEN_LIMIT = 1000000
    # База данных
    db = [{"id": "{:07d}".format(i), "ok": random.random() < 0.9}
          for i in random.sample(range(GEN_LIMIT, 10 * GEN_LIMIT), GEN_LIMIT)]

    # Структура db_opt должна быть оптимизированным хранилищем
    db_opt = {entry['id']: entry['ok'] for entry in db}

    print("Загружено записей: {:,}.\n\nПримеры:".format(GEN_LIMIT))
    print("Первый элемент:", db[0])
    print("Последний элемент:", db[-1])
    print("\n")

    passport_id = input("Введите номер паспорта (7 цифр): ").strip()

    output = """
                  1 способ   2 способ
    Допущен     {:>10s} {:>10s}
    Время (мс.) {:>10.2f} {:>10.2f}\
    """

    res1 = timeit(is_ok_to_pass_1, db, passport_id)
    res2 = timeit(is_ok_to_pass_2, db_opt, passport_id)

    print(output.format(ok_str(res1[1]),
                        ok_str(res2[1]),
                        res1[0],
                        res2[0]))

# -------------
# Пример вывода:
#
# Загрузка базы данных...
# Загружено записей: 1,000,000.
#
# Примеры:
# Первый элемент: {'ok': True, 'id': '4998753'}
# Последний элемент: {'ok': True, 'id': '6280964'}
#
#
# Введите номер паспорта (7 цифр): 6280964
#
#               1 способ   2 способ
# Допущен             Да         Да
# Время (мс.)     145.10       0.00



# Задание task_03_02_10.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241


import random
import time


def timeit(func, *args, **kw):
    """Выполнить функицю 'func' с параметрами '*args', '**kw' и
    вернуть время выполнения в мс."""

    time_start = time.time()
    res = func(*args, **kw)
    time_end = time.time()

    return (time_end - time_start) * 1000.0, res


def top3_1(db):
    """Вернуть список из ТОП-3 клиентов по сумме активов.

    Алгоритм:
        Сортировка (встроенный метод sort()) и возврат 3-х элементов.

    Сложность: 
        O(N log(N)).

    Параметры:
        - db (list of dict): список клиентов.

    Результат:
        tuple of dict: 3 клиента с максимальной суммой активов."""
    sorted_db = sorted(db, key=lambda x: x['assets'], reverse=True)
    return tuple(sorted_db[:3])


def top3_2(db):
    """Вернуть список из ТОП-3 клиентов по сумме активов.

    Алгоритм:
        Прямой перебор (1 проход в цикле).

    Сложность: 
        O(N).

    Параметры:
        - db (list of dict): список клиентов.

    Результат:
        tuple of dict: 3 клиента с максимальной суммой активов."""
    top = [{'client_id': 0, 'assets': -1}, 
           {'client_id': 0, 'assets': -1}, 
           {'client_id': 0, 'assets': -1}]
    
    for client in db:
        if client['assets'] > top[0]['assets']:
            top[2] = top[1]
            top[1] = top[0]
            top[0] = client
        elif client['assets'] > top[1]['assets']:
            top[2] = top[1]
            top[1] = client
        elif client['assets'] > top[2]['assets']:
            top[2] = client
    
    return tuple(top)


if __name__ == "__main__":
    print("Загрузка базы данных... ")

    GEN_LIMIT = 10000000
    # Список клиентов
    db = []
    for client_id, assets in enumerate(
      random.sample(range(0, 10 * GEN_LIMIT), GEN_LIMIT),
      start=1):
        db.append(dict(client_id=client_id, assets=assets))

    print("Загружено записей: {:,}.\n\nПримеры:".format(GEN_LIMIT))
    print("Первый элемент:", db[0])
    print("Последний элемент:", db[-1])
    print("\n")

    res1 = timeit(top3_1, db)
    res2 = timeit(top3_2, db)

    for i, (func_time, res) in enumerate((res1, res2), start=1):
        print("Способ №{}".format(i))
        print("Время: {:.2f} мс.".format(func_time))
        for j, client in enumerate(res, start=1):
            print("{}-е место: ID={client_id} Активы={assets:,} руб.".
                  format(j, **client))
        print()


# -------------
# Пример вывода:
#
# Загрузка базы данных...
# Загружено записей: 10,000,000.
#
# Примеры:
# Первый элемент: {'client_id': 1, 'assets': 79149360}
# Последний элемент: {'client_id': 10000000, 'assets': 92745004}
#
#
# Способ №1
# Время: 16779.14 мс.
# 1-е место: ID=1346588 Активы=99,999,995 руб.
# 2-е место: ID=9924557 Активы=99,999,979 руб.
# 3-е место: ID=2904705 Активы=99,999,967 руб.
#
# Способ №2
# Время: 4364.90 мс.
# 1-е место: ID=1346588 Активы=99,999,995 руб.
# 2-е место: ID=9924557 Активы=99,999,979 руб.
# 3-е место: ID=2904705 Активы=99,999,967 руб.
