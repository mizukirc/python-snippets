n, m = map(int, input().split())
str_pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(str_pattern + ['WELCOME'.center(m, '-')] + str_pattern[::-1]))