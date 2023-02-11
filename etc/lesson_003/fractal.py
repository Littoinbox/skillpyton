# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 900)


def branch(point, angle, length, width):
    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    vector.draw()

    point_2 = vector.end_point
    angle_2 = angle - 30
    length_2 = length * .7
    return point_2, angle_2, length_2, width


point = sd.get_point(600, 5)
angle = 90
length = 100
width = 4

# vector = sd.get_vector(start_point=point, angle=90, length=100, width=4)
# vector.draw()
#
# point_2 = vector.end_point
# angle_2 = angle - 30
# length_2 = length * .7
# vector_2 = sd.get_vector(start_point=point_2, angle=angle_2, length=length_2, width=width)
# vector_2.draw()
#
# point_3 = vector_2.end_point
# angle_3 = angle_2 - 30
# length_3 = length_2 * .7
# vector_3 = sd.get_vector(start_point=point_3, angle=angle_3, length=length_3, width=width)
# vector_3.draw()

point_2, angle_2, length_2, width_2 = branch(point, angle, length, width)
point_3, angle_3, length_3, width_3 = branch(point_2, angle_2, length_2, width_2)
point_3, angle_3, length_3, width_3 = branch(point_2, angle_2, length_2, width_2)

sd.pause()
