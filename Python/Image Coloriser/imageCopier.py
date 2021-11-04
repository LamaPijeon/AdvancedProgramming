import os
import cv2 as cv
import numpy as np
# import matplotlib as mplot
# import ntpath

# Parent Directory path
parentDir = "/Users/24nowak_p/Desktop/School/Programming/Programming Class/AdvancedProgramming/Python/Image Coloriser/Images/"

# print(len(next(os.walk(parentDir))[2])-1) #Number of images to be converted and dealt with

itemList = next(os.walk(parentDir))[2]

while len(itemList) != 0:

    directory = itemList.pop(0)

    if directory != '.DS_Store':

        # Path
        imagePath = os.path.join(parentDir, directory)
        path = imagePath + "_f"
        
        grayName = imagePath[imagePath.rfind('/')+1:imagePath.rfind('.')]+'-Gray'+imagePath[imagePath.rfind('.'):]

        imColor = cv.imread(imagePath, cv.IMREAD_COLOR)
        colorName = imagePath[imagePath.rfind('/')+1:imagePath.rfind('.')]+'-Color'+imagePath[imagePath.rfind('.'):]
        imLab = cv.cvtColor(imColor, cv.COLOR_BGR2Lab)
        l,a,b = cv.split(imLab)

        imGray = cv.imread(imagePath, cv.IMREAD_GRAYSCALE)

        os.mkdir(path)

        cv.imwrite(path+'/' + grayName, imGray)
        cv.imwrite(path+'/' + colorName, imColor)

        os.remove(imagePath)