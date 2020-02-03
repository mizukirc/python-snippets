from stats_func import geometric

numerator, denominator = map(int, input().split())
inspection = int(input())

print('%.3f' % geometric(inspection, numerator/denominator))