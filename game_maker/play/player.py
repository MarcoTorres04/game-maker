import pygame as pg
import settings
from pygame.key import get_pressed as keys_pressed

from .collider import Collider
from assets_loader import Asset


class Player(pg.sprite.Sprite):
    def __init__(self, image: Asset, pos, groups, collision_sprites: pg.sprite.Group) -> None:
        super().__init__(groups)
        self.metadata = image.metadata
        hitbox = self.metadata.get('hitbox', [1, 1])

        size_x = (settings.TILE_SIZE - settings.TILE_SIZE * hitbox[0]) // 2
        size_y = (settings.TILE_SIZE - settings.TILE_SIZE * hitbox[1]) // 2

        self.image = image.surface
        self.rect = self.image.get_rect(topleft=pos)

        left = self.rect.left + size_x
        top = self.rect.top + size_y
        w = int(settings.TILE_SIZE * hitbox[0])
        h = int(settings.TILE_SIZE * hitbox[1])
        self.hitbox = pg.Rect(left, top, w, h)

        self.direction = pg.math.Vector2()
        self.speed = settings.PLAYER_SPEED
        self.gravity = settings.PLAYER_GRAVITY
        self.jump_force = settings.PLAYER_JUMP
        self.can_double_jump = False
        self.can_jump = False
        self.water_jump = False
        self.jump_press = False

        self.collider = Collider(self)
        self.collision_sprites = collision_sprites

        self.score = 0
        self.is_alive = True
        self.win = False
        self.state = 'idle'
        self.dir = 'right'
        self.water_force = 1

    def key_input(self):
        keys = keys_pressed()

        if keys[pg.K_LEFT]:
            self.direction.x = -1
            self.dir = 'left'
        elif keys[pg.K_RIGHT]:
            self.direction.x = 1
            self.dir = 'right'
        else:
            self.direction.x = 0

        if keys[pg.K_SPACE]:
            if (self.can_jump or self.water_jump):
                self.can_jump = False
                self.direction.y = -self.jump_force * self.water_force
                self.can_double_jump = True
                self.jump_press = True
            elif self.can_double_jump and self.state == 'jump' and not self.jump_press:
                self.can_double_jump = False
                self.direction.y = -self.jump_force * self.water_force * 0.8

    def fall(self, dt: float):
        self.direction.y += self.gravity * dt
        self.rect.y += self.direction.y * self.speed * dt
        self.hitbox.y += self.direction.y * self.speed * dt

    def update(self, dt: float):
        self.key_input()
        self.water_jump = False
        self.rect.x += self.direction.x * self.speed * dt * self.water_force
        self.hitbox.x += self.direction.x * self.speed * dt * self.water_force
        self.water_force = 1
        self.collider.horizontal(self.collision_sprites)
        self.fall(dt)
        self.collider.vertical(self.collision_sprites)
        self.rect.center = self.hitbox.center

        # States
        if abs(self.direction.x) < 0.1 and abs(self.direction.y) < 0.1:
            self.state = 'idle'
        elif self.direction.x != 0:
            self.state = 'run'
        if not self.can_jump and abs(self.direction.y) > 0.3 and self.can_double_jump:
            self.state = 'jump'
        elif not self.can_double_jump and abs(self.direction.y) > 0.3:
            self.state = 'double_jump'
