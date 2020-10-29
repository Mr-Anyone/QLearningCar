import pygame
from Constants import *
from PIL import Image
import os
car_image = pygame.image.load(os.path.join(os.curdir, "Images", "Car.png"))
def draw_car(car, windows):
    center = car.pos[0], car.pos[1]
    new_img = pygame.transform.rotate(car_image, -car.current_degree)
    windows.blit(new_img, new_img.get_rect(center=center))
    # pygame.draw.rect(windows, (90, 0, 0), pygame.Rect(
    #     (car.pos[0], car.pos[1], BOX_WIDTH, BOX_HEIGHT)))  # Rect format is (left, top, width, height)
