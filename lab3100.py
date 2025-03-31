# Задание task_03_01_01.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def sgn(x):
    """Вернуть результат сигнум-функции.

    Параметры:
        - x (float): аргумент x.

    Результат:
        float: значение функции.
    """
    if x < 0:
        return -1
    elif x == 0:
        return 0
    elif x > 0: 
        return 1

def calculate_z(x, y): 
  ch = sgn(x) + y**2
  zn = sgn(y) - (abs(x)**(1/2))
  z = round(ch / zn, 2)
  return z

x = float(input('Введите x: '))
y = float(input('Введите y: '))

print("Ответ:", calculate_z(x, y))

# --------------
# Пример вывода:
#
# Введите x: -9
# Введите y: 0
# Ответ: 0.33



# Задание task_03_01_02.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def avg(data):
    """Вернуть среднее значение 'data'.

    Параметры:
        - data: список целых чисел (температур).

    Результат:
        Среднее значение температуры.
    """
    return sum(data) / len(data)


def cleared_data(data):
    """Вернуть список без значений None.

    Параметры:
        - data: список, содержащий целые числа и/или None.

    Результат:
        Список без значений None.
    """
    return [x for x in data if x is not None]


n = int(input("Кол-во измерений: "))

# Если с клавиатуры вводится прочерк, измерения нет
# (необходимо добавить в список None)
data = []
for i in range(n):
    measure = input(f"Измерение {i+1}-е: ")
    if measure == '-':
        data.append(None)
    else:
        data.append(int(measure))

# Получить очищенный список и среднее значение
cleaned_data = cleared_data(data)
average_temp = avg(cleaned_data)

print(f"Средняя температура: {average_temp:.2f}")

# --------------
# Пример вывода:
#
# Кол-во измерений: 3
# Измерение 1-е: 10
# Измерение 2-е: -
# Измерение 3-е: 20
# Средняя температура: 15.00



# Задание task_03_01_03.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def is_lucky(num):
    """Является ли 'num' номером счастливого билета?

    Параметры:
        - num (int): Номер билета.

    Результат:
        bool: True - да, False - нет.
    """
    even_count = 0
    odd_count = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count == odd_count


def lucky_numbers(a, b):
    """Вернуть список счастливых номеров от 'a' до 'b'.

    Параметры:
        - a (int): Начальный номер билета.
        - b (int): Конечный номер билета.

    Результат:
        list: Список счастливых номеров.
    """
    lucky_nums = []
    for num in range(a, b + 1):
        if is_lucky(num):
            lucky_nums.append(num)
    return lucky_nums


a = int(input('Первый номер билета: '))
b = int(input('Последний номер билета: '))

# Вывод должен быть осуществлен в строку с одним пробелом-разделителем
lucky_nums = lucky_numbers(a, b)
print(" ".join(map(str, lucky_nums)))

# --------------
# Пример вывода:
#
# Первый номер билета: 10
# Последний номер билета: 25
# 10 12 14 16 18 21 23 25



