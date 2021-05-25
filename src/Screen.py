from pygame import display, Surface


class Screen(Surface):

    def __init__(self):
        self.surface = display.set_mode((800, 600))
        self.surface.fill((255, 255, 255))
