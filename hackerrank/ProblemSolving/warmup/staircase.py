#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    string = [print(str('#'*(i+1)).rjust(n)) for i in range(n)]
    return string
    
if __name__ == '__main__':
    n = int(input())

    staircase(n)
