import random

import pygame as pg
import settings

from .tile import LevelTile


class AnimatedLevelTile(LevelTile):
    def __init__(self, images: dict[str, list[pg.Surface]], pos: tuple, groups, metadata: dict = {}) -> None:
        super().__init__(images['idle'][0], pos, groups, metadata)

        self.images = images
        self.animation_idx = 0
        self.state = 'idle'
        self.animation_spd = metadata.get(
            'animation_speed', settings.PLAYER_ANIMATION_SPEED)
        for _images in self.images.values():
            random.shuffle(_images)
        self.image = self.images[self.state][self.animation_idx]

    def update(self, dt: float):
        super().update(dt)
        self.animation_idx += self.animation_spd * dt
        self.image = self.images[self.state][int(self.animation_idx)]
        self.animation_idx %= (len(self.images[self.state]) - 1)
