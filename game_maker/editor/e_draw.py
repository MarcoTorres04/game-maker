import typing

import pygame as pg

import settings

if typing.TYPE_CHECKING:
    from .e_controller import EditorController


class EditorDrawer:
    def __init__(self, editor: 'EditorController'):
        self.display_surface = pg.display.get_surface()
        self.editor = editor
        self.font = pg.font.SysFont(settings.FONT, settings.FONT_SIZE)

    def draw(self):
        self.display_surface.fill(settings.SCREEN_FILL)
        if self.editor.grid_active:
            self.editor.grid.draw(self.editor.pan.center)
        self.editor.canvas.draw(self.editor.pan.center, self.editor.debug)
        self.editor.menu.draw()
        self.editor.ui.draw('edit')
        if self.editor.debug:
            self.debug_draw()

    def debug_draw(self):
        offset = self.editor.pan.center
        pg.draw.circle(self.display_surface, settings.DEBUG_COLOR,
                       offset, settings.DEBUG_SIZE)
        _text = str(self.editor.canvas.get_grid_cell(offset))
        text = self.font.render(_text, True, settings.DEBUG_COLOR,
                                settings.DEBUG_BG)
        rect = text.get_rect()
        rect.center = settings.WINDOW_WIDTH - settings.TILE_SIZE, 10
        self.display_surface.blit(text, rect)

        _text = str(self.editor.menu.scroll_index)
        current_cell = self.editor.canvas.get_grid_cell(offset)
        if current_cell in self.editor.canvas.canvas_tiles:
            _text += f' {self.editor.canvas.canvas_tiles[current_cell]}'
        text = self.font.render(f"Scroll Index: {_text}", True,
                                settings.DEBUG_COLOR, settings.DEBUG_BG)
        rect = text.get_rect()
        rect.center = settings.WINDOW_WIDTH - (3 * settings.TILE_SIZE), 30
        self.display_surface.blit(text, rect)
