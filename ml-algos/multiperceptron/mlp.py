import numpy as np
from typing import Any

np.random.seed(42)

class MLP:
    def __init__(self, input, output) -> None:
        self.input = input
        self.output = output
        self.weight = np.random.normal(0, 0.1, (input, output))
        self.delta = np.zeros((input, output))
        
    def forward(self, X):
        return np.dot(X, self.weight)

    def backward(self, delta):
        self.delta = np.dot(delta, self.weight.T)
        return self.delta

    def update(self, learning_rate):
        self.weight += learning_rate * self.delta

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.forward(*args, **kwds)

    def __str__(self):
        return 'input: {} output: {} weight: {}'.format(self.input, self.output, self.weight)
