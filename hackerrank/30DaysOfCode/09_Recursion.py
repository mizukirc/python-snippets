# https://www.hackerrank.com/challenges/30-recursion/
#!/bin/python3


import math
import os
import random
import re
import sys

def factorial(n):
    if(n <= 1):
        result = 1
    else: 
        result = n * math.factorial(n-1)
    
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()


