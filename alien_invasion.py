import sys
import pygame

from settings import Settings

def run_game():
    '''
    Initialize pygame ,
    create a screen object
    (window screen size & window caption) & settings
    '''
    pygame.init()
    ai_settings = Settings() #Object of Settings() class
    screen = pygame.display.set_mode(
    (ai_settings.scree_width, ai_settings.screen_height)) #set screen size by passing in Settings width & height attributes
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230) # Set the background color.

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        # Make the most recently drawn screen visible.
        pygame.display.flip()
run_game()
