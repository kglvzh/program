# Задание task_01_04.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241


# Двузначное число
num2 = int(input())
# Трехзначное число
num3 = int(input())

# 1-я цифра числа 'num2'
num2_1 = num2 // 10
# 2-я цифра числа 'num2'
num2_2 = num2 % 10

# Сумма цифр числа 'num2'
num2_s = num2_1 + num2_2
# Произведение цифр числа 'num2'
num2_p = num2_1 * num2_2

# 1-я цифра числа 'num3'
num3_1 = num3 // 100
# 2-я цифра числа 'num3'
num3_2 = (num3//10)%10
# 3-я цифра числа 'num3'
num3_3 = num3 % 10 

# Сумма цифр числа 'num3'
num3_s = num3_1 + num3_2+num3_3
# Произведение цифр числа 'num3'
num3_p = num3_1 * num3_2 * num3_3

# Вывод результата
print('Двузначное число: ',num2)
print('Трехзначное число: ',num3)
print('Сумма и произведение цифр двузначного числа: ',num2_s,num2_p)
print('Сумма и произведение цифр двузначного числа: ',num3_s,num3_p)



# --------------
# Пример вывода:
#
# Двузначное число: 45
# Трехзначное число: 456
# Сумма и произведение цифр двузначного числа: 9 20
# Сумма и произведение цифр трехзначного числа: 15 120
