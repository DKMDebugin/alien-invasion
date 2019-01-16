import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if the quit event is triggered
            sys.exit() # exit game

        elif event.type == pygame.KEYDOWN: #When key is pressed
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP: #When key is released
            check_keyup_events(event, ship)

def check_keydown_events(event, ship):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""

    screen.fill(ai_settings.bg_color) #Redraw the screen during each pass through the loop.
    ship.blitme() #Redraw ship at its current location
    pygame.display.flip() # Make the most recently drawn screen visible.
