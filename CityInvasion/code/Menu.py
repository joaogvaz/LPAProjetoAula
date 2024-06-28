#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import SCR_WIDTH


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surface = pygame.image.load('./assets/images/menubg.png')
        self.rectangle = self.surface.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./assets/sounds/menustk.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.screen.blit(source=self.surface, dest=self.rectangle)
            self.menu_text(50, "City", (0, 0, 0), ((SCR_WIDTH / 2), 70))
            pygame.display.flip()
            pass

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color)
        text_rectangle: Rect = text_surface.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surface, dest=text_rectangle)
