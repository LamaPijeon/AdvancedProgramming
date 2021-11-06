import os
import cv2 as cv
import numpy as np

def formatIm(size, im):
    im = cv.resize(im, size, interpolation = cv.INTER_AREA)
    im = cv.cvtColor(im, cv.COLOR_RGB2LAB)
    im = cv.flip(im, 1)
    l,a,b = cv.split(im)
    ab = cv.merge((a,b))
    return l, ab, im

imSize = (256, 256)

path = "/Users/24nowak_p/Desktop/School/Programming/Programming Class/AdvancedProgramming/Python/Image Coloriser/Images/"

folders = next(os.walk(path))[1]

for folder in folders:   # The below three lines find the path for the images and path of the Gray image
    imName = folder[ : folder.rfind("_")]
    grayName = path + folder + "/" + imName[ : imName.rfind(".")] + "-Gray" + imName[imName.rfind(".") : ]
    grayIm = cv.imread(grayName, cv.IMREAD_COLOR)

    l, ab, im = formatIm(imSize, grayIm)

    cv.imshow("Gray Image", im)
    cv.waitKey(0)