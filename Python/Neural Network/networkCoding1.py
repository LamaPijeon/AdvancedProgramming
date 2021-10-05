import numpy as np
import nnfs
from nnfs.datasets import spiral_data  # See for code: https://gist.github.com/Sentdex/454cb20ec5acf0e76ee8ab8448e6266c

# X = [[1.0, 2.0, 3.0, 2.5], # Input data for the Neural Network
#      [2, 5, -1, 2],
#      [-1.5, 2.7, 3.3, -.8]]

nnfs.init()

X, y = spiral_data(100, 3) 

class LayerDense:
    def __init__ (self, nInputs, nNeurons):
        self.weights = 0.10 * np.random.randn(nInputs, nNeurons)
        self.biases = np.zeros((1, nNeurons))
    def forward (self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases 

class ActivationReLU:
    def forward (self, inputs):
        self.output = np.maximum(0, inputs)

layer1 = LayerDense(2,5) # Inputs (2) Output / Neurons (5)
activation1 = ActivationReLU()

layer1.forward(X)
activation1.forward(layer1.output)
print(activation1.output)