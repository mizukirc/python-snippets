#!/bin/python3
# https://www.hackerrank.com/challenges/30-loops/


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    result = [n * i for i in range(1,11)]
    for i in range(0,10):
        print(str(n) + ' x ' + str(i+1) + ' = ' + str(result[i]))


