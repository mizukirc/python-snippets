def count_substring(string, sub_string):
    if sub_string[0] == sub_string[-1:]:
        num_str = string.replace(sub_string[0], sub_string[0]+sub_string[0]).count(sub_string)
    else:
        num_str = string.count(sub_string)
    return num_str

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
