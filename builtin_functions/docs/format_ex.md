### Documentation:

[format](https://docs.python.org/ja/3/library/functions.html#format)  
出力形式の書式設定

### Syntax:

```format(val, [, format_spec])```

- **val** (int/float): 書式設定したい対象の数値

### Returns:

str (書式設定された出力)

### Example: 

```python
>>> format(12345, ',')
'12,345'

>>> s = {1,2,3,4,5}
>>> eval('s.{0}({1})'.format(*input().split()+['']))
in> pop
1
```

### Note:
[standard format specifier](https://docs.python.org/ja/3/library/string.html#formatspec)





