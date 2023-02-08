from pathlib import Path

import pygame as pg
from pygame.image import load as load_image


class Asset:
    def __init__(self, image_path: Path, path: str, metadata: dict):
        self.surface = load_image(str(image_path))
        self.metadata = metadata
        self.path = path

    def __str__(self) -> str:
        return self.path

    def __eq__(self, other: 'Asset') -> bool:
        return self.path.split('-')[:2] == other.split('-')[:2]

    def draw_edit(self, surface: pg.Surface, loc: tuple, debug: bool):
        surface.blit(self.surface, loc)
        if debug:
            left = self.rect.left + loc[0]
            top = self.rect.top + loc[1]
            rect = pg.Rect(left, top, self.rect.w, self.rect.h)
            pg.draw.rect(surface, 'red', rect, 2)