# Задание task_03_01_04.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def is_leap(year):
    """Является ли 'year' високосным годом?

    Параметры:
        - year (int): Год.

    Результат:
        bool: True - да, False - нет.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days(month, year):
    """Вернуть количество дней в месяце 'month' года 'year'.

    Параметры:
        - month (int): Месяц.
        - year (int): Год.

    Результат:
        int: Количество дней в месяце.
    """
    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def previous_date(day, month, year):
    """Вернуть день, месяц, год предыдущего дня.

    Параметры:
        - day (int): День.
        - month (int): Месяц.
        - year (int): Год.

    Результат:
        (day, month, year) предыдущего дня.
    """
    if day > 1:
        return day - 1, month, year
    else:
        if month == 1:
            return 31, 12, year - 1
        else:
            prev_month = month - 1
            prev_days = days(prev_month, year)
            return prev_days, prev_month, year



def next_date(day, month, year):
    """Вернуть день, месяц, год следующего дня.

    Параметры:
        - day (int): День.
        - month (int): Месяц.
        - year (int): Год.

    Результат:
        (day, month, year) следующего дня.
    """
    days_in_month = days(month, year)
    if day < days_in_month:
        return day + 1, month, year
    else:
        if month == 12:
            return 1, 1, year + 1
        else:
            return 1, month + 1, year


day, month, year = map(int, input("День, месяц, год через пробел: ").split())

prev_day, prev_month, prev_year = previous_date(day, month, year)
next_day, next_month, next_year = next_date(day, month, year)

print(f"Предыдущий день: {prev_day:02d}/{prev_month:02d}/{prev_year}")
print(f"Следующий день: {next_day:02d}/{next_month:02d}/{next_year}")

# --------------
# Пример вывода:
#
# День, месяц, год через пробел: 1 3 2000
# Предыдущий день: 29/02/2000
# Следующий день: 02/03/2000



# Задание task_03_01_05.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def is_leap(year):
    """Является ли 'year' високосным годом?

    Параметры:
        year (int): Год.

    Результат:
        bool: True - да, False - нет.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days(month, year):
    """Вернуть количество дней в месяце 'month' года 'year'.

    Параметры:
        - month (int): Месяц.
        - year (int): Год.

    Результат:
        int: Количество дней в месяце.
    """
    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def another_date(day, month, year, delta=1):
    """Вернуть день, месяц, год, отличающийся на 'delta' дней.

    Параметры:
        - day (int): День.
        - month (int): Месяц.
        - year (int): Год.
        - delta (int): Количество дней для добавления (положительное) или вычитания (отрицательное).

    Результат:
        (day, month, year) новой даты.
    """

    def previous_date(day, month, year):
        """Вернуть день, месяц, год предыдущего дня.

        Параметры:
            - day (int): День.
            - month (int): Месяц.
            - year (int): Год.

        Результат:
            (day, month, year) предыдущего дня.
        """
        if day > 1:
            return day - 1, month, year
        else:
            if month == 1:
                return 31, 12, year - 1
            else:
                prev_month = month - 1
                prev_days = days(prev_month, year)
                return prev_days, prev_month, year


    def next_date(day, month, year):
        """Вернуть день, месяц, год следующего дня.

        Параметры:
            - day (int): День.
            - month (int): Месяц.
            - year (int): Год.

        Результат:
            (day, month, year) следующего дня.
        """
        days_in_month = days(month, year)
        if day < days_in_month:
            return day + 1, month, year
        else:
            if month == 12:
                return 1, 1, year + 1
            else:
                return 1, month + 1, year


    current_day, current_month, current_year = day, month, year

    if delta > 0:
        for _ in range(delta):
            current_day, current_month, current_year = next_date(current_day, current_month, current_year)
    elif delta < 0:
        for _ in range(abs(delta)):
            current_day, current_month, current_year = previous_date(current_day, current_month, current_year)

    return current_day, current_month, current_year

day, month, year = map(int, input("День, месяц, год через пробел: ").split())
delta = int(input("Сдвиг (может быть отрицательным): "))

new_day, new_month, new_year = another_date(day, month, year, delta)
print(f"Новый день: {new_day:02d}/{new_month:02d}/{new_year}")

# --------------
# Пример вывода:
#
# День, месяц, год через пробел: 1 1 2000
# Свдиг (может быть отрицательным): -2
# Новый день: 30/12/1999
#
# День, месяц, год через пробел: 1 1 2000
# Свдиг (может быть отрицательным): 2
# Новый день: 03/01/2000



# Задание task_03_01_06.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def gcd(first, second):
    """Вернуть НОД целых чисел 'first' и 'second'."""
    while second:
        first, second = second, first % second
    return abs(first)


def lcm(first, second):
    """Вернуть НОК целых чисел 'first' и 'second'."""
    return abs(first * second) // gcd(first, second)


def gcd_nums(nums):
    """Вернуть НОД чисел из списка 'nums'.

    Параметры:
        !!!.

    Результат:
        !!!.
    """
    if not nums:
        return 0
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
        if result == 1:
            break
    return result


def lcm_nums(nums):
    """Вернуть НОК чисел из списка 'nums'.

    Параметры:
        !!!.

    Результат:
        !!!.
    """
    if not nums:
        return 0
    result = nums[0]
    for num in nums[1:]:
        result = lcm(result, num)
    return result


nums = list(map(int, input("Введите числа через пробел: ").split()))

print(f"НОД = {gcd_nums(nums)}")
print(f"НОК = {lcm_nums(nums)}")

# --------------
# Пример вывода:
#
# Введите числа через пробел: 8 10 14
# НОД = 2
# НОК = 280
#
# Введите числа через пробел: 6 8 24 16
# НОД = 2
# НОК = 48



