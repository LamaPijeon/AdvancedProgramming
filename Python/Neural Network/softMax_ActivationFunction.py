import numpy as np 
import nnfs

nnfs.init()

layerOutputs = [[4.8, 1.21, 2.385],
                [8.9, -1.81, 0.2],
                [1.41, 1.051, 0.026]]

expValues = np.exp(layerOutputs)

# print(expValues)

# normBase = sum(expValues)

# print(np.sum(layerOutputs, axis = 1, keepdims=True))

normValues = expValues / np.sum(expValues, axis = 1, keepdims = True)

print(normValues)
# print(sum(normValues))