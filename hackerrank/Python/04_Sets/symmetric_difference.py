M = int(input())
A = list(map(int, input().split()))
N = int(input())
B = list(map(int, input().split()))

set_A = set(A)
set_B = set(B)
diff_A = set_A.difference(set_B)
diff_B = set_B.difference(set_A)
diff_A.update(diff_B)
list_diff = sorted(list(diff_A))

[print(list_diff[i], end='\n') for i in range(len(list_diff))]

