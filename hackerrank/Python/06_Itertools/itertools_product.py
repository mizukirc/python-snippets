from itertools import product

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
lst = list(product(A, B))
[print(lst[i], end=' ') for i in range(len(lst))]