N = int(input())
lst = list(map(int, input().split(' ')))
ans = (sum([lst[i] > 0 for i in range(N)]) == N) and ((sum([(0 <= lst[i] < 10)  for i in range(N)]) > 0) or (sum([str(lst[i])[0] == str(lst[i])[1] for i in range(N) if lst[i] > 9]) > 0))
print(ans)

# -- another solution
N = int(input())
lst = list(map(int, input().split(' ')))
ans = (all([lst[i] > 0 for i in range(N)]) and (any([(0 <= lst[i] < 10)  for i in range(N)]) or any([str(lst[i])[0] == str(lst[i])[1] for i in range(N) if lst[i] > 9])))
print(ans)