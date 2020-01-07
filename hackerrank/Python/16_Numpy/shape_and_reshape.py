# https://www.hackerrank.com/challenges/np-shape-reshape/
#!/bin/python3

import numpy

in_arr = input().strip().split(' ')
in_arr = numpy.array(in_arr, int)
out_arr = numpy.reshape(in_arr, (3,3))
print(out_arr)
