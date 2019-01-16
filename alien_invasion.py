import sys
import pygame

from settings import Settings
from ship import Ship

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

    bg_color = (230, 230, 230) # Set the background color.

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color) #Redraw the screen during each pass through the loop.
        ship.blitme() #Redraw ship at its current location
        pygame.display.flip() # Make the most recently drawn screen visible.
run_game()
