import pygame 
from pygame.sprite import Sprite 

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

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

    def update(self, user_input):
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


    def draw(self, screen):
        screen.blit(self.image, self.rect)   
