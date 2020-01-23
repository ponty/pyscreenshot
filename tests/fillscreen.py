import random

import pygame
from entrypoint2 import entrypoint


def fill(disp, size):
    w, h = pygame.display.get_surface().get_size()
    for x in range(0, w, size):
        for y in range(0, h, size):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            pygame.draw.rect(disp, (r, g, b), (x, y, size, size))
    pygame.display.update()


@entrypoint
def main():
    pygame.init()

    # Create a displace surface object
    # DISPLAYSURF = pygame.display.set_mode((400, 300))
    disp = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    fill(disp, 50)

    mainLoop = True
    while mainLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
        pygame.display.update()
    # sleep(5)
    pygame.quit()
