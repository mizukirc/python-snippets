'''
単語グループ A と単語グループ B の長さを標準入力として受け付け、単語グループ B に含まれる要素について単語グループ A 内のインデクスを標準出力として返す。

sample input: 
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6  

sample output:
78.00

'''
from collections import namedtuple

N = int(input())
names = input().split()
record = namedtuple('record', names)
marks = [int(record._make(input().split()).MARKS) for _ in range(N)]
print('%.2f' % (sum(marks)/len(marks)))