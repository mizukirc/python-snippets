import numpy as np

matrix_size = int(input())
A = []
B = []

for i in range(matrix_size):
    A_in = input().strip().split(' ')
    A.append(A_in)
    
for i in range(matrix_size):    
    B_in = input().strip().split(' ')
    B.append(B_in)

A = np.array(A).astype(int)
B = np.array(B).astype(int)

print(np.dot(A, B))


# -- another answer
matrix_size = int(input())
A = np.array([input().split() for _ in range(matrix_size)], int)
B = np.array([input().split() for _ in range(matrix_size)], int)

print(np.dot(A, B))