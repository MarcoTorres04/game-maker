import editor
import play
import pygame as pg
import settings
import state_machine
import tools
from pygame.key import get_pressed as keys_pressed
import start
import animations


class GameMaker:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.ui = tools.Ui()
        self.state_machine = state_machine.StateMachine()
        self.state_machine.push('start_menu')
        self.editor = editor.EditorController(self, self.state_machine)
        self.play = play.PlayController(
            self, self.state_machine, self.editor.canvas.canvas_tiles)
        self.start = start.StartMenu(self.state_machine)
        self.animation = animations.ScreenAnimation(self.state_machine)

        self.events_funcs = {
            "edit": self.editor.events,
            "play": self.play.events,
            "start_menu": self.start.input
        }

        self.state_funcs = {
            "edit": self.editor.run,
            "play": self.play.run,
            "start_menu": self.start_menu_state,
            "activate_play": self.active_play,
            "animate": self.animation.animate,
            "win": self.play.win_screen.loop
        }

    def run(self, dt: float):

        state = self.state_machine.view()

        # State Machine
        if state is None:
            pg.quit()
            exit(0)

        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit(0)
            if event.type == pg.KEYDOWN:
                keys = keys_pressed()

                if keys[pg.K_LCTRL] and keys[pg.K_d]:
                    settings.DEBUG = not settings.DEBUG

            if state in self.events_funcs:
                self.events_funcs[state](event)

        # # Always
        self.state_funcs[state](dt)

    def start_menu_state(self, dt: float):
        self.start.update()
        self.start.draw()

    def active_play(self, dt: float):
        self.play.start_level(self.editor.canvas.canvas_tiles.copy())
        self.state_machine.pop()
        self.state_machine.push('animate')
