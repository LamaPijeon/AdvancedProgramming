import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]

weights = [[.2, .8, -.5, 1],
           [.5, -.91, .26, -.5],
           [-.26, -.27, .17, .87]]

biases = [2,3,.5]

output = np.dot(weights, inputs) + biases 

print(output)