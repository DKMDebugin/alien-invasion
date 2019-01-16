import pygame

from settings import Settings
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

    #Make a ship
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        gf.check_events()# Watch for keyboard and mouse events.
        #Update images on the screen and flip to the new screen.
        gf.update_screen(ai_settings, screen, ship)




run_game()
