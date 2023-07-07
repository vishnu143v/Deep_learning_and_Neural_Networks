import numpy as np

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.asarray([0, 0, 0, 1])
y_pred = np.asarray([0, 0, 0, 0])
w = np.asarray([1, 1])


def step(_sum):
    if (_sum > 1.5):
        return 1
    else:
        return 0

for i in range(x.shape[0]):
    n= x[i]
    _sum = np.dot(n,w)
    y_pred[i] = step(_sum)

print(y_pred)


