# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ
# Например
#
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
#

# TODO здесь ваш код
import string
from itertools import permutations, combinations
from pprint import pprint
from random import choice, randint

names = ('Степан Ярослав Михаил Артём Ольга Бузова Земфира Гнойный Муммий Тролль '
         'Мария Ольга Анна Геннадий Ван Ли Пенг Сянцзян Хенг Чонгкун Яочуан Ли '
         'Владимир Дмитрий Джамшут Равшан Волочкова Чехова Нагиев Джигурда'.split())

email_domains = ['@mail.ru', '@gmail.com', '@ya.ru'] * 42 + ['.mail.ru', '.ru', 'figvam', '']
pprint(email_domains)

with open('../../solutions/lesson_010/registrations.txt', 'w') as ff:
    for i in range(10000):
        name = choice(names)
        email = ''.join([choice(string.ascii_lowercase) for _ in range(randint(2, 10))]) + choice(email_domains)
        age = str(randint(7, 101))
        if randint(1, 30) == 1:
            bad_line = list(combinations([name, age, email], randint(1, 4)))
            print(bad_line)
            if bad_line:
                bad_line = choice(bad_line)
                print(bad_line)
            bad_line = ' '.join(bad_line)
            print(bad_line)
            ff.write(f'{bad_line}\n')
        else:
            if randint(1, 30) == 1:
                name += choice(['666', '42', '!!!!1'])
            ff.write(f'{name} {email} {age}\n')
