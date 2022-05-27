import cv2 as cv
import os
from numexpr.necompiler import Immediate
import numpy as np
import numexpr as ne
import time as ti

from numpy.lib.type_check import imag
# import pandas
# from matplotlib.pyplot import imsave
# import numpy as np
# import torch
# from torch import nn, optim
# from torchvision import transforms
# from torch.utils.data import Dataset, DataLoader

dash = '/'

class ColorizationDataSet():

    def __init__(self, paths, split='train'):

        def prepairTain(paths):
            miniBatch = []
            maxSize = 256
            for path in paths:
                im = cv.imread(path, cv.IMREAD_COLOR)
                im = cv.cvtColor(im,cv.COLOR_BGR2Lab)
                if max(im.shape[0], im.shape[1]) > maxSize:
                    size = (maxSize, maxSize)
                    im = cv.resize(im, size)
                else:
                    maxLength = max(im.shape[0], im.shape[1])
                    im = cv.resize(im, (maxLength, maxLength))
                im = cv.flip(im, 1)
                l, a, b = cv.split(im)
                miniBatch.append(l)
                return miniBatch

        def train(paths):
            
            miniBatch = prepairTain(paths)
            for imNum in range(len(miniBatch)):
                miniBatch[imNum] = DoubleConvolution(miniBatch[imNum], 'LeakyReLu')

        def colorize(paths):
            pass

        def pooling(x):
            pass

        def normalization(imgMatrix, function):
            if function == 'ReLu':
                for row in range(len(imgMatrix)):
                    for column in range(len(imgMatrix[row])):
                        imgMatrix[row][column] = max(0, imgMatrix[row][column])
            elif function == 'LeakyReLu':
                for row in range(len(imgMatrix)):
                    for column in range(len(imgMatrix[row])):
                        imgMatrix[row][column] = max(.1*column, column)            
            # elif function == 'Sigmoid':
                # for row in range(len(imgMatrix)):
                    # for column in range(len(imgMatrix[row])):
            #             imgMatrix[row][column] = 1/(1+ne.E(-column))
            return imgMatrix
        
        def average(numbers):

            counting = 0
            for number in numbers:
                counting += number
            average = counting/len(numbers)
            return average
        
        def popConvolution(image, imgShape):
            image = image[1:imgShape]
            imgShape -= 1
            for row in range(imgShape):
                index = [0,-1]
                a = np.delete(image[row], index)
                image[row] = a
                ti.sleep(10)
            return image
        
        def DoubleConvolution(image, function):
            # kernalSize = 3
            for i in range(2):
                colNum = len(image[0])-1
                image[0] = np.zeros(shape=(colNum+1))
                image[-1] = np.zeros(shape=(colNum+1))
                for row in range(colNum):
                    image[row][0] = 0
                    image[row][-1] = 0
                for row in range(colNum):
                    if row != 0 and row != colNum:
                        for column in range(colNum):
                            averageField = average([image[row][column],image[row+1][column],image[row+1][column+1],image[row+1][column-2],image[row-1][column],image[row-1][column+1],image[row-1][column-1],image[row][column-1],image[row][column+1]])
                            image[row][column] = averageField
                        image[row][0] = 0
                        image[row][-1] = 0
                        popConvolution(image, len(image[0]))
            return image

        if split == 'train': # default
            train(paths)

        elif split == 'colorizse':
            colorize(paths)
                

class Discriminator():

    def __init__(self):
        print("Initiate")

    def forward (self, inputs):
        print("Forward")

# discriminator = Discriminator()

class Generator():

    def __init__(self):
        print("Initiate")

    def forward (self, inputs):
        print("Forward")

# generator = Generator()

batchDirectories = []
batchSize = 15
action = 'train'

parentDir = "/Volumes/Tech 1/tiny-imagenet-200/train"
parent_folderList = next(os.walk(parentDir))[1]

# Accessing all the images in the Training folder by entering each folders folder.
if action == 'train':
    for x in parent_folderList:

        # 'x' this is gonna get each image catagory, roughly 500 images
        if x != '.DS_Store':


            folder = parentDir + "/" +  x
            child_folderList = next(os.walk(folder))[1]
            
            # 'y' this is the 'Images' folder  ->|<- change the [:1] underneath to zero to access all images
            for y in child_folderList[:1][:1][:1][:10]:

                imageFolder = folder+dash+y+dash
                images_Folder = next(os.walk(imageFolder))[1]

                # 'z' this is the folder with suffix '_f' with the image
                for z in images_Folder:
                    
                    imagePath = imageFolder+z
                    imName = folder[ : folder.rfind("_")]
                    images = next(os.walk(imagePath))[2]

                    for a in images:

                        imCPath = imagePath + dash + a
                        # Bottom code sends COLOR images, in batch sizes, over to be made into the colorization dataset
                        if len(batchDirectories) != batchSize:

                            batchDirectories.append(imCPath)

                        else: 

                            ColorizationDataSet(batchDirectories)
                            batchDirectories = []
                            ti.sleep(2)
                            ti.sleep(5)
                            print('Next MiniBatch Incoming')