import typing

import canvas
import menu
import pygame as pg
import settings
import tools
from pygame.key import get_pressed as keys_pressed
from pygame.mouse import get_pos as mouse_pos

from .e_draw import EditorDrawer

if typing.TYPE_CHECKING:
    from game_maker import GameMaker


class EditorController:
    def __init__(self, game_maker: 'GameMaker'):
        # Game Maker
        self.game_maker = game_maker
        # Menu
        self.menu_images = menu.MenuImages()
        self.menu = menu.Menu(self.menu_images)
        # Tools
        self.ui = self.game_maker.ui
        self.grid = tools.GridTool()
        self.grid_active = settings.GRID
        self.pan = tools.PanTool()
        # Debug Utils
        self.debug = settings.DEBUG
        # Canvas
        self.canvas = canvas.Canvas(self.menu)
        # Draw
        self.drawer = EditorDrawer(self)

    def events(self, event: pg.event.Event):
        # Keyboard
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                self.menu.menu_index += 1
            elif event.key == pg.K_RIGHT:
                self.menu.menu_index -= 1
            self.menu.menu_index %= len(settings.MENU_ITEMS)
            keys = keys_pressed()
            if keys[pg.K_LCTRL] and keys[pg.K_d]:
                self.debug = not self.debug
        # Mouse
        if event.type == pg.MOUSEBUTTONDOWN:
            self.menu.click(event)
        elif event.type == pg.MOUSEWHEEL:
            self.menu.scroll(event)

        # Tools
        self.pan.update(event)

    def run(self, dt: float):
        pos = mouse_pos()
        if not (self.menu.collide(pos) or self.ui.collide(pos)):
            self.canvas.update(self.pan.center)

        # Draw
        self.drawer.draw()

    def get_canvas_images(self) -> dict:
        canvas_images = {}
        for loc, cell_path in self.canvas.canvas_tiles.items():
            menu, name, place = cell_path.split('-')
            canvas_images[loc] = self.menu.menu_images.menu_images[menu][name][place]
        return canvas_images
