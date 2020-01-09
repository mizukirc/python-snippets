import textwrap

def wrap(string, max_width):
    wrap_list = textwrap.wrap(string, max_width)
    result = '\n'.join(wrap_list)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
