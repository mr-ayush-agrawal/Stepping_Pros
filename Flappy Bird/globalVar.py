'''
This file contains all the Global Variable which shall be constant throughout the game
This only defines the status and the things present in the game.
'''

import pygame
from pygame import *

FPS = 45
SCREENWIDTH = 875
SCREENHEIGHT = 816
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
# BASEY = SCREENHEIGHT * 0.85
BASEY = SCREENHEIGHT * 0.85 + 2.4
GAME_IMAGES = {}
GAME_SOUNDS = {}
BIRD = 'Flappy Bird/Gallery/Images/bird.png'
BACKGROUND = 'Flappy Bird/Gallery/Images/Background.png'
PIPE = 'Flappy Bird/Gallery/Images/pipe.png'