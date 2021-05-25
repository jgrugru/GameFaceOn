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

    # screen = Screen()
    # screen.display_screen()
    # screen.set_background()

    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))

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

        # pygame.draw.circle(screen.get_screen(), (0, 0, 255), (250, 250), 75)

        # surface = pygame.Surface((50, 50))
        # surface.fill((100, 0, 100))
        # rect = surface.get_rect()
        # # breakpoint()

        # screen.blit(surface, surface_cent)
        # pygame.display.flip()

    pygame.quit()

