from pygame import display, Surface


class Screen(Surface):

    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        super().__init__((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self = self.display_screen()
        # breakpoint()
        print(type(self))

    def display_screen(self):
        return display.set_mode((
            self.SCREEN_WIDTH, self.SCREEN_HEIGHT
        ))

    def set_background(self):
        self.fill((255, 255, 255))


    # def get_width(self):
    #     return self.SCREEN_WIDTH

    # def get_height(self):
    #     return self.SCREEN_HEIGHT

    # def get_screen(self):
    #     return self.screen
