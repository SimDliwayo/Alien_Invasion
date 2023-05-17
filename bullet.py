import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):
        """Create a bullet object at the position the spaceship is on"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Creating a rect object at (0,0) and setting it the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.spaceship.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal value of the bullet's position
        self.y -= self.settings.bullet_speed

        # Update the rect's position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)