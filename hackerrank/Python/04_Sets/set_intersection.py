n = int(input())
n_num = set(map(int, input().split()))
b = int(input())
b_num = set(map(int, input().split()))
print(len(n_num.intersection(b_num)))