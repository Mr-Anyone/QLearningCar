from Car import Car
from GameUpdate import draw_car
from Constants import *
import numpy as np
import pygame

run = True # The state of the game
car = Car(pos = np.array([WINDOWS_WIDTH/2, WINDOWS_HEIGHT/2]))

pygame.init()
clock = pygame.time.Clock() # The clock or the update speed of the game
display = pygame.display.set_caption("AI Leans to drive")
windows = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
FPS = 30

while run: # Game Loop
    keys = pygame.key.get_pressed()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_w]:
        car.move_front()

    if keys[pygame.K_a]:
        car.turn_left()

    if keys[pygame.K_s]:
        car.move_backward()

    windows.fill((255,255,255)) # Drawing the background
    draw_car(car, windows)

    pygame.display.update()
    pygame.display.flip()
