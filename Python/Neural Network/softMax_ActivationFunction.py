import math

layerOutputs = [4.8, 1.21, 2.385]

# E = 2.71828182846
E = math.e

expValues = []

for outputs in layerOutputs:
    expValues.append(E**outputs)

print(expValues)

normBase = sum(expValues)
normValues = []

for value in expValues:
    normValues.append