S = input()
ans = ''.join(sorted(filter(str.islower, S)) ) \
+ ''.join(sorted(filter(str.isupper, S))) \
+ ''.join(list(map(str, sorted(filter(lambda j: j % 2 == 1, map(int, [i for i in S if str.isdigit(i)])))))) \
+ ''.join(list(map(str, sorted(filter(lambda j: j % 2 == 0, map(int, [i for i in S if str.isdigit(i)]))))))
print(ans)