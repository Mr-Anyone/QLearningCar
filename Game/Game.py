from Car import Car
from GameUpdate import draw_car, draw_cardot, draw_tracks, check_all_collision, get_data_from_sensor
from Constants import *
import numpy as np
import pygame
from utils import read_csv

run = True # The state of the game
car = Car(pos = np.array([WINDOWS_WIDTH/2, WINDOWS_HEIGHT/2]))

pygame.init()
clock = pygame.time.Clock() # The clock or the update speed of the game
display = pygame.display.set_caption("AI Leans to drive")
windows = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
outer_track, inner_track = read_csv()
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

    if keys[pygame.K_d]:
        car.turn_right()

    windows.fill((255,255,255)) # Drawing the background

    if check_all_collision(car, inner_track, outer_track): # Check for collision
        print("Collision")
        car.pos = np.array([WINDOWS_WIDTH/2, WINDOWS_HEIGHT/2])

    get_data_from_sensor(car, windows, inner_track, outer_track)# Calculate the Car Hit Point

    draw_car(car, windows) # Draw the car
    draw_cardot(car, windows) # Draw the hit box
    draw_tracks(windows, inner_track, outer_track) # Draw the car track

    pygame.display.update()
    pygame.display.flip()
