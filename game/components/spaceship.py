import pygame 
from pygame.sprite import Sprite
from game.components import game

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE
from game.components.bullets.bullet import Bullet

# la clase Spaceship va a heredad la clase Sprite
class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    SPACESHIP_POS_X = SCREEN_WIDTH / 2
    SPACESHIP_POS_Y = 550 


    def __init__(self):
        self.image = SPACESHIP 
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom = (self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))
        self.type = 'player'
        self.has_power_up = False
        self.power_up_type = DEFAULT_TYPE
        self.power_up_time_up = 0

    def update(self, user_input, game):
        if user_input[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 10
        elif user_input[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10     
        elif user_input[pygame.K_RIGHT]:
            self.rect.x += 10
            if self.rect.centerx > SCREEN_WIDTH:
                self.rect.left = 0
        elif user_input[pygame.K_LEFT]:
            self.rect.x -= 10
            if self.rect.centerx < 0:
                self.rect.right = SCREEN_WIDTH
        if user_input[pygame.K_q]:
            self.shoot(game.bullet_manager)


    def draw(self, screen):
        screen.blit(self.image, self.rect)   

    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)  

    def set_image(self, image = SPACESHIP, size = (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def reset(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom = (self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))  



