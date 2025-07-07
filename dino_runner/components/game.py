import pygame

from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS # Importa da pasta constants as constantes já definidas
from dino_runner.components.player.player import Player # Importa o arquivo player para a implementação dele no jogo. 

class Game: # Planta 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Function do pygame que adiciona as dimensões da tela 
        pygame.display.set_caption("Dino Runner Trigger") # Nomeia a janela
        self.clock = pygame.time.Clock() # Define o fps (que no caso está no final)
        self.player = Player()
        self.running = True

    def execute(self): # Função da exec do game 
        while self.running:
            for event in pygame.event.get(): # A cada evento, faça algo. Apenas se o jogador quiser quitar faça
                if event.type == pygame.QUIT: # -> 
                    self.running = False # Para de correr quando o jogador quitar 

            user_input = pygame.key.get_pressed() # -> Entrada do usuário, a tcle estará pressinada

            self.screen.fill((0, 0, 0))  # Fundo branco

            self.player.update(user_input) # Atualiza a entrada do usuário 
            self.player.draw(self.screen) # "Desenha" o usuário na tela 

            pygame.display.update() # Atualiza a tela
            self.clock.tick(FPS) # -> Nesse caso o FPS está definido em Utils

        pygame.quit()