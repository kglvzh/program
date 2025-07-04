
# Задание task_03_03_09.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241



"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""


def f(x):
    """Вернуть значение функции.

    Функция не обрабатывает исключения.
    """
    return x**2 / (x + 2) - 3


k = int(input("Введите границу интервала [-k; k]: "))
h = float(input("Введите шаг табуляции: "))

x = -k
print("{:>10} {:>10}".format("x", "f(x)"))
while x <= k:
    # Если во время вычисления функции возникнет ошибка,
    # при выводе необходимо указать прочерк "-"
    # Данный случай должен обрабатывать второй вложенный блок try
    print("{:10.2f} {:10.2f}".format(x, f(x)))

    x += h

 
# --------------
# Пример вывода:
#
# Введите границу интервала [-k; k]: 5
# Введите шаг табуляции: 0.5
#          x       f(x)
#      -5.00     -11.33
#      -4.50     -11.10
#      -4.00     -11.00
#      -3.50     -11.17
#      -3.00     -12.00
#      -2.50     -15.50
#      -2.00          -
#      -1.50       1.50
#      -1.00      -2.00
#      -0.50      -2.83
#       0.00      -3.00
#       0.50      -2.90
#       1.00      -2.67
#       1.50      -2.36
#       2.00      -2.00
#       2.50      -1.61
#       3.00      -1.20
#       3.50      -0.77
#       4.00      -0.33
#       4.50       0.12
#       5.00       0.57


"""
Ошибки (номера строк через пробел, данная строка - №2): 12 13 18
"""



def f(x):
    """Вернуть значение функции."""
    try:
        return x**2 / (x + 2) - 3
    except ZeroDivisionError:
        raise
    except OverflowError:
        return float('inf')

try:
    k = int(input("Введите границу интервала [-k; k]: "))
    h = float(input("Введите шаг табуляции: "))
except ValueError:
    print("Ошибка: необходимо ввести числовое значение")
    exit()

x = -k
print("{:>10} {:>10}".format("x", "f(x)"))
while x <= k:
    try:
        y = f(x)
        print("{:10.2f} {:10.2f}".format(x, y))
    except ZeroDivisionError:
        print("{:10.2f} {:>10}".format(x, "-"))
    except:
        print("{:10.2f} {:>10}".format(x, "ошибка"))

    x += h