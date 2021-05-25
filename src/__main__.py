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
    screen = pygame.display.get_surface()

    rect = pygame.Surface((50, 50))
    rect.fill((100, 0, 100))
    new_rect = rect.get_rect()

    center_rect = (
        (screen.get_width()-rect.get_height())/2,
        (screen.get_height()-rect.get_height())/2
    )

    screen.blit(rect, center_rect)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            running = event_controller(event)

    pygame.quit()

