from itertools import groupby
S = input()
for key, gr in groupby(S):
    print(tuple([len(list(gr)), int(key)]), end=' ')