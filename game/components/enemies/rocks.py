import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import ROCK, SCREEN_HEIGHT, SCREEN_WIDTH

class Rocks(Sprite):
    
    Y_POS = 100
    X_POS_RANGE = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    SPEED_ON_Y = 10
    SPEED_ON_X = 6
    MOVES = {0: 'left', 1: 'right'}

    def __init__(self):
        self.image = ROCK
        self.rect = self.image.get_rect(midtop=(random.choice(self.X_POS_RANGE), self.Y_POS))
        self.direction = self.MOVES[random.randint(0, 1)]
        self.movement_count = 0
        self.moves_before_change = random.randint(20, 40)
        self.random_size()

    def update(self, enemies):
        self.rect.y += self.SPEED_ON_Y

        if self.direction == self.MOVES[0]:
            self.rect.x -= self.SPEED_ON_X
        elif self.direction == self.MOVES[1]:
            self.rect.x += self.SPEED_ON_X

        self.handle_direction()

        if self.rect.top > SCREEN_HEIGHT:
            enemies.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_direction(self):
        self.movement_count += 1

        if (self.movement_count >= self.moves_before_change and self.direction == self.MOVES[1]) or self.rect.right >= SCREEN_WIDTH:
            self.direction = self.MOVES[0]
        elif self.movement_count >= self.moves_before_change and self.direction == self.MOVES[0] or self.rect.left <= 0:
            self.direction = self.MOVES[1]

        if self.movement_count >= self.moves_before_change:
            self.movement_count = 0

    def random_size(self):
        random_width = random.randint(20, 40)
        random_height = random_width 
        self.image = pygame.transform.scale(ROCK, (random_width, random_height))
        self.rect = self.image.get_rect(midtop=self.rect.midtop)
