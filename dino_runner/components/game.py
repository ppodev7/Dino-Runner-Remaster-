import pygame 
import sys 
import random
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, BG, GAME_OVER
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.player import Player
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.bird import Bird



class Game: 
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Chrome Dino Runner")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.jogando = True

        self.score = 0
        self.high_score = 0
        self.font = pygame.font.Font(None, 30)
        
        
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.all_sprites = pygame.sprite.Group()
        self.cloud_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        
        self.player = Player()
        self.all_sprites.add(self.player)
        
        for _ in range(5):
            cloud = Cloud()
            self.cloud_group.add(cloud)
            self.all_sprites.add(cloud)
        
        
    def execute (self):
        while self.jogando: 
            
            user_input = pygame.key.get_pressed()
            self.handle_events() # Verificar o que o jogador está fazendo
            self.update(user_input) # Mudança de estados
            self.draw()

            pygame.display.update()
            self.clock.tick(60)
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()

    def update(self, user_input):
        
        self.player.update(user_input)
        
        self.cloud_group.update(self.game_speed)
        
        self.score += 0.1
        
        self.update_background()
        self.spawn_obstacles()
        self.obstacle_group.update(self.game_speed)
        self.check_collision()
        
        
    def spawn_obstacles(self):
        if len(self.obstacle_group) == 0:
            # Escolhe aleatoriamente entre criar um Cacto ou um Pássaro
            obstacle = random.choice([Cactus(), Bird()])
            self.obstacle_group.add(obstacle)
            self.all_sprites.add(obstacle)
            
            
    def check_collision(self):
        if pygame.sprite.spritecollide(self.player, self.obstacle_group, False, pygame.sprite.collide_mask):
            
            if self.score > self.high_score:
                self.high_score = int(self.score)

            self.player.die()
            self.draw()
            
            game_over_rect = GAME_OVER.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(GAME_OVER, game_over_rect)
            draw_message_component(f"Sua Pontuação: {int(self.score)}", self.screen, pos_y_center=SCREEN_HEIGHT // 2 + 40)
            draw_message_component(f"Recorde: {int(self.high_score)}", self.screen, pos_y_center=SCREEN_HEIGHT // 2 + 90)
            
            pygame.display.update()
            pygame.time.delay(2300)
            
            self.jogando = False
        
    def draw_background(self):
        image_width = BG.get_width()
        
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))    
    
    
    
    def update_background(self):
        image_width = BG.get_width()
        self.x_pos_bg -= self.game_speed
        
        if self.x_pos_bg <= -image_width:
            self.x_pos_bg = 0    
    
    
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.draw_background()
        
        score_text = self.font.render(f"Pontos: {int(self.score)}", True, (0, 0, 0))
        text_rect = score_text.get_rect()
        text_rect.topright = (SCREEN_WIDTH - 20, 20)
        
        self.screen.blit(score_text, text_rect)
        
        self.all_sprites.draw(self.screen) 
        for laser in self.player.lasers: # Adiciona o desenho dos lasers na tela
            pygame.draw.rect(self.screen, self.player.laser_color, laser)

        