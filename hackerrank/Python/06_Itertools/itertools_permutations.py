from itertools import permutations

instr, num = input().split()
num = int(num)
results = sorted(permutations(instr, num))
for x in results:
    print(*x, sep='')