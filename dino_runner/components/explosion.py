import pygame

from dino_runner.utils.constants import EXPLOSION


class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.image = EXPLOSION
        
        self.rect = self.image.get_rect(center=pos)
        
        self.lifetime = 15 
        
    
    def update(self):
        self.lifetime -= 1
        
        if self.lifetime <= 0:
            self.kill()