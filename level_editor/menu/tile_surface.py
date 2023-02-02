import pygame


class TileSurface():
    def __init__(self, surface: pygame.Surface, path: str):
        self.surface = surface
        self.path = path
