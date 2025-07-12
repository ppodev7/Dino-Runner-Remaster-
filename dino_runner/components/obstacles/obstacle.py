import pygame
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed):
        self.rect.x -= game_speed
        
        if self.rect.right < 0:
            self.kill()
        