import numpy as np
import math
# '''
# solving for x

# e ** x = b
# '''

# b = 5.2

# print(np.log(b))
# print(np.e ** np.log(b))

softmaxOutput = [0.7, 0.1, 0.2]
targetOutput = [1, 0, 0]

loss = -(math.log(softmaxOutput[0] * targetOutput[0] + softmaxOutput[1] * targetOutput[2] + softmaxOutput[2] * targetOutput[2]))
print(loss)