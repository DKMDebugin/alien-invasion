import pygame

class Ship():
    '''
    Ship() helps manage most of the behaviour of the player's ship
    '''
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        #initialize the parameters
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx #centerx attribute position game element at the top center. center & centery are other attri that can be used
        self.rect.bottom = self.screen_rect.bottom #postion game element at the bottom

        #Store a decimal value for the ships's center
        self.center = float(self.rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''
        Update the ship's position based on the movement flag.
        '''
        #Update the ship's center value, not the rect.
        if  self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
