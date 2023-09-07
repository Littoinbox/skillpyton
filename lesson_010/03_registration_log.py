# -*- coding: utf-8 -*-
import os
import re


# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def checkName(name):
    pattern = r'[\d]'
    match = re.search(pattern, name)
    return not bool(match)


def checkEmail(email):
    pattern = r'[@]'
    pattern2 = r'[\.]'
    dog = re.search(pattern, email)
    coma = re.search(pattern2, email)
    return bool(dog) and bool(coma)


def writeToFile(file, string):
    try:
        file.write(string)
    except IOError as error:
        print(f'Не могу записать в файл{file} строку {string}')


goodfile = open('registrations_good.log', 'w')
badfile = open('registrations_bad.log', 'w')
filename = "registrations.txt"
with open(os.path.join(os.path.dirname(__file__), filename), 'r', encoding='utf8') as file:
    for line in file:
        try:
            map = line.split(' ')

            if len(map) != 3:
                raise ValueError("НЕ присутсвуют все три поля")
            if not checkName(map[0]):
                raise NotNameError("поле имени содержит НЕ только буквы")
            if not checkEmail(map[1]):
                raise NotEmailError("поле емейл НЕ содержит @ и .(точку)")
            if int(map[2]) < 10 or int(map[2]) > 99 or type(int(map[2])) != int:
                raise ValueError("поле возраст НЕ является числом от 10 до 99")
            writeToFile(goodfile, line )
        except (ValueError, NotNameError, NotEmailError) as e:
            writeToFile(badfile, line+" "+ e.__class__.__name__+"\n")

goodfile.close()
badfile.close()