# Задание task_03_01_07.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def has_digits(sentence):
    """Проверяет, содержит ли предложение хотя бы одну цифру."""
    for char in sentence:
        if char.isdigit():
            return True
    return False


def sentences_with_digits_count(sentences):
    """Подсчитывает количество предложений, содержащих хотя бы одну цифру."""
    count = 0
    for sentence in sentences:
        if has_digits(sentence):
            count += 1
    return count


n = int(input("Введите количество предложений: "))

sentences = []
for i in range(n):
    sentence = input(f"Введите предложение №{i + 1}:\n")
    sentences.append(sentence)

count = sentences_with_digits_count(sentences)
print(f"Предложений с цифрой = {count}")

# --------------
# Пример вывода:
#
# Введите количество предложений: 3
# Введите предложение №1:
# Просто текст
# Введите предложение №2:
# Текст с цифрой 1 (один)
# Введите предложение №3:
# Тут нет цифры
# Предложений с цифрой = 1



# Задание task_03_01_08.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def print_with_border(string, char):
    """Функция, которая рисует рамку вокруг строки с использованием заданного символа."""
    border = char * (len(string) + 2)  # Верхняя и нижняя границы рамки
    bordered_text = f"{char}{string}{char}"  # По бокам
    print(border)
    print(bordered_text)
    print(border)


s = input('Введите строку: ')
k = input('Введите символ: ')
print_with_border(s, k)

# --------------
# Пример вывода:
#
# Введите строку: Просто текст
# Введите символ: +
# ++++++++++++++
# +Просто текст+
# ++++++++++++++



# Задание task_03_01_09.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

LETTERS_EX = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
DIGITS_EX = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def to_base(number, base):
    """Преобразовать десятичное число 'number' в с.с. 'base'.

    Параметры:
        number (int): десятичное число;
        base (int): система счисления.

    Результат:
        str: число в с.с. 'base'."""
    if number == 0:
        return "0"
    
    result = ""
    while number > 0:
        remainder = number % base
        if remainder >= 10:
            result = LETTERS_EX[remainder] + result
        else:
            result = str(remainder) + result
        number = number // base
    return result


def from_base(number, base):
    """!!!

    Результат:
        int: число в 10-й с.с."""
    result = 0
    for i, digit in enumerate(reversed(number.str())):
        if digit.isalpha():
            digit_value = DIGITS_EX[digit.upper()]
        else:
            digit_value = int(digit)
        result += digit_value * (base ** i)
    return result

base = int(input())
number = int(input())
a = from_base(number, base)
b = to_base(number, base)
print(a)
print(b)
# print(to_base(255, 16))
# print(from_base("FF", 16))

# --------------
# Пример вывода:
#
# Нет



# Задание task_03_01_10.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def sentence_stats(sentence):
    """Вернуть символьную статистику 'sentence'. Регистр не учитывается."""
    stats = {}
    for char in sentence.lower():
        if char in stats:
            stats[char] += 1
        else:
            stats[char] = 1
    return stats


s = input("Введите предложение: ")

result = sentence_stats(s)
print(result)

# --------------
# Пример вывода:
#
# Введите предложение: мама МЫла РамУ
# {'л': 1, 'р': 1, 'у': 1, 'м': 4, 'а': 4, 'ы': 1, ' ': 2}



# Задание task_03_01_11.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def ceasar(text, shift):
    """Вернуть измененную строку 'text' со сдвигом 'shift'.

    Параметры:
        - text (str): строка;
        - shift (int): свдиг.

    Результат:
        str: измененная строка."""
    # Набор кириллических букв
    letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    letters_upper = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
    
    result = []
    
    for char in text:
        if char in letters:
            # Для строчных букв
            index = letters.index(char)
            new_index = (index + shift) % len(letters)
            result.append(letters[new_index])
        elif char in letters_upper:
            # Для заглавных букв
            index = letters_upper.index(char)
            new_index = (index + shift) % len(letters_upper)
            result.append(letters_upper[new_index])
        else:
            # Оставляем символы, не являющиеся буквами, без изменений
            result.append(char)
    return ''.join(result)


text = input("Введите предложение: ")
shift = int(input("Введите сдвиг: "))

encoded = ceasar(text, shift)
decoded = ceasar(encoded, -shift)
print("Зашифрованная строка:", encoded)
print("Расшифрованная строка:", decoded)

