# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 600)
sd.background_color = [255, 255, 255]
point = sd.get_point(600, 500)
# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
sd.circle(point, 100, [0, 0, 0])
sd.circle(point, 95, [0, 0, 0])
sd.circle(point, 90, [0, 0, 0])


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def draw_cir(center, steps):
    for i in range(1, 4):
        sd.circle(center, steps - (i * 5), [0, 0, 0])


# Нарисовать 10 пузырьков в ряд

for step in range(1, 11):
    center_x = 50 * step * 2
    draw_cir(sd.get_point(center_x, 350), 50)

# Нарисовать три ряда по 10 пузырьков
for step_x in range(1, 11):
    for step_y in range(50, 350, 100):
        center_x = 50 * step_x * 2
        draw_cir(sd.get_point(center_x, step_y), 50)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for step100 in range(1, 101):
    rand_x = random.uniform(0, 1200)
    rand_y = random.uniform(0, 600)
    rand_color_r = random.uniform(0, 255)
    rand_color_g = random.uniform(0, 255)
    rand_color_b = random.uniform(0, 255)
    sd.circle(sd.get_point(rand_x, rand_y), 10, [rand_color_r, rand_color_g, rand_color_b])

sd.pause()

# зачет!
