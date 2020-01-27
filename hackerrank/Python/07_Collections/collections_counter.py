from collections import Counter

X = int(input())
shoe_size = list(map(int, input().split()))
N = int(input())

c = Counter(shoe_size)

totalval = 0
for i in range(N):
    size, val = map(int, input().split())
    if c[size] != 0:
        totalval = totalval + val
        c[size] = c[size]-1
print(totalval)