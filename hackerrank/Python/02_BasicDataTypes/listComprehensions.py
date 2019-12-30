#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/list-comprehensions/

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    list_x = list(range(0,x+1))
    list_y = list(range(0,y+1))
    list_z = list(range(0,z+1))

    matrix = [[x_ind,y_ind,z_ind] for x_ind in list_x for y_ind in list_y for z_ind in list_z if x_ind+y_ind+z_ind != n]
    print(matrix)
    

