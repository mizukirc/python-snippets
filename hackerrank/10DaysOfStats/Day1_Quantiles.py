#!/usr/bin/python
# -*- coding: utf-8 -*-

from statistics import median


if __name__ == '__main__':
    '''Day 1: Quantiles
    Calculate the 2nd, 3rd and 4th quantiles of the list of array 
    reading from standard input and print output to STDOUT

    Args (stdin):
        int
        str (list of integers)

    Returns (stdout): 
        int
        int
        int

    Examples: 
        $ python Day1_StandardDeviation.py
        in> 9
        in> 3 7 8 5 12 14 21 13 18
        out> 6  
        out> 12 
        out> 16

    '''

    n = int(input())
    X = sorted(list(map(int, input().split())))

    print(int(median(X[:n//2])))
    print(int(median(X)))
    print(int(median(X[(n+1)//2:])))


