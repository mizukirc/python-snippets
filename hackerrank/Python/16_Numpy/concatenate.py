import numpy as np

size_A = list(map(int, input().strip().split(' ')))

A = []
for i in range(size_A[0]):
    in_A = list(map(int, input().strip().split(' ')))
    A.append(in_A)

B = []
for i in range(size_A[1]):
    in_B = list(map(int, input().strip().split(' ')))
    B.append(in_B)

print(np.concatenate([A, B]))


# -- another answer
n, m, p = map(int, input().split())
A = np.array([input().split() for _ in range(n)], int)
B = np.array([input().split() for _ in range(m)], int)
print(np.concatenate([A, B], axis=0))