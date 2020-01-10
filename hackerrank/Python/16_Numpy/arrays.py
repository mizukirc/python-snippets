import numpy

def arrays(arr):
    result = numpy.array(arr, float)
    result = result[::-1]
    return result

arr = input().split()
result = arrays(arr)
print(result)

