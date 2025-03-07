# Name:     Onur Onel
# StudenID: 0865803
# Email:    onuronel@trentu.ca
# Date:     02.13.2025
# Part2:    Image Processing & Gray-Scale Inverse Conversion

import matplotlib.pyplot 
import numpy

myImage = matplotlib.pyplot.imread('flower.png') # Load the image as an array

# Extract height and width
height=myImage.shape[0] # Number of rows
width=myImage.shape[1]  # Number of columns

# Convert the image to grayscale, then invert it
for x in range(0, height-1):
   for y in range(0,width-1):
        rgbAverage = numpy.mean(myImage[x, y][:3]) # Compute the average of RGB
        rgbAverage = 1-rgbAverage  # Inverse the grayscale value
        myImage[x, y] = [rgbAverage,rgbAverage,rgbAverage,1] # Assign as inversed grayscale 

# Display the grayscaled image
imgplot = matplotlib.pyplot.imshow(myImage) 
matplotlib.pyplot.show()
