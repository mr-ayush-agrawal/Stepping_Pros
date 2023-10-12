import pyautogui as pg
from PIL import Image, ImageGrab
from time import sleep

def hit(key):
    pg.keyDown(key)
    
def draw():
    '''This we are using for making the square for detecting the position of the obstacle'''


def takeSS():
    # Grabbing it in grey scale
    image = ImageGrab.grab().convert('L')
    # image.show()
    return image

sleep(2.5)
image = takeSS()  
# this is used to convert the image to arraafu frmat
imdata = image.load()

for i in range (200,225):
    for j in range(600, 730):
        imdata[i,j] = 0
image.show()
