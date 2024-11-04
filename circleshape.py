import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # allows the use of containers pygame parent classes group functionalities: See updateable and drawable in main.py 
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        # still inherits from pygame.sprite.Sprite just now with-out our containers named
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius
