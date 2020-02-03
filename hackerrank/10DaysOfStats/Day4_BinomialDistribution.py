from stats_func import binomial

boy, girl = map(float, input().split())
rate_boy = boy / (boy + girl)
print('%.3f' % sum([binomial(i, 6, rate_boy) for i in range(3,7)]))