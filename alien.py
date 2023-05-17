import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    """Initialize the character and set its starting position"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the image to the screen and set the location.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start the alien in the top corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Give the alien position to a decimal
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move alien right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_dir)
        self.rect.x = self.x