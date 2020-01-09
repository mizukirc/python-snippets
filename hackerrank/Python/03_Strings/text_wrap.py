import textwrap

def wrap(string, max_width):
    result = textwrap.wrap(string, max_width)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    wrap_list = wrap(string, max_width)
    result = '\n'.join(wrap_list)
    print(result)
