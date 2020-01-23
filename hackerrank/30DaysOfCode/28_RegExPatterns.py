#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    namelist = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        if emailID[-10:] == '@gmail.com':
            namelist.append(firstName)    

    namelist = sorted(namelist)
    [print(namelist[i]) for i in range(len(namelist))]
