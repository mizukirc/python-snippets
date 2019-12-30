### Documentation:

[list](https://docs.python.org/ja/3/library/functions.html#list)  
[シーケンス型](https://docs.python.org/ja/3/library/stdtypes.html#typesseq)
複数の順序ありの要素を含むリスト（各要素は異なる型でもよい）

### Syntax:

```list([a])```

- **a**: any iteratable

**[ ]** でもリストを作成可能．

### Returns:

list

### Example: 

```python
>>> list()
list

>>> list([1,2,3])
[1, 2, 3]

>>> (1,2,3)
[1, 2, 3]

# 追加 (リストは上書きされる)
>>> a.append(4)
>>> a
[1, 2, 3, 4]

# 削除 (リストは上書きされる)
>>> a.remove(2)
>>> a
[1, 3, 4]

# in で検索
>>> a = [1, 2, 3]
>>> 3 in a  
True

# 各要素に operation を適用
>>> [x*2 for x in a]
[2, 6, 8]

# combine list elements into a string
>>> b = ['This', 'is', 'a', 'pen']
>>> b
['This', 'is', 'a', 'pen']
>>> ' '.join(b)
'This is a pen'
```

