import numpy as np
from mlp import MLP
import functional as F

# Network size
N_input = 4
N_hidden = 3
N_output = 2

X = np.random.randn(N_input)
layer1 = MLP(N_input, N_hidden)
layer2 = MLP(N_hidden, N_output)

hidden1_out = F.sigmoid(layer1(X))
print("After layer 1:", hidden1_out)

output_out = F.sigmoid(layer2(hidden1_out))
print("Output of last layer:", output_out)