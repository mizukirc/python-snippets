import numpy as np

size_A = list(map(int, input().split()))
print(np.zeros(size_A).astype(int))
print(np.ones(size_A).astype(int))


# -- another answer
m_size = tuple(map(int, input().split()))
print(np.zeros(m_size, int), np.ones(m_size, int), sep='\n')