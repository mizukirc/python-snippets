import numpy as np
n, m = map(int, input().split())

A = np.array([input().split() for _ in range(n)], int) 
B = np.array([input().split() for _ in range(n)], int) 

print(A+B, A-B, A*B, A//B, A%B, A**B, sep='\n')