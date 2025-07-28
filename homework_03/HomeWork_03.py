# Задание 1: Конвертер регистров
# Написать функцию, которая будет переводить snake_case в PascalCase и наоборот.
#
# Функция должна сама определять - какой формат ей передали. Можно добавить ключевой аргумент, который будет принудительно возвращать один из форматов.
#
#
# Примеры:
#
# otus_course     -> OtusCourse
# PythonIsTheBest -> python_is_the_best

def convert_case(text):

        if text[0].islower():
            return ''.join(word.capitalize() for word in text.split('_'))
        elif text[0].isupper():

            text = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
            return re.sub('([a-z0-9])([A-Z])', r'\1_\2', text).lower()

import re
while True:

    strings = input('Введите строку:')
    if strings == '':
        print('Введите строку ещё раз ')
    else:
        break


pascal_snake_string = convert_case(strings)
print(f"Исходная строка: {strings}, в  : {pascal_snake_string}")

# Задание 2: Проверка валидности даты
# Написать функцию проверяющую валидность введенной даты.
#
#
# Примеры:
#
# 29.02.2000 -> True
# 29.02.2001 -> False
# 31.04.1962 -> False

from datetime import datetime

def valid_date(date_string, format="%d.%m.%Y"):

    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False

in_data = input('Введите дату формата "День.Месяц.Год": ')

print(valid_date(in_data))

# Задание 3:
# Функция проверки на простое число. Простые числа – это такие числа, которые делятся на себя и на единицу.
#
#
# Примеры:
#
# 17 -> True
# 20 -> False
# 23 -> True

def just_number(n):

    if n <= 1:
        return False

    for i in range(2, int((n ** (1/2) + 1))):

        if n % i == 0:
            return False

    return True

number = int(input('Введите число: '))

print(just_number(number))

# Задание 4: Учет пользователей
# Пользователь в бесконечном цикле вводит данные пользователей: имя, затем фамилию, возраст и ID. Ввод продолжается
# до тех пор, пока не будет введено пустое поле.
#
# Пользователи заносятся в словарь, где ключ это ID пользователя, а остальные данные записываются в виде кортежа.
#
# Программа должна проверять:
#
# имя и фамилия состоят только из символов и начинаются с большой буквы - если не с большой, то заменяет букву на большую;
# возраст должен быть числом от 18 до 60;
# ID - целое число, дополненное до 8 знаков незначащими нулями, ID должен быть уникальным.
# Дополнительно: написать функцию, которая будет выводить полученный словарь в виде таблицы.

def create_user():
    users = {}
    unic_id = set()
    while True:
        info_user = ( )

        first_name = (input(f"Введите Имя пользователя (или 'Enter' для завершения): "))
        if first_name == '':
            break

        if first_name.isalpha():
            info_user += (first_name.title(),)

        else:
            print('Введите буквы')
            continue
        while True:
            last_name = (input(f"Введите Фамилию пользователя: "))
            if last_name.isalpha():
                info_user += (last_name.title(),)
                break
            else:
                print('Введите буквы')


        while True:
            try:
                age = int(input("Введите возраст (от 18 до 60): "))
                if 18 <= age <= 60:
                    info_user += (age,)
                    break
                else:
                    print("Возраст должен быть от 18 до 60. Попробуйте еще раз.")
            except ValueError:
                print("Ошибка: Введите число.")

        while True:
            try:
                id_user = (input("Введите уникальный № ID пользователя (целое число) : "))
                id_user = (id_user.zfill(8))

                if id_user not in unic_id:
                    users[id_user] = {}
                    users[id_user] = info_user
                    unic_id.add(id_user)
                    break
                else:
                    print("ID должен быть от уникальным. Введите другой ID !")
            except ValueError:
                print("Ошибка: Введите число.")

    return users


def print_dict_as_table(data, headers = ['ID', '       Name','Last_name','Age']):

    if not data:
        print("Словарь пуст.")
        return

    if headers is None:
        headers = list(data.keys())

    column_widths = [len(str(header)) for header in headers]
    for value in data.values():
        if isinstance(value, dict):
            for key, val in value.items():
                column_widths[0] = max(column_widths[0], len(str(key)))
                column_widths[1] = max(column_widths[1], len(str(val)))
        else:
            column_widths[1] = max(column_widths[1], len(str(value)))


    print(" ".join(headers[i].ljust(column_widths[i]) for i in range(len(headers))))
    print("-" * sum(column_widths) + "-" * (len(headers) - 1))


    for key, value in data.items():
        if isinstance(value, dict):
            for inner_key, inner_value in value.items():
                print(f"{str(inner_key).ljust(column_widths[0])} {str(inner_value).ljust(column_widths[1])}")
        else:
            print(f"{str(key).ljust(column_widths[0])} {str(value).ljust(column_widths[1])}")


a = create_user()

print(a)

print_dict_as_table(a)

