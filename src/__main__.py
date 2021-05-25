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


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def event_controller(event):
    print(event)
    running = True
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            running = False
    elif event.type == QUIT:
        running = False
    return running


def init_game():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((100, 0, 255))
    pygame.display.flip()
    return screen


def add_rectangle(screen):

    rect = pygame.Surface((50, 50))
    rect.fill((255, 0, 100))
    new_rect = rect.get_rect()

    center_rect = (
        (screen.get_width()-rect.get_height())/2,
        (screen.get_height()-rect.get_height())/2
    )

    screen.blit(rect, center_rect)


if __name__ == "__main__":
    screen = init_game()

    add_rectangle(screen)

    pygame.display.flip()  # update screen

    running = True
    while running:
        for event in pygame.event.get():
            running = event_controller(event)

    pygame.quit()
