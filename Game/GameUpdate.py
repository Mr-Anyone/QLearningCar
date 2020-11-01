import pygame

from Constants import *
from utils import distance, interesction_point

car_image = pygame.image.load(os.path.join(os.curdir, "Images", "Car.png"))


def draw_car(car, windows):
    """
    Draw an car and return the position of the rect
    :param car: The car object to get the position
    :param windows: the windows that the car will be drawn on
    :return: the position of the four conner of the car
    """
    center = car.pos[0], car.pos[1]
    new_img = pygame.transform.rotate(car_image, -car.current_degree)
    rect = new_img.get_rect(center=center)
    windows.blit(new_img, rect)


def draw_cardot(car, windows):
    """
    Drawing all the corner of the dot
    :param car:
    :param windows:
    :return:
    """
    points = car.get_four_side()
    for point in points:
        pygame.draw.rect(windows, ORANGE, (point[0], point[1], 5, 5))  # Drawing the four point of the car
    pygame.draw.rect(windows, ORANGE,
                     (car.center_point()[0], car.center_point()[1], 1, 1))  # RECT Format (left, top, width, height)


def draw_tracks(windows, inner_tracks, outer_tracks):
    """
    Drawing all the tracks in the car game
    :param windows: The windows of the screen
    :param inner_tracks: Points that are inside the track
    :param outer_tracks: Points that are outside the track
    """
    if len(inner_tracks) >= 2:
        pygame.draw.lines(windows, RED, True, inner_tracks)

    if len(outer_tracks) >= 2:
        pygame.draw.lines(windows, BLUE, True, outer_tracks)


def collide(p1, p2, p3, p4):
    """
    The function checks weather the 4 points collides
    Tutorial Page: http://jeffreythompson.org/collision-detection/line-line.php
    :return: True means collide False Means Not Collide
    """
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    x4, y4 = p4[0], p4[1]

    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))

    if ua >= 0 and ua <= 1 and ub >= 0 and ub <= 1:
        return True

    return False


def check_all_collision(car, inner_tracks, outer_tracks):
    """
    Checking if collision happens with the given car and tracks
    """
    tr, tl, br, bl = car.get_four_side()  # Top right, top left, bottom right, bottom left
    check_combos = [[tr, tl], [tr, br], [tl, bl], [bl, br]]  # A list of points to check
    for combo in check_combos:
        for i in range(1, len(inner_tracks)):  # Checking for inner track
            if collide(combo[0], combo[1], inner_tracks[i - 1], inner_tracks[i]):
                return True

        if collide(combo[0], combo[1], inner_tracks[0], inner_tracks[
            -1]):  # Checking the first point with the last point it will not be checked in the for loop above
            return True

        for i in range(1, len(outer_tracks)):  # Checking for outer track
            if collide(combo[0], combo[1], outer_tracks[i - 1], outer_tracks[i]):
                return True

        if collide(combo[0], combo[1], outer_tracks[0], outer_tracks[-1]):
            return True
    return False


def get_data_from_sensor(car, windows, inner_track, outer_track):
    """
    Draw the line that the sensor hit
    :param car: The car object
    :param windows: The display to draw the line
    :param inner_track: Points of the inner tracks
    :param outer_track: Poitns of the outer tracks
    :return: The intersection points
    """
    sensor_line = car.sensor_line()
    result = []
    distances = []

    for line in sensor_line:
        _ = 100000000
        intersection_cor = None
        # Checking for inner_track
        for i in range(1, len(inner_track)):
            if collide(line[0], line[1], inner_track[i - 1], inner_track[i]):
                _2 = interesction_point(line[0], line[1], inner_track[i - 1], inner_track[i])
                if _ > distance(line[0], _2):
                    _ = distance(line[0], _2)
                    intersection_cor = _2

        # Special Case the front and the end of the line in the inner track
        if collide(line[0], line[1], inner_track[0], inner_track[-1]):
            _2 = interesction_point(line[0], line[1], inner_track[0], inner_track[-1])
            if _ > distance(line[0], _2):
                _ = distance(line[0], _2)
                intersection_cor = _2

        # Checking for outer_track
        for i in range(1, len(outer_track)):
            if collide(line[0], line[1], outer_track[i - 1], outer_track[i]):
                _2 = interesction_point(line[0], line[1], outer_track[i - 1], outer_track[i])
                if _ > distance(line[0], _2):
                    _ = distance(line[0], _2)
                    intersection_cor = _2

        # Special Case the front and the end of the line in the outer track
        if collide(line[0], line[1], outer_track[0], outer_track[-1]):
            _2 = interesction_point(line[0], line[1], outer_track[0], outer_track[-1])
            if _ > distance(line[0], _2):
                _ = distance(line[0], _2)
                intersection_cor = _2

        result.append(intersection_cor)
        distances.append(_)

    for point in result:
        pygame.draw.line(windows, BLUE, car.pos, point)
    return result
