def draw_branches(point, sd, angle=30, length=100):
    if length > 10:
        v1 = sd.get_vector(point, angle, length)
        v1.draw()
        # Чтобы чарм не ругался
        draw_branches(v1.end_point,sd,  angle + 30, int(length * 0.82))
        draw_branches(v1.end_point,sd,  angle - 30, int(length * 0.82))



def draw_branches2(point, sd,  angle=30, length=100 ):
    if length > 10:
        v1 = sd.get_vector(point, angle, length)
        v1.draw()
        draw_branches(v1.end_point, sd,  angle + 30 * (1 - sd.random_number(0, 40) / 100), int(length * 0.75))
        draw_branches(v1.end_point, sd, angle - 30 * (1 - sd.random_number(0, 40) / 100), int(length * 0.75))

