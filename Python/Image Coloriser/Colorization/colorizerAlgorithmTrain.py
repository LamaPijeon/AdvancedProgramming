import os
import cv2 as cv
# from matplotlib.pyplot import imsave
import numpy as np
# import torch
# from torch import nn, optim
# from torchvision import transforms
# from torch.utils.data import Dataset, DataLoader

class ColorizationDataSet():

    def __init__(self, paths, split='train'):

        for path in paths.values():
            im = cv.imread(path, cv.IMREAD_COLOR)

            if split == 'train':
                size = (256, 256)
                im = cv.resize(im, size)
                im = cv.flip(im, 1)
                imLab = cv.cvtColor(im, cv.COLOR_RGB2LAB)
                l,a,b = cv.split(imLab)
                ab = np.zeros_like(imLab)
                ab[:,:,1] = a
                ab[:,:,2] = b
                cv.imshow('im', ab)
                cv.waitKey(0)
    
class Discriminator():

    def __init__(self):
        print("Initiate")

    def forward (self, inputs):
        print("Forward")

discriminator = Discriminator()

class Generator():

    def __init__(self):
        print("Initiate")

    def forward (self, inputs):
        print("Forward")

generator = Generator()

path = "/Users/24nowak_p/Desktop/School/Programming/Programming Class/AdvancedProgramming/Python/Image Coloriser/Images/"
imPaths = {}
paths = 1
folders = next(os.walk(path))[1]

for folder in folders:   # The below three lines find the path for the images and path of the Gray image
    
    imName = folder[ : folder.rfind("_")]
    imPath = path + folder + "/" + imName[ : imName.rfind(".")] + "-Color" + imName[imName.rfind(".") : ]
    imPaths[paths] = imPath
    paths += 1

dataset = ColorizationDataSet(imPaths)