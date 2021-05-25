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

def event_controller(event):
    print(event)
    running = True
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            running = False
    elif event.type == QUIT:
        running = False
    return running

if __name__ == "__main__":
    pygame.init()

    screen = Screen()
    # screen.display_screen()
    screen.set_background()

    running = True
    while running:
        for event in pygame.event.get():
            running = event_controller(event)

        # pygame.draw.circle(screen.get_screen(), (0, 0, 255), (250, 250), 75)

        surface = pygame.Surface((50, 50))
        surface.fill((0, 0, 0))
        rect = surface.get_rect()

        screen.get_screen().blit(surface,
                                 ((screen.get_width()-surface.get_width())/2,
                                  (screen.get_height()-surface.get_height())/2))
        pygame.display.flip()

    pygame.quit()

