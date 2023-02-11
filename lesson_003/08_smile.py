# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def draw_smile(x, y, color):
    """
    Рисуем смайлик в точке
    """
    sd.circle(sd.get_point(x, y), 100, color, 1)
    sd.circle(sd.get_point(x - 30, y + 30), 10, color, 1)
    sd.circle(sd.get_point(x + 30, y + 30), 10, color, 1)
    sd.line(sd.get_point(x - 30, y), sd.get_point(x - 10, y - 20), color, 1)
    sd.line(sd.get_point(x - 10, y - 20), sd.get_point(x + 10, y - 20), color, 1)
    sd.line(sd.get_point(x + 10, y - 20), sd.get_point(x + 30, y), color, 1)


sd.resolution = (1200, 600)
for _ in range(0, 10):
    draw_smile(random.uniform(0, 1200), random.uniform(0, 600), sd.COLOR_WHITE)

sd.pause()

# зачет!
