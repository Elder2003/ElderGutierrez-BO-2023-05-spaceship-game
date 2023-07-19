import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import DARK_HOLE, SCREEN_HEIGHT, SCREEN_WIDTH

class DarkHole(Sprite):
    Y_POS = 0
    X_POS_RANGE = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    SPEED_ON_Y = 7
    SPEED_ON_X = 6
    MOVES = {0: 'left', 1: 'right'}

    def __init__(self):
        self.image = DARK_HOLE
        self.direction = self.MOVES[random.randint(0, 1)]
        self.movement_count = 0
        self.moves_before_change = random.randint(20, 50)
        self.size_change_count = 0
        self.size_change_limit = random.randint(30, 70)

        random_size = random.randint(80, 120)
        self.image = pygame.transform.scale(self.image, (random_size, random_size))
        self.rect = self.image.get_rect(midtop=(random.choice(self.X_POS_RANGE), self.Y_POS))

    def update(self, enemies):
        self.rect.y += self.SPEED_ON_Y

        if self.direction == self.MOVES[0]:
            self.rect.x -= self.SPEED_ON_X
        elif self.direction == self.MOVES[1]:
            self.rect.x += self.SPEED_ON_X

        self.handle_direction()
        self.size_change()

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

    def size_change(self):
        self.size_change_count += 1

        if self.size_change_count >= self.size_change_limit:
            self.size_change_count = 0
            self.random_size()

    def random_size(self):
        random_size = random.randint(80, 120)
        self.image = pygame.transform.scale(DARK_HOLE, (random_size, random_size))
        self.rect = self.image.get_rect(midtop=self.rect.midtop)
