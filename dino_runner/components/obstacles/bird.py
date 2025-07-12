import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    Y_POS_LIST = [250, 290] # Alturas alternadas de posições de vioo do pássaro

    def __init__(self):
        self.image_list = BIRD # Puxa as imgs do passaro
        y_pos = random.choice(self.Y_POS_LIST) # Escolhas alternativas das alturas dos pássaros

        # Pega a primeira imagem da lista para a inicialização
        # A classe Obstacle precisa de uma imagem no construtor.
        image = self.image_list[0]
        super().__init__(image)

        self.rect.y = y_pos
        self.step_index = 0

    def update(self, game_speed):
        # Animação do pássaro
        if self.step_index >= 10:
            self.step_index = 0
        self.image = self.image_list[self.step_index // 5]
        self.step_index += 1

        # Movimento do pássaro (mais rápido que o cenário)
        self.rect.x -= game_speed + 5

        if self.rect.right < 0:
            self.kill()
        
        

        