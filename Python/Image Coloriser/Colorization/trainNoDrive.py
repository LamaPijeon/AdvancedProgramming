# https://github.com/yacineMahdid/artificial-intelligence-and-machine-learning/blob/master/deep-learning-from-scratch-python/.ipynb_checkpoints/Gradient%20Descent%20Optimization%20Algorithms-checkpoint.ipynb
# https://www.youtube.com/watch?v=p6tG-dep8f4
import cv2 as cv
import os
import numpy as np
import time as ti

dash = '/'

class ColorizationDataSet():

    def __init__(self, paths, split='train'):
         
        sharpen = np.array([ #https://setosa.io/ev/image-kernels/
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
            ])
        blur = np.array([
            [0.0625, 0.125, 0.0625],
            [0.125,  0.25,  0.125],
            [0.0625, 0.125, 0.0625]
            ])
        outline = np.array([
            [-1, -1, -1],
            [-1,  10, -1],
            [-1, -1, -1]
            ])
        
        def calculate_target_size(img_size: int, kernel_size: int) -> int:
            num_pixels = 0
            
            # From 0 up to img size (if img size = 224, then up to 223)
            for i in range(img_size):
                # Add the kernel size (let's say 3) to the current i
                added = i + kernel_size
                # It must be lower than the image size
                if added <= img_size:
                    # Increment if so
                    num_pixels += 1
            
            return num_pixels

        def prepairTain(paths):
            miniBatch = []
            maxSize = 2**15
            minSize = 2**8
            for path in paths:
                im = cv.imread(path, cv.IMREAD_COLOR)
                im = cv.cvtColor(im,cv.COLOR_BGR2Lab)
                smallerSide = min(im.shape[0], im.shape[1])
                largerSide = max(im.shape[0], im.shape[1])
                if minSize > smallerSide: im = cv.resize(im, (minSize, minSize))
                elif maxSize < largerSide: im = cv.resize(im, (maxSize, maxSize))
                else: im = cv.resize(im, (max(im.shape[0], im.shape[1]), max(im.shape[0], im.shape[1])))
                im = cv.flip(im, 1)
                l, a, b = cv.split(im)
                miniBatch.append(l)
            return miniBatch

        def train(paths):           
            miniBatch = prepairTain(paths)
            for image in miniBatch:
                ogImage = image
                for i in range(1):
                    newimage = average(ogImage, 0, '')
                    newimage = convolve(img=np.array(newimage), kernel=blur)
                    newimage = normalization(image, 'LeakyReLu')
                    newimage = convolve(img=np.array(newimage), kernel=sharpen)
                    newimage = normalization(image, 'LeakyReLu')
                    newimage = convolve(img=np.array(newimage), kernel=outline)
                    newimage = normalization(image, 'LeakyReLu')
                    newimage = MaxPoolings(newimage)
                cv.imshow('newimage (average)', newimage)
                cv.imshow('orimage', ogImage)
                cv.waitKey(2500)

        def colorize(paths):
            pass

        def normalization(imgMatrix, function):
            image = imgMatrix
            if function == 'ReLu':
                for row in range(len(image)):
                    for column in range(len(image[row])):
                        image[row][column] = max(0, image[row][column])
            elif function == 'LeakyReLu':
                for row in range(len(image)):
                    for column in range(len(image[row])):
                        image[row][column] = max(image[row][column] * .1 , image[row][column])
            # elif function == 'Sigmoid':
                # for row in range(len(image)):
                #     for column in range(len(image[row])):
            #             image[row][column] = 1/(1+ne.E(-image[row][column]))
            return image
            
        def average(image, thingy, numbers):
            k = 3
            # Assuming a rectangular image
            if thingy == 0:
                imageSize = image.shape[0]
                tgt_size = calculate_target_size(
                    imageSize,
                    kernel_size=k
                )
                imageSize-=2
                # 2D array of zeros
                average_image = np.zeros(shape=(tgt_size, tgt_size))
                for row in range(imageSize):
                    for column in range(imageSize): average_image[row][column] = average('', 1, (image[row][column],image[row+1][column],image[row+1][column+1],image[row+1][column-2],image[row-1][column],image[row-1][column+1],image[row-1][column-1],image[row][column-1],image[row][column+1]))
                return average_image
            else:
                counting = 0
                for number in numbers:
                    counting += number
                averageNumber = counting/len(numbers)
                return averageNumber
            
        def convolve(img: np.array, kernel: np.array) -> np.array:
            # Assuming a rectangular image
            tgt_size = calculate_target_size(
                img_size=img.shape[0],
                kernel_size=kernel.shape[0]
            )
            # To simplify things
            k = kernel.shape[0]
            
            # 2D array of zeros
            convolved_img = np.zeros(shape=(tgt_size, tgt_size))
            
            # Iterate over the rows
            for i in range(tgt_size):
                # Iterate over the columns
                for j in range(tgt_size):
                    # img[i, j] = individual pixel value
                    # Get the current matrix
                    mat = img[i:i+k, j:j+k]
                    
                    # Apply the convolution - element-wise multiplication and summation of the result
                    # Store the result to i-th row and j-th column of our convolved_img array
                    convolved_img[i, j] = np.sum(np.multiply(mat, kernel))
            return convolved_img

        def MaxPoolings(image):
            stride = 2
            filterSize = 2
            newImage = []
            imageShape = image.shape[1]

            for row in range(0, len(image), 2):
                colNum = 0
                newImage.append([])
                while 0 < (imageShape - colNum) > filterSize and 0 < (imageShape - row) > filterSize: # This is actual maxpooling, though code right now only works for filtersize = 2
                    if 0 > (imageShape - row) and 0 <= (imageShape - colNum) >= filterSize: newImage[row].append(max(image[row][colNum], image[row][colNum + 1]))                                                                                # if not enough rows 
                    elif 0 > (imageShape - colNum) and 0 <= (imageShape - row) >= filterSize: newImage[row].append(max(image[row][colNum], image[row + 1][colNum]))                                                                              # if not enough columns
                    elif 0 <= (imageShape - colNum) >= filterSize and 0 <= (imageShape - row) >= filterSize: newImage[int(row/2)].append(max(image[row][colNum], image[row][colNum + 1], image[row + 1][colNum], image[row+ 1][colNum + 1]))     # if enough rows and enough columns
                    colNum += filterSize
            for row in range(len(newImage)):
                if len(newImage[row]) == 0: del newImage[row]
            return np.array(newImage)
        def coloriseFAKE(images):
            print('colorise')
            for image in range(len(images)):
                theImage = cv.imread(images[image], cv.IMREAD_GRAYSCALE)
                a = np.zeros(shape=theImage.shape)
                b = np.zeros(shape=theImage.shape)
                for row in range(len(a)):
                    for column in range(len(a)):
                        firstNum = np.random.uniform(-128,128)
                        secondNum = np.random.uniform(-128,128)

                        if row != 0 and column != 0: # not first row or collumn
                            if row > 1 and column > 1:
                                firstNum = ( firstNum + a[row-1][column] + a[row][column-1] +  a[row-1][column-1] + a[row-2][column] + a[row-2][column-1] + a[row-2][column-2] + a[row][column-1] + a[row][column-2] ) / 9
                                secondNum = ( secondNum + a[row-1][column] + b[row][column-1] +  b[row-1][column-1] + b[row-2][column] + b[row-2][column-1] + b[row-2][column-2] + b[row][column-1] + b[row][column-2] ) / 9
                            else:
                                firstNum = ( firstNum + a[row-1][column] + a[row][column-1] + a[row-1][column-1] ) / 4
                                secondNum = ( secondNum + b[row-1][column] + b[row][column-1] + b[row-1][column-1] ) / 4
                        elif row != 0: # first column, but not row
                            if row > 1:
                                firstNum = ( firstNum + a[row-1][column] + a[row-2][column] ) / 3
                                secondNum = ( secondNum + b[row-1][column] + b[row-2][column] ) / 3
                            else:
                                firstNum = ( firstNum + a[row-1][column] ) / 2
                                secondNum = ( secondNum + b[row-1][column] ) / 2              
                        elif column != 0: # first row, but not colun
                            if column > 1:
                                firstNum = ( firstNum + a[row][column-1] + a[row][column-2] ) / 3
                                secondNum = ( secondNum + b[row][column-1] + b[row][column-2] ) / 23
                            else:
                                firstNum = ( firstNum + a[row][column-1] ) / 2
                                secondNum = ( secondNum + b[row][column-1] ) / 2          
                        if firstNum < 0: firstNum *= .75
                        if secondNum < 0: secondNum *= .75
                        a[row][column] = "{:.2f}".format(((firstNum)))
                        b[row][column] = "{:.2f}".format((secondNum))
                newImage = np.dstack([theImage,a,b])
                newImage = cv.normalize(src=newImage, dst=None, alpha=2, beta=257, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)
                newImage = cv.cvtColor(newImage, cv.COLOR_BGR2LAB)
                # cv.imshow('a', a)
                # cv.imshow('b', b)
                # cv.imshow('theimage', theImage)
                cv.imshow('newimage', newImage)
                cv.waitKey(500)
                ti.sleep(.5)
                # images[image] = cv.merge([theImage, a, b])
            return images

        def printImagesFAKE(images):
            print('print images')
            for image in images:
                cv.imshow('image', image)
                cv.waitKey(1000)
                ti.sleep(100)
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

parentDir = "/Users/24nowak_p/Desktop/images"
parent_folderList = next(os.walk(parentDir))[1]

# Accessing all the images in the Training folder by entering each folders folder.
for x in parent_folderList:
    if x != 'DS.store':
        x = x.lower()
        y = parentDir + dash + x
        imagePath = y + dash + x[ :x.rfind(".")] + '-Color' + x[x.rfind("."):x.rfind("_")]
        if len(batchDirectories) != batchSize:

            batchDirectories.append(imagePath)

        else: 

            ColorizationDataSet(batchDirectories)
            batchDirectories = []
            ti.sleep(7)
            print('Next MiniBatch Incoming')