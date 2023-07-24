import random

import pygame
from game.components.enemies.enemy import Enemy
from game.components.enemies.rocks import Rocks
from game.components.enemies.dark_holes import DarkHole
from game.utils.constants import SHIELD_TYPE
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.rocks = []
        self.dark_holes = []
        self.enemy_images = [ENEMY_1, ENEMY_2, ENEMY_3]
        self.spawn_enemies = True
        self.nuke_deactivation_time = 0
        self.nuke_effect_duration = 10000

    def update(self, game):
        if not self.spawn_enemies:
            current_time = pygame.time.get_ticks()
            if current_time - self.nuke_deactivation_time >= self.nuke_effect_duration:
                self.spawn_enemies = True

        self.add_enemy()
        self.add_rock()
        self.add_dark_holes()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

        for rock in self.rocks:
            rock.update(self.rocks)
            if rock.rect.colliderect(game.player.rect):
                if game.player.power_up_type != SHIELD_TYPE:
                    game.death_counter.update()
                    game.playing = False
                    pygame.time.delay(500)
                    break

        for dark_hole in self.dark_holes:
            dark_hole.update(self.dark_holes)
            if dark_hole.rect.colliderect(game.player.rect):
                if game.player.power_up_type != SHIELD_TYPE:
                    game.death_counter.update()
                    game.playing = False
                    pygame.time.delay(500)
                    break

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

        for rock in self.rocks:
            rock.draw(screen)

        for dark_hole in self.dark_holes:
            dark_hole.draw(screen)

    def add_enemy(self):
        if self.spawn_enemies and len(self.enemies) < 2:
            image = random.choice(self.enemy_images)
            speed_on_x = random.randint(10, 20)
            speed_on_y = random.randint(1, 5)
            enemy = Enemy(image, speed_on_x, speed_on_y)
            self.enemies.append(enemy)

    def add_rock(self):
        if len(self.rocks) < 3 and len(self.dark_holes) == 0:
            rock = Rocks()
            self.rocks.append(rock)

    def add_dark_holes(self):
        if len(self.dark_holes) < 1:
            dark_hole = DarkHole()
            self.dark_holes.append(dark_hole)

    def reset(self):
        self.enemies = []
        self.dark_holes = []
        self.rocks = []

       