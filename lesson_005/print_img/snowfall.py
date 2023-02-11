import random


def new_snowflake(start_x, end_x, start_Y):
    snowflake = {'start_x': random.randint(start_x, end_x),
                 'start_y': start_Y,
                 'lenght': random.randint(10, 50),
                 'factor_b': random.uniform(0.1, 1),
                 'factor_c': random.randint(30, 91)
                 }
    return snowflake


def print_snow(start_x, end_x, start_y, end_y, step, step_x, snowflakes, backGroundColor, sd):
    step += 1

    for i in snowflakes:
        sd.snowflake(center=sd.get_point(snowflakes[i]['start_x'], snowflakes[i]['start_y']),
                     length=snowflakes[i]['lenght'],
                     factor_b=snowflakes[i]['factor_b'],
                     factor_c=snowflakes[i]['factor_c'],
                     color=backGroundColor
                     )
        if step == 0:
            step_x = 0
        elif step == 1:
            step_x = 40
        elif step == 2:
            step_x = 0
        elif step == 3:
            step_x = -40
        else:
            step_x = 0
            step = 0

        snowflakes[i]['start_x'] -= step_x
        snowflakes[i]['start_y'] -= 20
        sd.snowflake(center=sd.get_point(snowflakes[i]['start_x'], snowflakes[i]['start_y']),
                     length=snowflakes[i]['lenght'],
                     factor_b=snowflakes[i]['factor_b'],
                     factor_c=snowflakes[i]['factor_c'],
                     color=sd.COLOR_WHITE
                     )
        if snowflakes[i]['start_y'] <= end_y:
            snowflakes[i] = new_snowflake(start_x, end_x, start_y)


    return step, step_x, snowflakes