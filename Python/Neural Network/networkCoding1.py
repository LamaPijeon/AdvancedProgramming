import numpy as np
import nnfs
from nnfs.datasets import spiral_data, vertical_data

nnfs.init()

class LayerDense:
    def __init__ (self, nInputs, nNeurons):
        self.weights = 0.10 * np.random.randn(nInputs, nNeurons)
        self.biases = np.zeros((1, nNeurons))
    def forward (self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases 

class ActivationReLU:
    def forward (self, inputs):
        self.output = np.maximum(0, inputs)

class ActivationSoftmax:
    def forward (self, inputs):
        expValues = np.exp(inputs - np.max(inputs, axis = 1, keepdims = True))
        probabilities = expValues / np.sum(expValues, axis = 1, keepdims = True)
        self.output = probabilities
        
class Loss:
    def calculate (self, output, y):
        sampleLosses = self.forward(output, y)
        dataLoss = np.mean(sampleLosses)
        return dataLoss

class LossCatagoricalCrossentropy(Loss):
    def forward (self, yPred, yTrue):
        samples = len(yPred)
        yPredClipped = np.clip(yPred, 1e-7, 1-1e-7)

        if len(yTrue.shape) == 1:
            # scalar values
            correctConfidences = yPredClipped[range(samples), yTrue]
        elif len(yTrue.shape) == 2:
            # one-hot encoding
            correctConfidences = np.sum(yPredClipped * yTrue, axis = 1)
        negativeLogLikleyhoods = -np.log(correctConfidences)
        return negativeLogLikleyhoods            

X, y = spiral_data(samples = 100, classes = 3)

dense1 = LayerDense(2, 3)
activation1 = ActivationReLU()

dense2 = LayerDense(3,3)
activation2 = ActivationSoftmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])

lossFunction = LossCatagoricalCrossentropy()
loss = lossFunction.calculate(activation2.output, y)

print("Loss: ",loss)