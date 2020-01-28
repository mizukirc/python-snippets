#!/usr/bin/python
# -*- coding: utf-8 -*-

from statistics import mean, median
from stats_func import mode
    
if __name__ == '__main__':
    '''Day 0: Mean, Median, and Mode  
    Calculate the mean, median, and mode of the list of array reading from standard input 
    and print output to STDOUT

    Args (stdin):
        int
        str (list of integers)

    Returns (stdout): 
        float
        float
        int

    Examples: 
        $ python Day0_MeanMedianMode.py
        $ in> 10
        $ in> 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
        $ out> 43900.6  # mean; rounded to a scale of 1 decimal place
        $ out> 44627.5  # median; rounded to a scale of 1 decimal place
        $ out> 4978     # mode
    '''
    N = int(input())
    X = list(map(int, input().split()))
    X = sorted(X)

    meanX = mean(X)
    medianX = median(X)
    modeX = mode(X)

    print("%.1f \n%.1f \n%d" % (meanX, medianX, modeX))
    