import logging
import os
import tempfile
from os.path import join

import pygame
from entrypoint2 import entrypoint
from pygame.locals import *

from genimg import generate_image

log = logging.getLogger(__name__)


def fillscreen_pygame(fimage):
    pygame.init()
    pygame.mouse.set_visible(0)
    log.info("pygame modes:%s", pygame.display.list_modes())
    # log.info("pygame info:%s", pygame.display.Info())
    log.info("env $DISPLAY= %s", os.environ.get("DISPLAY"))

    windowSurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    img = pygame.image.load(fimage)

    mainLoop = True

    while mainLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mainLoop = False

        windowSurface.blit(img, (0, 0))
        # pygame.display.flip()
        pygame.display.update()

    pygame.quit()


@entrypoint
def main(image=""):
    if not image:
        d = tempfile.mkdtemp(prefix="fillscreen")
        image = join(d, "ref.bmp")
        im = generate_image()
        im.save(image)
    fillscreen_pygame(image)
