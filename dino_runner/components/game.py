import pygame 
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Dino Runner Trigger")
        self.clock = pygame.time.Clock()
        self.running = True

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill ((0, 0, 0))
            pygame.display.update()
            self.clock.tick(60)
    
        pygame.quit()