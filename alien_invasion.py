import pygame
from pygame.sprite import Group

from settings import Settings
from background import Background
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_function as gf

def run_game():
    '''
    Initialize pygame ,
    create a screen object
    (window screen size & window caption) & settings
    '''
    pygame.init()
    ai_settings = Settings() #Object of Settings() class
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height)) #set screen size by passing in Settings width & height attributes
    pygame.display.set_caption("Alien Invasion")

    #initialize Bbackgroup picture
    background = Background()
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    # Create an instance to store game statistics and scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Make a ship, a group of bullets & a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship,
            aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, background, screen, stats, sb, ship,
            aliens, bullets, play_button)




run_game()
