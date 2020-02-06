meanA, meanB = map(float, input().split())

CA = 160 + 40 * (meanA + meanA**2)
CB = 128 + 40 * (meanB + meanB**2)

print('%.3f' % CA)
print('%.3f' % CB)
