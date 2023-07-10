import random 
import sys
from load import *

# Our Program will start from here
pygame.init()
FPSCLOCK = time.Clock()     # -> From pygame
display.set_caption("Flappy Bird")

loadImages()        # Loading the images form the system to program
loadSounds()        # Loading Sound files
