import sys 
import pygame 
from settings import Settings 
from ship import Ship, SmallAlien
from bullet import Bullet

class AlienInvasion:

    ''' Overall class to manage game assets and behavior.'''

    def __init__(self):
        ''' Initialize the game, and create resources. '''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings() #Instance of Settings class

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.background_image = pygame.image.load('background.bmp').convert()
        self.full_background = pygame.transform.scale(self.background_image,self.screen.get_size())

        # Allows full screen mode. Just redefine self.screen with the code below 
        ''' 
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_width = self.screen.get_rect().height
        '''

        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _check_events (self): # Captures the user input via an event queue through pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)  


    def _check_keydown_events (self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        elif event.key == pygame.K_q:
            sys.exit()
             

    def _check_keyup_events (self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _update_bullets (self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _fire_bullet (self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _create_fleet (self):
        alien = SmallAlien (self)
        self.aliens.add(alien)
        alien_width = alien.rect.width

        current_x = alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            new_alien = SmallAlien(self)
            new_alien.x = current_x
            new_alien.rect.x = current_x
            self.aliens.add(new_alien)
            current_x += 2 * alien_width

    def _update_screen(self):
        self.screen.blit(self.full_background, (0,0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

    def run_game (self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self._update_bullets()
            self.aliens.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
            ''' 
            When we move the game elements around, pygame.display
            .flip() continually updates the display to show the new positions of game
            elements and hide the old ones, creating the illusion of smooth movement.
            '''
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

