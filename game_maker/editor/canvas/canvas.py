import typing

import pygame as pg
import settings
from pygame.math import Vector2
from pygame.mouse import get_pos, get_pressed

if typing.TYPE_CHECKING:
    from menu import Menu


class Canvas:
    def __init__(self, editor_menu: 'Menu'):
        self.display_surface = pg.display.get_surface()
        self.menu = editor_menu
        self.canvas_tiles: dict[tuple, str] = {}
        self.assets = self.menu.assets

    def get_grid_cell(self, pan_center: Vector2):  # -> tuple[int, int]:
        """Cell position in grid"""
        x, y = Vector2(get_pos()) - pan_center
        x_cell = int(x // settings.TILE_SIZE)
        y_cell = int(y // settings.TILE_SIZE)
        return x_cell, y_cell

    def get_neighbors_locs(self, cell_loc: tuple) -> dict:
        """Cell locs in grid (N,S,E,W)"""
        return {
            "up": (cell_loc[0], cell_loc[1] - 1),
            "down": (cell_loc[0], cell_loc[1] + 1),
            "left": (cell_loc[0] - 1, cell_loc[1]),
            "right": (cell_loc[0] + 1, cell_loc[1]),
            "loc": cell_loc
        }

    def add_tile(self, pan_center: Vector2):
        """Add tile to canvas"""
        current_cell = self.get_grid_cell(pan_center)
        if not settings.OVERRIDE_CELL and current_cell in self.canvas_tiles:
            return

        item = self.menu.images_list[self.menu.selected_item]
        menu, name, _ = item.path.split('-')

        if current_cell in self.canvas_tiles and item == self.canvas_tiles[current_cell]:
            return

        neighbors = self.get_neighbors_locs(current_cell)
        self.review_locs(item.path, neighbors)

    def remove_tile(self, pan_center: Vector2):
        """Remove tile"""
        current_cell = self.get_grid_cell(pan_center)
        if not current_cell in self.canvas_tiles:
            return
        self.canvas_tiles.pop(current_cell)
        nbrs = self.get_neighbors_locs(current_cell)
        self.review_nbrs(nbrs)

    def review_locs(self, cell_name: str, nbrs: dict):
        menu, name, place = cell_name.split('-')
        if 'player' in menu:
            self.delete_unique()
            self.canvas_tiles[nbrs['loc']] = cell_name
            return
        elif 'idle' in place:
            self.canvas_tiles[nbrs['loc']] = cell_name
            return
        if not any(
                map(lambda cell: cell in self.canvas_tiles,
                    list(nbrs.values())[:-1])):
            self.canvas_tiles[nbrs['loc']] = f'{menu}-{name}-alone'
            return
        self.review_cell(cell_name, nbrs, True)

    def review_cell(self,
                    cell_name: str,
                    nbrs: dict,
                    review_nbrs: bool = False):
        menu, name, place = cell_name.split('-')
        if 'unique' in place or 'idle' in place:
            return
        if self.is_top(cell_name, nbrs):
            place = 'top'
            if self.is_column(nbrs):
                place += '_column'
            elif self.is_left(nbrs):
                place += '_left'
            elif self.is_right(nbrs):
                place += '_right'
        elif self.is_bottom(cell_name, nbrs):
            place = 'bottom'
            if self.is_column(nbrs):
                place += '_column'
            if self.is_left(nbrs):
                place += '_left'
            elif self.is_right(nbrs):
                place += '_right'
        elif self.is_middle(cell_name, nbrs):
            place = 'middle'
            if self.is_column(nbrs):
                place += '_column'
            elif self.is_left(nbrs):
                place += '_left'
            elif self.is_right(nbrs):
                place += '_right'
        self.canvas_tiles[nbrs['loc']] = f'{menu}-{name}-{place}'
        nbrs['loc'] = f'{menu}-{name}-{place}'

        if not review_nbrs:
            return

        self.review_nbrs(nbrs)

    def review_nbrs(self, nbrs: dict):
        for nbr in list(nbrs.values())[:-1]:
            if not nbr in self.canvas_tiles:
                continue
            nbr_name = self.canvas_tiles[nbr]
            nbr_nbrs = self.get_neighbors_locs(nbr)
            self.review_cell(nbr_name, nbr_nbrs)

    def is_top(self, cell_name: str, nbrs: dict) -> bool:
        if not nbrs['up'] in self.canvas_tiles:
            return True
        up_cell = self.canvas_tiles[nbrs['up']]
        u_menu, u_name, _ = up_cell.split('-')
        menu, name, _ = cell_name.split('-')
        if (u_menu != menu) or (u_name != name):
            return True
        return False

    def is_bottom(self, cell_name: str, nbrs: dict) -> bool:
        if not nbrs['down'] in self.canvas_tiles:
            return True
        up_cell = self.canvas_tiles[nbrs['up']]
        u_menu, u_name, _ = up_cell.split('-')
        menu, name, _ = cell_name.split('-')
        if (u_menu == menu) and (u_name == name):
            return False
        return True

    def is_middle(self, cell_name: str, nbrs: dict) -> bool:
        if nbrs['down'] in self.canvas_tiles:
            return True
        up_cell = self.canvas_tiles[nbrs['up']]
        u_menu, u_name, _ = up_cell.split('-')
        menu, name, _ = cell_name.split('-')
        if (u_menu == menu) and (u_name == name):
            return True
        return False

    def is_left(self, nbrs: dict) -> bool:
        return (not nbrs['left'] in self.canvas_tiles
                and nbrs['right'] in self.canvas_tiles)

    def is_right(self, nbrs: dict) -> bool:
        return (not nbrs['right'] in self.canvas_tiles
                and nbrs['left'] in self.canvas_tiles)

    def is_column(self, nbrs: dict) -> bool:
        return not (nbrs['right'] in self.canvas_tiles
                    or nbrs['left'] in self.canvas_tiles)

    def delete_unique(self):
        locs = []
        for loc, cell in self.canvas_tiles.items():
            if 'player' in cell:
                locs.append(loc)
        for loc in locs:
            self.canvas_tiles.pop(loc)

    def update(self, pan_center: Vector2):
        mouse = get_pressed()
        if mouse[0]:
            self.add_tile(pan_center)
        elif mouse[2]:
            self.remove_tile(pan_center)

    def draw(self, offset: Vector2, debug: bool):
        for loc, asset in self.canvas_tiles.items():
            menu, name, place = asset.split('-')
            images = self.menu.assets[menu][name]
            place = place.replace('_ANIMATION', '')
            if not place in images:
                if 'top' in place or 'alone' in place:
                    place = 'top'
                elif 'bottom' in place and 'bottom' in images:
                    place = 'bottom'
                elif 'middle' in images:
                    place = 'middle'
                else:
                    place = 'top'
                self.canvas_tiles[loc] = f'{menu}-{name}-{place}'
            surface = self.menu.assets[menu][name][place][0]

            x = offset[0] + loc[0] * settings.TILE_SIZE
            y = offset[1] + loc[1] * settings.TILE_SIZE

            surface.draw_edit(self.display_surface, (x, y), debug)
