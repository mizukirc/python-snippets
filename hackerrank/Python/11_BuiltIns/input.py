x, k = map(int, input().split())
P = input()  
print(eval(P, {'x': x}) == k)
