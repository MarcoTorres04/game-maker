import settings
from pygame.mouse import get_pos
from pygame.math import Vector2
import menu
import pygame


class TileCreator:
    def __init__(self, editor_menu: menu.Menu):
        self.display_surface = pygame.display.get_surface()
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
        cell_name = list(self.menu.buttons)[
            self.menu.selected_item].current_tile.path
        if current_cell in self.canvas_tiles and cell_name == self.canvas_tiles[current_cell]:
            return
        self.canvas_tiles[current_cell] = cell_name

    def run(self, pan_center: Vector2):
        self.add_tile(pan_center)

    def draw(self, offset: Vector2):
        for loc, tile_path in self.canvas_tiles.items():
            menu, name, place = tile_path.split('-')
            tile_surface = self.menu.menu_images.menu_images[menu][name][place]
            image = tile_surface.surface

            x = offset[0] + loc[0] * settings.TILE_SIZE
            y = offset[1] + loc[1] * settings.TILE_SIZE
            self.display_surface.blit(image, (x, y))
