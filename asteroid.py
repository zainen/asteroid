import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt / 1000

    def rotate(self, angle):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(angle)
        rotated_speed_with_vector = rotated_vector
        self.position += rotated_speed_with_vector


    def split(self):
        self.kill()
        radius = self.radius - ASTEROID_MIN_RADIUS

        if ASTEROID_MIN_RADIUS < radius:
            log_event("asteroid_split")
            (x,y) = self.position

            a1 = Asteroid(x, y, radius)
            random_1 = random.uniform(20,50)
            a1_vec = self.velocity.rotate(random_1)
            a1.velocity = a1_vec

            a2 = Asteroid(x, y, radius)
            random_2 = random.uniform(-20,50)
            a2_vec = self.velocity.rotate(random_2)
            a2.velocity = a2_vec
        

