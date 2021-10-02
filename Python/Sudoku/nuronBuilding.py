inputs = [1.0, 2.0, 3.0, 2.5]
weights1 = [.4, 2.8, -.5, .24]
weights2 = [-.9, -.23, .52, -.21]
weights3 = [3.2, -.28, -.1, .42]

bias1 = 2
bias2 = 3.5
bias3 = 1.23

outputs = [
    inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + bias1, 
    inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + bias2,
    inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + bias3
]

print(outputs)