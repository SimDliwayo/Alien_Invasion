import pygame


class SpaceShip:

    def __init__(self, ai_game):
        """Initialise the ship and get its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """Load the image..."""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()


        """Place the rocket to the bottom of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom

        # storing the decimal value for the spaceship's horizontal position
        self.x = float(self.rect.x)

        # Flag for movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the position of the spaceship according to movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Updating rect object from self.x.
        self.rect.x = self.x

    """Each and everytime the screen restart the ship should appear"""
    def blitme(self):
        self.screen.blit(self.image, self.rect)
