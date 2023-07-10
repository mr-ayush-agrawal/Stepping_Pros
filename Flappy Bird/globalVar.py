import pygame
from pygame import *

FPS = 45
SCREENWIDTH = 600
SCREENHEIGHT = 960
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
BASEY = SCREENHEIGHT * 0.85
GAME_IMAGES = {}
GAME_SOUNDS = {}
BIRD = 'Gallery/Images/bird.png'
BACKGROUND = 'Gallery/Images/Background.png'
PIPE = 'Gallery/Images/pipe.png'