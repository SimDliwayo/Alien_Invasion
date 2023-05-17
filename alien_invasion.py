import sys

import pygame

from settings import Settings
from spaceship import SpaceShip
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Initialize the game"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_height = self.screen.get_rect().height
        # self.settings.screen_width = self.screen.get_rect().width
        """Display screen to the user"""
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("AmaALien Afikile")

        # Adding instances to the game/screen
        self.spaceship = SpaceShip(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        """Set the colour background for your screen"""
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """This is a while loop for the game and updating the screen"""
        while True:
            # Helper method for handling screen updates and events
            self._check_events_()
            self.spaceship.update()
            self._update_bullets()
            self._update_aliens()
            self.bullets.update()

            self._update_screen_()

    def _check_events_(self):
        # Event listener for keyboard/mouse reactions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key press"""
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key release"""
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and free memory from bullets thats have disappeared"""
        # Update bullets position.
        self.bullets.update()

        # Free memory off bullets that have disappeared from screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _update_aliens(self):
        """If the fleet is at an edge then update the position of all the aliens"""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        # Creating an alien and find the number of aliens in row.
        # Spacing between aliens is equals to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        spaceship_height = self.spaceship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - spaceship_height)
        number_rows = available_space_y // (3 * alien_height)

        for row_number in range(number_rows):
            for number_alien in range(number_aliens_x):
                self._create_alien(number_alien, row_number)

    def _create_alien(self, number_alien, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * number_alien
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_dir()
                break

    def _change_fleet_dir(self):
        """Drop the fleet and change the direction of the fleet"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_dir *= - 1

    def _update_screen_(self):
        # Updating image to the screen and flip to new screen
        self.screen.fill(self.bg_color)
        self.spaceship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

































