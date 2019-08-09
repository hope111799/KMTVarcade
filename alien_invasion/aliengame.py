# -------------------Attribution Section Started------------------------------
# Code created with the help Rahul Goswami
#
# Accessed through github at https://github.com/goswami-rahul/alien-invasion-game
# 
# --------------------Attribution Section Ended-----------------------------
import pygame

import game_functions as gf
from game_items import GameItems
from game_stats import GameStats
from settings import Settings

# FPS = 60

def main():

    FPS = 60

    # Initialize game, settings and create a screen object.
    pygame.init()
    fps_clock = pygame.time.Clock()
    ai_settings = Settings()

    # Create statistics.
    stats = GameStats(ai_settings)

    # Create game items.
    game_items = GameItems(ai_settings, stats)

    # Create a fleet of aliens.
    gf.create_fleet(ai_settings, game_items)

    # Start the main loop for the game.
    while True:

        stats.time_passed = fps_clock.tick(FPS) / 1000  # Time in seconds since previous loop.

        gf.check_events(ai_settings, stats, game_items)

        if stats.game_active:
            game_items.ship.update(stats)
            gf.update_bullets(ai_settings, stats, game_items)
            gf.update_aliens(ai_settings, stats, game_items)

        gf.update_screen(ai_settings, stats, game_items)


if __name__ == '__main__':
    main()
