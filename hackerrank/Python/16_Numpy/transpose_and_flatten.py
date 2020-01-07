# https://www.hackerrank.com/challenges/np-transpose-and-flatten/
#!/bin/python3

import numpy

in_size = input().strip().split(' ')
in_size = numpy.array(in_size, int)
in_size = tuple(in_size)

arr = []
for i in range(in_size[0]):
    in_arr = input().strip().split(' ')
    in_arr = numpy.array(in_arr, int)
    arr = numpy.append(arr, in_arr, axis=0)

out_arr = numpy.reshape(arr, in_size)
out_arr = out_arr.astype(int)
    
transpose_arr = numpy.transpose(out_arr)
flatten_arr = out_arr.flatten()

print(transpose_arr)
print(flatten_arr)
