import editor
import play
import pygame as pg
import settings
import tools
from pygame.key import get_pressed as keys_pressed


class GameMaker:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        # Ui
        self.ui = tools.Ui()
        # Modes
        self.mode = 'edit'
        self.editor = editor.EditorController(self)
        self.play = play.PlayController(self)

        self.modes_funcs = {
            "edit": self.editor.run,
            "play": self.play.run
        }
        self.events_funcs = {
            "edit": self.editor.events,
            "play": self.play.events
        }

    def run(self, dt: float):

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit(0)
            if event.type == pg.KEYDOWN:
                keys = keys_pressed()
                if keys[pg.K_LCTRL] and keys[pg.K_d]:
                    settings.DEBUG = not settings.DEBUG
                elif keys[pg.K_LCTRL] and keys[pg.K_r]:
                    self.mode = 'play' if self.mode == 'edit' else 'edit'
                    self.play.set_canvas_images(
                        self.editor.get_canvas_images())
            if self.ui.click(event):
                self.mode = 'play' if self.mode == 'edit' else 'edit'
                self.play.set_canvas_images(self.editor.get_canvas_images())

            self.events_funcs[self.mode](event)

        # Always
        self.modes_funcs[self.mode](dt)
