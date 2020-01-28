#!/usr/bin/python
# -*- coding: utf-8 -*-

from stats_func import weighted_mean


if __name__ == '__main__':
    '''Day 0: Weighted Mean
        Calculate the weighted mean of the list of array reading from standard input 
        and print output to STDOUT

    Args (stdin):
        int
        str (list of integers)
        str (list of integers)

    Returns (stdout): 
        float

    Examples: 
        $ python Day0_WeightedMean.py
        in> 5
        in> 10 40 30 50 20
        in> 1 2 3 4 5
        out> 32.0   # weighted mean; rounded to a scale of 1 decimal place
    '''
    N = int(input())
    X = list(map(int, input().split()))
    W = list(map(int, input().split()))

    weighted_meanX = weighted_mean(X, W)

    print("%.1f" % weighted_meanX)

