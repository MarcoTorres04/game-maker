import typing

import pygame as pg

from .p_draw import PlayDrawer
from .player import Player

if typing.TYPE_CHECKING:
    from game_maker import GameMaker


class PlayController:
    def __init__(self, game_maker: 'GameMaker'):
        self.game_maker = game_maker
        self.images = {}
        self.player = None
        self.ui = self.game_maker.ui
        self.drawer = PlayDrawer(self)

    def find_player_loc(self):
        for loc, tile in self.images.items():
            if 'player' in tile.path:
                return loc, tile
        return None, None

    def set_canvas_images(self, images: dict):
        self.images = images
        loc, tile = self.find_player_loc()
        if loc is None:
            return
        self.player = Player(self.images.pop(loc), loc)

    def events(self, event: pg.event.Event):
        if self.player is None:
            return
        self.player.move_event(event)

    def run(self, dt: float):
        # Keyboard
        if not self.player is None:
            self.player.update(dt)

        self.drawer.draw()
