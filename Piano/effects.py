import pygame
from settings import WHITE, BLACK, GREY

def draw_key_effect(screen, rect, is_pressed=False):
    base_color = GREY if is_pressed else (170, 220, 255)
    border_color = BLACK

    pygame.draw.rect(screen, base_color, rect, border_radius=8)
    pygame.draw.rect(screen, border_color, rect, 2, border_radius=8)
