from . import wall
from . import smile


def print_house(sd, start_x, start_y, width, height):
    if (height - 50 > 50):  # вычисляем высоту сетены дома
        height_wall = height - 50
    else:
        height_wall = height

    window_start_x = start_x + (width // 4)  # нчало окна по x
    wimdow_start_y = start_y + (height_wall // 4)  # начало окна по y
    side = width // 2  # рамер окна
    sd.rectangle(sd.get_point(start_x, start_y), sd.get_point(start_x + width, start_y + height_wall), sd.COLOR_WHITE,
                 1)  # обводка дома
    wall.print_wall(sd, start_x, start_y, width, height_wall)  # стена
    sd.line(sd.get_point(start_x, start_y + height_wall),
            sd.get_point(start_x + (width // 2), start_y + height_wall + 50), sd.COLOR_WHITE, 1)  # крыша 1 часть
    sd.line(sd.get_point(start_x + (width // 2), start_y + height_wall + 50),
            sd.get_point(start_x + width, start_y + height_wall), sd.COLOR_WHITE, 1)  # крыша 2 часть

    sd.square(sd.get_point(window_start_x, wimdow_start_y), side, sd.COLOR_BLACK, 0)  # заливка окна
    sd.square(sd.get_point(window_start_x, wimdow_start_y), side, sd.COLOR_WHITE, 1)  # окно
    smile.draw_smile(window_start_x + (side // 2), wimdow_start_y + (side // 2), (side // 2), sd.COLOR_WHITE,
                     sd)  # смайлик
