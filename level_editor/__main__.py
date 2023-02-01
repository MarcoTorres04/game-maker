import editor
import pygame
import settings


class MainLoop:
    def __init__(self):
        self.display_surface = pygame.display.set_mode(
            (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.editor = editor.Editor()

    def run(self):
        while True:
            dt = self.clock.tick(settings.FPS) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                self.editor.run(event, dt)
            pygame.display.flip()


main_loop = MainLoop()
main_loop.run()
