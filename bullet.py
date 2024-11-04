from circleshape import CircleShape
from constants import *

class Bullet(CircleShape):
    def __init__(self, x, y):
        # Circleshape needs to be initialised
        super().__init__(x, y, BULLET_RADIUS)
        self.__width = 2

    def draw(self, screen):
        pygame.draw.circle(screen, BULLET_COLOR, self.position, self.radius, self.__width)

    def update(self, dt):
        self.position += self.velocity * dt
