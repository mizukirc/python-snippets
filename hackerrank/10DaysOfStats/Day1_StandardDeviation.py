#!/usr/bin/python
# -*- coding: utf-8 -*-

from stats_func import std


if __name__ == '__main__':
    '''Day 1: Standard Deviation
    Calculate the standard deviation of the list of array reading from standard input 
    and print output to STDOUT

    Args (stdin):
        int
        str (list of numbers)

    Returns (stdout): 
        float

    Examples: 
        $ python Day1_StandardDeviation.py
        in> 5
        in> 10 40 30 50 20
        out> 14.1   # std; rounded to a scale of 1 decimal place

    '''
    N = int(input())
    X = list(map(int, input().split()))
    print('%.1f'%std(X))



