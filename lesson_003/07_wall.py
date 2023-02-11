# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (1200, 600)
len_x, len_y = 100, 50
step = 0
for cord_y in range(0, 600, 50):
    for cord_x in range(0, 1200, 100):

        sd.rectangle(sd.get_point(cord_x + step, cord_y), sd.get_point(cord_x + step + len_x, cord_y + len_y),
                     sd.COLOR_WHITE, width=1)
    # Можно здесь тернальный оператор использовать
    step = 50 if step == 0 else 0
sd.pause()

# зачет!
