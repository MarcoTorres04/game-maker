import pygame


class TileSurface():
    def __init__(self, surface: pygame.Surface, path: str):
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.path = path
