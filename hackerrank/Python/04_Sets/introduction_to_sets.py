def average(array):
    a = set(array)
    result = sum(a)/len(a)
    return result
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)