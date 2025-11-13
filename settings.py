class Settings :
    def __init__(self):
        # Screen settings 
        self.screen_width = 1400
        self.screen_height = 1000

        # Ship's speed 
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (225, 165, 0)
        self.bullets_allowed = 3

        # Alien's settings 
        self.alien_speed = 1.0
        self.fleet_drop_speed = 3
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1