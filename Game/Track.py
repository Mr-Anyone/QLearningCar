import time
import numpy as np
import pygame
import csv
from Car import Car
from Constants import *
from GameUpdate import draw_tracks, draw_car

pygame.init()
pygame.display.set_caption("Track Creator")
windows = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))

run = True
inner_tracks = []
outer_tracks = []
get_inner = True
clock = pygame.time.Clock()


def save(inner, outer):
    with open(TRACK_DIR, "w") as f:
        file = csv.writer(f)

        if len(inner) > len(outer):
            for x in range(len(inner)):
                try:
                    file.writerow([inner[x][0], inner[x][1], outer[x][0], outer[x][1]])
                except IndexError:
                    file.writerow([inner[x][0], inner[x][1]])
        else:
            for x in range(len(outer)):
                try:
                    file.writerow([inner[x][0], inner[x][1], outer[x][0], outer[x][1]])
                except IndexError:
                    file.writerow([None, None, outer[x][0], outer[x][1]])

        f.close()

car = Car(pos=np.array([WINDOWS_WIDTH / 2, WINDOWS_HEIGHT / 2]))
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save(inner_tracks, outer_tracks)
            run = False

    if pygame.mouse.get_pressed()[0]:
        if get_inner:
            inner_tracks.append(pygame.mouse.get_pos())
            time.sleep(0.1)
        else:
            outer_tracks.append(pygame.mouse.get_pos())
            time.sleep(0.1)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_k]:
        if get_inner:
            get_inner = False
            time.sleep(0.5)
        else:
            get_inner = True
            time.sleep(0.5)

    if keys[pygame.K_z]:
        if get_inner:
            inner_tracks.pop()
        else:
            outer_tracks.pop()
        time.sleep(0.5)

    windows.fill((0, 0, 0))
    draw_car(car, windows)
    draw_tracks(windows, inner_tracks, outer_tracks)

    pygame.display.flip()
    pygame.display.update()
