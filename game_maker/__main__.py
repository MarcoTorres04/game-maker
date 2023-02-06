import game_maker
import pygame as pg
import settings


class MainLoop:
    def __init__(self):
        # Init Setup
        pg.init()
        self.display_surface = pg.display.set_mode(
            (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pg.display.set_caption(settings.WINDOW_TITLE)
        self.clock = pg.time.Clock()
        # Cursor
        cursor_path = settings.TILES_PATH / 'ui' / 'cursor.png'
        cursor_surface = pg.image.load(cursor_path).convert_alpha()
        cursor = pg.cursors.Cursor((0, 0), cursor_surface)
        pg.mouse.set_cursor(cursor)
        # Maker
        self.game_maker = game_maker.GameMaker()

    def run(self):
        while True:
            dt = self.clock.tick(settings.FPS) / 50
            self.game_maker.run(dt)
            pg.display.flip()
            pg.display.update()


main_loop = MainLoop()
main_loop.run()
