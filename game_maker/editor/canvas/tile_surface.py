import pygame as pg
import settings


class TileSurface():
    def __init__(self, surface: pg.Surface, path: str, metadataba: dict = {}):
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.path = path
        self.metadata = metadataba
        self.inflate_x = 0
        self.inflate_y = 0

        if 'hitbox' in metadataba:
            hitbox = self.metadata['hitbox']
            self.inflate_x = self.rect.size[0] - self.rect.size[0] * hitbox[0]
            self.inflate_y = self.rect.size[1] - self.rect.size[1] * hitbox[1]
            self.rect = self.rect.inflate(-self.inflate_x, -self.inflate_y)

    def draw_edit(self, surface: pg.Surface, loc: tuple, debug: bool):
        surface.blit(self.surface, loc)
        if debug:
            left = self.rect.left + loc[0]
            top = self.rect.top + loc[1]
            rect = pg.Rect(left, top, self.rect.w, self.rect.h)
            pg.draw.rect(surface, 'red', rect, 2)

    def draw_play(self, surface: pg.Surface, loc: tuple[int, int], center: pg.math.Vector2,  debug: bool):
        x = loc[0] * settings.TILE_SIZE - center[0] + self.rect.width
        y = loc[1] * settings.TILE_SIZE - center[1] + self.rect.height // 2
        self.rect.center = (x, y)
        surface.blit(self.surface, self.rect)
        if debug:
            pg.draw.rect(surface, 'red', self.rect, 2)

    def __str__(self) -> str:
        return self.path
