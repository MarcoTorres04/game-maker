import pygame
import settings


class EditorGrid:
    def __init__(self):
        self.grid_surface = pygame.Surface(
            (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.grid_surface.set_colorkey(settings.GRID_COLOR_KEY)
        self.grid_surface.set_alpha(settings.GRID_ALPHA)

    def update(self, offset_tool: dict, surface: pygame.Surface):
        cols = settings.WINDOW_WIDTH // settings.TILE_SIZE
        rows = settings.WINDOW_HEIGHT // settings.TILE_SIZE

        offset = (
            offset_tool['center'][0] -
            int(offset_tool['center'][0] /
                settings.TILE_SIZE) * settings.TILE_SIZE,
            offset_tool['center'][1] -
            int(offset_tool['center'][1] /
                settings.TILE_SIZE) * settings.TILE_SIZE
        )

        self.grid_surface.fill(settings.GRID_COLOR_KEY)

        for col in range(cols):
            x = offset[0] + col * settings.TILE_SIZE
            pygame.draw.line(self.grid_surface, settings.GRID_LINE_COLOR,
                             (x, 0), (x, settings.WINDOW_HEIGHT))

        for row in range(rows):
            y = offset[1] + row * settings.TILE_SIZE
            pygame.draw.line(self.grid_surface, settings.GRID_LINE_COLOR,
                             (0, y), (settings.WINDOW_WIDTH, y))

        surface.blit(self.grid_surface, (0, 0))
