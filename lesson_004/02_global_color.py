# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def draw_figure(point, angle=0, long=200, peaks=3, color=sd.COLOR_WHITE):
    step = round(360 / peaks, 0)
    last_point = point
    last_peaks = peaks - 1
    for i in range(0, peaks):
        new_angle = step * i + angle
        if i == last_peaks:
            sd.line(last_point, point, width=3, color=color)
        else:
            vector = sd.get_vector(start_point=last_point, angle=new_angle, length=long, width=3)
            vector.draw(color=color)
            last_point = vector.end_point


def draw_triangle(point, angle=0, long=200, color=sd.COLOR_WHITE):
    draw_figure(point, angle, long, 3, color=color)


def draw_square(point, angle=0, long=200, color=sd.COLOR_WHITE):
    draw_figure(point, angle, long, 4, color=color)


def draw_pentagon(point, angle=0, long=200, color=sd.COLOR_WHITE):
    draw_figure(point, angle, long, 5, color=color)


def draw_hexagon(point, angle=0, long=200, color=sd.COLOR_WHITE):
    draw_figure(point, angle, long, 6, color=color)


colors = {0: {'title': 'красный', 'values': sd.COLOR_RED},
          1: {'title': 'оранжевый', 'values': sd.COLOR_ORANGE},
          2: {'title': 'желый', 'values': sd.COLOR_YELLOW},
          3: {'title': 'зеленый', 'values': sd.COLOR_GREEN},
          4: {'title': 'голубой', 'values': sd.COLOR_CYAN},
          5: {'title': 'синий', 'values': sd.COLOR_BLUE},
          6: {'title': 'фиолетовый', 'values': sd.COLOR_PURPLE}
          }

for i, color in colors.items():
    print(i, ' цвет ', color['title'])

while True:
    color_num = int(input("Введите номмер цвета: "))
    if color_num in colors:
        # Так понятнее будет
        user_color = colors[color_num]['values']
        break
    else:
        print("Вы ввели неправилиный номер цвета!")

draw_triangle(sd.get_point(50, 10), 0, 100, user_color)
draw_square(sd.get_point(350, 10), 0, 100, user_color)
draw_pentagon(sd.get_point(50, 210), 0, 100, user_color)
draw_hexagon(sd.get_point(350, 210), 0, 100, user_color)

sd.pause()

# зачет!
