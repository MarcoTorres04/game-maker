import pygame as pg
import settings


class LevelTile(pg.sprite.Sprite):
    def __init__(self, image: pg.Surface, pos: tuple, groups, metadata: dict = {}) -> None:
        super().__init__(groups)
        # pg.Surface((settings.TILE_SIZE, settings.TILE_SIZE))
        self.image = image
        # self.image.fill(settings.TILES_BG)
        self.rect = self.image.get_rect(topleft=pos)
        self.metadata = metadata
