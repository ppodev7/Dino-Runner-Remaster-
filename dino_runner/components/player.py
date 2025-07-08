import pygame 
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DUCKING_SHIELD, ICON


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.dino_run = RUNNING
        self.dino_jump = JUMPING
        self.dino_duck = DUCKING
        self.dino_duck_shield = DUCKING_SHIELD
        self.step_index = 0
        self.image = ICON
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 310

        self.is_running = True
        self.is_jumping = False
        self.is_ducking = False
        
        self.jump_vel = 8.5
    
    
    def run (self):
        self.image = self.dino_run[self.step_index // 5]
        
        self.rect.y = 310
        self.step_index += 1
        
        if self.step_index >= 10:
            self.step_index = 0
    
    def jump (self):
        self.image = self.dino_jump
        
        self.rect.y -= self.jump_vel * 4
        self.jump_vel -= 0.8
        
        if self.jump_vel < -8.5:
            self.is_jumping = False
            self.jump_vel = 8.5 

    def duck (self):
        self.image = self.dino_duck[self.step_index // 5]
        
        self.rect.y = 340
        self.step_index += 1
        
        if self.step_index >= 10:
            self.step_index = 0
    
    
    def shoot (self):
        pass
    
    
    def update (self, user_input):
        
        if self.is_running:
            self.run()
        elif self.is_jumping:
            self.jump()
        elif self.is_ducking:
            self.duck()
        
        # State transitions based on user input.
        # The jump state is handled by the jump() method, so we only check for other inputs if not jumping.
        if not self.is_jumping:
            if user_input[pygame.K_UP]:
                self.is_jumping = True
                self.is_running = False
                self.is_ducking = False
            elif user_input[pygame.K_DOWN]:
                self.is_ducking = True
                self.is_running = False
            else:
                self.is_running = True
                self.is_ducking = False

    
    def draw (self, screen):
        screen.blit(self.image, self.rect)
    
