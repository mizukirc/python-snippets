# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/
#!/bin/python3

n = int(input())
phonebook = dict()
for i in range(n):
    entry = input().rstrip().split()
    phonebook[entry[0]] = int(entry[1])

namelist = []
try:
    while True:
        name = input()
        if name =='':
            break
        namelist.append(name)
except EOFError:
    pass

for i in range(len(namelist)):
    if namelist[i] in phonebook:
        print(namelist[i] + '=' + str(phonebook[namelist[i]]))
    else:
        print('Not found')

