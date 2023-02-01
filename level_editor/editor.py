import menu
import pygame
import settings
import tools
import tile_creator
from pygame.mouse import get_pressed, get_pos


class Editor:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        # Tools
        self.grid_tool = tools.GridTool()
        self.pan_tool = tools.PanTool()
        # Menu
        self.menu = menu.Menu()
        # Tile Creator
        self.tile_creator = tile_creator.TileCreator(self.menu)
        # Debug Utils
        if settings.DEBUG:
            pygame.font.init()
            self.font = pygame.font.SysFont(settings.FONT, settings.FONT_SIZE)

    def run(self, event: pygame.event.Event, dt: float):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.menu.menu_index -= 1
            if event.key == pygame.K_RIGHT:
                self.menu.menu_index += 1
            self.menu.menu_index %= len(settings.MENU_ITEMS)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.menu.click(event)

        self.display_surface.fill(settings.SCREEN_FILL)
        self.pan_tool.update(event)

        if settings.GRID:
            self.grid_tool.draw(self.pan_tool.center)

        self.menu.update(event)

        if get_pressed()[0] and not self.menu.rect.collidepoint(get_pos()):
            self.tile_creator.run(self.pan_tool.center)

        if settings.DEBUG:
            pygame.draw.circle(self.display_surface, settings.DEBUG_COLOR,
                               (self.pan_tool.center), settings.DEBUG_SIZE)
            _text = str(self.tile_creator.get_grid_cell(self.pan_tool.center
                                                        ))
            text = self.font.render(
                _text, True, settings.DEBUG_COLOR, settings.DEBUG_BG)
            rect = text.get_rect()
            rect.center = settings.WINDOW_WIDTH - settings.TILE_SIZE, 10
            self.display_surface.blit(text, rect)
