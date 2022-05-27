import cv2 as cv
import numpy as np
import os

acceptableFileTypes = ['.jpg', 
                  '.jpeg', 
                  '.png', 
                  '.webp', 
                  '.jp2', 
                  '.bmp', 
                  '.dib', 
                  '.pbm', 
                  '.pgm', 
                  '.ppm', 
                  '.pxm', 
                  '.pnm', 
                  '.pfm', 
                  '.sr', 
                  '.tiff', 
                  '.sr', 
                  '.tiff', 
                  '.tif', 
                  '.exr', 
                  '.hdr', 
                  '.pic']

def colorise(image):
    theImage = cv.imread(image, cv.IMREAD_GRAYSCALE)
    r = np.zeros(shape=theImage.shape)
    g = np.zeros(shape=theImage.shape)
    b = np.zeros(shape=theImage.shape)
    theImage = cv.cvtColor(theImage, cv.COLOR_GRAY2RGB)
    for row in range(len(r)):
        for column in range(len(r)):
            rValue = np.random.uniform(0,255)
            gValue = np.random.uniform(0,255)
            bValue = np.random.uniform(0,255)

            if row != 0 and column != 0: # not first row or collumn
                if row > 1 and column > 1:
                    rValue = ( rValue + r[row-1][column] + r[row][column-1] +  r[row-1][column-1] + r[row-2][column] + r[row-2][column-1] + r[row-2][column-2] + r[row][column-1] + r[row][column-2] ) / 9
                    gValue = ( gValue + g[row-1][column] + g[row][column-1] +  g[row-1][column-1] + g[row-2][column] + g[row-2][column-1] + g[row-2][column-2] + g[row][column-1] + g[row][column-2] ) / 9
                    bValue = ( bValue + b[row-1][column] + b[row][column-1] +  b[row-1][column-1] + b[row-2][column] + b[row-2][column-1] + b[row-2][column-2] + b[row][column-1] + b[row][column-2] ) / 9
                else:
                    rValue = ( rValue + r[row-1][column] + r[row][column-1] + r[row-1][column-1] ) / 4
                    gValue = ( gValue + g[row-1][column] + g[row][column-1] + g[row-1][column-1] ) / 4
                    bValue = ( bValue + b[row-1][column] + b[row][column-1] + b[row-1][column-1] ) / 4
            elif row != 0: # first column, but not row
                if row > 1:
                    rValue = ( rValue + r[row-1][column] + r[row-2][column] ) / 3
                    gValue = ( gValue + g[row-1][column] + g[row-2][column] ) / 3
                    bValue = ( bValue + b[row-1][column] + b[row-2][column] ) / 3
                else:
                    rValue = ( rValue + r[row-1][column] ) / 2
                    gValue = ( gValue + g[row-1][column] ) / 2              
                    bValue = ( bValue + b[row-1][column] ) / 2              
            elif column != 0: # first row, but not colun
                if column > 1:
                    rValue = ( rValue + r[row][column-1] + r[row][column-2] ) / 3
                    gValue = ( gValue + g[row][column-1] + g[row][column-2] ) / 3
                    bValue = ( bValue + b[row][column-1] + b[row][column-2] ) / 3
                else:
                    rValue = ( rValue + r[row][column-1] ) / 2
                    gValue = ( gValue + g[row][column-1] ) / 2          
                    bValue = ( bValue + b[row][column-1] ) / 2          
            r[row][column] = "{:.2f}".format(rValue)
            g[row][column] = "{:.2f}".format(gValue)
            b[row][column] = "{:.2f}".format(bValue)

    r = (r + theImage[:,:,0]) / 2
    g = (g + theImage[:,:,1]) / 2
    b = (b + theImage[:,:,2]) / 2
        
    newImage = np.dstack([r,g,b])
    newImage = cv.normalize(src=newImage, dst=None, alpha=1, beta=265, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)
    newImage = cv.cvtColor(newImage, cv.COLOR_BGR2LAB)
    return newImage

def printImages(image, path):
    cv.imshow('image', image)
    cv.waitKey(0)

imagePath = input("Drag and drop the image that you want colored:  ")[1:-1]

period = imagePath.rfind('.')

if imagePath[period:] in acceptableFileTypes:
    image = colorise(imagePath)
    printImages(image, imagePath[:period]+'-color')