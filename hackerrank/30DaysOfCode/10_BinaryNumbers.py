#!/bin/python3
# https://www.hackerrank.com/challenges/30-binary-numbers/

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    binnum = format(n, 'b')
    num_consecutive = max(map(len, binnum.split('0')))
    print(num_consecutive)

