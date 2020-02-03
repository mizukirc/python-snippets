from stats_func import geometric

numerator, denominator = map(int, input().split())
inspection = int(input())

print('%.3f' % sum([geometric(i, numerator/denominator) for i in range(1,6)]))