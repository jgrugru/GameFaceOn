import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from Screen import Screen

if __name__ == "__main__":
    pygame.init()

    screen = Screen()
    # screen.display_screen()
    screen.set_background()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.circle(screen.get_screen(), (0, 0, 255), (250, 250), 75)

        pygame.display.flip()

    pygame.quit()
