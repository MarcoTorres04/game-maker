import menu
import pygame
import screen_animation
import settings
import tile_creator
import tools
from pygame.mouse import get_pos, get_pressed


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
        # Ui
        self.ui = tools.Ui()
        # Screen Animation
        self.active_animation = False
        # Debug Utils
        if settings.DEBUG:
            pygame.font.init()
            self.font = pygame.font.SysFont(settings.FONT, settings.FONT_SIZE)

    def run(self, event: pygame.event.Event, dt: float):

        if self.active_animation:
            self.draw(event)
            self.animation.animate()
            if self.animation.is_done():
                self.active_animation = False
                del self.animation
            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.menu.menu_index -= 1
            if event.key == pygame.K_RIGHT:
                self.menu.menu_index += 1
            self.menu.menu_index %= len(settings.MENU_ITEMS)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.menu.click(event)

        elif event.type == pygame.MOUSEWHEEL:
            self.menu.scroll(event)

        self.pan_tool.update(event)

        self.draw(event)

    def draw(self, event: pygame.event.Event):
        self.display_surface.fill(settings.SCREEN_FILL)

        if settings.GRID:
            self.grid_tool.draw(self.pan_tool.center)

        pos = get_pos()
        if get_pressed()[0] and not self.menu.rect.collidepoint(pos) and not self.ui.rect.collidepoint(pos):
            self.tile_creator.run(self.pan_tool.center)

        self.tile_creator.draw(self.pan_tool.center)

        self.menu.update(event)

        self.ui.draw()
        if self.ui.click(event) and not self.active_animation:
            self.active_animation = True
            self.animation = screen_animation.ScreenAnimation()

        if settings.DEBUG:
            pygame.draw.circle(self.display_surface, settings.DEBUG_COLOR,
                               (self.pan_tool.center), settings.DEBUG_SIZE)
            _text = str(self.tile_creator.get_grid_cell(self.pan_tool.center))
            text = self.font.render(_text, True, settings.DEBUG_COLOR,
                                    settings.DEBUG_BG)
            rect = text.get_rect()
            rect.center = settings.WINDOW_WIDTH - settings.TILE_SIZE, 10
            self.display_surface.blit(text, rect)

            _text = str(self.menu.scroll_index)
            current_cell = self.tile_creator.get_grid_cell(
                self.pan_tool.center)
            if current_cell in self.tile_creator.canvas_tiles:
                _text += f' {self.tile_creator.canvas_tiles[current_cell]}'
            text = self.font.render(f"Scroll Index: {_text}", True,
                                    settings.DEBUG_COLOR, settings.DEBUG_BG)
            rect = text.get_rect()
            rect.center = settings.WINDOW_WIDTH - (3 * settings.TILE_SIZE), 30
            self.display_surface.blit(text, rect)
