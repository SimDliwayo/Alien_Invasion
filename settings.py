class Settings:

    def __init__(self):
        """Initializing settings of the game"""
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # The speed of the spaceship
        self.ship_speed = .8
        self.alien_speed = .3
        self.fleet_drop_speed = 5
        # Fleet direction 1 represent right, and fleet direction - 1 represent left
        self.fleet_dir = 1

        # bullet settings
        self.bullet_speed = 0.2
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (20, 20, 20)
        self.bullets_allowed = 3
