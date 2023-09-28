# This is the main file where Bulf of the code is
import numpy as np
from image import Image
from os import getcwd, chdir


def adjustBrightness(image, factor):
    '''Here we will adjust the brightness of the image just scale up/down with some factor
    factor > 0 -> how much we want to change it (>1 = Brighten, <1 = Darken) it '''

    # getting the sizes
    x_pixels, y_pixels, num_channels = image.array.shape

    # Creating a new Image
    newImage = Image(x_pixel=x_pixels, y_pixel = y_pixels, num_channels=num_channels)
    '''# Intutive way -> scaling each pixel
    for x in range(x_pixels):
        for y in range(y_pixels):
            for ch in range(num_channels):
                newImage.array[x,y,ch] = image.array[x,y,ch]*factor'''
    
    # Vectorized approach
    newImage = image.array * factor

    return newImage


if __name__ == '__main__':
    if not getcwd().endswith('PyPhotoshop'):
        chdir(getcwd() + '/PyPhotoshop')
        # print(getcwd())

    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    # lets brighten the imgae
    brightenImage = adjustBrightness(lake, 1.7)
    brightenImage.write_image('lakeBright.png')
    brightenImage = adjustBrightness(lake, .5)
    brightenImage.write_image('lakeDark.png')
