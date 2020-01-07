#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/write-a-function/

def is_leap(year):
    leap = False
    
    _,year4 = divmod(year,4)
    _,year100 = divmod(year,100)
    _,year400 = divmod(year,400)
    if year400 == 0:
        leap = True
    elif year4 == 0 and year100 != 0:
        leap = True

    return leap

year = int(input())
print(is_leap(year))
