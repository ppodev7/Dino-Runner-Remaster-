import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


def draw_message_component(
    message,
    screen,
    font,  
    font_color=(0, 0, 0),
    font_size=None,  
    pos_y_center=SCREEN_HEIGHT // 2,
    pos_x_center=SCREEN_WIDTH // 2,
):
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text, text_rect)