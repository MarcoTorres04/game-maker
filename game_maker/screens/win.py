import pygame as pg
import settings
import state_machine as sm
from pygame.key import get_pressed as keys_pressed
from pygame.mouse import get_pressed as mouse_pressed


class WinScreen:
    def __init__(self, state_machine: sm.StateMachine):
        self.display_surface = pg.display.get_surface()
        self.state_machine = state_machine
        self.font = pg.font.SysFont(
            settings.FONT, settings.START_MENU_FONTSIZE * 2)

    def set_player(self, player):
        self.player = player

    def input(self):
        keys = keys_pressed()
        mouse = mouse_pressed()
        if keys[pg.K_RETURN] or keys[pg.K_ESCAPE] or mouse[0]:
            self.state_machine.pop()
            self.state_machine.push('edit')

    def update(self):
        self.input()

    def draw(self):
        self.display_surface.fill(settings.START_MENU_BG)
        # Title
        string = "Nivel Superado"
        text = self.font.render(string, True, 'Crimson',
                                settings.START_MENU_BG)
        rect = text.get_rect()
        rect.center = settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 2
        self.display_surface.blit(text, rect)
        # Score
        string = f"Score: {self.player.score}"
        text = self.font.render(string, True, 'Crimson',
                                settings.START_MENU_BG)
        rect = text.get_rect()
        rect.center = settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 1.5
        self.display_surface.blit(text, rect)

    def loop(self, dt: float):
        self.update()
        self.draw()
