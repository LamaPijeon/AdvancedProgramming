import numpy as np

def GD(x, y): # gradient decent
    iterations = 10000
    mCurr = bCurr = 0
    n = len(x)
    learningRate = .0001
    for i in range(iterations):
        yPredicted = mCurr * x + bCurr
        md = -(2/n)*sum(x*(y-yPredicted))
        bd = -(2/n)*sum(y-yPredicted)
        mCurr -= learningRate * md
        bCurr -= learningRate * bd
        print('m {}, b [], iterations {}'.format(mCurr, bCurr, i))
        
def SGD(): # stochastic gradient decent
    pass
def miniBGD(): # mibi batch gradient decent + stochastic gradient decent + momentum
    pass
def SGDMA(): # stochastic gradient decent + momentum + accelleration
    pass
def adagrad():
    pass
def adadelta():
    pass
def adam():
    pass

x = np.array([5, 3, 9 , 5, 1])
y = np.array([1, 9, 2, 7, 6])

GD(x, y)