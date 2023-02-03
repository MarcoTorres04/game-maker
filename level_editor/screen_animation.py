import settings
import pygame


class ScreenAnimation:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        top = 0
        left = -settings.WINDOW_WIDTH
        width = int(settings.WINDOW_WIDTH * 1.05)
        height = settings.WINDOW_HEIGHT // 5 * 3
        self.surface_1 = pygame.Surface((width, height))
        self.rect_1 = self.surface_1.get_rect()
        self.rect_1.topleft = (left, top)

        top = settings.WINDOW_HEIGHT // 5 * 2
        left = settings.WINDOW_WIDTH
        self.surface_2 = pygame.Surface((width, height))
        self.rect_2 = self.surface_2.get_rect()
        self.rect_2.topleft = (left, top)

        self.animation_speed = settings.ANIMATION_SPEED
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 10)

    def move(self):
        self.rect_1.left += int(self.animation_speed)
        self.rect_2.left -= int(self.animation_speed)

    def animate(self):
        self.surface_1.fill(settings.ANIMATION_COLOR)
        self.surface_2.fill(settings.ANIMATION_COLOR)
        self.display_surface.blit(self.surface_1, self.rect_1.topleft)
        self.display_surface.blit(self.surface_2, self.rect_2.topleft)
        self.move()

    def is_done(self) -> bool:
        return self.rect_1.left > settings.WINDOW_WIDTH

    def __del__(self):
        pygame.time.set_timer(self.timer_event, 0)
        print('Se detuvo el timer')
