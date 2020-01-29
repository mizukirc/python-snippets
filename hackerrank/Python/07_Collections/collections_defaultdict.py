'''
単語グループ A と単語グループ B の長さを標準入力として受け付け、単語グループ B に含まれる要素について単語グループ A 内のインデクスを標準出力として返す。

sample input: 
5 2
a
a
b
a
b
a
b

sample output:
1 2 4
3 5

'''
n, m = map(int, input().split())
A = [input() for i in range(n)]
B = [input() for i in range(m)]

for j in range(len(B)):
    lst = [i+1 for i, val in enumerate(A) if val == B[j]]
    if not lst:
        lst = [-1]
    print(*lst, sep=' ')