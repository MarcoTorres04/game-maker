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
    def __init__(self, game_maker: 'GameMaker', state_machine: StateMachine, canvas: dict, assets: dict):
        self.game_maker = game_maker
        self.ui = self.game_maker.ui
        self.drawer = PlayDrawer(self)
        self.state_machine = state_machine
        self.level_loader = LevelLoader()
        self.win_screen = WinScreen(self.state_machine)
        self.canvas = canvas
        self.assets = assets

    def start_level(self):
        self.level = Level()
        self.player = self.level_loader(self.level, self.canvas, self.assets)
        self.level.set_player(self.player)
        self.level.set_dead_line()
        self.win_screen.set_player(self.player)

    def run(self, dt: float):
        self.level.update_sprites.update(dt)
        self.drawer()
        if self.player is None:
            return
        if not self.player.is_alive:
            self.start_level()
        elif self.player.win:
            self.state_machine.pop()
            self.state_machine.push('win')
        elif self.player.hitbox.bottom > self.level.dead_level:
            self.player.is_alive = False

    def events(self, event: pg.event.Event):
        # Keyboard
        keys = keys_pressed()
        if event.type == pg.KEYDOWN:

            if keys[pg.K_ESCAPE]:
                self.state_machine.pop()
                return

            if (keys[pg.K_LCTRL] and keys[pg.K_r]):
                self.state_machine.pop()
                return

        elif event.type == pg.KEYUP:
            if not self.player is None and not keys[pg.K_SPACE]:
                self.player.jump_press = False

        if self.ui.click(event):
            self.state_machine.pop()
