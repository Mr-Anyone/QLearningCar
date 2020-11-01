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
        pygame.draw.lines(windows, RED, False, inner_tracks)

    if len(outer_tracks) >= 2:
        pygame.draw.lines(windows, BLUE, False, outer_tracks)


