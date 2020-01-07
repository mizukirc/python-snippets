if __name__ == '__main__':
    s = input()

print(any([s[i].isalnum() for i in range(len(s))]))
print(any([s[i].isalpha() for i in range(len(s))]))
print(any([s[i].isdigit() for i in range(len(s))]))
print(any([s[i].islower() for i in range(len(s))]))
print(any([s[i].isupper() for i in range(len(s))]))
