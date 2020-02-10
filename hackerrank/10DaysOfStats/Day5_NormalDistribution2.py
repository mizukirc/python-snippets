from stats_func import cdf 

mu, sigma = map(float, input().split())
lim1 = float(input())
lim2 = float(input())

print('%.2f' % ((1 - cdf(lim1, mu, sigma))*100))
print('%.2f' % ((1 - cdf(lim2, mu, sigma))*100))
print('%.2f' % (cdf(lim2, mu, sigma)*100))