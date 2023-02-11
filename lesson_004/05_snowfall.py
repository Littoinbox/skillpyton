# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
width = 1200
height = 600
sd.resolution = (width, height)
snowflakes = {}
sd.background_color = sd.COLOR_BLACK


def new_snowflake():
    snowflake = {'start_x': random.randint(20, width),
                 'start_y': height,
                 'lenght': random.randint(10, 50),
                 'factor_b': random.randint(0, 1),
                 'factor_c': random.randint(30, 91)
                 }
    return snowflake


step, step_x = 0, 0
while True:
    step += 1
    snow_len = len(snowflakes)
    if snow_len < N:
        snowflakes[snow_len] = new_snowflake()

    for i in snowflakes:
        sd.snowflake(center=sd.get_point(snowflakes[i]['start_x'], snowflakes[i]['start_y']),
                     length=snowflakes[i]['lenght'],
                     factor_b=snowflakes[i]['factor_b'],
                     factor_c=snowflakes[i]['factor_c'],
                     color=sd.COLOR_BLACK
                     )
        if step == 0:
            step_x = 0
        elif step == 1:
            step_x = 40
        elif step == 2:
            step_x = 0
        elif step == 3:
            step_x = -40
        else:
            step_x = 0
            step = 0

        snowflakes[i]['start_x'] -= step_x
        snowflakes[i]['start_y'] -= 20
        sd.snowflake(center=sd.get_point(snowflakes[i]['start_x'], snowflakes[i]['start_y']),
                     length=snowflakes[i]['lenght'],
                     factor_b=snowflakes[i]['factor_b'],
                     factor_c=snowflakes[i]['factor_c'],
                     color=sd.COLOR_WHITE
                     )
        if snowflakes[i]['start_y'] <= 20:
            snowflakes[i] = new_snowflake()

    #sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

# зачет!
