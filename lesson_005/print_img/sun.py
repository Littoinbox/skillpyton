def print_sun(center, radius, max_size_rays, sd, agile=45, old_r=[]):
    if (len(old_r)==0):
        sd.circle(center, radius, sd.COLOR_YELLOW, 0)
    for old_rays in old_r:
        sd.line(old_rays[0], old_rays[1], sd.COLOR_BLACK, 1)
    for i in range(0, 360, agile):
        line_size = sd.random_number(10, max_size_rays)
        if (round(radius * sd.sin(i)) == 0):
            start_point_y = center.y
            end_point_y = center.y
        else:
            start_point_y = round(radius * sd.sin(i)) + center.y
            end_point_y = round((radius + line_size) * sd.sin(i)) + center.y

        if (round(radius * sd.cos(1)) == 0):
            start_point_x = center.x
            end_point_x = center.x
        else:
            start_point_x = round(radius * sd.cos(i)) + center.x
            end_point_x = round((radius + line_size) * sd.cos(i)) + center.x

        start_point = sd.get_point(start_point_x, start_point_y)
        end_point = sd.get_point(end_point_x, end_point_y)
        old_r.append([start_point, end_point])
        sd.line(start_point, end_point, sd.COLOR_YELLOW, 1)
    return old_r
