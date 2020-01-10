import numpy as np
np.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
A = np.array([input().split() for _ in range(n)], int)

print(np.mean(A, axis=1), np.var(A, axis=0), np.std(A), sep='\n')
