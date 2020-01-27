from itertools import combinations_with_replacement

instr, num = input().split()

[print("".join(i)) for i in combinations_with_replacement(sorted(instr), int(num))]