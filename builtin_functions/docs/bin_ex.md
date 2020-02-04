### Documentation:

[bin](https://docs.python.org/ja/3/library/functions.html#bin)  
整数を2進数の文字列に変換

### Syntax:

```bin(num)```

- **num** (int): 2進数に変換する整数値

### Returns:

str

### Example: 

```python
>>> bin(30)
'0b11110'

>>> format(30, '#b')
'0b11110'

>>> format(30, 'b')
'11110'
```

### Note:
文字列のはじめの '0b' が不要な場合は format のオプションで 'b' を指定する．
```python
>>> format(a, 'b')
'11'
```