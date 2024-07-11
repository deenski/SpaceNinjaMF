from typing import override

import pygame
from pygame.locals import *


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, SCREEN_WIDTH, SCREEN_HEIGHT, lives=3):
        super(Player, self).__init__()
        self.surf = pygame.image.load(image_path).convert().convert_alpha()
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.lives = lives

        # Move the sprite based on user keypresses

    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.SCREEN_HEIGHT:
            self.rect.bottom = self.SCREEN_HEIGHT

    def increment_lives(self, val):
        self.lives += val
