import logging
import os
import tempfile
from os.path import join

import pygame
from entrypoint2 import entrypoint
from genimg import generate_image
from pygame.locals import K_ESCAPE, KEYDOWN

log = logging.getLogger(__name__)


def fillscreen_pygame(fimage):
    # DBus org.kde.kwin.Screenshot disappears on Kubuntu 20.04 after starting pygame
    #  fix: System Settings > Compositor > uncheck Allow apps to turn off compositing.
    #       or https://www.pygame.org/docs/ref/pygame.html
    #           SDL_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR
    #           Set to "0" to re-enable the compositor.
    os.environ["SDL_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR"] = "0"
    pygame.init()
    pygame.mouse.set_visible(0)
    log.info("pygame modes:%s", pygame.display.list_modes())
    # log.info("pygame info:%s", pygame.display.Info())
    log.info("env $DISPLAY= %s", os.environ.get("DISPLAY"))

    infoObject = pygame.display.Info()
    im = generate_image(infoObject.current_w, infoObject.current_h)
    im.save(fimage)

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
        # atexit.register(lambda: rmtree(d))
        image = join(d, "ref.bmp")
    # im = generate_image()
    # im.save(image)
    fillscreen_pygame(image)
