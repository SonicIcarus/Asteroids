from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        # Circleshape needs to be initialised
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # set up our shape
    def triangle(self):
        #get our orientation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # perpendicular vector to forward
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        # assemble the points
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # rotate by players turn speed * {-dt to +dt} 
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # unit vector points forward and speed is applied * {-dt to +dt}
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # keeps log of key press data for us updates dt to keep cycles in order
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        elif keys[pygame.K_d]:
            self.rotate(dt)
            
        if keys[pygame.K_w]:
            self.move(dt)
        elif keys[pygame.K_s]:
            self.move(-dt)

    """ 
    screen: send the surface to render on
    pygame.draw.polygon: draw a three (or more) sided shape
    "white": apply a color 
    self.triangle(): send it the co-ordinates 
    2: apply a width or size to the shape
    """
    def draw(self, screen):
        
        pygame.draw.polygon(screen, "white", self.triangle(), 2)