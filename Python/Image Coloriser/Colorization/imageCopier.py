import os
import cv2 as cv

dash = "/"
imagesDone = 0

def getImages(image, fileType, path):
    name = image[image.rfind('/')+1:image.rfind('.')]+'-Color'+fileType
    imageColor = cv.imread(image, cv.IMREAD_COLOR)
    pathImage = path+'/'+name
    cv.imwrite(pathImage, imageColor)

#   We won't make gray images since it takes up a lot of space and it can just be done in the second code
    # name = image[image.rfind('/')+1:image.rfind('.')]+'-Gray'+fileType
    # imagePath = cv.imread(image, cv.IMREAD_GRAYSCALE)
    # cv.imwrite(path+'/' + name, imagePath)

    # return imageColor

def getFolder(image, parent):
    global imagesDone
    global possibleValues 
    imagePath = os.path.join(parent, image)
    fileType = imagePath[imagePath.rfind('.'):].lower()
    if image != '.DS_Store' and fileType in possibleValues:
        path = imagePath + "_f"
        if os.path.exists(path) == False:
            os.mkdir(path)
            getImages(imagePath, fileType, path)
            imagesDone += 1
            print()
            print(imagesDone)

            os.remove(imagePath)
# Parent Directory path
parentDir = "/Volumes/Tech 1/tiny-imagenet-200/train"
parent_folderList = next(os.walk(parentDir))[1]
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

# Accessing all the images in the Training folder by entering each folders folder.
for x in parent_folderList:
    folder = parentDir + "/" +  x
    child_folderList = next(os.walk(folder))[1]
    for y in child_folderList:
        imageFolder = folder+dash+y+dash
        images_Folder = next(os.walk(imageFolder))[2]
        for z in images_Folder:
            imagePath = imageFolder+z
            getFolder(imagePath, imageFolder)
            # print(z)