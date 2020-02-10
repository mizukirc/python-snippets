from math import exp, sqrt, pi, erf
from stats_func import cdf 

mu, sigma = map(float, input().split())
lim1 = float(input())
lim2, lim3 = map(float, input().split())

print('%.3f' % cdf(lim1, mu, sigma))
print('%.3f' % (cdf(lim3, mu, sigma) - cdf(lim2, mu, sigma)))