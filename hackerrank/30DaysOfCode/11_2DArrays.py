#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    summat = []
    for i in range(4):
        sumvec = [0] * 4
        for j in range(4):
            sumvec[j] = sum( arr[i][j:j+3] + [arr[i+1][j+1]] + arr[i+2][j:j+3] ) 

        summat.append(sumvec) 

    print(max([max(l) for l in summat]))