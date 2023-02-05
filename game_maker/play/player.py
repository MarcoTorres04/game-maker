import menu
import pygame as pg
import settings
from pygame.key import get_pressed as keys_pressed


class Player:
    def __init__(self, image: menu.TileSurface, loc: tuple):
        # Image Surface
        self.image = image
        self.surface = self.image.surface
        self.rect = self.surface.get_rect()
        self.metadata = self.image.metadata
        self.rect.left = loc[0] * settings.TILE_SIZE
        self.rect.top = loc[1] * settings.TILE_SIZE
        if 'hitbox' in self.metadata:
            hitbox = self.metadata['hitbox']
            self.inflate_x = self.rect.size[0] - \
                (self.rect.size[0] * hitbox[0])
            self.inflate_y = self.rect.size[1] - \
                (self.rect.size[1] * hitbox[1])
            self.rect = self.rect.inflate(-self.inflate_x, -self.inflate_y)
        else:
            self.inflate_x = 0
            self.inflate_y = 0
        # Stats
        self.speed_value = settings.PLAYER_SPEED
        self.speed = 0
        # States
        self.state = 'idle'
        self.direction = 'right'
        self.can_jump = False

    def move_event(self, event: pg.event.Event):

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                self.direction = 'left'
                self.speed -= self.speed_value
            elif event.key == pg.K_RIGHT:
                self.direction = 'right'
                self.speed += self.speed_value

        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                self.speed += self.speed_value
            elif event.key == pg.K_RIGHT:
                self.speed -= self.speed_value

    def move(self, dt: float):
        self.state = 'run' if self.speed != 0 else 'idle'
        self.rect.move_ip(self.speed * dt, 0)

    def update(self, dt: float):
        """Animate and move player loc"""
        self.move(dt)

    def draw(self, surface: pg.Surface):
        # left = self.rect.left + self.inflate_x / 2
        # top = self.rect.top + self.inflate_y / 2
        # rect = pg.Rect(left, top, self.rect.w, self.rect.h)
        # pg.draw.rect(surface, 'red', rect, 2)
        surface.blit(self.surface, self.rect)
