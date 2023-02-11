# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_x, end_x, start_y, end_y = 50, 350, 50, 450
for line_color in rainbow_colors:
    sd.line(sd.get_point(start_x, start_y), sd.get_point(end_x, end_y), line_color, 4)
    start_x += 5
    end_x += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
start_rad = 300
for line_color in rainbow_colors:
    sd.circle(sd.get_point(600, 0), start_rad, line_color, 4)
    start_rad -= 5
sd.pause()

# зачет!
