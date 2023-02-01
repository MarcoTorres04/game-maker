import pygame
import settings
from pygame.math import Vector2


class GridTool:
    def __init__(self):
        self.surface_display = pygame.display.get_surface()
        self.grid_surface = pygame.Surface(
            self.surface_display.get_rect().size)
        self.grid_surface.set_colorkey(settings.GRID_COLOR_KEY)

    def draw(self, offset: Vector2):

        self.grid_surface.set_alpha(settings.GRID_ALPHA)
        self.grid_surface.fill(settings.GRID_COLOR_KEY)

        x_offset = offset[0] - (offset[0] //
                                settings.TILE_SIZE) * settings.TILE_SIZE
        y_offset = offset[1] - (offset[1] //
                                settings.TILE_SIZE) * settings.TILE_SIZE

        # Vertical
        cols = settings.WINDOW_WIDTH / settings.TILE_SIZE
        for col in range(int(cols)):
            x_pos = x_offset + col * settings.TILE_SIZE
            pygame.draw.line(self.grid_surface, settings.GRID_COLOR,
                             (x_pos, 0), (x_pos, settings.WINDOW_HEIGHT))
        # Horizontal
        rows = settings.WINDOW_HEIGHT / settings.TILE_SIZE
        for row in range(int(rows)):
            y_pos = y_offset + row * settings.TILE_SIZE
            pygame.draw.line(self.grid_surface, settings.GRID_COLOR,
                             (0, y_pos), (settings.WINDOW_WIDTH, y_pos))

        self.surface_display.blit(self.grid_surface, (0, 0))
