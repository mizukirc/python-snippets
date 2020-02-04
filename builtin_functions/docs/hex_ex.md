### Documentation:

[hex](https://docs.python.org/ja/3/library/functions.html#hex)  
整数を16進数の文字列に変換

### Syntax:

```hex(num)```

- **num** (int): 16進数に変換する整数

### Returns:

str

### Example: 

```python
>>> hex(30)
'0x1e'
>>> format(30, 'x')
'1e'
# 大文字のオプションにするとA-Fが大文字になる
>>> format(30, 'X')
'1E'
# オプションの最初に#をつけると、16進数であることを出力の文字列内で明示する事ができる
>>> format(30, '#x')
'0x1e'

```