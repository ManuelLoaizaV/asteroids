import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position, radius=SHOT_RADIUS):
        super().__init__(position.x, position.y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt: float):
        self.position += self.velocity * dt
