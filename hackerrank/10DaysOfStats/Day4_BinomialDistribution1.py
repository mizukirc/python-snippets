from stats_func import binomial

percentage_reject, batch_size = map(float, input().split())
batch_size = int(batch_size)
print('%.3f' % sum([binomial(i, 10, percentage_reject/100) for i in range(0, 3)]))
print('%.3f' % sum([binomial(i, 10, percentage_reject/100) for i in range(2, 11)]))