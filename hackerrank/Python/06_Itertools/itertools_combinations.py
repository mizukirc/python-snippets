from itertools import combinations

instr, num = input().split()

[print("".join(i)) for x in range(1, int(num)+1) for i in combinations(sorted(instr), x)]
