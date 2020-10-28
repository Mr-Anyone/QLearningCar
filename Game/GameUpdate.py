import pygame

def draw_car(car, windows):
    pygame.draw.rect(windows, (90,0, 0), pygame.Rect((0, 0, 100, 100))) # Rect format is (left, top, width, height)
