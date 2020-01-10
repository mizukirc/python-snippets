import numpy as np

in_A = input().strip().split(' ')
in_B = input().strip().split(' ')
A = np.array(in_A).astype(int)
B = np.array(in_B).astype(int)

print(np.inner(A, B))
print(np.outer(A, B))


# -- another answer
A, B = [np.array(input().split(), int) for _ in range(2)]

print(np.inner(A, B), np.outer(A, B), sep='\n')
