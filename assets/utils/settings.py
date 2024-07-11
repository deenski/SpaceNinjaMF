import pygame

from assets.utils.colors import BLACK


class Settings:
    """Settings
    A class containing all the info you need to interact with.
    params:
    - window_size: tuple(int, int) - height and width of the pygame display
    - background_color: tuple(int, int, int) - 0-255
    - font: pygame.font.Font object

    attributes:
    - WINDOW_SIZE
    - WIDTH - Width of the window
    - HEIGHT - Height of the window
    - BACKGROUND_COLOR
    - font - pygame Font object
    - screen - fully initialized pygame.display.Display using the WIDTH and HEIGHT params
    - score - int - default 0

    functions:
    - increment_score
    """

    pygame.init()

    def __init__(
        self,
        window_size: tuple = (1080, 760),
        background_color: tuple = BLACK,  # https://encycolorpedia.com/4a43ea
        font: pygame.font.Font = pygame.font.Font(pygame.font.get_default_font(), 32),
    ):

        self.WINDOW_SIZE = window_size
        self.WIDTH = self.WINDOW_SIZE[0]
        self.HEIGHT = self.WINDOW_SIZE[1]
        self.BACKGROUND_COLOR = background_color
        self.font = font
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.score = 0
        self.level = 1

    def increment_score(self, val):
        self.score += val

    def increment_level(self):
        self.level += 1
