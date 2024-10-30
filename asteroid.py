from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Circleshape needs to be initialised
        super().__init__(x, y, radius)
        self.__width = 2

    def update(self, dt):
       # Use the position and velocity from the parent class
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, self.__width)