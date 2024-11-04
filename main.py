import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock=pygame.time.Clock()

    """
    pygame allows gameobjects to added to groups and is the convention I'm told. This does allow us a group of items
    that should operate under the same logic i.e. drawing or interacting with environment

    In our case so far its only the player with their update (asteroids and bullets will follow a similar update method)
    and the player with their draw (you get the trend)
    """
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    collision_group = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Set which groups asteroids should be a part of
    Asteroid.containers = (asteroids, updateable, drawable, collision_group)
    AsteroidField.containers = (updateable,) #comma to make it a tuple

    # Add the player to their groups
    updateable.add(player)
    drawable.add(player)
    collision_group.add(player)
    Player.containers = (updateable, drawable, collision_group)

    # add bullets to group
    Bullet.containers = (bullets, updateable, drawable, collision_group)

    # spawns asteroids
    asteroid_field = AsteroidField()
    # created seperate game_loop function to handle running my game engine(chugging like a train choo choo)
    game_loop(screen, clock, updateable, collision_group, drawable, dt=0)
    

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
    return True

# Where the magic happens: runs the show/handles objects/beins our time log dt
def game_loop(screen, clock, updatable, drawable, collision_group, dt):
    running = True
    print(len(f"total drawables: {drawable}"))
    while running:
        screen.fill("black")
        for gameobject in updatable:
            gameobject.update(dt)
        for gameobject in drawable:
            gameobject.draw(screen)

        player = next((sprite for sprite in collision_group if isinstance(sprite, Player)), None)

        if player:
            for asteroid in collision_group:
                if isinstance(asteroid, Asteroid) and asteroid.collides_with(player):
                    print("Game over!")
                    sys.exit()

        for sprite1 in collision_group:
            if isinstance(sprite1, Bullet):  # if it's a bullet
                for sprite2 in collision_group:
                    if isinstance(sprite2, Asteroid):  # if it's an asteroid
                        if sprite2.collides_with(sprite1):  # use sprite1 and sprite2
                            sprite1.kill()  # kill() is a method on the sprite
                            sprite2.split()

        pygame.display.flip()
        running = events()
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()
