def print_rainbow(start_x, start_y, end_x, end_y, width, step, sd):
    for _ in range(0, 7):
        sd.line(sd.get_point(start_x, start_y), sd.get_point(end_x, end_y), sd.random_color(), width)
        start_x += step
        end_x += step

