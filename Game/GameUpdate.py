import os
import pygame
from Constants import *

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
        pygame.draw.rect(windows, ORANGE, (point[0], point[1], 5, 5)) # Drawing the four point of the car
    pygame.draw.rect(windows, ORANGE, (car.center_point()[0], car.center_point()[1], 1, 1))  # RECT Format (left, top, width, height)


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
    ua = ((p4[0]-p3[0])*(p1[1]-p3[1]) - (p4[1]-p3[1])*(p1[0]-p3[0]))/((p4[1]-p3[1])*(p2[0]-p1[0]) - (p4[0]-p3[0])*(p2[1]-p2[1]))
    ub = ((p2[0]-p1[0])*(p1[1]-p3[1]) - (p2[1]-p1[1])*(p1[0]-p3[0]))/((p4[1]-p3[1])*(p2[0]-p1[0]) - (p4[0]-p3[0])*(p2[1]-p1[1]))
    if ua >= 0 and ua <= 1 and ub >=0 and ub <= 1:
        return True

    return False

def check_all_collision(car, inner_tracks, outer_tracks):
    """
    Checking if collision happens with the given car and tracks
    """
    tr, tl, br, bl = car.get_four_side() # Top right, top left, bottom right, bottom left
    check_combos = [[tr, tl], [tr, br], [tl, bl], [bl, br]] # A list of points to check
    for combo in check_combos:
        for i in range(1, len(inner_tracks)):# Checking for inner track
            if collide(combo[0], combo[1], inner_tracks[i -1], inner_tracks[i]):
                return True

        if collide(combo[0], combo[1], inner_tracks[0], inner_tracks[-1]): # Checking the first point with the last point it will not be checked in the for loop above
                return True

        for i in range(1, len(outer_tracks)):# Checking for outer track
            if collide(combo[0], combo[1], outer_tracks[i-1], outer_tracks[i]):
                return True

        if collide(combo[0], combo[1], outer_tracks[0], outer_tracks[-1]):
            return True
    return False

