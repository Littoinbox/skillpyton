def print_wall(sd, start_x, start_y, w,h):
    len_x, len_y = 50, 25
    step = 0
    for cord_y in range(start_y, h+start_y, len_y):
        for cord_x in range(start_x, w+start_x, len_x):
            if (cord_x+step + len_x> w+start_x):
                max_x = w+start_x
            else :
                max_x =cord_x+step+len_x

            if (cord_y + len_y > start_y+h):
                max_y = start_y+h
            else:
                max_y = cord_y + len_y
            sd.rectangle(sd.get_point(cord_x + step, cord_y), sd.get_point(max_x, max_y),
                         sd.COLOR_WHITE, width=1)
        step = 50 if step == 0 else 0