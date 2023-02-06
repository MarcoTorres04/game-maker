import typing

import pygame as pg
from pygame.key import get_pressed as keys_pressed
from screens import WinScreen
from state_machine import StateMachine

from .level import Level
from .level_loader import LevelLoader
from .play_draw import PlayDrawer

if typing.TYPE_CHECKING:
    from game_maker import GameMaker


class PlayController:
    def __init__(self, game_maker: 'GameMaker', state_machine: StateMachine, canvas: dict):
        self.game_maker = game_maker
        self.ui = self.game_maker.ui
        self.drawer = PlayDrawer(self)
        self.loader = LevelLoader()
        self.state_machine = state_machine
        self.win_screen = WinScreen(self.state_machine)
        self.canvas = canvas

    def start_level(self, canvas_map: dict):
        self.level = Level()
        self.player = self.loader(self.level, canvas_map)
        self.level.set_player(self.player)

    def run(self, dt: float):
        self.level.update_sprites.update(dt)
        self.drawer()
        if not self.player.is_alive:
            self.start_level(self.canvas)
        elif self.player.win:
            self.state_machine.pop()
            self.state_machine.push('win')

    def events(self, event: pg.event.Event):
        # Keyboard
        if event.type == pg.KEYDOWN:
            keys = keys_pressed()

            if keys[pg.K_ESCAPE]:
                self.state_machine.pop()
                return

            if (keys[pg.K_LCTRL] and keys[pg.K_r]):
                self.state_machine.pop()
                return

        if self.ui.click(event):
            self.state_machine.pop()
