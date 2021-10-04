import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]

weights = [[.2, .8, -.5, 1],
           [.5, -.91, .26, -.5],
           [-.26, -.27, .17, .87]]

biases = [2,3,.5]

outputs = [
    inputs[0] * weights[0][0] + inputs[1] * weights[0][1] + inputs[2] * weights[0][2] + biases[0],
    inputs[0] * weights[1][0] + inputs[1] * weights[1][1] + inputs[2] * weights[1][2] + biases[1],
    inputs[0] * weights[2][0] + inputs[1] * weights[2][1] + inputs[2] * weights[2][2] + biases[2]
]






'''
layerOutputs = [] # Output of current layer

for neuronWeights, neuronBias in zip(weights,biases):
    neuronOutput = 0 # Output of given neutron
    for nInput, weight in zip(inputs, neuronWeights):
        neuronOutput += nInput * weight
    neuronOutput += neuronBias
    layerOutputs.append(neuronOutput)

print(layerOutputs)
'''