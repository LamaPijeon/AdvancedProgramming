import os
import cv2 as cv
import numpy as np
# import matplotlib as mplot
# import ntpath

imagesDone = 0
def getImages(image, fileType, path):
    global imagesDone
    name = image[image.rfind('/')+1:image.rfind('.')]+'-Color'+fileType
    imageColor = cv.imread(image, cv.IMREAD_COLOR)
    cv.imwrite(path+'/' + name, imageColor)

    name = image[image.rfind('/')+1:image.rfind('.')]+'-Gray'+fileType
    imagePath = cv.imread(image, cv.IMREAD_GRAYSCALE)
    cv.imwrite(path+'/' + name, imagePath)
   
    imagesDone += 1
    print()
    print(imagesDone)
    return imageColor

def getFolder(image, parent):
    global possibleValues 
    imagePath = os.path.join(parent, image)
    fileType = imagePath[imagePath.rfind('.'):]
    if image != '.DS_Store' and fileType in possibleValues:
        path = imagePath + "_f"
        os.mkdir(path)
        getImages(imagePath, fileType, path)
        imColor = getImages(imagePath, fileType, path)

        imLab = cv.cvtColor(imColor, cv.COLOR_BGR2Lab)
        l,a,b = cv.split(imLab)

        os.remove(imagePath)

# Parent Directory path
parentDir = "/Users/24nowak_p/Desktop/School/Programming/Programming Class/AdvancedProgramming/Python/Image Coloriser/Images/"
imageList = next(os.walk(parentDir))[2]
possibleValues = ['.jpg', 
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

for image in imageList:
    print(image)
    getFolder(image, parentDir)
    # imageList.remove(image)