# Name:     Onur Onel
# StudenID: 0865803
# Email:    onuronel@trentu.ca
# Date:     02.13.2025
# Part1:    Image Processing & Gray-Scale Conversion

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

# Since human eyes not perceive RGB colors equally, luminance formula gives a more accurate grayscale image.
# Each luminance value is calculated by taking the weighted sum of the RGB values of the corresponding pixel.
# The standard luminance equation `Y = 0.299R + 0.587G + 0.114B`
# for x in range(0, height-1):
#    for y in range(0,width-1):
#         luminance = (0.299 * myImage[x, y][0]) + (0.587 * myImage[x,y][1]) + (0.114 * myImage[x, y][2])
#         myImage[x,y] = [luminance, luminance, luminance, myImage[x,y][3]]
        
# Display the grayscaled image
imgplot = matplotlib.pyplot.imshow(myImage) 
matplotlib.pyplot.show()
