"""
Для проверок:
единственно-верный путь по локациям 0-2-5-9-11-B2
При этом в конце остаётся 0.0000000001 времени
"""

import json
import datetime
import re
from decimal import Decimal, getcontext
import csv

with open('rpg.json', 'r') as read_file:                    # загружаем файл с "картой"
    loaded_json_file = json.load(read_file)

getcontext().prec = 50

time_pattern = r'_[time]{2,4}'                              # пишем паттерны для реджекса
exp_pattern = r'_exp.{1,}_'


def exp_up(mob):                                            # функции для получения опыта и уменьшения времени
    return int(mob[re.search(exp_pattern, mob).start() + 4: re.search(exp_pattern, mob).end()-1])


def time_down(mob):
    return Decimal(str(mob[re.search(time_pattern, mob).end():]))


# Задаем начальные параметры
remaining_time = Decimal('123456.0987654321')
all_time = datetime.timedelta(seconds=1234567890.0987654321)
journal = []
field_names = ['current_location', 'current_experience', 'current_date']
experience = 0
locations = loaded_json_file

game = True
while game:
    action = 0
    monsters = []
    outs = []
    current_position = list(locations.keys())[0]
    print(f'Вы находитесь в {current_position}')
    current_date = all_time - datetime.timedelta(seconds=float(remaining_time))
    journal.append({'current_location': current_position, 'current_experience': experience, 'current_date': current_date})
    print(f'У вас {experience} опыта и осталось {remaining_time} секунд')
    if experience >= 280 and remaining_time > 0:
        if 'Hatch' in current_position:
            print('Игра пройдена!')
            game = False
            break
        else:
            print('Нужно срочно найти выход из этой пещеры!')
    print(f'Прошло уже {current_date}')
    print(f'Внутри вы видите')
    for dungeon_object in locations[current_position]:
        if type(dungeon_object) is str:
            print(f'Монстра {dungeon_object}')
            monsters.append(dungeon_object)
        elif type(dungeon_object) is dict:
            print(f'Вход в локацию: {list(dungeon_object.keys())[0]}')
            outs.append([list(dungeon_object.keys())[0], locations[current_position].index(dungeon_object)])
        elif type(dungeon_object) is list:
            print(f'Группу монстров {dungeon_object}')
            monsters.extend(dungeon_object)
        else:
            print('Неопознанный объект')
            break
    while True:
        print(remaining_time)
        print('Выберите действие:')
        print('1.Атаковать монстра')
        print('2.Перейти в другую локацию')
        print('3.Выход')
        action = int(input())
        if action == 1:
            if len(monsters) == 0:
                print('Монстров в локации не осталось')
            else:
                print('Выберите монстра для атаки')
                for number, name in enumerate(monsters, start=1):
                    print(f'{number}.{name}')
                chosen_monster = int(input())
                if chosen_monster in range(1, len(monsters) + 1):
                    experience += exp_up(monsters[chosen_monster - 1])
                    remaining_time -= time_down(monsters[chosen_monster - 1])
                    print(f'Вы получили {exp_up(monsters[chosen_monster - 1])} опыта, '
                          f'но потеряли {time_down(monsters[chosen_monster - 1])} единиц времени')
                    if remaining_time <= 0:
                        game = False
                        print('Время вышло.')
                        break
                    monsters.remove(monsters[chosen_monster - 1])
                else:
                    print('Такого номера не было в списке')
        elif action == 2:
            if len(outs) == 0:
                print('Вы зашли в тупик.')
            else:
                print('Вы можете:')
                for num, loc in enumerate(outs, start=1):
                    print(f'{num}.Перейти в локацию {loc[0]} за {time_down(loc[0])} секунд')
                chosen_path = int(input(f'Введите число от 1 до {len(outs)}'))
                if chosen_path in range(1, len(outs) + 1):
                    locations = locations[current_position][outs[chosen_path - 1][1]]
                    remaining_time -= time_down(outs[chosen_path - 1][0])
                    print('Отправляемся в путь...')
                    if remaining_time <= 0:
                        game = False
                        print('Время вышло.')
                        break
                    print(f'Спустя {time_down(outs[chosen_path - 1][0])} секунд')
                    break
                else:
                    print('Такой локации в списке не было')
        elif action == 3:
            game = False
            break

field_names = ['current_location', 'current_experience', 'current_date']

with open('journal.csv', 'w', newline='') as out_csv:
    writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=field_names)
    writer.writeheader()
    writer.writerows(journal)