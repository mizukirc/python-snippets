# https://www.hackerrank.com/challenges/np-arrays/
#!/bin/python3

import numpy

def arrays(arr):
    result = numpy.array(arr, float)
    result = result[::-1]
    return result

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


