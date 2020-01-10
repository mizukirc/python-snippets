import numpy as np

N = int(input())

A = []
for i in range(N):
    A_in = list(map(float, input().split()))
    A.append(A_in)

print(round(np.linalg.det(A),2))


# -- another answer
N = int(input())
A = np.array([input().split() for _ in range(N)], float)

print(round(np.linalg.det(A),2))

