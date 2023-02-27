# -*- coding: utf-8 -*-

import simple_draw as sd
import random


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake(object):
    def __init__(self, snowflake, width, height, sd):
        self.width = width
        self.height = height
        self.sd = sd
        self.snowflake = snowflake
        self.draw(color=self.sd.COLOR_WHITE)

    def draw(self, color):
        self.sd.snowflake(center=sd.get_point(self.snowflake['start_x'], self.snowflake['start_y']),
                          length=self.snowflake['lenght'], factor_b=self.snowflake['factor_b'],
                          factor_c=self.snowflake['factor_c'],
                          color=color
                          )

    def move(self):
        self.draw(color=self.sd.COLOR_BLACK)
        no_tru_point = True
        while no_tru_point:
            x = random.randint(-50, 50)
            if self.width > x + self.snowflake['start_x'] > 0:
                no_tru_point = False
                self.snowflake['start_x'] += x
        self.snowflake['start_y'] += -50
        self.draw(color=self.sd.COLOR_WHITE)

    def can_fall(self):
        if (self.snowflake['start_y'] <= 50):

            return False
        else:

            return True


width = 1200
height = 600
count_snow = 20
snowflake = {'start_x': random.randint(0, width),
             'start_y': height,
             'lenght': random.randint(10, 50),
             'factor_b': random.uniform(0.1, 1),
             'factor_c': random.randint(30, 91)
             }
sd.resolution = (width, height)
sd.background_color = sd.COLOR_BLACK
#flake = Snowflake(snowflake, width, height, sd)
flakes = []
def create_snow():
    if len(flakes)<count_snow:
        snowflake = {'start_x': random.randint(0, width),
                     'start_y': height,
                     'lenght': random.randint(10, 50),
                     'factor_b': random.uniform(0.1, 1),
                     'factor_c': random.randint(30, 91)
                     }
        flakes.append(Snowflake(snowflake, width, height, sd))


while True:
    for flake in flakes:
        flake.move()
        if not flake.can_fall():
            flakes.remove(flake)

    create_snow()

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
