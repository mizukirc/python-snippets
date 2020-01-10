import numpy as np
np.set_printoptions(legacy='1.13')

size_A = map(int, input().split())
print(np.eye(*size_A))