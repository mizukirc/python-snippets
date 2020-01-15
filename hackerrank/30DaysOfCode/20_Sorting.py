#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0

for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1] 
            numSwaps += 1
firstElement = a[0]
lastElement = a[-1]

print('Array is sorted in %d swaps.' % numSwaps)
print('First Element: %s' % firstElement)
print('Last Element: %s' % lastElement)


# -- Another solution
#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def bubble(n):
    numSwaps = 0

    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1] 
                numSwaps += 1
    return a, numSwaps
sorted_a, numSwaps = bubble(a)
firstElement = sorted_a[0]
lastElement = sorted_a[-1]

print('Array is sorted in %d swaps.' % numSwaps)
print('First Element: %s' % firstElement)
print('Last Element: %s' % lastElement)

