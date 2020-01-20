#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    s_new = s.split(' ')
    result = [s_new[i].capitalize() for i in range(len(s_new))]
    result = ' '.join(result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
