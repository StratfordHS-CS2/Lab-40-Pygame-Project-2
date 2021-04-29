import pygame, sys, random
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    '''
    This class represents the player.
    It derives its properites from the Sprite class.
    '''
    def __init__(self, x, y, scale_factor):
        super().__init__()
        # add more setup code here

    
    def update(self):
        # add code that should run each frame to update the player
        pass

    def draw(self):
        # add any drawing code here (like blit)
        pass


pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

BGCOLOR = (100, 200, 100)

screen = pygame.display.set_mode((0,0), FULLSCREEN)
WIDTH = screen.get_width()
HEIGHT = screen.get_height()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill(BGCOLOR)

    pygame.display.update()

    fpsClock.tick(FPS)

