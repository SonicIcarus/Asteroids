# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    events()
    set_up_screen(screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH)))

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

def set_up_screen(screen):
    while True:
        screen.fill(color="Black")
        pygame.display.flip()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()