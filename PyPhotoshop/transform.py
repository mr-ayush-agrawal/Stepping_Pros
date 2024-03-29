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

def adjustContast(image, factor, mid = 0.5):
    '''Contrast increases the diffetence from the mid-point
    Increaseing the difference by factors times    '''

    x_pixels, y_pixels, num_channels = image.array.shape
    newImage = Image(x_pixel=x_pixels, y_pixel = y_pixels, num_channels=num_channels)

    '''# Intutive way 
    for x in range(x_pixels):
        for y in range (y_pixels):
            for num in range(num_channels):
                newImage.array[x,y,num] = (image.array[x,y,num] - mid) * factor + mid'''

    newImage.array = (image.array - mid) * factor + mid

    return newImage


def blur(image, size):
    '''size is the number of pixels to take into account whrn applying blur
    The Pixels are from Left/Right/Top/Bottom/Diagonals
    size should always be a odd number'''

    # Creating new image
    x_pixel, y_pixel, num_channels = image.array.shape
    newImage = Image(x_pixel=x_pixel, y_pixel=y_pixel, num_channels=num_channels)

    neighbour = size//2             # Number of neighbour at a side
    for x in range(x_pixel):
        for y in range(y_pixel):
            for z in range(num_channels):
                # Going through the neighbour and summing
                total = 0
                for x_i in range(max(0, x-neighbour), min(x+neighbour,x_pixel-1)+1):
                    for y_i in range(max(0, y-neighbour), min(y_pixel-1,y+neighbour)):
                        total += image.array[x_i,y_i,z]
                    
                # Normalizing it (As we are summing over squre)
                newImage.array[x,y,z] = total/(size**2)

    return newImage
    # '''Note : In this function we implementd the blur of kernal size n
    # where each value is 1/n**2; for ex of size = 3 the kernal matrix is 
    # [1/9 1/9 1/9]
    # [1/9 1/9 1/9]
    # [1/9 1/9 1/9]
    # '''



def apply_kernal(image, kernal):
    '''Kernal should be a 2D matrix of any diamension
    For simplycity we shall be using a NxN square matrix
    '''

    # Creating new image
    x_pixel, y_pixel, num_channels = image.array.shape
    newImage = Image(x_pixel=x_pixel, y_pixel=y_pixel, num_channels=num_channels)

    neighbour = kernal.shape[0]//2
    for x in range(x_pixel):
        for y in range(y_pixel):
            for z in range(num_channels):
                # Going through the neighbour and summing
                total = 0
                for x_i in range(max(0, x-neighbour), min(x+neighbour,x_pixel-1)+1):
                    for y_i in range(max(0, y-neighbour), min(y_pixel-1,y+neighbour)):
                        x_k = x_i + neighbour - x
                        y_k = y_i + neighbour - y
                        kernal_val = kernal[x_k, y_k]
                        total += image.array[x_i,y_i,z] * kernal_val

                # Normalizing it (As we are summing over squre)
                newImage.array[x,y,z] = total

    return newImage

def combine_images(image1, image2):
    '''Combine 2 images using squred sum of squares : val= sqrt(value_1**2, value_2**2)
    size of image 1 == image2
    '''
    # if (image1.array.shape != image2.array.shape):
    #     return
    
    # Creating new image
    x_pixel, y_pixel, num_channels = image1.array.shape
    newImage = Image(x_pixel=x_pixel, y_pixel=y_pixel, num_channels=num_channels)
    
    for x in range(x_pixel):
        for y in range(y_pixel):
            for z in range(num_channels):
                newImage.array[x,y,z] = np.sqrt(image1.array[x,y,z]**2 + image2.array[x,y,z])

        return newImage


if __name__ == '__main__':
    if not getcwd().endswith('PyPhotoshop'):
        chdir(getcwd() + '/PyPhotoshop')
        # print(getcwd())

    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    # lets Contrast the imgae
    # brightenImage = adjustContast(lake, .3)
    # brightenImage.write_image('lakeBright.png')
    # brightenImage = adjustContast(lake, 1.2)
    # brightenImage.write_image('lakeDark.png')

    # Adding blur
    # blurImg = blur(city, 3)
    # blurImg.write_image('blurcity3.png')
    # blurImg = blur(city, 17)
    # blurImg.write_image('blurcity7.png')
    
    # Edge detection using sobel's kernal
    sobel_x_kernal = np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ])
    sobel_y_kernal = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])

    edgeX = apply_kernal(lake, sobel_x_kernal)
    edgeX.write_image('Xedge.png')
    edgeY = apply_kernal(lake, sobel_y_kernal)
    edgeY.write_image('Yedge.png')

    edges = combine_images(edgeX, edgeY)
    edges.write_image("Edge_detection.png")