# --------------
# Пример вывода:
#
# Введите предложение: ПрограММиРОВание С++
# Введите сдвиг: 4
# Зашифрованная строка: УфтзфдРРмФТЖдсмй Х++
# Расшифрованная строка: ПрограММиРОВание С++



# Задание task_03_01_12.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

# В данной задаче ввод с клавиатуры не нужен.
#
# Используйте пример данных ниже, при необходимости измените его для
# проверки правильности решения

data = [
    {1: 'м', 2: 'м', 3: 'м', 4: 'ж'},
    {1: 'ж', 2: 'м', 3: 'ж', 4: 'ж'},
    {1: 'ж', 2: 'ж', 3: 'ж', 4: 'ж'},
    {1: 'м', 2: 'м', 3: 'м', 4: 'м'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: None, 3: None, 4: 'ж'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: 'м', 3: None, 4: 'м'},
    {1: 'ж', 2: None, 3: None, 4: 'ж'}
]


def vacant_compartments(data):

    return [
        i + 1 for i, compartment in enumerate(data)
        if all(v is None for v in compartment.values())
    ]

def vacant_seats(data, compartments_condition=None, seat_condition=None):

    result = []
    for comp_num, compartment in enumerate(data, 1):

        if compartments_condition and not compartments_condition(compartment):
            continue

        for seat, value in compartment.items():
            if value is None:
                if seat_condition is None or seat_condition(seat, value):
                    result.append((comp_num, seat))
    return result

def is_same_sex_and_vacant(compartment, sex):

    occupied = [v for v in compartment.values() if v is not None]
    has_vacant = any(v is None for v in compartment.values())
    return len(occupied) > 0 and all(g == sex for g in occupied) and has_vacant

# Результаты
print(vacant_compartments(data))
print(vacant_seats(data))
print(vacant_seats(data, seat_condition=lambda s, _: s % 2 == 1))
print(vacant_seats(data, seat_condition=lambda s, _: s % 2 == 0))
print(vacant_seats(data, lambda c: is_same_sex_and_vacant(c, "м")))
print(vacant_seats(data, lambda c: is_same_sex_and_vacant(c, "ж")))


# --------------
# Пример вывода:
#
# [5, 7]
# [(5, 1), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3),
#  (7, 4), (8, 3), (9, 2), (9, 3)]
# [(5, 1), (5, 3), (6, 3), (7, 1), (7, 3), (8, 3), (9, 3)]
# [(5, 2), (5, 4), (6, 2), (7, 2), (7, 4), (9, 2)]
# [(8, 3)]
# [(9, 2), (9, 3)]



# Задание task_03_01_13.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

# В данной задаче ввод с клавиатуры не нужен.
#
# Используйте значения 'votes', при необходимости измените его для
# проверки правильности решения

votes = [
    2, 3, -1, 2, 5, 1, 1, 4, 1, 1, 1, 3, 1, 3, 5, -1, 5, 2, 5, 5,
    3, 3, 2, 3, 3, 2, 2, 1, 3, 2, 5, 2, 2, 4, 1, 1, 3, 2, 2, 3, 3,
    3, 1, 4, 2, 1, 4, 2, 3, 3, 3, -1, 5, 3, 1, 4, 5, 1, 1, 3, 3,
    3, -1, 5, 3, 3, 2, 5, 1, 1, 5, -1, 1, 2, 2, 3, -1, 4, 2, 5, 4,
    2, -1, 3, 1, 4, 3, 5, 4, 1, 5, 3, 2, 4, 2, 1, 3, 4, 1, 1, 3, 4
]

parties = {
    1: "Партия №1", 2: "Партия №2", 3: "Партия №3",
    4: "Партия №4", 5: "Партия №5", -1: "Испорчено"
}


def parties_votes(parties, votes):
    """Вернуть информацию о голосах 'votes', отданных за партии 'parties'.
    Испорченные бланки также присутствуют в результате.

    Параметры:
        - parties (dict): информация о партиях (номер голоса: название);
        - votes (list): номера голосов.

    Результат:
        dict: название: кол-во отданных голосов."""
    vote_count = {party: 0 for party in parties.values()}
    for vote in votes:
        vote_count[parties[vote]] += 1
    return vote_count


