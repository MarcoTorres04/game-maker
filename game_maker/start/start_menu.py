import pygame as pg
import settings
import state_machine as sm
from pygame.key import get_pressed as keys_pressed


class StartMenu:
    def __init__(self, state_machine: sm.StateMachine):
        self.display_surface = pg.display.get_surface()
        self.image = pg.image.load(settings.TILES_PATH / 'ui' / 'main.png')
        self.state_machine = state_machine
        self.font = pg.font.SysFont(
            settings.FONT, settings.START_MENU_FONTSIZE * 2)
        self.sub_font = pg.font.SysFont(
            settings.FONT, settings.START_MENU_FONTSIZE)
        self.title_index = 0
        self.color = settings.START_MENU_TITLE_COLORS[self.title_index]

    def input(self, event: pg.event.Event):
        if not (event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN):
            return
        keys = keys_pressed()
        if keys[pg.K_RETURN]:
            self.state_machine.push('edit')
        elif keys[pg.K_ESCAPE]:
            self.state_machine.pop()
            return

    def update(self):
        self.title_index += settings.START_MENU_SPEED
        self.color = settings.START_MENU_TITLE_COLORS[int(self.title_index)]
        self.title_index %= (len(settings.START_MENU_TITLE_COLORS) - 1)

    def draw(self):
        self.display_surface.fill(settings.START_MENU_BG)
        string = 'Press Return to Start'
        text = self.sub_font.render(string, True, self.color,
                                    settings.START_MENU_BG)
        rect = text.get_rect()
        rect.center = settings.WINDOW_WIDTH // 6, settings.WINDOW_HEIGHT // 1.15
        self.display_surface.blit(self.image, (0, 0))
        self.display_surface.blit(text, rect)
