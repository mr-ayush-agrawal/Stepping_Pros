import numpy as np
import png
from os import getcwd, chdir

class Image :
    def __init__ (self, x_pixel=0, y_pixel=0, num_channels = 0, filename=''):
        # Here you need to either input the filename or x,y pixels, numchannels

        self.input_path = '/input/'
        self.output_path = '/output/'
        if x_pixel and y_pixel and num_channels :
            self.x_pixels = x_pixel
            self.y_pixels = y_pixel
            self.num_channels = num_channels
            self.array = np.zeros(x_pixel,y_pixel,num_channels)

        elif filename :
            self.array = self.read_image(filename)
            self.x_pixels, self.y_pixels, self.num_channels = self.array.shape

        else :
            raise ValueError ("You Need to input either the file name or specify the diamension of the image")
        
    def read_image(self, filename, gamma = 2.2):
        # Gamma is just for encodig and decodeing the image
        '''Takes the PNG RGB image file and returns the 3D np array with Y,X,channel
        values  and float, gamma is decoded'''
        
        # print(getcwd() + self.input_path + filename)
        im = png.Reader(getcwd() + self.input_path + filename).asFloat()
        resized_image = np.vstack(list(im[2]))
        resized_image .resize(im[1],im[0],3)
        resized_image = resized_image**gamma
        return resized_image
    
    def write_image(self, output_file_name, gamma = 2.2):
        """3D numpy array (Y,X, channels) values of range 0-1 -> write it to a png"""
        im = np.clip(self.array, 0,1)
        y,x = self.array.shape[0], self.array.shape[1]
        im = im.reshape(y,x*3)
        writer = png.Writer(x,y)
        with open (getcwd() + self.output_path + output_file_name , 'wb') as f:
            writer.write(f,255*(im**(1/gamma)))
        self.array.resize(y,x,3)

if __name__ =='__main__' :
    if not getcwd().endswith('PyPhotoshop'):
        chdir(getcwd() + '/PyPhotoshop')
        # print(getcwd())

    # This is just for the testing purpose
    im = Image(filename='lake.png')
    im.write_image('test.png')