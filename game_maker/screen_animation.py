import pygame
import settings
import star


class ScreenAnimation:
    def __init__(self, state: str):
        pygame.init()
        self.display_surface = pygame.display.get_surface()
        rect = self.display_surface.get_rect()
        self.surface = pygame.Surface(rect.size)
        self.surface.set_colorkey(settings.ANIMATION_COLOR)

        self.corner_distance = settings.WINDOW_WIDTH / 2
        self.small_distance = self.corner_distance * 0.9
        self.center = settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 2

        self.animation_speed = settings.ANIMATION_SPEED
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 20)

        self.state = state

    def move(self):
        self.corner_distance -= self.animation_speed
        self.small_distance = self.corner_distance * 0.9

    def animate(self):
        x, y = star.get_star_points(
            16, self.corner_distance, self.small_distance, 0, self.center)
        self.surface.fill('black')
        pygame.draw.polygon(
            self.surface, settings.ANIMATION_COLOR, list(zip(x, y)))
        self.display_surface.blit(self.surface, (0, 0))
        self.move()

    def is_done(self) -> bool:
        return self.corner_distance <= 0

    def stop_events(self):
        pygame.time.set_timer(self.timer_event, 0)

    def __del__(self):
        pass
