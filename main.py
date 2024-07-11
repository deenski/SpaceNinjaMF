# Import and initialize the pygame library
import pygame
from pygame.locals import *

# Import abstractions
from assets.classes.bomb import Bomb
from assets.classes.enemy import Enemy
from assets.classes.life import Life
from assets.classes.player import Player
from assets.utils.events import ADDBOMB, ADDENEMY, ADDLIFE
from assets.utils.groups import all_sprites, bombs, enemies, lives
from assets.utils.helpers import blit_that_shit, check_collisions
from assets.utils.settings import Settings

# sets the screen size, score, font, inits a screen, inits pygame, etc..
settings = Settings()

pygame.time.set_timer(ADDENEMY, 250)
pygame.time.set_timer(ADDLIFE, 5000)
pygame.time.set_timer(ADDBOMB, 8000)


# Create the player
player = Player("assets/images/me.png", settings.WIDTH, settings.HEIGHT)
# Add player to all_sprites group
all_sprites.add(player)

clock = pygame.time.Clock()
clock_tick = 30
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

        # Add a new enemys
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy(settings.WIDTH, settings.HEIGHT)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDLIFE:
            life = Life("assets/images/Gem.png", settings.WIDTH, settings.HEIGHT)
            lives.add(life)
            all_sprites.add(life)

        elif event.type == ADDBOMB:
            new_bomb = Bomb("assets/images/bomb.png", settings.WIDTH, settings.HEIGHT)
            bombs.add(new_bomb)
            all_sprites.add(new_bomb)

    pressed_keys = pygame.key.get_pressed()
    # update player position/actions
    player.update(pressed_keys)
    # update enemy positions
    enemies.update()
    lives.update()
    bombs.update()

    if check_collisions(player, enemies, lives, bombs):
        running = False

    settings.increment_score(10)

    # render everything
    blit_that_shit(settings, player, all_sprites)

    # increase speed as score increases
    if settings.score % 3000 == 0:
        settings.increment_level()
        if clock_tick >= 90:
            clock_tick = 90
        else:
            clock_tick += 10

    clock.tick(clock_tick)

print(f"score: {settings.score}")
# print(f"lives: {player.lives}")

# Done! Time to quit.

pygame.quit()
