import numpy as np


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)



input_data = np.array([[0, 0, 1],
                       [0, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

train = np.array([[0],
                  [1],
                  [1],
                  [0]])


w1 = np.random.random((3, 4))
w2 = np.random.random((4, 1))

for epoch in range(9):
    out1 = sigmoid(np.dot(input_data, w1))
    out2 = sigmoid(np.dot(out1, w2))

    error2 = train - out2

    delta2 = error2 * sigmoid_derivative(out2)
    delta2alt = error2.dot(sigmoid_derivative(out2))

    print()

    error1 = delta2.dot(w2.T)

    delta1 = error1 * sigmoid_derivative(out1)

    w2 += out1.T.dot(delta2)
    w1 += input_data.T.dot(delta1)

    if epoch % 1000 == 0:
        print("Error: ", error2)
        print("Error squared: ", sum(np.square(error2)))

print("Error: ", error2)
print("Error squared: ", sum(np.square(error2)))
print("Output: ", out2)



