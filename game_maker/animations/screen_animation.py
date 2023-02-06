import pygame
import settings
from .star import get_star_points
import state_machine as sm


class ScreenAnimation:
    def __init__(self, state_machine: sm.StateMachine):
        # pygame.init()
        self.display_surface = pygame.display.get_surface()
        self.state_machine = state_machine
        rect = self.display_surface.get_rect()
        self.surface = pygame.Surface(rect.size)
        self.surface.set_colorkey(settings.ANIMATION_COLOR)
        self.set_animations_values()

        self.animation_speed = settings.ANIMATION_SPEED

    def set_next_state(self, state: str):
        self.next_state = state

    def move(self, dt: float):
        self.corner_distance -= self.animation_speed * dt
        self.small_distance = self.corner_distance * 0.9

    def animate(self, dt: float):
        x, y = get_star_points(
            16, self.corner_distance, self.small_distance, 0, self.center)
        self.surface.fill('black')
        pygame.draw.polygon(
            self.surface, settings.ANIMATION_COLOR, list(zip(x, y)))
        self.display_surface.blit(self.surface, (0, 0))
        self.move(dt)
        if self.is_done():
            self.state_machine.pop()
            self.state_machine.push('play')
            self.set_animations_values()

    def set_animations_values(self):
        self.corner_distance = settings.WINDOW_WIDTH / 2
        self.small_distance = self.corner_distance * 0.9
        self.center = settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 2

    def is_done(self) -> bool:
        return self.corner_distance <= 0

    def __del__(self):
        pass
