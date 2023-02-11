def draw_smile(x, y,radios, color,  sd):
    """
    Рисуем смайлик в точке
    """

    sd.circle(sd.get_point(x, y), radios, color, 1)
    sd.circle(sd.get_point(x - 30, y + 30), radios // 10, color, 1)
    sd.circle(sd.get_point(x + 30, y + 30), radios // 10, color, 1)
    sd.line(sd.get_point(x - 30, y), sd.get_point(x - 10, y - 20), color, 1)
    sd.line(sd.get_point(x - 10, y - 20), sd.get_point(x + 10, y - 20), color, 1)
    sd.line(sd.get_point(x + 10, y - 20), sd.get_point(x + 30, y), color, 1)
