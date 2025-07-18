import pygame 
import sys 
import random
import os

from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BG, GAME_OVER, RESTART
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.player import Player
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.explosion import Explosion 
from dino_runner.components.notification import Notification 

os.environ['SDL_VIDEO_CENTERED'] = '1' #centraliza a janela no meio da tela 

class Game: 
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(0)
        pygame.display.set_caption("Chrome Dino Runner")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.jogando = True
        
        assets_path = os.path.join(os.path.dirname(__file__), '..', 'assets')
        sound_path = os.path.join(assets_path, 'Sound')
        font_path = os.path.join(assets_path, 'Font', 'fonte.ttf')

        pygame.mixer.music.load(os.path.join(sound_path, 'music.mp3'))
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1) 

        self.laser_sound = pygame.mixer.Sound(os.path.join(sound_path, 'laser.mp3'))
        self.laser_sound.set_volume(0.3)
        self.explosion_sound = pygame.mixer.Sound(os.path.join(sound_path, 'explosion.mp3'))
        self.explosion_sound.set_volume(0.2)

        self.score = 0
        self.high_score = 0
        self.font = pygame.font.Font(font_path, 15)

        self.score_milestone = 100
        self.bullet_milestone = 100
        
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 380 
        self.game_state = "start"  # Adiciona o estado do jogo
        self.all_sprites = pygame.sprite.Group()
        self.cloud_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.explosion_group = pygame.sprite.Group()
        # Cria um grupo para gerenciar as notificações na tela.
        self.notification_group = pygame.sprite.Group()
        
        self.player = Player()
        self.all_sprites.add(self.player)
        
        for _ in range(5):
            cloud = Cloud()
            self.cloud_group.add(cloud)
            self.all_sprites.add(cloud)
        
        
    def reset(self):
        self.score = 0
        self.game_speed = 10
        self.score_milestone = 100
        self.x_pos_bg = 0
        self.bullet_milestone = 100
        self.y_pos_bg = 380 
        
        self.obstacle_group.empty()
        self.cloud_group.empty()
        self.all_sprites.empty()
        self.explosion_group.empty()
        self.notification_group.empty()
        
        self.player = Player()
        self.all_sprites.add(self.player)
        for _ in range(5):
            cloud = Cloud()
            self.cloud_group.add(cloud)
            self.all_sprites.add(cloud)
        
        self.game_state = "playing" 
        
    def execute (self):
        while self.jogando: 
            
            user_input = pygame.key.get_pressed()
            
            if self.game_state == "start":
                self.draw_start_screen()
                self.handle_start_events()
            elif self.game_state == "playing":
                self.handle_events() # Verificar o que o jogador está fazendo
                self.update(user_input) # Mudança de estados
                self.draw()
            elif self.game_state == "game_over": # Atualiza o game over aqui
                self.draw_game_over_screen() # Chama para desenhar a tela de game over
                self.handle_game_over_events()

            pygame.display.update()
            self.clock.tick(60)
            
    def handle_start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.player.shoot():
                    self.laser_sound.play()

    def update(self, user_input):
        
        self.player.update(user_input, self.game_speed)
        
        self.cloud_group.update(self.game_speed)
        
        self.score += 0.1
        self.check_milestone()
        # Chama o novo método para verificar se o jogador deve ganhar balas.
        self.check_bullet_milestone()
        
        self.update_background()
        self.spawn_obstacles()
        self.obstacle_group.update(self.game_speed)
        self.explosion_group.update()
        # Atualiza o estado de todas as notificações (para fazê-las desaparecer).
        self.notification_group.update()
        self.check_laser_collision()
        self.check_collision()
        
        
    def spawn_obstacles(self):
        if len(self.obstacle_group) == 0:
            # Escolhe aleatoriamente entre criar um Cacto ou um Pássaro
            obstacle = random.choice([Cactus(), Bird()])
            self.obstacle_group.add(obstacle)
            self.all_sprites.add(obstacle)
            
    def check_milestone(self):
        if self.score >= self.score_milestone:
            
            self.game_speed += 1
            self.score_milestone += 50
            
    def check_bullet_milestone(self):
        # Verifica se a pontuação atual atingiu o marco para ganhar balas.
        if self.score >= self.bullet_milestone:
            
            self.player.bullet_count += 5
            
            self.bullet_milestone += 100
            
            notification = Notification("Ganhou 5 lasers!", font=self.font)
            self.all_sprites.add(notification)
            self.notification_group.add(notification)
            
            
    def check_laser_collision(self):
        for laser in self.player.lasers[:]:
            # Verifica se o laser colidiu com algum obstáculo.
            for obstacle in self.obstacle_group:
                if laser.colliderect(obstacle.rect):
                    # A colisão só importa se o obstáculo for um pássaro.
                    if isinstance(obstacle, Bird):
                        # Remove o pássaro e o laser.
                        obstacle.kill()
                        self.explosion_sound.play()
                        self.player.lasers.remove(laser)
                        # Cria uma instância da classe Explosion na posição do pássaro.
                        explosion = Explosion(obstacle.rect.center)
                        self.all_sprites.add(explosion)
                        self.explosion_group.add(explosion)

                        
                        self.player.birds_killed_count += 1
                        if self.player.birds_killed_count >= 3:
                            self.player.birds_killed_count = 0  
                            self.player.activate_shield()
                            
                            notification = Notification("Escudo ativado (5s)!", font=self.font)
                            self.all_sprites.add(notification)
                            self.notification_group.add(notification)
                        break

    def check_collision(self):
        if (
            self.game_state == "playing" and  # Verifica se o jogo está em andamento
            not self.player.is_shielded and 
            pygame.sprite.spritecollide(self.player, self.obstacle_group, False, pygame.sprite.collide_mask)
        ):
            if self.score > self.high_score:
                self.high_score = int(self.score)
            self.player.die()
            self.game_state = "game_over"  # Muda o estado para game over
            self.draw_game_over_screen()  # Desenha a tela de game over
            
    def draw_start_screen(self):
        self.screen.fill((255, 255, 255))

        # Lista de instruções para exibir na tela inicial
        instructions = [
            "Pressione ESPAÇO para começar!",
            "", 
            "A cada 100 pontos ganhe 5 lasers!",
            "A cada 3 pássaros mortos o dino fica invencível por 5 segundos",
            "Pressione ESPAÇO durante o jogo para atirar",
            "Use as setas para abaixar e pular!",
            "Você vai evoluindo, o jogo vai ficando mais frenético!"
        ]

        line_spacing = 40  # Espaçamento vertical entre as linhas de texto
        middle_index = len(instructions) // 2  # Encontra o índice da linha central

        # Itera sobre a lista para desenhar cada linha de instrução
        for i, line in enumerate(instructions):
            # Calcula a posição Y para cada linha para centralizar o bloco de texto
            offset = (i - middle_index) * line_spacing
            y_pos = (SCREEN_HEIGHT // 2) + offset
            draw_message_component(line, self.screen, font=self.font, pos_y_center=y_pos)
            
        pygame.display.update()

    def draw_game_over_screen(self):
        self.screen.fill((255, 255, 255))  # Limpa a tela

        # Desenha a imagem de Game Over
        game_over_rect = GAME_OVER.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
        self.screen.blit(GAME_OVER, game_over_rect)

        draw_message_component(f"Sua Pontuação: {int(self.score)}", self.screen, font=self.font, pos_y_center=SCREEN_HEIGHT // 2)
        draw_message_component(f"Recorde: {int(self.high_score)}", self.screen, font=self.font, pos_y_center=SCREEN_HEIGHT // 2 + 40)

         # Desenha a imagem de reinício
        restart_rect = RESTART.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        self.screen.blit(RESTART, restart_rect)

    def handle_game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()  # Reinicia o jogo
        
    def draw_background(self):
        image_width = BG.get_width()  
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))  
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))      
    
    def update_background(self):
        image_width = BG.get_width()
        self.x_pos_bg -= self.game_speed
        
        if self.x_pos_bg <= -image_width:
            self.x_pos_bg = 0    
    
    
    def draw(self) -> list[pygame.Rect]:
        self.screen.fill((255, 255, 255))
        self.draw_background()
        
        # Desenha e armazena o retângulo da pontuação
        score_text = self.font.render(f"Pontos: {int(self.score)}", True, (0, 0, 0))
        score_rect = score_text.get_rect()
        score_rect.topright = (SCREEN_WIDTH - 20, 20)
        self.screen.blit(score_text, score_rect)
        
        # Desenha e armazena o retângulo da contagem de lasers
        bullet_text = self.font.render(f"Lasers: {self.player.bullet_count}", True, (0, 0, 0))
        bullet_rect = bullet_text.get_rect()
        bullet_rect.topleft = (20, 20)
        self.screen.blit(bullet_text, bullet_rect)
        
        self.all_sprites.draw(self.screen) 
        for laser in self.player.lasers:
            pygame.draw.rect(self.screen, self.player.laser_color, laser)

        # Retorna a lista de retângulos que foram modificados
        return [
            self.player.rect,
            * [obstacle.rect for obstacle in self.obstacle_group], # "*" = add varios itens de uma lista
            * [cloud.rect for cloud in self.cloud_group],
            * [explosion.rect for explosion in self.explosion_group],
            * [notification.rect for notification in self.notification_group],
            score_rect,
            bullet_rect,
        ]