def print_results(votes_for_p):
    """Вывести результаты голосования в формате:

    1. Партия №2 | 1111 | 58.21%
    2. Партия №4 |  999 | 38.14%

    Параметры:
        - votes_for_p (dict): результат функции parties_votes().
    """
    total_votes = sum(votes_for_p.values())
    sorted_votes = sorted(votes_for_p.items(), key=lambda x: x[1], reverse=True)
    for i, (party, count) in enumerate(sorted_votes, 1):
        percentage = (count / total_votes) * 100
        print(f"{i}. {party} | {count:2} | {percentage:.2f}%")


print_results(parties_votes(parties, votes))

# --------------
# Пример вывода:
#
# 1. Партия №3 | 27 | 26.47%
# 2. Партия №1 | 22 | 21.57%
# 3. Партия №2 | 20 | 19.61%
# 4. Партия №5 | 14 | 13.73%
# 5. Партия №4 | 12 | 11.76%
# 6. Испорчено |  7 |  6.86%



# Задание task_03_01_14.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def split_numbers(*args):
    """Вернуть 2 списка - отрицательных и неотицательных значений.

    Аргументы:
        *args: произвольное количество числовых аргументов.

    Результат:
        - list: отрицательные значения;
        - list: неотицательные значения."""
    negative_numbers = [x for x in args if x < 0]
    non_negative_numbers = [x for x in args if x >= 0]
    
    negative_numbers.sort(reverse=True)
    
    non_negative_numbers.sort()
    
    return (negative_numbers, non_negative_numbers)


print(split_numbers(1, 4, -5, 0, -33))

# --------------
# Пример вывода:
#
# ([-5, -33], [0, 1, 4])



# Задание task_03_01_15.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def gdp(c, i, g, ex, im):
    """Вернуть значение ВВП.

    Параметры:
        - c: конечное потребление
        - i: валовое накопление капитала
        - g: государственные расходы
        - ex: экспорт
        - im: импорт

    Результат:
        - значение ВВП
    """
    return c + i + g + ex - im


c = int(input("Конечное потребление: "))
i = int(input("Валовое накопление капитала: "))
g = int(input("Государственные расходы: "))
ex = int(input("Экспорт: "))
im = int(input("Импорт: "))

info_dict = {'c': c, 'i': i, 'g': g, 'ex': ex, 'im': im}
info_list = [c, i, g, ex, im]

gdp_from_list = gdp(*info_list)
gdp_from_dict = gdp(**info_dict)

print(f"ВВП = {gdp_from_list}")
print(f"ВВП = {gdp_from_dict}")

# --------------
# Пример вывода:
#
# Конечное потребление: 100
# Валовое накопление капитала: 200
# Государственные расходы: 300
# Экспорт: 400
# Импорт: 500
# ВВП = 500
# ВВП = 500



# Задание task_03_01_16.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def pow1(value, power):
    """Вернуть 'value' в степени 'power'.

    Параметры:
        - value: число, которое нужно возвести в степень (int или float).
        - power: степень, в которую нужно возвести число (неотрицательное целое число).

    Результат:
        - value ** power.
    """
    result = 1
    for _ in range(power):
        result *= value
    return result


def pow2(value, power):
    """Вернуть 'value' в степени 'power'. Рекурсивный алгоритм.

    Параметры:
        - value: число, которое нужно возвести в степень (int или float).
        - power: степень, в которую нужно возвести число (неотрицательное целое число).

    Результат:
        - value ** power.
    """
    if power == 0:
        return 1
    else:
        return value * pow2(value, power - 1)


print(pow1(5, 3))
print(pow2(5, 3))

# --------------
# Пример вывода:
#
# 125
# 125



# Задание task_03_01_17.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241

def digits_sum(value):
    """Вернуть сумму цифр числа 'value'. Рекурсивная реализация.

    Параметры:
        - value (int): Натуральное число, для которого вычисляется сумма цифр.

    Результат:
        - int: Сумма цифр числа 'value'.
    """
    if value == 0:
        return 0
    return (value % 10) + digits_sum(value // 10)


def digits_count(value):
    """Вернуть количество цифр числа 'value'. Рекурсивная реализация.

    Параметры:
        - value (int): Натуральное число, для которого вычисляется количество цифр.

    Результат:
        - int: Количество цифр числа 'value'.
    """
    if value == 0:
        return 0
    return 1 + digits_count(value // 10)


print(digits_sum(12345))
print(digits_count(12345))

# --------------
# Пример вывода:
#
# 15
# 5
