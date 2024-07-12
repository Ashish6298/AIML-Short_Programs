#backpropagation

import numpy as np
x = np.array([[2, 9], [1, 5], [3, 6]], dtype=float) / 9
y = np.array([[92], [86], [89]], dtype=float) / 100
sigmoid = lambda x: 1 / (1 + np.exp(-x))
deriv_sigmoid = lambda x: x * (1 - x)
epoch = 5000
lr = 0.1
wh, bh = np.random.uniform(size=(2, 3)), np.random.uniform(size=(1, 3))
wout, bout = np.random.uniform(size=(3, 1)), np.random.uniform(size=(1, 1))
for _ in range(epoch):
    hlayer_act = sigmoid(np.dot(x, wh) + bh)
    output = sigmoid(np.dot(hlayer_act, wout) + bout)

    d_output = (y - output) * deriv_sigmoid(output)
    d_hiddenlayer = np.dot(d_output, wout.T) * deriv_sigmoid(hlayer_act)

    wout += np.dot(hlayer_act.T, d_output) * lr
    wh += np.dot(x.T, d_hiddenlayer) * lr
predicted_output = output
print("Input (scaled):\n", x)
print("Actual Output (scaled):\n", y)
print("Predicted Output (scaled):\n", predicted_output)


# Input (scaled):
#  [[0.22222222 1.        ]
#  [0.11111111 0.55555556]
#  [0.33333333 0.66666667]]
# Actual Output (scaled):
#  [[0.92]
#  [0.86]
#  [0.89]]
# Predicted Output (scaled):
#  [[0.89706931]
#  [0.88321736]
#  [0.88981129]]