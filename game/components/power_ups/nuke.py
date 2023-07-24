
import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import NUKE, NUKE_TYPE

class Nuke(PowerUp):
    def __init__(self):
        super().__init__(NUKE, NUKE_TYPE)
        self.set_image()

    def set_image(self):
        self.image = pygame.image.load("Other/Nuke.2") 
        self.image = pygame.transform.scale(self.image, (80, 40))

    def activate(self, power_up_manager):
        self.start_time = pygame.time.get_ticks()
        power_up_manager.active_nuke = True
        power_up_manager.nuke_activation_time = self.start_time
        if power_up_manager.enemy_manager:
            power_up_manager.enemy_manager.spawn_enemies = False




