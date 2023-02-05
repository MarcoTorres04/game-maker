import pygame as pg


class TileSurface():
    def __init__(self, surface: pg.Surface, path: str, metadataba: dict = {}):
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.path = path
        self.metadata = metadataba

        if 'hitbox' in metadataba:
            hitbox = self.metadata['hitbox']
            inflate_x = self.rect.size[0] - (self.rect.size[0] * hitbox[0])
            inflate_y = self.rect.size[1] - (self.rect.size[1] * hitbox[1])
            self.rect = self.rect.inflate(-inflate_x, -inflate_y)

    def draw(self, surface: pg.Surface, loc: tuple, debug: bool):
        surface.blit(self.surface, loc)
        if debug:
            left = self.rect.left + loc[0]
            top = self.rect.top + loc[1]
            rect = pg.Rect(left, top, self.rect.w, self.rect.h)
            pg.draw.rect(surface, 'red', rect, 2)

    def __str__(self) -> str:
        return self.path
