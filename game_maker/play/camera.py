import pygame as pg
import settings

from .player import Player


class Camera(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = pg.math.Vector2(0, 0)
        self.player = None
        self.dead_line = 0

        if settings.CAMERA_MODE == 'center':
            self.setup_center_camera()
        elif settings.CAMERA_MODE == 'box':
            self.setup_box_camera()
        else:
            self.update_camera = lambda: None

    def track_player(self, player: Player):
        """Add Player"""
        self.player = player

    def set_dead_line(self, dead_line: float):
        """Add Dead Line"""
        self.dead_line = dead_line

    def setup_center_camera(self):
        """Player Always in Center"""
        self.camera_width = settings.WINDOW_WIDTH // 2
        self.camera_height = settings.WINDOW_HEIGHT // 2
        self.update_camera = self.update_center_camera

    def update_center_camera(self):
        if self.player is None:
            return
        self.offset.x = self.player.rect.centerx - self.camera_width
        self.offset.y = self.player.rect.centery - self.camera_height

    def setup_box_camera(self):
        """Camera in box"""
        cam_left = settings.CAMERA_BOX['left']
        cam_top = settings.CAMERA_BOX['top']
        cam_width = settings.WINDOW_WIDTH - settings.CAMERA_BOX['width']
        cam_height = settings.WINDOW_HEIGHT - \
            settings.CAMERA_BOX['height']
        self.rect = pg.Rect(cam_left, cam_top, cam_width, cam_height)
        self.update_camera = self.update_box_camera

    def update_box_camera(self):

        if self.player.rect.left < self.rect.left:
            self.rect.left = self.player.rect.left
        elif self.player.rect.right > self.rect.right:
            self.rect.right = self.player.rect.right
        elif self.player.rect.top < self.rect.top:
            self.rect.top = self.player.rect.top
        elif self.player.rect.bottom > self.rect.bottom:
            self.rect.bottom = self.player.rect.bottom

        self.offset.x = self.rect.left - settings.CAMERA_BOX['left']
        self.offset.y = self.rect.top - settings.CAMERA_BOX['top']

    def draw_with_camera(self):

        self.update_camera()

        for sprite in self.sprites():
            pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, pos)

        if not settings.SHOW_DEAD_LEVEL:
            return
        start_pos = (0, self.dead_line - self.offset[1])
        end_pos = (settings.WINDOW_WIDTH, self.dead_line - self.offset[1])
        pg.draw.line(self.display_surface,
                     settings.DEAD_LEVEL_COLOR, start_pos, end_pos)
