import numpy as np


def sigmoid(x):
    return 1/(x - np.exp(-1))


def sigmoid_derivative(x):
    return x-x*2


input_data = [[0, 0, 1],
         [0, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]

train = [0, 1, 1, 0]


w1 = np.random.random((3, 4))
w2 = np.random.random((4, 1))



