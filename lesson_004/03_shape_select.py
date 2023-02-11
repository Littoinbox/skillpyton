# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


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


shapes = {
    0: {'title': 'треугольник', 'function': draw_triangle},
    1: {'title': 'квадрат', 'function': draw_square},
    2: {'title': 'пятиугольник', 'function': draw_pentagon},
    3: {'title': 'шестиугольник', 'function': draw_hexagon},
}


for i, color in colors.items():
    print(i, ' цвет ', color['title'])

while True:
    color_num = int(input("Введите номмер цвета: "))

    if color_num in colors:
        break
    else:
        print("Вы ввели неправилиный номер цвета!")

for i, shape in shapes.items():
    print(i, ' Фигура ', shape['title'])

while True:
    figur_num = int(input("Введите номер фигуры "))
    if figur_num in shapes:
        break
    else:
        print('Вы ввели неверный номер фигуры')

center_point = sd.get_point(150, 150)

user_figure = shapes[figur_num]['function']
user_color = colors[color_num]['values']
user_figure(point=center_point, color=user_color)

sd.pause()

# зачет!
