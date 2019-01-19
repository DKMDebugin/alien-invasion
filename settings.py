class Settings():
       """A class to store all settings for Alien Invasion."""
       def __init__(self):
           """Initialize the game's settings."""
           # Screen settings
           self.screen_width = 1200
           self.screen_height = 800
           self.bg_color = (169,169,169)
           #Ship Settings
           self.ship_speed_factor = 5.5
           #Bullet settings
           self.bullet_speed_factor = 7.5
           self.bullet_width = 3
           self.bullet_height = 15
           self.bullet_color = 128, 0, 0
           self.bullets_allowed = 3
