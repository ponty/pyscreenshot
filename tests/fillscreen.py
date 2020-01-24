from time import sleep

import pygame
from entrypoint2 import entrypoint


def init(size=None):
    rectsize = 50

    pygame.display.init()
    pygame.mouse.set_visible(0)

    if size:
        disp = pygame.display.set_mode(size)
    else:
        disp = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        disp = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # TODO: for travis

    w, h = pygame.display.get_surface().get_size()
    i = 0
    for x in range(0, w, rectsize):
        for y in range(0, h, rectsize):
            r = x * 255 / w
            g = y * 255 / h
            b = (i % 5) * 255 / 5
            pygame.draw.rect(disp, (r, g, b), (x, y, rectsize, rectsize))
            i += 1

    pygame.display.update()
    pygame.display.update()
    pygame.display.update()

    pygame.image.save(disp, "/tmp/fillscreen.bmp")  # TODO

    # sleep(1)


@entrypoint
def main(size=None):
    if size:
        size = map(int, size.split(":"))
        size = tuple(size)

    init(size)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(1)
    pygame.quit()
