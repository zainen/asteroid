from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, LINE_WIDTH, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, position, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        vel = pygame.Vector2(0, 1) * PLAYER_SHOOT_SPEED
        rotated_vel = vel.rotate(rotation)
        self.velocity = rotated_vel
        # unit_vector = pygame.Vector2(0, 1)
        # rotated_vector = unit_vector.rotate(rotation)
        # rotated_speed_with_vector = rotated_vector * self.velocity
        # self.position = rotated_speed_with_vector



    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt / 1000
