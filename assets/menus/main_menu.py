import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

from assets.utils.colors import BLACK


def main_menu_screen(settings, play_function):
    surface = create_example_window("SpaceNinjaMF", settings.WINDOW_SIZE)

    main_menu = pygame_menu.Menu(
        "SpaceNinjaMF",
        settings.WIDTH,
        settings.HEIGHT,
        theme=pygame_menu.themes.THEME_DARK,
    )
    main_menu.add.button("Play", play_function)
    main_menu.add.button("Quit", pygame_menu.events.EXIT)
    FPS = 30
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        surface.fill(BLACK)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if main_menu.is_enabled():
            main_menu.mainloop(surface, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()
