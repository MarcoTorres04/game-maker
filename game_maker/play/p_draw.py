import typing

import pygame as pg

import settings

if typing.TYPE_CHECKING:
    from .p_controller import PlayController


class PlayDrawer:
    def __init__(self, play: 'PlayController'):
        self.display_surface = pg.display.get_surface()
        self.play = play

    def draw(self):
        self.display_surface.fill(settings.SCREEN_FILL)

        for loc, tile in self.play.images.items():
            x = loc[0] * settings.TILE_SIZE
            y = loc[1] * settings.TILE_SIZE
            self.display_surface.blit(tile.surface, (x, y))

        if not self.play.player is None:
            self.play.player.draw(self.display_surface)

        self.play.ui.draw('play')
