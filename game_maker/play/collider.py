import typing

import pygame as pg
from pygame.sprite import Group

if typing.TYPE_CHECKING:
    from .player import Player


class Collider:

    def __init__(self, player: 'Player'):
        self.player = player
        self.collide_handlers = {
            "kill": self.handler_kill,
            "win": self.handler_win,
            "score_3": lambda sprite: self.handler_score(sprite, 3),
            "score_2": lambda sprite: self.handler_score(sprite, 2),
            "score_1": lambda sprite: self.handler_score(sprite, 1),
            "swim": self.handler_swim
        }

    def __call__(self, collision_sprites: Group):
        self.horizontal(collision_sprites)
        self.vertical(collision_sprites)

    def horizontal(self, collision_sprites: Group):
        for sprite in collision_sprites.sprites():
            if not sprite.rect.colliderect(self.player.rect):
                continue

            collide_effect = sprite.metadata.get('collide', 'solid')
            if collide_effect == 'solid':
                self.horizontal_solid_collide(sprite)
            else:
                self.collide_handlers[collide_effect](sprite)

    def vertical(self, collision_sprites: Group):
        for sprite in collision_sprites.sprites():
            if not sprite.rect.colliderect(self.player.rect):
                continue
            collide_effect = sprite.metadata.get('collide', 'solid')
            if collide_effect == 'solid':
                self.vertical_solid_collide(sprite)
            else:
                self.collide_handlers[collide_effect]

        if self.player.can_jump and self.player.direction.y != 0:
            self.player.can_jump = False

    def horizontal_solid_collide(self, sprite: pg.sprite):
        #  <- Left
        if self.player.direction.x < 0:
            self.player.rect.left = sprite.rect.right
        # -> Right
        elif self.player.direction.x > 0:
            self.player.rect.right = sprite.rect.left

    def vertical_solid_collide(self, sprite: pg.sprite):
        # ^ Up
        if self.player.direction.y < 0:
            self.player.rect.top = sprite.rect.bottom
        # v Down
        elif self.player.direction.y > 0:
            self.player.rect.bottom = sprite.rect.top
            self.player.direction.y = 0
            self.player.can_jump = True

    def handler_kill(self, sprite: pg.sprite.Sprite):
        self.player.is_alive = False

    def handler_win(self, sprite: pg.sprite.Sprite):
        self.player.win = True

    def handler_score(self, sprite: pg.sprite.Sprite, score: int):
        self.player.score += score
        sprite.kill()

    def handler_swim(self, sprite: pg.sprite.Sprite):
        self.player.water_jump = True
