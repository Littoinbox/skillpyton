# -*- coding: utf-8 -*-
import random

import simple_draw as sd
import snowfall

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
#snowfall.width =
width = 1200
#snowfall.height =
height = 600
#snowfall.sd = sd
sd.resolution = (width, height)
sd.background_color = sd.COLOR_BLACK

while True:
    snowfall.print_color_snow(sd.background_color, sd)
    snowfall.move_snowflake(width)
    snowfall.print_color_snow(sd.COLOR_WHITE, sd)
    snowfall.remove_snow(snowfall.list_del(), width, height)
    snowfall.create_snow(random.randint(1, 10), width, height)
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
