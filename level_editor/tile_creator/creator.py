import pygame
import settings
from pygame.mouse import get_pos
from pygame.math import Vector2
import menu


class TileCreator:
    def __init__(self, editor_menu: menu.Menu):
        self.menu = editor_menu
        self.canvas_tiles: dict[tuple, str] = {}

    def get_grid_cell(self, pan_center: Vector2) -> tuple[int, int]:
        x, y = Vector2(get_pos()) - pan_center
        x_cell = int(x // settings.TILE_SIZE)
        y_cell = int(y // settings.TILE_SIZE)
        return x_cell, y_cell

    def add_tile(self, pan_center):
        current_cell = self.get_grid_cell(pan_center)
        if not settings.OVERRIDE_CELL and current_cell in self.canvas_tiles:
            return
        self.canvas_tiles[current_cell] = 'Cell'

    def run(self, pan_center: Vector2):
        self.add_tile(pan_center)
