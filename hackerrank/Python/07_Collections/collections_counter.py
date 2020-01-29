'''
靴の総数、それぞれの靴のサイズ、購入数、各購入時の靴のサイズと価格を標準入力として受け付け、実際に購入された総価格を標準出力として返す。

sample input: 
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

sample output:
200

'''
from collections import Counter

X = int(input())
shoe_size = list(map(int, input().split()))
N = int(input())

c = Counter(shoe_size)

totalval = 0
for i in range(N):
    size, val = map(int, input().split())
    if c[size] != 0:
        totalval = totalval + val
        c[size] = c[size]-1
print(totalval)