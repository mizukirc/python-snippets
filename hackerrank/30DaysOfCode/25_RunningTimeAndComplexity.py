import math

def check_prime(num):
    if num == 1:
        return print("Not prime")
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return print("Not prime")
    return print("Prime")

n = int(input())
T = [int(input()) for i in range(n)]
for j in range(len(T)):
    ans = check_prime(T[j])