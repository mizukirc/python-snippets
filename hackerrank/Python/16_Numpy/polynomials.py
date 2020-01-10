import numpy as np

A = list(map(float, input().strip().split(' ')))
B = float(input())

print(np.polyval(A, B))


# -- another answer
A = np.array(input().split(), float)
B = float(input())

print(np.polyval(A, B))