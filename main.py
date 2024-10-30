# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    game_loop(screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)), clock=pygame.time.Clock(), dt=0, player=Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
    return True

def game_loop(screen, clock, dt, player):
    running = True  # Start with the game running
    while running:  # Keep going while running is True
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        running = events()  # Store the result from events()
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()