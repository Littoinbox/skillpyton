# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd

sd.resolution = (1200, 900)
sd.background_color = sd.COLOR_BLACK

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


N = 6
MIN_RADIUS = 10
REDUCE_KOEF = 0.5


def bubble(point, radius, deep=0):
    if radius < MIN_RADIUS:
        return
    color = rainbow_colors[deep % 7]
    width = 5 - deep
    sd.circle(center_position=point, radius=radius, color=color, width=width if width > 1 else 1)
    new_radius = int(radius * REDUCE_KOEF)
    for angle in range(0, 360, 360 // N):
        vector = sd.get_vector(start_point=point, angle=angle, length=radius)
        bubble(point=vector.end_point, radius=new_radius, deep=deep + 1)


point = sd.get_point(600, 450)

bubble(point=point, radius=200)

sd.pause()
