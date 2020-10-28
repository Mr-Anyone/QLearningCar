from Car import Car
import numpy as np
import pygame

run = True # The state of the game
car = Car(pos = np.array([0, 0]))
WIDTH = 700
HEIGHT = 700

pygame.init()
clock = pygame.time.Clock() # The clock or the update speed of the game
display = pygame.display.set_caption("Car Learns to drive")
windows = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 30

while run: # Game Loop
    keys = pygame.key.get_pressed()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_w]:
        car.move_front()

    windows.fill((255,255,255)) # Drawing the background
    pygame.display.update()
    pygame.display.flip()
