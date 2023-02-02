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
        cell_name: str = list(self.menu.buttons)[
            self.menu.selected_item].current_tile.path
        if current_cell in self.canvas_tiles:
            menu, name, _ = cell_name.split('-')
            c_menu, c_name, _ = self.canvas_tiles[current_cell].split('-')
            if c_menu == menu and c_name == name:
                return
        new_cell_name = self.review_up(current_cell, cell_name)
        self.review_down(current_cell, new_cell_name)

    def review_up(self, current_cell: tuple[int, int], cell_name: str) -> str:
        up_loc = current_cell[0], current_cell[1] - 1
        if not up_loc in self.canvas_tiles:
            self.canvas_tiles[current_cell] = cell_name
            return cell_name
        up_cell = self.canvas_tiles[up_loc]
        up_menu, up_name, up_place = up_cell.split('-')
        menu, name, _ = cell_name.split('-')
        if (up_menu != menu) or (up_name != name):
            self.canvas_tiles[current_cell] = cell_name
            if up_place == 'bottom':
                self.canvas_tiles[up_loc] = f'{up_menu}-{up_name}-middle'
            return cell_name
        if up_place == 'top':
            self.canvas_tiles[current_cell] = f'{menu}-{name}-bottom'
            return f'{menu}-{name}-bottom'
        if up_place == 'middle':
            self.canvas_tiles[current_cell] = f'{menu}-{name}-bottom'
            return f'{menu}-{name}-bottom'
        if up_place == 'bottom':
            self.canvas_tiles[up_loc] = f'{up_menu}-{up_name}-middle'
            self.canvas_tiles[current_cell] = f'{menu}-{name}-bottom'
            return f'{menu}-{name}-bottom'

    def review_down(self, current_cell: tuple[int, int], cell_name: str):
        down_loc = current_cell[0], current_cell[1] + 1
        if not down_loc in self.canvas_tiles:
            self.canvas_tiles[current_cell] = cell_name
            return
        down_cell = self.canvas_tiles[down_loc]
        down_menu, down_name, down_place = down_cell.split('-')
        menu, name, place = cell_name.split('-')
        if (down_menu != menu) or (down_name != name):
            self.canvas_tiles[current_cell] = cell_name
            self.canvas_tiles[down_loc] = f'{down_menu}-{down_name}-top'
            return
        if down_place == 'top':
            self.canvas_tiles[down_loc] = f'{down_menu}-{down_name}-middle'
            if place == 'bottom':
                self.canvas_tiles[current_cell] = f'{menu}-{name}-middle'
                return
        self.canvas_tiles[current_cell] = cell_name

    def run(self, pan_center: Vector2):
        self.add_tile(pan_center)

    def draw(self, offset: Vector2):
        for loc, tile_path in self.canvas_tiles.items():
            menu, name, place = tile_path.split('-')
            menu_images = self.menu.menu_images.menu_images[menu][name]
            if not place in menu_images:
                place = 'middle' if place == 'bottom' and 'middle' in menu_images else 'top'
            tile_surface = self.menu.menu_images.menu_images[menu][name][place]
            image = tile_surface.surface

            x = offset[0] + loc[0] * settings.TILE_SIZE
            y = offset[1] + loc[1] * settings.TILE_SIZE
            self.display_surface.blit(image, (x, y))
