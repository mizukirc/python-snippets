cube = lambda x: pow(x,3)

def fibonacci(n):
    if n >= 0:
        lst = [0]
    if n >= 1:
        lst.append(1)
    if n >= 2:
        for i in range(2,n+1):
            lst.append(lst[-1]+ lst[-2]) 
    return lst[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))