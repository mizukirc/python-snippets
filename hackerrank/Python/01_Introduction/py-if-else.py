#!/bin/python3
# problem: https://www.hackerrank.com/challenges/py-if-else/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    a,b = divmod(n, 2)
    if(b == 1):
        print("Weird")
    elif(b == 0):
        if(2 <= n <= 5) or (n > 20):
            print("Not Weird")
        elif(6 <= n <= 20):
            print("Weird")
        
    
