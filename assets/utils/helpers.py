import pygame

from .colors import LIGHT_MAIN, LIGHTER_MAIN, MAIN


def blit_that_shit(settings, player, all_sprites):
    settings.screen.fill(settings.BACKGROUND_COLOR)
    score_surface = settings.font.render(f"Score: {settings.score}", True, MAIN)
    level_surface = settings.font.render(f"Level: {settings.level}", True, LIGHT_MAIN)
    lives_surface = settings.font.render(f"Lives: {player.lives}", True, LIGHTER_MAIN)

    settings.screen.blit(
        score_surface, dest=(settings.WIDTH - 250, settings.HEIGHT - 80)
    )
    settings.screen.blit(
        lives_surface, dest=(settings.WIDTH - 250, settings.HEIGHT - 50)
    )
    settings.screen.blit(
        level_surface, dest=(settings.WIDTH - 250, settings.HEIGHT - 110)
    )
    # Draw all sprites
    for entity in all_sprites:
        settings.screen.blit(entity.surf, entity.rect)

    pygame.display.flip()


def check_collisions(player, enemies, lives, bombs):
    # Check if any enemies have collided with the player
    enemy_collision = pygame.sprite.spritecollideany(player, enemies)
    if enemy_collision:
        player.lives -= 1
        # print(player.lives)
        enemy_collision.kill()
        if player.lives <= 0:
            player.kill()
            # end the game
            return True

    life_collisions = pygame.sprite.spritecollideany(player, lives)
    if life_collisions:
        player.increment_lives(1)
        life_collisions.kill()

    bomb_collision = pygame.sprite.spritecollideany(player, bombs)
    if bomb_collision:
        bomb_collision.kill()
        # kill all enemies on the screen
        for enemy in enemies:
            enemy.kill()

    return False
