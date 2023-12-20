# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_figure(point, angle=0, long=200, peaks=n):
        step = round(360 / peaks, 0)
        last_point = point
        last_peaks = peaks - 1
        for i in range(0, peaks):
            new_angle = step * i + angle
            if i == last_peaks:
                sd.line(last_point, point, width=3)
            else:
                vector = sd.get_vector(start_point=last_point, angle=new_angle, length=long, width=3)
                vector.draw()
                last_point = vector.end_point

    return draw_figure




draw_triangle = get_polygon(n=4)

draw_triangle(point=sd.get_point(200, 200), angle=13, long=100)


sd.pause()
