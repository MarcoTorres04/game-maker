import pygame as pg
from assets_loader import Asset


class LevelTile(pg.sprite.Sprite):
    def __init__(self, image: Asset, pos: tuple, groups) -> None:
        super().__init__(groups)
        self.image = image.surface
        self.metadata = image.metadata
        self.rect = self.image.get_rect(topleft=pos)
