# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import print_img.rainbow as rain
import print_img.snowfall as snowfall
import print_img.tree as tree
import print_img.house as house
import print_img.sun as sun
import simple_draw as sd

countSnow = 20
snowflake = {}
start_snow_x = 0
end_snow_x = 300
start_snow_y = 450
end_snow_y = 50
step, step_x = 0, 0

sd.resolution = (1200, 600)
sd.background_color = sd.COLOR_BLACK


def painting():
    for i in range(0, countSnow):
        snowflake[i] = (snowfall.new_snowflake(start_snow_x, end_snow_x, end_snow_y))

    snowfall.print_snow(start_snow_x, end_snow_x, start_snow_y, end_snow_y, step, step_x, snowflake, sd.COLOR_BLACK, sd)
    house.print_house(sd, 400, 0, 400, 500)
    sun.print_sun(sd.get_point(300, 550), 50, 30, sd)
    tree.draw_branches2(sd.get_point(1000, 0), sd, 90, 100)
    rain.print_rainbow(900, 650, 1200, 450, 4, 5, sd)


def animate_painting(step, step_x):
    house.print_house(sd, 400, 0, 400, 500)
    tree.draw_branches2(sd.get_point(1000, 0), sd, 90, 100)
    rays =[]
    while True:
        rays = sun.print_sun(sd.get_point(300, 550), 20, 30, sd, sd.random_number(15, 45), rays)
        rain.print_rainbow(900, 650, 1200, 450, 10, 11, sd)
        snow_len = len(snowflake)
        if (snow_len < countSnow):
            snowflake[snow_len] = (snowfall.new_snowflake(start_snow_x, end_snow_x, start_snow_y))
        step, step_x, snowflakes = snowfall.print_snow(start_snow_x, end_snow_x, start_snow_y, end_snow_y, step, step_x,
                                                   snowflake, sd.COLOR_BLACK, sd)
        sd.sleep(0.1)
        if sd.user_want_exit():
            break



#painting()
animate_painting(step, step_x)
sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
