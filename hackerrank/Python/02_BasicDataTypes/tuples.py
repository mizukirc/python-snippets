#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/python-tuples/

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    lst = tuple(integer_list)
    print(hash(lst))





