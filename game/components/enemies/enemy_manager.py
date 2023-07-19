import pygame
from game.components.enemies.enemy import Enemy
from game.components.enemies.rocks import Rocks
from game.components.enemies.dark_holes import DarkHole

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.rocks = []
        self.dark_holes = []

    def update(self):
        self.add_enemy()
        self.add_rock()
        self.add_dark_holes()

        for enemy in self.enemies:
            enemy.update(self.enemies)

        for rock in self.rocks:
            rock.update(self.rocks)

        for dark_hole in self.dark_holes:
            dark_hole.update(self.dark_holes)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen) 

        for rock in self.rocks:
            rock.draw(screen)

        for dark_hole in self.dark_holes:
            dark_hole.draw(screen)  

    def add_enemy(self):
        if len(self.enemies) < 2:
            enemy = Enemy()
            self.enemies.append(enemy)

    def add_rock(self):
        if len(self.rocks) < 5 and len(self.dark_holes) == 1:
            rock = Rocks()
            self.rocks.append(rock)

    def add_dark_holes(self):
        if len(self.dark_holes) < 1:
            dark_hole = DarkHole()
            self.dark_holes.append(dark_hole)
