import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([1.0, 2.0, 42.1])
print(sigmoid(x))