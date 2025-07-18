import pygame
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Notification(pygame.sprite.Sprite):
    def __init__(self, message, font, color=(0, 0, 0)):
        super().__init__()
        self.image = font.render(message, True, color)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        
        
        self.lifetime = 70
        
        
    def update(self):
        self.lifetime -= 1
        
        if self.lifetime <= 0:
            self.kill()
