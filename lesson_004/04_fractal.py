# -*- coding: utf-8 -*-

import simple_draw as sd


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# А смысл на одну букву сокращать? :)
def draw_branches(point=sd.get_point(300, 0), angle=30, length=100):
    if length > 10:
        v1 = sd.get_vector(point, angle, length)
        v1.draw()
        # Чтобы чарм не ругался
        draw_branches(v1.end_point, angle + 30, int(length * 0.82))
        draw_branches(v1.end_point, angle - 30, int(length * 0.82))


draw_branches(sd.get_point(300, 30), 90, 100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
def draw_branches2(point=sd.get_point(300, 0), angle=30, length=100):
    if length > 10:
        v1 = sd.get_vector(point, angle, length)
        v1.draw()
        draw_branches(v1.end_point, angle + 30 * (1 - sd.random_number(0, 40) / 100), int(length * 0.75))
        draw_branches(v1.end_point, angle - 30 * (1 - sd.random_number(0, 40) / 100), int(length * 0.75))


#draw_branches2(sd.get_point(300, 30), 90, 100)


sd.pause()

# зачет!
