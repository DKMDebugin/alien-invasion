class Settings():
       """A class to store all settings for Alien Invasion."""
       def __init__(self):
           """Initialize the game's settings."""
           # Screen settings
           self.screen_width = 1200
           self.screen_height = 800
           self.bg_color = (169,169,169)
           #Ship Settings
           self.ship_limit = 3
           #Bullet settings
           self.bullets_allowed = 3
           # Alien settings
           self.fleet_drop_speed = 10

           # How quickly the game speeds up
           self.speedup_scale = 1.2
           self.initialize_dynamic_settings()

       def  initialize_dynamic_settings(self):
            """Initialize settings that change throughout the game."""
            self.ship_speed_factor = 5
            self.bullet_speed_factor = 7
            self.alien_speed_factor = 5

            # fleet_direction of 1 represents right; -1 represents left.
            self.fleet_direction = 1

       def increase_speed(self):
            """Increase speed settings."""
            self.ship_speed_factor *= self.speedup_scale
            self.bullet_speed_factor *= self.speedup_scale
            self.alien_speed_factor *= self.speedup_scale
