
# Задание task_02_18.
#
# Выполнил: Гловели Д. К.
# Группа: ЦИБ-241



sentence = input('Введите предложение: ')
sentence = sentence.lower()

count_gl = 0  # Кол-во гласных
count_sogl = 0  # Кол-во согласных
gl = 'уеыаоэяию'
sogl = 'йцкнгшщзхфвпрлджчсмтбъь'

for i in sentence:
    if i in gl:
        count_gl += 1
    elif i in sogl:
        count_sogl += 1
    elif i in ' ':
        continue
print(f'Кол-во букв в предложении: гласных - {count_gl}, согласных - {count_sogl}')



# --------------
# Пример вывода:
#
# Введите предложение: Программирование
# Кол-во букв в предложении: гласных - 7, согласных - 9
