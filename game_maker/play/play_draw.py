import typing

import pygame as pg
import settings

if typing.TYPE_CHECKING:
    from .play_controller import PlayController


class PlayDrawer:
    def __init__(self, play: 'PlayController'):
        self.display_surface = pg.display.get_surface()
        self.play = play
        self.font = pg.font.SysFont(settings.FONT, settings.FONT_SIZE)

    def __call__(self):
        self.display_surface.fill(settings.SCREEN_FILL)
        self.play.level.draw_sprites.draw_with_camera()
        self.play.ui.draw('play')
        if self.play.player is None:
            return
        # rect = self.play.player.hitbox.copy()
        # rect.topleft -= self.play.level.draw_sprites.offset
        # rect2 = self.play.player.rect.copy()
        # rect2.topleft -= self.play.level.draw_sprites.offset
        # pg.draw.rect(self.display_surface, 'green', rect, 2)
        # pg.draw.rect(self.display_surface, 'red', rect2, 2)
        self.show_score()

    def show_score(self):
        string = f"Score: {self.play.player.score}"
        text = self.font.render(string, True, settings.PLAY_UI_FONT_COLOR,
                                settings.PLAY_UI_BG)
        rect = text.get_rect()
        rect.center = settings.WINDOW_WIDTH - settings.TILE_SIZE, 10
        self.display_surface.blit(text, rect)
