import pygame

class Player:
    PLAYER_X_POS = 80
    PLAYER_Y_POS = 310
    PLAYER_Y_POS_DUCK = 340

    def __init__(self):
        self.run_images = [
            pygame.image.load('dino_runner/assets/Dino/DinoRun1.png'),
            pygame.image.load('dino_runner/assets/Dino/DinoRun2.png')
        ]
        self.duck_images = [
            pygame.image.load('dino_runner/assets/Dino/DinoDuck1.png'),
            pygame.image.load('dino_runner/assets/Dino/DinoDuck2.png')
        ]

        self.is_ducking = False
        self.is_running = True

        self.step_index = 0

        self.image = self.run_images[self.step_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.PLAYER_X_POS
        self.rect.y = self.PLAYER_Y_POS

    def update(self, user_input): 
        if user_input[pygame.K_DOWN]:
            self.is_ducking = True
            self.is_running = False
        else:
            self.is_ducking = False
            self.is_running = True

        self.animate()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def animate(self):
        animation_speed = 5
        if self.is_ducking:
            self.image = self.duck_images[self.step_index // animation_speed]
            self.rect.y = self.PLAYER_Y_POS_DUCK
        elif self.is_running:
            self.image = self.run_images[self.step_index // animation_speed]
            self.rect.y = self.PLAYER_Y_POS
        self.step_index += 1

        if self.step_index >= (len(self.run_images) * animation_speed):
            self.step_index = 0
