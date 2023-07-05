import pygame
import settings
from pygame.image import load
from pygame.mouse import get_pos, get_pressed


class Ui:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        ui_path = settings.TILES_PATH / 'ui'
        # Play button
        self.images = {
            "edit": load(str(ui_path / 'play.png')),
            "edit-hover": load(str(ui_path / 'play-hover.png')),
            "play": load(str(ui_path / 'pause.png')),
            "play-hover": load(str(ui_path / 'pause-hover.png'))
        }
        self.rect = self.images['edit'].get_rect()
        self.rect.topleft = settings.TILE_SIZE // 8, settings.WINDOW_HEIGHT - \
            settings.TILE_SIZE

    def hover(self) -> bool:
        if not self.rect.collidepoint(get_pos()):
            return False
        return True

    def click(self, event: pygame.event.Event) -> bool:
        if event.type != pygame.MOUSEBUTTONDOWN:
            return False
        if not get_pressed()[0]:
            return False
        return self.rect.collidepoint(get_pos())

    def draw(self, mode: str):
        if self.hover():
            mode = f'{mode}-hover'
        self.display_surface.blit(self.images[mode], self.rect.topleft)

    def collide(self, pos: tuple) -> bool:
        return self.rect.collidepoint(pos)
