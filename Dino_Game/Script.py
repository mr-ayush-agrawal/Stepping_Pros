import pyautogui as pg
from PIL import ImageGrab
from time import sleep
def hit(key):
    pg.keyDown(key)

def isCollide(imdata,ref):
    for i in range (350,510):
        for j in range(630, 740):
            if imdata[i,j] != ref:
                return True
            
    for i in range (710,800):
        for j in range(500,630):
            if abs(imdata[i,j] - ref) > 40 :
                return True

    return False

if __name__ == '__main__':

    sleep(2)

    while True :
        # Taking SS of the screen in grey scale
        image = ImageGrab.grab().convert('L')
        # this is used to convert the image to arraafu frmat
        imdata = image.load()
        ref = imdata[105,205]
        if isCollide(imdata,ref):
            hit('UP')
        