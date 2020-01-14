#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    print('{:.6f}'.format(sum([arr[i]>0 for i in range(len(arr))])/len(arr)))
    print('{:.6f}'.format(sum([arr[i]<0 for i in range(len(arr))])/len(arr)))
    print('{:.6f}'.format(sum([arr[i]==0 for i in range(len(arr))])/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
