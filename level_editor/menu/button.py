import pygame
import settings


class Button(pygame.sprite.Sprite):
    def __init__(self, group, left: int, top: int, width: int, height: int,
                 idx: int):
        super().__init__(group)
        self.display_surface = pygame.display.get_surface()
        self.image_surface = pygame.Surface((width, height))
        self.image_surface.set_alpha(settings.MENU_HL_ALPHA)
        self._rect = self.image_surface.get_rect()
        self._rect.topleft = (left, top)
        self.menu_loc = idx

    def update(self, menu: list):
        if len(menu) <= self.menu_loc:
            self.image = self.image_surface
            self.rect = self._rect
            return
        self.image: pygame.Surface = menu[self.menu_loc]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self._rect.left, self._rect.top)
