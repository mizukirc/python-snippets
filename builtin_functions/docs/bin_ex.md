### Documentation:

[bin](https://docs.python.org/ja/3/library/functions.html#bin)  
バイナリ値に変換

### Syntax:

```bin(a)```

- **a**: バイナリに変換したい整数値

### Returns:

str

### Example: 

```python
>>> a = 3
>>> bin(a)
'0b11'
```

### Note:
文字列のはじめの '0b' が不要な場合は format のオプションで 'b' を指定する．
```python
>>> format(a, 'b')
'11'
```
