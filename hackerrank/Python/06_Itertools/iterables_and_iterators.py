import itertools

N = int(input())
lst = input().split()
K = int(input())

lst_tuple = list(itertools.combinations(lst, K))
lst_contains_a = [i for i in lst_tuple if 'a' in i]
print(len(lst_contains_a )/len(lst_tuple))