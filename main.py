# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # used to update our dt which keeps our program from eating cpu cycles
    clock=pygame.time.Clock()

    """
    pygame allows gameobjects to added to groups and is the convention I'm told. This does allow us a group of items
    that should operate under the same logic i.e. drawing or interacting with environment

    In our case so far its only the player with their update (asteroids and bullets will follow a similar update method)
    and the player with their draw (you get the trend)
    """
    updateable = pygame.sprite.Group()
    updateable.add(player)
    drawable = pygame.sprite.Group()
    drawable.add(player)
    # created seperate game_loop function to handle running my game engine(chugging like a train choo choo)
    game_loop(screen, clock, updateable, drawable, dt=0)
    

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
    return True
# Where the magic happens: runs the show/handles objects/beins our time log dt
def game_loop(screen, clock, updatable, drawable, dt):
    running = True  # Start with the game running
    while running:  # Keep going while running is True
        screen.fill("black")
        # here we have a group of gameobjects created in main() that share logic and are called efficently
        for gameobjects in updatable:
            gameobjects.update(dt)
        for gameobjects in drawable:
            gameobjects.draw(screen)
        
        # keep updating frames in the animation
        pygame.display.flip()

        # Store the result from events() which closes screen with x button on window hotkey
        running = events()

        # restricts game to 60fps
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()