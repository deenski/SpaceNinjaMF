import random

import pygame


# Define the Life object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'Life'
class Bomb(pygame.sprite.Sprite):
    def __init__(self, image_path, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Bomb, self).__init__()
        self.surf = pygame.image.load(image_path).convert().convert_alpha()
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
