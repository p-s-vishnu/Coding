import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


learnrate = 0.5
x = np.array([1, 2, 3, 4])
y = np.array(0.5)

# Initial weights
w = np.array([0.5, -0.5, 0.3, 0.1])

# Gradient descent step for each weight
h = x.dot(w)  # Hypothesis function
nn_output = sigmoid(h)  # Output of neural network
error = y - nn_output  # Error of neural network

# Error function: Sum of Square Error
# Note: Summing up all the weight steps can lead to really large updates that make the gradient descent diverge. 
# To compensate for this, you'd need to use a quite small learning rate. 
# Instead, we can just divide by the number of records in our data, mm to take the average. 
# This way, no matter how much data we use, our learning rates will typically be in the range of 0.01 to 0.001.

# (y - y_hat) * f'(h) where h = x.w
error_term = error * sigmoid_prime(x.dot(w))
# w_new = w_new + del_w where del_w = - learningrate * (del_E / del_w)
del_w = learnrate * error_term * x

print("Neural Network output:")
print(nn_output)
print("Amount of Error:")
print(error)
print("Change in Weights:")
print(del_w)
print("Old weights")
print(w)
print("New weights")
print(w + del_w)
