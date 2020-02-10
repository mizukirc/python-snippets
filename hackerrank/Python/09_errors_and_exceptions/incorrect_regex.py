import re

T = int(input())

for i in range(T):
    try: 
        S = input()
        re.compile(S)
        print('True')
    except re.error:
        print('False')