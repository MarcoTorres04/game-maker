import pygame as pg


class LevelTile(pg.sprite.Sprite):
    def __init__(self, image: pg.Surface, pos: tuple, groups, metadata: dict = {}) -> None:
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.metadata = metadata
