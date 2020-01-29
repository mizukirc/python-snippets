from statistics import median

n = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))

lst_db = [[X[i]] * F[i] for i in range(len(F))]
lst = sorted([i for j in lst_db for i in j])
res = median(lst[(len(lst)+1) // 2:]) - median(lst[:len(lst) // 2])
print('%.1f' % res)