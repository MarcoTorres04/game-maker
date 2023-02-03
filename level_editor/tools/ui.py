import pygame
import settings
from pygame.image import load
from pygame.mouse import get_pos, get_pressed


class Ui:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        ui_path = settings.TILES_PATH / 'ui'
        # Play button
        self.image = load(str(ui_path / 'play.png'))
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, settings.WINDOW_HEIGHT - settings.TILE_SIZE

    def hover(self):
        if not self.rect.collidepoint(get_pos()):
            return
        surface = pygame.Surface(self.rect.size)
        surface.fill('gold')
        return surface

    def click(self, event: pygame.event.Event) -> bool:
        if event.type != pygame.MOUSEBUTTONDOWN:
            return False
        if not get_pressed()[0]:
            return False
        return self.rect.collidepoint(get_pos())

    def draw(self):
        hover_surface = self.hover()
        if not hover_surface is None:
            self.display_surface.blit(hover_surface, self.rect.topleft)
        self.display_surface.blit(self.image, self.rect.topleft)
