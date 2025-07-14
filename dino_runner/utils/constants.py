import pygame
import os

# Inicializa o pygame e cria uma tela "fantasma" para permitir a conversão de imagens
# com transparência (.convert_alpha()) antes da janela principal do jogo ser criada.
pygame.init()
_ = pygame.display.set_mode((1, 1), pygame.NOFRAME)

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 60
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png")).convert_alpha()

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")).convert_alpha(),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")).convert_alpha(),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")).convert_alpha(),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png")).convert_alpha()
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png")).convert_alpha()
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png")).convert_alpha()

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")).convert_alpha(),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")).convert_alpha(),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")).convert_alpha(),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")).convert_alpha(),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")).convert_alpha(),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")).convert_alpha(),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png')).convert_alpha()
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png')).convert_alpha()
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png')).convert_alpha()

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png')).convert_alpha()

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png')).convert_alpha()

DEAD = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDead.png')).convert_alpha()

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png')).convert_alpha()

RESTART = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png')).convert_alpha(), (60, 60)) 

EXPLOSION = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Other/explosion.png')).convert_alpha(), (100, 100)) 

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
