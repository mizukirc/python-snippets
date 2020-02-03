from stats_func import poisson, factorial
import math 

Xmean = float(input())
target = int(input())

print('%.3f' % poisson(Xmean, target))