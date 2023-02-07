import pygame as pg
import settings

from .player import Player


class AnimatedPlayer(Player):
    def __init__(self, images: dict[str, list[pg.Surface]], pos, groups, collision_sprites: pg.sprite.Group, metadata: dict = ...) -> None:
        super().__init__(images['idle'][0], pos,
                         groups, collision_sprites, metadata)

        self.metadata = metadata
        self.images = images
        self.animation_idx = 0
        self.animation_spd = self.metadata.get(
            'animation_speed', settings.PLAYER_ANIMATION_SPEED)
        self.image = self.images[self.state][self.animation_idx]

    def update(self, dt: float):
        super().update(dt)
        self.animation_idx += self.animation_spd * dt
        self.animation_idx = min(
            self.animation_idx, len(self.images[self.state])-1)
        self.image = self.images[self.state][int(self.animation_idx)]
        if self.dir == 'left':
            self.image = pg.transform.flip(self.image, True, False)
        # self.animation_idx %= (len(self.images[self.state]) - 1)
        if self.animation_idx >= (len(self.images[self.state]) - 1):
            self.animation_idx = 0
