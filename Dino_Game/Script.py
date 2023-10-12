import pyautogui as pg
from PIL import Image, ImageGrab
from time import sleep

def hit(key):
    pg.keyDown(key)

def isCollide(imdata):
    for i in range (370,500):
        for j in range(630, 740):
            if imdata[i,j] >= 160:
                return True
    return False

    
def draw():
    '''This we are using for making the square for detecting the position of the obstacle'''

if __name__ == '__main__':

    sleep(2)

    # while True :
    #     # Taking SS of the screen in grey scale
    #     image = ImageGrab.grab().convert('L')
    #     # this is used to convert the image to arraafu frmat
    #     imdata = image.load()

    #     if isCollide(imdata):
    #         hit('UP')
        

    image = ImageGrab.grab()
    imdata = image.load()
    for i in range (370,500):
        for j in range(630, 740):
            imdata[i,j] = 160

    image.show()