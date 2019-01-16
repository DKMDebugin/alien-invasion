import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if the quit event is triggered
            sys.exit() # exit game

        elif event.type == pygame.KEYDOWN: #When key is pressed
            if event.key == pygame.K_RIGHT: #if its the right arrow key
                #Move the ship to right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT: #if its the left arrow key
                #Move the ship to left
                ship.moving_left = True

        elif event.type == pygame.KEYUP: #When key is released
            if event.key == pygame.K_RIGHT: #if its the right arrow key
                ship.moving_right = False #stay put
            if event.key == pygame.K_LEFT: #if its the right arrow key
                ship.moving_left = False #stay put

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""

    screen.fill(ai_settings.bg_color) #Redraw the screen during each pass through the loop.
    ship.blitme() #Redraw ship at its current location
    pygame.display.flip() # Make the most recently drawn screen visible.
