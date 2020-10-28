import pygame
from Constants import *

def draw_car(car, windows):
    pygame.draw.rect(windows, (90,0, 0), pygame.Rect((car.pos[0], car.pos[1], BOX_WIDTH, BOX_HEIGHT))) # Rect format is (left, top, width, height)
