import pygame 
from dino_runner.utils.constants import (RUNNING, JUMPING, DUCKING, DEAD, RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.dino_run = RUNNING 
        self.dino_jump = JUMPING
        self.dino_duck = DUCKING
        self.dino_dead = DEAD
        self.dino_run_shield = RUNNING_SHIELD
        self.dino_jump_shield = JUMPING_SHIELD
        self.dino_duck_shield = DUCKING_SHIELD
        
        self.step_index = 0
        
        # Retângulo de colisão
        self.image = self.dino_run[0]
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 310

        self.is_running = True
        self.is_jumping = False
        self.is_ducking = False
        
        self.is_shielded = False 
        self.shield_time = 0
        self.birds_killed_count = 0 # Lógica para a ativaçõa do escudo 
        
        self.jump_vel = 5.5 # Valor inicial do pulo
        
        #lasers
        self.bullet_count = 0
        self.lasers = []
        self.laser_speed = 15 
        self.laser_color = (255, 0, 0)
    
    def run (self):
        
        image_list = self.dino_run_shield if self.is_shielded else self.dino_run
        self.image = image_list[self.step_index // 5]
        
        self.rect.y = 310
        self.step_index += 1
        
        if self.step_index >= 10:
            self.step_index = 0
    
    def jump (self):
        self.image = self.dino_jump_shield if self.is_shielded else self.dino_jump
        
        self.rect.y -= self.jump_vel * 4
        self.jump_vel -= 0.4

    def duck (self):
        image_list = self.dino_duck_shield if self.is_shielded else self.dino_duck
        self.image = image_list[self.step_index // 5] # Cuida da animação
        
        self.rect.y = 340
        self.step_index += 1
        
        if self.step_index >= 10:
            self.step_index = 0
    
    
    def shoot (self):
        # Apenas atira se o jogador tiver balas.
        if self.bullet_count > 0:
            laser_rect = pygame.Rect(self.rect.right, self.rect.centery - 2, 20, 4)
            self.lasers.append(laser_rect)
            self.bullet_count -= 1
            return True
        return False
            
    def die(self):
        self.image = self.dino_dead
        self.rect.y = 310
        
    def activate_shield(self):
        self.is_shielded = True
        self.shield_time = 300
    
    
    def update (self, user_input, game_speed):
        
        if self.is_shielded:
            self.shield_time -= 1 # Diminuição do shield a cada segundo
            if self.shield_time <= 0:
                self.is_shielded = False
                
        
        if user_input [pygame.K_UP] and not self.is_jumping:
            self.is_running = False
            self.is_jumping = True
            self.is_ducking = False
            # A força do pulo agora depende da velocidade do jogo!

            self.jump_vel = 5.5 + (game_speed - 10) * 0.05
        elif user_input [pygame.K_DOWN] and not self.is_jumping:
            self.is_running = False
            self.is_jumping = False
            self.is_ducking = True
        elif not (self.is_jumping  or user_input[pygame.K_DOWN]):
            self.is_running = True
            self.is_jumping = False
            self.is_ducking = False
        
            
        if self.is_running:
            self.run()
        elif self.is_jumping:
            self.jump()
        elif self.is_ducking:
            self.duck()


        if self.is_jumping and self.rect.y >= 310:
            self.rect.y = 310
            self.is_jumping = False

          
        
        for laser in self.lasers:
            laser.x += self.laser_speed
            
            
        self.lasers = [laser for laser in self.lasers if laser.x < 1200]
        
    
