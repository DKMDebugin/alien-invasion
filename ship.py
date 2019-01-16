import pygame

class Ship():
    '''
    Ship() helps manage most of the behaviour of the player's ship
    '''
    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx #centerx attribute position game element at the center. center & centery are other attri that can be used
        self.rect.bottom = self.screen_rect.bottom #postion game element at the bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
