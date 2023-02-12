import random

import simple_draw as sd

snowflakes = {}
max_count_snow = 70
width, height = 1200, 600


def new_snowflake():
    snowflake = {'start_x': random.randint(0, width),
                 'start_y': height,
                 'lenght': random.randint(10, 50),
                 'factor_b': random.uniform(0.1, 1),
                 'factor_c': random.randint(30, 91)
                 }
    return snowflake


def print_color_snow(color):
    global snowflakes
    for i in snowflakes:
        sd.snowflake(center=sd.get_point(snowflakes[i]['start_x'], snowflakes[i]['start_y']),
                     length=snowflakes[i]['lenght'],
                     factor_b=snowflakes[i]['factor_b'],
                     factor_c=snowflakes[i]['factor_c'],
                     color=color
                     )


def create_snow(n):
    global width, height
    global snowflakes
    for i in range(0, n):
        if len(snowflakes) <= max_count_snow:
            snowflakes[len(snowflakes)] = new_snowflake()
        else:
            break


def move_snowflake():
    global snowflakes
    for i in snowflakes:
        no_tru_point = True
        while no_tru_point:
            x = random.randint(-50, 50)
            if width > x + snowflakes[i]['start_x'] > 0:
                no_tru_point = False
                snowflakes[i]['start_x'] += x
        snowflakes[i]['start_y'] += -50


def list_del():
    global snowflakes
    delit_sow = []
    for i in snowflakes:
        if snowflakes[i]['start_y'] <= 50:
            delit_sow.append(i)
    return delit_sow


def remove_snow(list):
    global snowflakes
    for i in list:
        snowflakes[i] = new_snowflake()
