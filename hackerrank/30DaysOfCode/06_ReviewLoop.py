# https://www.hackerrank.com/challenges/30-review-loop/

T = int(input())
S = list()
for i in range(T):
    S.append(str(input()))

for i in range(len(S)):
    print(S[i][0] + S[i][2::2] + ' ' + S[i][1::2])
