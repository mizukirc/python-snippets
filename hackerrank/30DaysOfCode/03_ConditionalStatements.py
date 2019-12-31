#!/bin/python3
# https://www.hackerrank.com/challenges/30-conditional-statements/

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    a,b = divmod(N,2)
    if(b == 1):
        print("Weird")
    elif(b == 0):
        if(2 <= N <= 5) or (N > 20):
            print("Not Weird")
        elif(6 <= N <= 20):
            print("Weird")

