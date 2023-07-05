import pygame as pg

from .camera import Camera
from .player import Player


class Level:

    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.player = None
        self.dead_level = float('-inf')

        # Sprites Groups
        self.draw_sprites = Camera()
        self.update_sprites = pg.sprite.Group()
        self.collision_sprites = pg.sprite.Group()

    def set_player(self, player: Player):
        self.player = player
        self.draw_sprites.track_player(self.player)

    def set_dead_line(self):
        self.draw_sprites.set_dead_line(self.dead_level)
