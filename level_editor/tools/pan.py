import pygame
from pygame.mouse import get_pressed, get_pos
from pygame.math import Vector2


class PanTool:
    def __init__(self):
        self.active = False
        self.offset = Vector2()
        self.center = Vector2()

    def update(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
            self.active = True
            self.offset = Vector2(get_pos()) - self.center

        if not get_pressed()[1]:
            self.active = False

        if self.active:
            self.center = get_pos() - self.offset
