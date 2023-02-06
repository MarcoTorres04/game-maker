import math


def get_star_points(corners: int, corner_distance: int, small_distance: int,
                    start_angle: int, center: tuple) -> tuple:
    corner_angle = 360 / corners
    small_angle = corner_angle / 2
    corners_angles = [start_angle + corner_angle * x for x in range(corners)]
    smalls_angles = [(start_angle + small_angle) + corner_angle * x
                     for x in range(corners)]
    corner_point_x = map(
        lambda angle: corner_distance * math.cos(math.radians(angle)),
        corners_angles)
    corner_poiyt_y = map(
        lambda angle: corner_distance * math.sin(math.radians(angle)),
        corners_angles)
    small_point_x = map(
        lambda angle: small_distance * math.cos(math.radians(angle)),
        smalls_angles)
    small_point_y = map(
        lambda angle: small_distance * math.sin(math.radians(angle)),
        smalls_angles)
    x, y = list(), list()
    for x_cor, x_sma, y_cor, y_sma in zip(corner_point_x, small_point_x,
                                          corner_poiyt_y, small_point_y):
        x.append(x_cor + center[0])
        x.append(x_sma + center[0])
        y.append(y_cor + center[1])
        y.append(y_sma + center[1])
    x.append(x[0])
    y.append(y[0])
    return x, y
