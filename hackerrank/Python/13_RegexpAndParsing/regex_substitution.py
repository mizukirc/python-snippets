import re

N = int(input())
for _ in range(N):
    S = input() 
    S = re.sub(r'(?<= )\&\&(?= )', 'and', S)
    S = re.sub(r'(?<= )\|\|(?= )', 'or', S)
    print(S)