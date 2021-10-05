import numpy as np

inputs = [[1.0, 2.0, 3.0, 2.5],
           [2, 5, -1, 2],
           [-1.5, 2.7, 3.3, -.8]]

weights = [[.2, .8, -.5, 1],
           [.5, -.91, .26, -.5],
           [-.26, -.27, .17, .87]]

biases = [2,3,.5]

weights2 = [[.1, -.14, .5],
           [-.5, .12, -.3],
           [-.44, .73, -.13]]

biases2 = [-1,2,-.5]

layer1Outputs = np.dot(inputs, np.array(weights).T) + biases 

layer2Outputs = np.dot(layer1Outputs, np.array(weights2).T) + biases2

print(layer2Outputs)