import pygame 
import sys 
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.components.player import Player



class Game: 
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Chrome Dino Runner Trigger")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.jogando = True
        # Usar um grupo de sprites facilita o gerenciamento de múltiplos objetos (jogador, obstáculos, nuvens).
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

    def execute (self):
        while self.jogando: 
            self.handle_events() # Verificar o que o jogador está fazendo

            user_input = pygame.key.get_pressed()
            self.update(user_input) # Mudança de estados 
            self.draw()

            self.clock.tick(60)
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self, user_input):
        
        self.all_sprites.update(user_input)
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        
        self.all_sprites.draw(self.screen)
        pygame.display.update()